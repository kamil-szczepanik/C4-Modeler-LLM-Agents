## Overview
The Recommendation & Search Service is a Python-based microservice within the Online Bookstore that delivers product search and personalized recommendations. It operates on AWS ECS Fargate across three global regions to support 1 million MAU with low latency.

## Key Elements
- **API Controller Component**: FastAPI app handling incoming gRPC requests, JWT validation, and schema checks.
- **Search Engine Component**: Translates user queries into OpenSearch DSL queries with input sanitization.
- **Recommendation Engine Component**: Computes collaborative filtering heuristics and manages a circuit breaker.
- **Catalog Sync Consumer Component**: Processes domain events asynchronously from SQS to update search indices.
- **Amazon OpenSearch**: Managed search cluster storing book catalog and search indexes.
- **Amazon ElastiCache Redis**: In-memory data store caching precomputed recommendation vectors.
- **Amazon SQS / SNS**: Messaging infrastructure with Dead Letter Queues (DLQs) for asynchronous catalog synchronization.

## Relationships
- **API Gateway** -> **API Controller**: Routes search and recommendation queries [gRPC with JWT over internal VPC]
- **API Controller** -> **Search Engine & Recommendation Engine**: Delegates execution flows [In-process async calls via Python `asyncio`]
- **Search Engine** -> **Amazon OpenSearch**: Queries index [HTTPS/REST with SigV4 and mTLS]
- **Recommendation Engine** -> **Amazon ElastiCache Redis**: Fetches cached vectors [Redis Protocol with TLS via `redis-py`]
- **Catalog Sync Consumer** -> **Amazon SQS**: Consumes catalog update events [AWS SDK]
- **Catalog Sync Consumer** -> **Amazon OpenSearch**: Updates document indices [HTTPS/REST]

## Technology Stack
- **Python & FastAPI**: Chosen for the service runtime and API layer due to rapid development and robust asynchronous support.
- **NumPy & SciPy**: Utilized for mathematical vector computations in the recommendation heuristics.
- **AWS ECS Fargate**: Serverless container orchestration allowing independent auto-scaling based on CPU/memory bottlenecks.
- **Amazon OpenSearch**: Provides faceted search capabilities with cross-cluster replication across regions.
- **Amazon ElastiCache Redis**: Delivers low-latency access to hot recommendation vectors.

## Rationale
Isolating CPU-heavy vector calculations from I/O-bound API routing within AWS ECS Fargate enables independent auto-scaling and protects the 2-second page load performance goal. Multi-region OpenSearch deployment ensures low-latency global search performance while meeting strict uptime and security constraints.