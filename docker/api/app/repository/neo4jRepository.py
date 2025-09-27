from datetime import datetime
class Neo4jRepository():
    def __init__(self, driver,mongo):
        self.driver = driver
        self.mongo = mongo

    '''
    Recopila los datos de las peliculas encontradas para que este en el formato de un json
    Devuelve una lista de json
    '''
    def recopilarDatosPeliculas(self, resultados,user):
        
        devolver = []
        for resultado in resultados.records:
            devolver.append ({'title' :resultado['m.title'], 'plot':resultado['m.tagline'],
                    'year':resultado['m.released'],
                    'cast':self.getActoresDePelicula(resultado['m.title']),
                    'directores':self.getDirectoresDePelicula(resultado['m.title'])})
            self.mongo.insertDataLogs({'title' :resultado['m.title'], 'plot':resultado['m.tagline'],
                    'year':resultado['m.released'],
                    'cast':self.getActoresDePelicula(resultado['m.title']),
                    'directores':self.getDirectoresDePelicula(resultado['m.title']),
                    'timestamp':datetime.now(),'user':user})
        return devolver

    '''
    Recopila los datos de las personas encontradas para que este en el formato de un json
    Devuelve una lista de json
    '''
    def recopilarDatosPersonas(self, resultados):
        devolver = []
        for resultado in resultados.records:
            devolver.append ({'born' :resultado['p.born'], 'name':resultado['p.name']})
        return devolver


    '''
    Consigue los datos de los directores que trabajaron en la pelicula con el nombre exacto al indicado
    ''' 
    def getDirectoresDePelicula(self, titulo):
        resultados = self.driver.execute_query("MATCH (p:Person)-[d:DIRECTED]-(m:Movie {title: $title}) RETURN p.born,p.name",title=titulo)
        datos = self.recopilarDatosPersonas(resultados)
        return datos

    '''
    Consigue los datos de los actores que trabajaron en la pelicula con el nombre exacto al indicado
    ''' 
    def getActoresDePelicula(self, titulo):
        resultados = self.driver.execute_query("MATCH (p:Person)-[r:ACTED_IN]-(m:Movie {title: $title}) RETURN p.born,p.name",title=titulo)
        datos = self.recopilarDatosPersonas(resultados)
        return datos

    '''
    Busca Las peliculas en el que la persona indicada es actor
    ''' 
    def getPeliculasActuadas(self, nombre,user):
        resultados = self.driver.execute_query("MATCH (p:Person {name: $name})-[r:ACTED_IN]-(m:Movie) RETURN m.title, m.tagline, m.released, m.votes",name=nombre)
        datos = self.recopilarDatosPeliculas(resultados,user)
        return datos
          
    '''
    Busca Las peliculas en el que la persona indicada es director
    '''    
    def getPeliculasDirigidas(self, nombre,user):
        resultados = self.driver.execute_query("MATCH (p:Person {name: $name})-[d:DIRECTED]-(m:Movie) RETURN m.title, m.tagline, m.released, m.votes",name=nombre)
        datos = self.recopilarDatosPeliculas(resultados,user)
        return datos

    '''
    Filtra de manera dinamica las peliculas basandose en el titulo, tagline, actor, director
    '''
    def buscarPeliculasTodosLosFiltros(self, titulo,tagline, actor, director,user):
            q1 = ""
            q2 = ""
            q3 = ""
            q4 = ""
            if titulo != "'":
                q1="MATCH (m:Movie) WHERE m.title =~ '(?i).*{}.*'".format(titulo)
            if tagline != "'":
                q2="MATCH (m:Movie) WHERE m.tagline =~ '(?i).*{}.*'".format(tagline)
            if actor != "'":
                q3="MATCH (p2:Person)-[r:ACTED_IN]-(m:Movie) where p2.name = $name2 "
            if director != "'":
                q4="MATCH (p:Person)-[d:DIRECTED]-(m:Movie) where p.name = $name1 "
            consulta = q1 +\
                    q2 +\
                    q3 +\
                    q4 +\
                    "RETURN m.title, m.tagline, m.released, m.votes"
            resultados = self.driver.execute_query( 
                                            consulta, name1 = director, name2 = actor
                                            )                               
            datos = self.recopilarDatosPeliculas(resultados,user)
            return datos