## Overview
The Recommendation Engine container generates AI-powered 'Customers also bought' suggestions for the Online Bookstore. It uses a decoupled micro-architecture to deliver real-time recommendations under high traffic loads.

## Key Elements
- **API Controller**: FastAPI (Python) service handling incoming requests.
- **Model Inference Worker**: PyTorch (Python) worker executing scoring logic.
- **Feature Cache Client**: Redis-py client fetching pre-computed user/item embeddings.
- **Data Ingestion Consumer**: Kafka Python client consuming clickstream and purchase events.
- **Fallback Engine**: Heuristic rule component for handling timeouts.
- **Model Registry Client**: AWS SageMaker client for dynamic weight hot-reloading.

## Relationships
- **API Controller** -> **Model Inference Worker**: Invokes scoring logic [In-process / Asyncio]
- **Model Inference Worker** -> **Feature Cache Client**: Retrieves user preference vectors [TCP / Redis Protocol]
- **Model Inference Worker** -> **Amazon DynamoDB**: Fetches fallback recommendation metadata [TLS]
- **Amazon MSK** -> **Data Ingestion Consumer**: Streams real-end user interaction events [TCP / Kafka Protocol]
- **API Controller** -> **Fallback Engine**: Queries fallback rules on cache/inference timeout [In-process]
- **Model Inference Worker** -> **Model Registry Client**: Polls/fetches updated model artifacts [HTTPS / S3]
- **Data Ingestion Consumer** -> **Amazon DynamoDB**: Persists processed interaction features [TLS]

## Technology Stack
- **FastAPI (Python)**: Chosen for high-performance asynchronous API handling.
- **PyTorch (Python)**: Selected for executing collaborative filtering and NLP models.
- **Amazon ElastiCache (Redis)**: Utilized for sub-10ms feature cache retrieval.
- **Amazon MSK**: Deployed for scalable real-time event streaming.
- **AWS SageMaker Model Registry**: Used for zero-downtime model artifact management.

## Rationale
This architecture ensures sub-2-second page loads and high availability under 1M MAU by isolating memory-heavy inference routines. Asynchronous event ingestion and resilient fallback mechanisms prevent bottlenecks and guarantee uninterrupted service.