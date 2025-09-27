# Movie Search & Analytics Platform

## Descripción General
Una plataforma web que simula una interfaz móvil y permite a los usuarios buscar y explorar películas utilizando las bases de datos MongoDB Atlas (documentos) y Neo4J (grafos). La plataforma proporciona información detallada de películas y consultas relacionales basadas en actores y directores. El backend es una API REST en Python desarrollada con Flask, y el sistema usa Firebase para la autenticación. La solución está desplegada con Docker, Kubernetes y Helm Charts, y es monitoreada con Prometheus y Grafana.

## Funcionalidades
- Búsqueda de películas en MongoDB Atlas y Neo4J por título, reparto, trama y directores.  
- Visualización de información detallada de películas y datos relacionales (actores/directores).  
- Autenticación y autorización de usuarios mediante Firebase.  
- Registro de todas las solicitudes a la API en MongoDB para análisis (incluye cuerpo de la solicitud, marca de tiempo y usuario).  
- Arquitectura de microservicios desplegada en Kubernetes con contenedores Docker.  
- Monitoreo en tiempo real con métricas de Prometheus y tableros de Grafana (conteo de solicitudes y tiempo de respuesta).  

## Tecnologías
- Lenguajes y Frameworks: Python, Flask  
- Bases de Datos: MongoDB Atlas (documentos), Neo4J (grafos)  
- DevOps & Despliegue: Docker, Kubernetes, Helm Charts  
- Monitoreo: Prometheus, Grafana  
- Autenticación: Firebase  
- Otros: Ngrok para exponer endpoints de la API localmente  

## Arquitectura
1. **API REST en Python**  
   - Maneja las solicitudes de la interfaz web  
   - Se comunica con MongoDB y Neo4J  
   - Autentica usuarios con Firebase  
   - Registra solicitudes en MongoDB para análisis  

2. **Bases de Datos**  
   - MongoDB Atlas: almacena datos de películas en formato documento  
   - Neo4J: almacena datos relacionales de actores y directores  

3. **Interfaz Web**  
   - Simula la experiencia de una aplicación móvil  
   - Envía consultas a la API y muestra la información de las películas  

4. **Despliegue y Monitoreo**  
   - Contenedores Docker orquestados con Kubernetes  
   - Arquitectura de microservicios para escalabilidad y resiliencia  
   - Prometheus monitorea los endpoints de la API y métricas de MongoDB  
   - Grafana visualiza métricas como número de solicitudes y tiempos de respuesta  
