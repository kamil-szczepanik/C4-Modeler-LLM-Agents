## Overview
The Recommendation Service is a high-performance Python-based microservice that generates personalized "Customers also bought" suggestions for the Online Bookstore. It ensures low-latency reads, GDPR compliance, and business conversion growth across multiple global regions.

## Key Elements
- Recommendation API Router (FastAPI)
- Scoring Engine (Python/NumPy)
- Model Ingestion Worker (Python)
- Data Access Repository (boto3)
- Fallback Handler Component
- Amazon DynamoDB (with Global Tables and TTL)
- Amazon SQS

## Relationships
- API Gateway -> Recommendation API Router: HTTPS / mTLS via AWS App Mesh
- Recommendation API Router -> Scoring Engine: In-process Python call
- Recommendation API Router -> Data Access Repository: Read cached scores / TCP / AWS SDK
- Data Access Repository -> Amazon DynamoDB: Low-latency read/write / HTTPS / AWS SDK
- Amazon SQS -> Model Ingestion Worker: Consume clickstream/order events / AMQP / AWS SDK

## Technology Stack
- Python (FastAPI): Chosen for high-performance async request handling and robust data science ecosystem integration.
- Amazon DynamoDB: Utilized with Global Tables for active-active multi-region replication and sub-50ms global reads.
- Amazon SQS: Implemented to decouple offline ML ingestion from real-time read paths.
- AWS App Mesh & KMS: Enforces TLS 1.3 mTLS and column-level encryption at rest with customer-managed keys (CMK).

## Rationale
This architecture decouples heavy asynchronous model ingestion from real-time read paths, ensuring strict 99.95% availability and sub-200ms response times. Global data replication, fallback handling, and automated security controls satisfy global scalability, performance, and GDPR/CCPA compliance requirements.