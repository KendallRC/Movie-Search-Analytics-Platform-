import unittest
from config.neo4j_connector import get_neo4j_connector
from config.mongo_connector import get_mongo_connector

class TestStringMethods(unittest.TestCase):

    def test_updateDoc(self):
        self.assertIsNotNone(get_neo4j_connector("movies","movies","neo4j+s://demo.neo4jlabs.com:7687"))

    def test_cnxMongo(self):
        self.assertIsNotNone(get_mongo_connector("mongodb+srv://kendall:1234@cluster0.qw1evub.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"))

if __name__ == '__main__':
    unittest.main()