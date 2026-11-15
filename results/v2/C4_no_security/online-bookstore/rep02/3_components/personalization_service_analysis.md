## Overview
The Personalization Service provides real-time book recommendations and manages user preference vectors for the Online Bookstore. It is designed to scale to 1M MAU while ensuring strict GDPR/CCPA compliance and sub-second performance.

## Key Elements
- **Recommendation API Router** (Python / FastAPI)
- **Recommendation Engine** (Python / NumPy / scikit-learn)
- **Event Consumer Worker** (Python / Celery)
- **Data Access Layer** (Python / boto3)
- **Amazon DynamoDB** (Multi-region Global Tables)
- **Amazon SQS** (Event ingestion queue)
- **Amazon ElastiCache (Redis)** (Region-local caching)
- **AWS CloudWatch / Datadog** (Telemetry and alerts)

## Relationships
- **AWS API Gateway** -> **Recommendation API Router**: Routes synchronous queries [Internal HTTPS / gRPC]
- **Recommendation API Router** -> **Recommendation Engine**: Triggers inference [In-memory function call with 200ms timeout]
- **Recommendation Engine** -> **Data Access Layer**: Fetches user profiles [Python / boto3]
- **Event Consumer Worker** -> **Amazon SQS**: Consumes clickstream events [AWS SDK / Long-polling]
- **Data Access Layer** -> **Amazon DynamoDB**: Reads/writes vectors and executes purges [HTTPS / AWS SDK]
- **Data Access Layer** -> **Amazon ElastiCache (Redis)**: Caches user profiles locally [TCP / Redis Protocol]
- **All Components** -> **AWS CloudWatch/Datadog**: Emits telemetry and metrics [HTTPS]

## Technology Stack
- **Python (FastAPI/Celery)**: Core framework for asynchronous event processing and high-performance routing.
- **NumPy & scikit-learn**: Libraries powering collaborative filtering and recommendation heuristics.
- **Amazon DynamoDB**: NoSQL database utilized for fast profile lookups and global replication.
- **Amazon SQS & EventBridge**: Messaging infrastructure ensuring resilient event delivery.
- **Amazon ElastiCache (Redis)**: Caching layer minimizing cross-region latency and absorbing traffic spikes.

## Rationale
This architecture decouples synchronous API traffic from asynchronous ML event processing to guarantee sub-second page loads. Furthermore, multi-region DynamoDB Global Tables, Redis caching, and circuit breakers ensure 99.95% uptime and strict GDPR/CCPA compliance.