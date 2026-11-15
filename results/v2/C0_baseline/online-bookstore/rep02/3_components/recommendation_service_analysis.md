## Overview
The Online Bookstore is a globally scaled e-commerce system that delivers book purchasing, reviews, and personalized recommendations. Its core purpose is to provide a robust, compliant retail platform handling 1M MAU across multiple cloud regions.

## Key Elements
- **Users**: Registered Shoppers, Customers, Store Administrators
- **Containers**: Single Page Application (React/TypeScript via CloudFront/S3), API Gateway (Amazon API Gateway, AWS App Mesh), Recommendation Service (Python, FastAPI), Amazon DynamoDB
- **Components**: Recommendation Controller, Recommendation Aggregator, User Preference Cache (AWS ElastiCache Redis)
- **External Systems**: Recommendation Engine, Identity Provider, Payment Gateway, Shipping Provider

## Relationships
- API Gateway -> Recommendation Controller: Routes REST/GraphQL requests [mTLS]
- Recommendation Controller -> Recommendation Aggregator: Delegates logic [In-process calls]
- Recommendation Aggregator -> User Preference Cache: Reads/writes vectors [Redis TCP via TLS]
- Recommendation Aggregator -> Amazon DynamoDB: Persists history [AWS SDK / HTTPS]
- Recommendation Aggregator -> Recommendation Engine: Fetches ML suggestions [HTTPS]

## Technology Stack
- **Backend**: Python with FastAPI for low-latency recommendation processing
- **Caching**: AWS ElastiCache (Redis) with Global Datasets for active-passive multi-region replication
- **Database**: Amazon DynamoDB for scalable user interaction history
- **Compute**: Amazon ECS on AWS Fargate with auto-scaling policies
- **Security/Compliance**: AWS KMS (AES-256) for encryption at rest, AWS Secrets Manager for credentials, AWS IAM for least privilege access

## Rationale
This architecture uses a resilient microservices design with circuit breakers, fallbacks, and multi-region deployment to satisfy high availability (99.95% uptime) and performance constraints. Automated data erasures and KMS encryption ensure strict GDPR and CCPA compliance.