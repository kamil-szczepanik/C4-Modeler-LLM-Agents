## Overview
The Recommendation Service is a Python/FastAPI microservice within the Online Bookstore that generates AI-driven personalized book recommendations. It provides scalable, low-latency 'Customers also bought' suggestions for 1M MAU.

## Key Elements
* Recommendation API Controller (FastAPI): Handles incoming REST requests over HTTPS from the API Gateway.
* Recommendation Engine Core (Python, NumPy, Scikit-learn): Executes collaborative filtering algorithms.
* Cache Repository (Redis Client): Interfaces with Amazon Redis via TCP for hot recommendations.
* Data Enrichment Client (httpx): Fetches real-time book metadata from the Catalog Service.
* Event Consumer (SQS Worker): Consumes order and clickstream events asynchronously from Amazon SQS.
* Offline Training Pipeline (AWS SageMaker Job): Computes model weights and embeddings.
* Model Loader / Feature Store Client: Fetches serialized models and embeddings from Amazon S3 over HTTPS.

## Relationships
* API Gateway -> Recommendation API Controller: Routes REST requests [HTTPS]
* Recommendation API Controller -> Cache Repository: Queries hot recommendations [TCP / Redis Protocol]
* Recommendation Engine Core -> Data Enrichment Client: Fetches book metadata [HTTP/REST]
* Recommendation Engine Core -> Model Loader / Feature Store Client: Retrieves embeddings [HTTPS / S3 API]
* Event Consumer -> Amazon SQS: Consumes real-time interaction updates [AMQP / HTTPS]

## Technology Stack
* Python & FastAPI: High asynchronous performance suitable for ML inference routing.
* Amazon Redis: Sub-millisecond retrieval of cached recommendations to meet performance NFRs.
* AWS SageMaker & Amazon S3: Offloads heavy batch ML training to prevent real-time resource starvation.
* Amazon SQS: Decoupled event ingestion for real-time model updates.

## Rationale
This architecture separates fast-path caching, asynchronous event ingestion, and decoupled batch training to guarantee high availability and sub-second response times. It ensures the system meets strict performance, scalability, and security constraints under peak load.