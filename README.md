# Movie Search & Analytics Platform

## Overview
A web-based platform simulating a mobile interface that allows users to search and explore movies using MongoDB Atlas (document) and Neo4J (graph) databases. The platform provides detailed information about movies and relational queries based on actors and directors. The backend is a Python REST API built with Flask, and the platform uses Firebase for authentication. The system is deployed with Docker, Kubernetes, and Helm Charts, and is monitored with Prometheus and Grafana.

## Features
- Search movies across MongoDB Atlas and Neo4J databases by title, cast, plot, and directors.  
- Display detailed movie information and relational data (actors/directors).  
- User authentication and authorization via Firebase.  
- Logging of all API requests in MongoDB for analytics (includes request body, timestamp, and user).  
- Microservices architecture deployed on Kubernetes with Docker containers.  
- Real-time monitoring with Prometheus metrics and Grafana dashboards (request count and response time).  

## Technologies
- Programming Languages & Frameworks: Python, Flask  
- Databases: MongoDB Atlas (document), Neo4J (graph)  
- DevOps & Deployment: Docker, Kubernetes, Helm Charts  
- Monitoring: Prometheus, Grafana  
- Authentication: Firebase  
- Other: Ngrok for exposing local API endpoints externally  

## Architecture
1. Python REST API  
   - Handles requests from the web-based interface  
   - Communicates with both MongoDB and Neo4J  
   - Authenticates users with Firebase  
   - Logs requests in MongoDB for analytics  

2. Databases  
   - MongoDB Atlas: stores movie data in document format  
   - Neo4J: stores relational data about actors and directors  

3. Web Interface  
   - Simulates a mobile app interface  
   - Sends queries to API and displays movie information  

4. Deployment & Monitoring  
   - Docker containers orchestrated with Kubernetes  
   - Microservices architecture for scalability and resilience  
   - Prometheus monitors API endpoints and MongoDB metrics  
   - Grafana dashboards display request counts and response times  