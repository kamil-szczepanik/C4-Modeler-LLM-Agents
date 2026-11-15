## Overview
The Recommendation Service is an internal containerized subsystem of the Online Bookstore that provides "Customers also bought" recommendations. It processes user activity to deliver personalized suggestions while maintaining strict GDPR/CCPA compliance and high availability.

## Key Elements
- Recommendation API Router (FastAPI, Python)
- Recommendation Engine Core (SciPy/NumPy, Python)
- ML Model Client (boto3, gRPC, Python)
- Cache & Persistence Repository (redis-py client)
- Event Consumer (boto3 worker)
- Business Analytics Logging Component
- Amazon ECS Fargate
- Amazon ElastiCache Redis
- Amazon S3
- Amazon SQS

## Relationships
- API Gateway -> Recommendation API Router via mTLS/IAM [HTTP/REST]
- ML Model Client -> Amazon S3 via IAM Task Roles [HTTPS/gRPC]
- Cache & Persistence Repository -> Amazon ElastiCache Redis [Redis Protocol]
- Event Consumer -> Amazon SQS [AMQP/SQS]
- Business Analytics Logging -> Downstream Analytics Stores via Asynchronous Events [HTTP/Queue]

## Technology Stack
- FastAPI & Pydantic: Chosen for high-performance REST routing and strict input schema validation.
- Python & SciPy/NumPy: Provides mathematical operations for collaborative filtering and ranking logic.
- Amazon ECS Fargate: Serverless container execution ensuring scalable, zero-downtime rolling updates.
- Amazon ElastiCache Redis: Delivers low-latency retrieval of pre-computed recommendation lists to meet performance SLAs.
- Amazon S3 & SQS: Manages artifact storage and asynchronous event processing with least-privilege IAM roles.

## Rationale
This architecture uses localized caching, asynchronous event processing, and a resilient FastAPI component to isolate compute-heavy ranking tasks from I/O paths. These decisions ensure the system satisfies the <2s page load performance SLA and 99.95% availability under a 1M MAU scale.