## Overview
The Recommendation & Review Container provides personalized book suggestions and authenticated customer reviews for the Online Bookstore. It ensures high performance, security, and scalability for 1 million monthly active users using Python FastAPI.

## Key Elements
- Review Controller & Service (Python FastAPI)
- Recommendation Controller & Service (Python FastAPI)
- Helpfulness Service (Python FastAPI)
- Order Verification Client (Python FastAPI)
- Async Event Publisher (Celery / Python)
- AWS SQS & Amazon DynamoDB
- External Recommendation Engine

## Relationships
- AWS API Gateway -> FastAPI Recommendation & Review Container: Routes requests [REST / JSON over HTTP, mTLS]
- Review Controller -> AWS SQS: Publishes review events [Async / AWS SQS SDK]
- Recommendation Controller -> External Recommendation Engine: Fetches suggestions [gRPC / TLS]
- Helpfulness Service -> Amazon DynamoDB: Persists vote tallies [NoSQL / AWS SDK]
- Order Verification Client -> Order & Checkout Container: Validates purchases [REST / JSON over HTTP, VPC]

## Technology Stack
- Python FastAPI: High-performance asynchronous REST API framework
- Pydantic: Strict input validation for OWASP Top-10 mitigation
- Celery: Asynchronous task queue for offloading review moderation events
- Amazon DynamoDB: High-concurrency NoSQL storage for review helpfulness votes
- AWS SQS: Message broker for decoupled sentiment analysis and moderation

## Rationale
FastAPI and asynchronous event processing via Celery and AWS SQS maintain sub-2-second page load times under heavy traffic. Strict input validation, mTLS, and RBAC fulfill rigorous security and compliance requirements.