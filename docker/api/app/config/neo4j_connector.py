from neo4j import GraphDatabase


def get_neo4j_connector(username, password, url):
  
  try:
      cnx = GraphDatabase.driver(url, auth=(username, password))
      cnx.verify_connectivity()
      
      return cnx

  except Exception as e:
      print(e)
      
      return None
