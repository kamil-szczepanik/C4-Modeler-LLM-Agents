## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with integrated recommendations and reviews. The Recommendation Service component specifically provides high-performance book suggestions using asynchronous processing to meet strict scalability and latency targets.

## Key Elements
- Recommendation API Controller (Python FastAPI)
- Recommendation Engine Core (Python)
- Cache Repository (Python, `redis-py`)
- Event Consumer (Python, Celery / SQS Worker)
- Async Model Updater (Python, Celery Worker)
- External dependencies: API Gateway, Amazon ElastiCache (Redis), Amazon SQS

## Relationships
- API Gateway -> Recommendation API Controller: Routes requests [gRPC over HTTP/2]
- Recommendation API Controller -> Recommendation Engine Core: In-process function calls
- Recommendation Engine Core -> Cache Repository: Data lookup [TCP / Redis protocol]
- Amazon SQS -> Event Consumer: Pulls order completion events [HTTPS / SQS SDK]
- Event Consumer -> Cache Repository: Invalidates and updates cache [TCP / Redis protocol]
- Async Model Updater -> Cache Repository: Bulk updates pre-computed results [TCP / Redis protocol]

## Technology Stack
- Python FastAPI: High-performance framework for handling incoming API requests.
- Amazon ElastiCache (Redis): In-memory caching for sub-2-second page load performance (R-06).
- Celery / Amazon SQS: Asynchronous messaging and background worker execution to decouple heavy ML computations from the request path.
- `redis-py`: Python client for efficient cache repository interactions.

## Rationale
Decoupling heavy machine learning computations from synchronous request handling ensures the system scales smoothly for 1 million monthly active users (R-05). Utilizing in-memory caching and background workers guarantees high availability (R-07) and performance SLAs (R-06).