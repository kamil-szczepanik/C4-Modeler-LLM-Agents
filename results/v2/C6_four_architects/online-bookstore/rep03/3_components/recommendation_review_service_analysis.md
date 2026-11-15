## Overview
The Recommendation & Review Service delivers personalized book recommendations and customer reviews for the Online Bookstore. It processes high-throughput asynchronous events and low-latency queries to support 1 million monthly active users.

## Key Elements
- API Router / Controller (FastAPI)
- Review & Rating Manager (FastAPI / SQLAlchemy / asyncpg)
- Recommendation Engine Client (Python SDK)
- Caching & Aggregation Layer (async-lru / Redis client)
- Event Consumer Worker (Python / boto3)
- Amazon RDS (PostgreSQL)
- Amazon ElastiCache (Redis)
- AWS Personalize
- Amazon SQS

## Relationships
- API Router -> Review & Rating Manager: In-process method calls
- API Router -> Recommendation Engine Client: In-process method calls
- Review & Rating Manager -> Amazon RDS (PostgreSQL): SQL over TLS [TCP 5432] via asyncpg connection pooling
- Review & Rating Manager -> Amazon ElastiCache (Redis): Caches rating aggregates and review snippets [Redis RESP over TLS]
- Recommendation Engine Client -> AWS Personalize: Fetches personalized recommendations [HTTPS]
- Recommendation Engine Client -> Amazon ElastiCache (Redis): Caches recommendation payloads [Redis RESP over TLS]
- Amazon SQS -> Event Consumer Worker: Polls asynchronous events [HTTPS / SQS Long Polling]
- Event Consumer Worker -> Review & Rating Manager: Internal async method calls

## Technology Stack
- Python with FastAPI: Chosen for native asynchronous support, high-throughput I/O handling, and seamless machine learning ecosystem integration.
- SQLAlchemy with `asyncpg`: Provides non-blocking database operations and connection pooling to prevent connection exhaustion.
- Amazon ElastiCache (Redis): Offloads database read traffic by caching review aggregates and recommendation payloads.
- AWS Personalize: Managed ML service powering "Customers also bought" recommendations.
- Amazon SQS: Decouples asynchronous event consumption from synchronous request paths to maintain high availability.

## Rationale
This component architecture isolates machine learning integrations and separates synchronous request handling from asynchronous background processing. These design decisions ensure sub-second response times and 99.95% availability under high concurrent load.