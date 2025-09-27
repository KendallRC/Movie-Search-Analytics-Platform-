from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask import jsonify
from bson.json_util import dumps
from datetime import datetime
import json


# ----------------------------------------------------------- CLASE MONGO DB -------------------------------------------------------------------


class MongoDBRepository:

    def __init__(self, client):
        self.client = client
        # Select the database and collection
        self.db = client["sample_mflix"]
        self.collection = self.db["movies"]


    

    # ---------------------------------------------- OBTENER LAS PELICULAS POR ACTOR -------------------------------------------------

    def getMoviesCast(self, cast, user):

        

        query = {
            "$search": {
                "index": "Movies",
                "text": { "query": cast, "path": "cast" } 
            
            }
        }
            # Ejecutar la consulta en Atlas Search
        results = self.collection.aggregate([query])

        results = [json.loads(json.dumps(doc, default=str)) for doc in results]

        #documentos_json = [doc for doc in results]

        # Mostrar los resultados
        for result in results:
            result['timestamp'] = datetime.now()
            del result["_id"]
            result["user"] = user
            self.insertDataLogs(result)
            del result["_id"]
        
        return results

    # ---------------------------------------------- OBTENER LAS PELICULAS POR DIRECTOR -------------------------------------------------

    def getMoviesDirector(self, director, user):

        query = {
            "$search": {
                "index": "Movies",
                "text": { "query": director, "path": "directors" } 
            }
        }

        
            # Ejecutar la consulta en Atlas Search
        results = self.collection.aggregate([query])

        results = [json.loads(json.dumps(doc, default=str)) for doc in results]

        #documentos_json = [doc for doc in results]

        # Mostrar los resultados
        for result in results:
            result['timestamp'] = datetime.now()
            result["user"] = user
            self.insertDataLogs(result)
            del result["_id"]
        
        return results



    # ------------------------------------- OBTENER LAS PELICULAS POR PLOD | TITLE | CAST | DIRECTOR ----------------------------------------------


    def getMovies(self, title, plot, cast, director, user):

        query = {
            "$search": {
                "index": "Movies",
                "compound": {
                    "must": [                  
                    ]
                }
            },
            
        }

        # Verificar si titulo está vacío, y si no realizo la busqueda por titulo

        if title != "'":
            query["$search"]["compound"]["must"].append({ "text": { "query": title, "path": "title" } })

        # Verificar si plot está vacío, y si no realizo la busqueda por plot

        if plot != "'":    
            query["$search"]["compound"]["must"].append({ "text": { "query": plot, "path": "plot" } })
        
        # Verificar si cast está vacío, y si no realizo la busqueda por cast

        if cast != "'":
            query["$search"]["compound"]["must"].append({ "text": { "query": cast, "path": "cast" } })

        # Verificar si director está vacío, y si no realizo la busqueda por director

        if director != "'":
            query["$search"]["compound"]["must"].append({ "text": { "query": director, "path": "directors" } })

        
        results = self.collection.aggregate([query])

        results = [json.loads(json.dumps(doc, default=str)) for doc in results]
    
        # Mostrar los resultados
        for result in results:
            del result["_id"]
            result['timestamp'] = str(datetime.now())
            result["user"] = user
            self.insertDataLogs(result)
            del result["_id"]
            
        return results
        



    # ---------------------------------------------- INSERTAR DATOS EN COLECCTION LOGS -------------------------------------------------

    def insertDataLogs(self, json):


        db = self.client["Logs"]
        collection = db["Logs"]  # Nombre de la colección

        # Insertar un solo documento
        collection.insert_one(json)
