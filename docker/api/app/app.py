from flask import Flask, request, abort, jsonify
from config.mongo_connector import get_mongo_connector
from repository.mongoDBRepository import MongoDBRepository
from config.neo4j_connector import get_neo4j_connector
from repository.neo4jRepository import Neo4jRepository
from flask_cors import CORS
from firebase_admin import credentials, db, initialize_app
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
from time import time
import os

MONGO_URL = os.getenv('MONGO_URL')

NEO4J_URL = os.getenv('NEO4J_URL')

NEO4J_USERNAME = os.getenv('NEO4J_USERNAME')

NEO4J_PASSWORD = os.getenv('NEO4J_PASSWORD')

FIREBASE_URL = os.getenv('FIREBASE_URL')

FIREBASE_PATH = os.getenv('FIREBASE_PATH')

PORT = os.getenv('PORT')

cnx = get_mongo_connector(MONGO_URL)

neo4jRepository = Neo4jRepository(get_neo4j_connector(NEO4J_USERNAME,NEO4J_PASSWORD,NEO4J_URL),MongoDBRepository(cnx))

app = Flask(__name__)

CORS(app)

#########################################################################################################################################
########################################################### MONGO METRICS ###############################################################
#########################################################################################################################################

MONGO_FILTER_BY_COUNTER = Counter('mongo_filter_by_counter', 'Description of counter for filtering by paramters')
MONGO_FILTER_BY_HISTOGRAM = Histogram('mongo_filter_by_latency_seconds', 'Description of histogram for latency of requests related to filtering by paramters')
#MONGO_FILTER_BY_TITLE_COUNTER = Counter('mongo_filter_by_title_counter', 'Description of counter for filtering by title')
#MONGO_FILTER_BY_TITLE_HISTOGRAM = Histogram('mongo_filter_by_title_latency_seconds', 'Description of histogram for latency of requests related to filtering by title')

#MONGO_FILTER_BY_CAST_COUNTER = Counter('mongo_filter_by_cast_counter', 'Description of counter for filtering by cast')
#MONGO_FILTER_BY_CAST_HISTOGRAM = Histogram('mongo_filter_by_cast_latency_seconds', 'Description of histogram for latency of requests related to filtering by cast')

#MONGO_FILTER_BY_PLOT_COUNTER = Counter('mongo_filter_by_plot_counter', 'Description of counter for filtering by plot')
#MONGO_FILTER_BY_PLOT_HISTOGRAM = Histogram('mongo_filter_by_plot_latency_seconds', 'Description of histogram for latency of requests related to filtering by plot')

#MONGO_FILTER_BY_DIRECTOR_COUNTER = Counter('mongo_filter_by_director_counter', 'Description of counter for filtering by director')
#MONGO_FILTER_BY_DIRECTOR_HISTOGRAM = Histogram('mongo_filter_by_director_latency_seconds', 'Description of histogram for latency of requests related to filtering by director')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#MONGO_ACTOR_FROM_CAST_IS_ACTOR_COUNTER = Counter('mongo_actor_from_cast_is_actor_counter', 'Description of counter for filtering actors by title')
#MONGO_ACTOR_FROM_CAST_IS_ACTOR_HISTOGRAM = Histogram('mongo_actor_from_cast_is_actor_latency_seconds', 'Description of histogram for latency of requests related to filtering actors by title')

MONGO_ACTOR_FROM_CAST_IS_DIRECTOR_COUNTER = Counter('mongo_actor_from_cast_is_director_counter', 'Description of counter for filtering directors by title')
MONGO_ACTOR_FROM_CAST_IS_DIRECTOR_HISTOGRAM = Histogram('mongo_actor_from_cast_is_director_latency_seconds', 'Description of histogram for latency of requests related to filtering directors by title')

MONGO_DIRECTOR_IS_DIRECTOR_COUNTER = Counter('mongo_director_is_director_counter', 'Description of counter for filtering directors by title')
MONGO_DIRECTOR_IS_DIRECTOR_HISTOGRAM = Histogram('mongo_director_is_director_latency_seconds', 'Description of histogram for latency of requests related to filtering directors by title')

#MONGO_DIRECTOR_IS_ACTOR_COUNTER = Counter('mongo_director_is_actor_counter', 'Description of counter for filtering actors by title')
#MONGO_DIRECTOR_IS_ACTOR_HISTOGRAM = Histogram('mongo_director_is_actor_latency_seconds', 'Description of histogram for latency of requests related to filtering actors by title')


