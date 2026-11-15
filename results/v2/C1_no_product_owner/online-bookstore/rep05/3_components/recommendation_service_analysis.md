## Overview
[Component-level architecture of the Recommendation Service for the Online Bookstore, detailing internal modules, security controls, and AWS integrations. Its core purpose is delivering scalable, sub-second personalized book recommendations while maintaining strict data privacy compliance.]

## Key Elements
* **API Controller**: Built with **FastAPI**, handling incoming gRPC routing and input sanitization.
* **Recommendation Engine**: Core Python component running collaborative filtering logic and fallback mechanisms.
* **Model Gateway**: Abstraction layer managing interactions with **Amazon SageMaker**.
* **Event Consumer**: Background worker using **Celery** to ingest asynchronous events.
* **Cache & Storage Adapter**: Uses **Redis-py** to interface with **Amazon ElastiCache (Redis)**.

## Relationships
* **API Gateway -> API Controller**: Routes recommendation requests via gRPC over TLS [AWS App Mesh].
* **Event Consumer -> Amazon SQS**: Pulls asynchronous purchase/browsing events [JSON over HTTPS].
* **Recommendation Engine -> Cache & Storage Adapter**: Reads/writes recommendation caches [RESP over TCP with TLS].
* **Model Gateway -> Amazon SageMaker**: Fetches model inference predictions [HTTPS / AWS SDK via SigV4].

## Technology Stack
* **Python FastAPI / gRPC**: Powers the high-performance API Controller and routing layer.
* **Amazon SageMaker**: Offloads heavy machine learning inference to prevent ECS CPU starvation.
* **Amazon ElastiCache (Redis)**: Provides sub-millisecond cached responses and static fallback data.
* **Celery & Amazon SQS**: Manages asynchronous background event ingestion.
* **AWS IAM & Secrets Manager**: Enforces least-privilege security and credential management.

## Rationale
[Decomposing the Recommendation Service into decoupled micro-components with SageMaker offloading ensures the system handles 1 million MAU without performance degradation. Strict security protocols and caching mechanisms guarantee GDPR compliance, encrypted data in transit, and 99.95% uptime availability.]