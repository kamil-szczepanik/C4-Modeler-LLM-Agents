## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site for buying physical and electronic books with recommendations and reviews. This architecture defines the internal component structure of the Recommendation Service container to deliver AI-driven book suggestions.

## Key Elements
- **API Router**: FastAPI Router (Python) handling incoming requests.
- **Recommendation Engine**: Scikit-learn / PyTorch Light (Python) for inference and similarity computation.
- **Feature Store Client**: Redis Client (Python) fetching user interaction history.
- **Vector DB Repository**: Pinecone / pgvector client (Python) querying book embeddings.
- **Embedding Sync Worker**: Celery / Python Background Task (Python) updating item embeddings asynchronously.

## Relationships
- API Gateway -> API Router: Routes recommendation queries [gRPC / HTTP]
- API Router -> Recommendation Engine: Delegates scoring logic [In-process / Python function calls]
- Recommendation Engine -> Feature Store Client: Retrieves user context [TCP / Redis Protocol]
- Recommendation Engine -> Vector DB Repository: Queries book embeddings [gRPC]
- Background Worker -> Embedding Sync Worker: Publishes catalog change events [AWS SQS / AMQP]
- Embedding Sync Worker -> Vector DB Repository: Upserts book embeddings [gRPC]

## Technology Stack
- **Python FastAPI**: Core framework chosen for high-performance async request handling.
- **Scikit-learn / PyTorch Light**: Machine learning libraries selected for fast similarity matrix computation and inference.
- **Redis Client**: Enables low-latency retrieval of user context from the cache layer.
- **Pinecone / pgvector**: Vector database client chosen for efficient similarity search over book embeddings.
- **Celery**: Background task runner used for asynchronous embedding synchronization.

## Rationale
This component-level architecture ensures the Recommendation Service scales to support 1M MAU while maintaining sub-2-second page loads. Decoupling the inference engine from data access and offline ingestion layers guarantees high availability and performance.