#########################################################################################################################################
########################################################### NEO4J METRICS ###############################################################
#########################################################################################################################################
NEO4J_FILTER_BY_COUNTER = Counter('neo4j_filter_by_counter', 'Description of counter for filtering by paramters')
NEO4J_FILTER_BY_HISTOGRAM = Histogram('neo4j_filter_by_latency_seconds', 'Description of histogram for latency of requests related to filtering by paramters')

#NEO4J_FILTER_BY_TITLE_COUNTER = Counter('neo4j_filter_by_title_counter', 'Description of counter for filtering by title')
#NEO4J_FILTER_BY_TITLE_HISTOGRAM = Histogram('filter_by_title_latency_seconds', 'Description of histogram for latency of requests related to filtering by title')

#NEO4J_FILTER_BY_CAST_COUNTER = Counter('neo4j_filter_by_cast_counter', 'Description of counter for filtering by cast')
#NEO4J_FILTER_BY_CAST_HISTOGRAM = Histogram('neo4j_filter_by_cast_latency_seconds', 'Description of histogram for latency of requests related to filtering by cast')

#NEO4J_FILTER_BY_PLOT_COUNTER = Counter('neo4j_filter_by_plot_counter', 'Description of counter for filtering by plot')
#NEO4J_FILTER_BY_PLOT_HISTOGRAM = Histogram('neo4j_filter_by_plot_latency_seconds', 'Description of histogram for latency of requests related to filtering by plot')

#NEO4J_FILTER_BY_DIRECTOR_COUNTER = Counter('neo4j_filter_by_director_counter', 'Description of counter for filtering by director')
#NEO4J_FILTER_BY_DIRECTOR_HISTOGRAM = Histogram('neo4j_filter_by_director_latency_seconds', 'Description of histogram for latency of requests related to filtering by director')
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
NEO4J_ACTOR_FROM_CAST_IS_ACTOR_COUNTER = Counter('neo4j_actor_from_cast_is_actor_counter', 'Description of counter for filtering actors by title')
NEO4J_ACTOR_FROM_CAST_IS_ACTOR_HISTOGRAM = Histogram('neo4j_actor_from_cast_is_actor_latency_seconds', 'Description of histogram for latency of requests related to filtering actors by title')

#NEO4J_ACTOR_FROM_CAST_IS_DIRECTOR_COUNTER = Counter('neo4j_actor_from_cast_is_director_counter', 'Description of counter for filtering directors by title')
#NEO4J_ACTOR_FROM_CAST_IS_DIRECTOR_HISTOGRAM = Histogram('neo4j_actor_from_cast_is_director_latency_seconds', 'Description of histogram for latency of requests related to filtering directors by title')

NEO4J_DIRECTOR_IS_DIRECTOR_COUNTER = Counter('neo4j_director_is_director_counter', 'Description of counter for filtering directors by title')
NEO4J_DIRECTOR_IS_DIRECTOR_HISTOGRAM = Histogram('neo4j_director_is_director_latency_seconds', 'Description of histogram for latency of requests related to filtering directors by title')

#NEO4J_DIRECTOR_IS_ACTOR_COUNTER = Counter('neo4j_director_is_actor_counter', 'Description of counter for filtering actors by title')
#NEO4J_DIRECTOR_IS_ACTOR_HISTOGRAM = Histogram('neo4j_director_is_actor_latency_seconds', 'Description of histogram for latency of requests related to filtering actors by title')

#########################################################################################################################################
########################################################### GET USERNAME FIREBASE #######################################################
#########################################################################################################################################


# Inicializar Firebase una sola vez al inicio de la aplicación
cred = credentials.Certificate(FIREBASE_PATH)
default_app = initialize_app(cred, {
    'databaseURL': FIREBASE_URL
})

def get_username(uuid):
    try:
        # Asegurarse de que la aplicación ya esté inicializada
        datos = db.reference("/").get()
        name = datos[uuid]['nombre']
        
        return name
    except Exception as e:
        print(f"Error al obtener el nombre de usuario: {e}")
        return None

# ---------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------- MONGO QUERYS ------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------


