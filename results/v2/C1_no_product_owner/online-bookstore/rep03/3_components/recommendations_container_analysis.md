## Overview
The Recommendations Container provides real-time, personalized book recommendations for the Online Bookstore using an isolated microservice architecture. It ensures low-latency responses and high availability for up to 1 million monthly active users.

## Key Elements
- **Recommendation API Router**: FastAPI component handling REST endpoints and Pydantic input validation.
- **Cache Manager**: Orchestrates cache-aside logic for high-performance data retrieval.
- **Scoring Engine**: Python and NumPy component executing co-purchase algorithms.
- **Recommendation Repository**: SQLAlchemy-based data access layer.
- **Amazon ElastiCache (Redis)**: In-memory cache for hot co-purchase lists.
- **Amazon Aurora PostgreSQL Read Replica**: Dedicated database read-replica for offline-computed associations.
- **Amazon ECS (AWS Fargate)**: Serverless container deployment platform with auto-scaling.

## Relationships
- **API Gateway** -> **Recommendation API Router**: Routes recommendation requests [gRPC/REST over VPC internal load balancers].
- **Recommendation API Router** -> **Cache Manager**: Delegates validated requests [In-memory / TCP].
- **Cache Manager** -> **Amazon ElastiCache (Redis)**: Reads and writes cached recommendation payloads [TCP].
- **Cache Manager** -> **Scoring Engine**: Executes fallback scoring on cache misses [In-process].
- **Cache Manager** -> **Recommendation Repository**: Populates cache on misses [SQL via psycopg3].
- **Recommendation Repository** -> **Amazon Aurora PostgreSQL Read Replica**: Fetches pre-aggregated associations [TLS 1.3].

## Technology Stack
- **Python / FastAPI**: Core language and framework for building lightweight, asynchronous REST APIs with automatic schema validation.
- **NumPy**: Powers fast mathematical matrix operations for collaborative filtering.
- **Amazon ElastiCache (Redis)**: Provides sub-50ms caching to meet performance SLAs under peak loads.
- **Amazon Aurora PostgreSQL**: Dedicated read-replica providing isolated data access without cross-container contention.
- **Amazon ECS (AWS Fargate)**: Serverless orchestration enabling automatic scaling based on CPU and request metrics.
- **AWS Secrets Manager**: Securely injects database credentials and Redis tokens at runtime.

## Rationale
This architecture offloads heavy model training to offline cron jobs while utilizing a Redis caching layer and dedicated database read-replica to guarantee sub-2-second page loads. Isolating data dependencies and employing circuit breaker patterns ensures 99.95% availability under high concurrent traffic.