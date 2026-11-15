## Overview
The system is an Amazon-style online bookstore providing product catalogs, secure checkout, reviews, and personalized recommendations. The architecture uses microservices deployed on AWS to ensure scalability and compliance across multiple global regions.

## Key Elements
- **Recommendation Service**: Python FastAPI container deployed on AWS ECS Fargate
- **API Router**: FastAPI component handling incoming gRPC/HTTP routing
- **Model Loader**: Component fetching artifacts from AWS S3 using AWS SDK
- **Recommendation Engine**: Core logic for collaborative filtering using NumPy and Pandas
- **Cache & Persistence Repository**: Amazon ElastiCache (Redis) storing pre-computed recommendations
- **Event Consumer**: Background worker processing clickstream and purchase events from AWS SQS
- **External Systems**: AWS S3, Amazon ElastiCache, AWS SQS, AWS KMS

## Relationships
- API Gateway & ALB -> API Router: Routes requests via App Mesh sidecars [gRPC over mTLS]
- API Router -> Cache Repository: Reads pre-computed lists [Redis Protocol over TLS]
- Model Loader -> S3 Bucket: Fetches model artifacts [HTTPS / AWS SDK]
- Event Consumer -> Async Event Bus (AWS SQS): Consumes user events [AWS SDK / HTTPS]

## Technology Stack
- **Python / FastAPI**: Core framework for high-performance async request handling
- **AWS ECS Fargate**: Serverless container execution for scalable deployments
- **Amazon ElastiCache (Redis)**: In-memory store for sub-millisecond recommendation retrieval
- **AWS S3**: Secure object storage for heavy recommendation model artifacts
- **AWS KMS**: Cryptographic key management for encryption at rest

## Rationale
This containerized microservices architecture handles high concurrent user loads while meeting strict performance targets. Distributed caching and decoupled model loading ensure low latency, high availability, and global compliance.