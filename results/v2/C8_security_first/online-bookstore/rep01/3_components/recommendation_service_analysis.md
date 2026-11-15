## Overview
The Recommendation Service is an internal container within the Online Bookstore that delivers personalized and context-aware book suggestions to registered customers. It drives engagement and average order value while maintaining strict compliance, high availability, and performance SLAs.

## Key Elements
- Registered Customer: End-user persona browsing the catalogue and receiving recommendations.
- Recommendation Service: Python/FastAPI application running on AWS ECS on Fargate.
- API Controller: FastAPI module managing incoming gRPC/REST traffic from the Envoy Service Mesh.
- Recommendation Engine: Core Python module processing suggestion algorithms and personalization.
- Recommendation Formatter / Explainer: Module appending transparency context tags (e.g., "Because you bought X").
- Event Consumer: Asynchronous background component processing real-time events.
- Amazon ElastiCache (Redis): In-memory data store for pre-computed recommendation vectors and feature caching.
- Amazon SQS & Amazon EventBridge: Messaging infrastructure for asynchronous event streaming.

## Relationships
- Envoy Service Mesh -> API Controller: Routes recommendation requests [gRPC over mTLS].
- API Controller -> Recommendation Engine: Executes in-process logic [Python].
- Recommendation Engine -> Amazon ElastiCache (Redis): Reads/writes cached vectors [RESP over TCP with TLS].
- Amazon SQS -> Event Consumer: Delivers domain events [HTTPS/SQS API].
- Event Consumer -> Amazon ElastiCache (Redis): Updates feature cache [RESP over TCP with TLS].

## Technology Stack
- Python / FastAPI: Core runtime and web framework for high-throughput asynchronous request handling.
- AWS ECS on Fargate: Serverless container orchestration ensuring isolated and scalable deployments.
- Amazon ElastiCache (Redis): Clustered in-memory cache providing ultra-low latency reads to satisfy the <2s page load SLA.
- Amazon SQS & Amazon EventBridge: Decoupled messaging infrastructure for non-blocking asynchronous event processing.
- Pydantic: Data validation library enforcing strict input hygiene and preventing injection vulnerabilities.

## Rationale
This architecture uses an asynchronous, event-driven design with caching to isolate the recommendation path from core checkout, guaranteeing 99.95% uptime and sub-2-second performance. Containerized deployment on AWS ECS with strict mTLS trust boundaries and Redis security secures user behavioral data for GDPR and CCPA compliance.