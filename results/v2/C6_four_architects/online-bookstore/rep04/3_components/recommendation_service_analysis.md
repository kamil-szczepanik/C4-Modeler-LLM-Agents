## Overview
[The Online Bookstore is a scaled-down Amazon-style e-commerce site for physical and electronic books with recommendations and reviews. Its core purpose is to provide scalable, low-latency book discovery, purchasing, and personalization capabilities on AWS.]

## Key Elements
- Recommendation API Controller (FastAPI)
- Scoring Engine (Python / NumPy / Pandas)
- Model Ingestion Worker (Python / Celery)
- Recommendation Cache Client (Redis-py)
- Feature Store / Vector DB Client
- Telemetry Interceptor Middleware
- Amazon ElastiCache (Redis)
- Amazon OpenSearch
- Amazon SQS

## Relationships
- Recommendation API Controller calls Scoring Engine [In-memory function call]
- Scoring Engine reads from Recommendation Cache Client [Redis TCP / RESP]
- Scoring Engine queries Feature Store Client [REST/HTTPS]
- Model Ingestion Worker consumes events from Amazon SQS [AWS SDK / HTTPS]
- Model Ingestion Worker writes to Recommendation Cache Client [Redis TCP / RESP]
- Telemetry Interceptor Middleware emits traces to AWS X-Ray and metrics to Amazon CloudWatch [AWS SDK / HTTPS]

## Technology Stack
- Python / FastAPI: High-performance asynchronous API framework for handling inbound gRPC requests.
- NumPy / Pandas: Optimized libraries for in-memory collaborative filtering and scoring logic.
- Amazon ElastiCache (Redis): In-memory data store for sub-second recommendation retrieval to meet performance SLAs.
- Amazon OpenSearch: Vector database and feature store for semantic similarity book recommendations.
- Amazon SQS: Message queue for asynchronously decoupling order events from the model ingestion pipeline.

## Rationale
[This architecture uses in-memory caching and vector search to deliver sub-second recommendations, meeting strict performance and scalability constraints. Asynchronous event ingestion via SQS decouples the ML pipeline from transactional databases, ensuring high availability and system resilience.]