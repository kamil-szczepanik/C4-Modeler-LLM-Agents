## Overview
- Microservice container managing customer reviews, 5-star ratings, helpful votes, and moderation for the online bookstore.
- Designed for high write-availability, low-latency reads, and global scalability to support 1M MAU.

## Key Elements
- **Review API Router:** FastAPI component handling HTTP/gRPC requests, JWT validation, and Pydantic input sanitization.
- **Moderation Service:** Automated NLP/AWS Comprehend pipeline for profanity and sentiment filtering.
- **Vote Processor:** Isolated component handling atomic helpful votes and anti-sybil checks.
- **Rating Aggregator:** Asynchronous background worker using AWS SQS.
- **Review Data Access Layer:** Boto3 client interfacing with Amazon DynamoDB.
- **Read Caching Layer:** Amazon ElastiCache (Redis) cluster.
- **Infrastructure:** AWS ECS with AWS Fargate across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Relationships
- API Gateway -> Review API Router: Routes requests via gRPC over mTLS
- Review API Router -> Moderation Service: Internal in-memory calls
- Review API Router -> Vote Processor: Internal in-memory calls
- Vote Processor & Review Data Access Layer -> Amazon DynamoDB: TCP over AWS PrivateLink with KMS encryption
- Rating Aggregator -> AWS SQS: Asynchronous messaging
- Review Data Access Layer -> Amazon ElastiCache (Redis): Read-through caching over TLS

## Technology Stack
- **Python / FastAPI:** High-performance asynchronous API framework with native Pydantic schema validation.
- **Amazon DynamoDB:** NoSQL database with Global Tables and Global Secondary Indexes (`BookID-HelpfulVotes-Index`, `BookID-Rating-Index`) for sub-50ms queries.
- **Amazon ElastiCache (Redis):** In-memory caching for aggregated ratings to maintain <2s page loads.
- **AWS SQS:** Asynchronous event queue preventing write-lock contention.
- **AWS ECS / Fargate:** Serverless container orchestration for multi-region deployment.
- **AWS KMS:** Encryption at rest for GDPR/CCPA compliance and data protection.

## Rationale
- Decouples review writes, rating aggregation, and helpful voting using asynchronous queues and isolated components to prevent performance degradation under peak load.
- Combines DynamoDB Global Tables, Redis caching, and multi-region Fargate deployment to ensure 99.95% availability, strict global compliance, and sub-second response times.