#########################################################################################################################################
###################################################### FILTER BY TITLE, PLOT, CAST, DIRECTORS ###########################################
#########################################################################################################################################

@app.route('/filter_by_title_mongo/<title>/<plot>/<cast>/<directors>/<userId>', methods=['GET'])
def filter_by_title_mongo(title, plot, cast, directors, userId):
  start_time = time()

  user = get_username(userId)

  prueba = MongoDBRepository(cnx)

  result = jsonify(prueba.getMovies(title, plot, cast, directors, user))
  
  end_time = time()

  MONGO_FILTER_BY_HISTOGRAM.observe(end_time - start_time) 

  MONGO_FILTER_BY_COUNTER.inc()

  return result
  
  
#########################################################################################################################################
############################################################## FILTER BY ACTOR ##########################################################
#########################################################################################################################################

@app.route('/get_movies_by_actor_mongo/<actor>/<userId>', methods=['GET'])
def get_movies_by_actor_director_mongo(actor, userId):
  start_time = time()
    
  user = get_username(userId)
  
  prueba = MongoDBRepository(cnx)
  
  result = jsonify(prueba.getMoviesCast(actor, user))
  
  end_time = time()

  NEO4J_ACTOR_FROM_CAST_IS_ACTOR_HISTOGRAM.observe(end_time - start_time) 

  NEO4J_ACTOR_FROM_CAST_IS_ACTOR_COUNTER.inc()
  
  return result


#########################################################################################################################################
############################################################## FILTER BY DIRECTORS ######################################################
#########################################################################################################################################

@app.route('/get_movies_by_director_mongo/<director>/<userId>', methods=['GET'])
def get_movies_by_director_mongo(director, userId):
  start_time = time()

  user = get_username(userId)

  prueba = MongoDBRepository(cnx)

  result = jsonify(prueba.getMoviesDirector(director, user))
  
  end_time = time()

  NEO4J_DIRECTOR_IS_DIRECTOR_HISTOGRAM.observe(end_time - start_time) 

  NEO4J_DIRECTOR_IS_DIRECTOR_COUNTER.inc()
  
  return result



# ---------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------- NEO4J QUERYS ------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------


#########################################################################################################################################
###################################################### FILTER BY TITLE, PLOT, CAST, DIRECTORS ###########################################
#########################################################################################################################################

@app.route('/filter_by_neo4j/<title>/<plot>/<cast>/<directors>/<userId>', methods=['GET'])
def filter_by_neo4j(title, plot, cast, directors,userId):
  start_time = time()

  user = get_username(userId)
  
  result = jsonify(neo4jRepository.buscarPeliculasTodosLosFiltros(title,plot,cast,directors,user))
  
  end_time = time()

  NEO4J_FILTER_BY_COUNTER.inc()
  
  NEO4J_FILTER_BY_HISTOGRAM.observe(end_time - start_time) 
  
  return result

#########################################################################################################################################
############################################################## FILTER BY ACTOR ##########################################################
#########################################################################################################################################

@app.route('/search_acted_movies_neo4j/<actor>/<userId>', methods=['GET'])
def search_acted_movies_neo4j(actor,userId):
  start_time = time()

  user = get_username(userId)

  result = jsonify(neo4jRepository.getPeliculasActuadas(actor,user))

  end_time = time()

  NEO4J_ACTOR_FROM_CAST_IS_ACTOR_HISTOGRAM.observe(end_time - start_time) 

  NEO4J_ACTOR_FROM_CAST_IS_ACTOR_COUNTER.inc()
   
  return result


#########################################################################################################################################
############################################################## FILTER BY DIRECTORS ######################################################
#########################################################################################################################################

@app.route('/search_directed_movies_neo4j/<director>/<userId>', methods=['GET'])
def search_directed_movies_neo4j(director,userId):
  start_time = time()
  
  user = get_username(userId)
    
  result = jsonify(neo4jRepository.getPeliculasDirigidas(director,user))
  
  end_time = time()

  NEO4J_DIRECTOR_IS_DIRECTOR_HISTOGRAM.observe(end_time - start_time) 

  NEO4J_DIRECTOR_IS_DIRECTOR_COUNTER.inc()

  return result

# ---------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------- PROMETHEUS METRICS ------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------

@app.route('/metrics', methods=['GET'])
def prometheus_metrics():
  return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
  app.run(port=int(PORT))
