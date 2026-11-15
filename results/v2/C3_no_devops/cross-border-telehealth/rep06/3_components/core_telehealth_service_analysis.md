## Overview
[The Core Telehealth Service handles business logic, session management, and secure synchronization for cross-border telemedicine. It operates on GCP across europe-west3 and us-central1 with strict data residency enforcement.]

## Key Elements
[Session & Consent Manager (Go) with Consent Evaluation Engine]
[Integration Anti-Corruption Layer (Go)]
[Event Dispatcher (Go)]
[Idempotent Sync Coordinator (Go)]
[Cloud SQL for PostgreSQL and Memorystore for Redis]
[Google Cloud Pub/Sub]

## Relationships
[Regional API Gateways -> Core Telehealth Service: Routes API requests via gRPC over mTLS]
[Core Telehealth Service -> Google Cloud Pub/Sub: Publishes asynchronous domain events via Cloud Pub/Sub API]
[Core Telehealth Service -> Cloud SQL for PostgreSQL: Reads/writes relational data via PostgreSQL Protocol]
[Core Telehealth Service -> Memorystore for Redis: Caches transient state via Redis Protocol]
[Integration Anti-Corruption Layer -> Identity Verification & Regional Payment Gateways: Communicates via HTTPS/REST with circuit breakers]

## Technology Stack
[Go: Selected for backend microservices to ensure high concurrency and low memory footprint]
[Google Cloud Platform (europe-west3, us-central1): Enforces regional data residency constraints]
[Cloud SQL for PostgreSQL & Memorystore for Redis: Provides persistent and transient regional data storage]
[Google Cloud Pub/Sub: Enables asynchronous, decoupled event-driven messaging]

## Rationale
[Decomposing the service into specialized Go components ensures strict isolation of regional data while supporting offline resilience for rural users. Mandatory mTLS, OAuth2/OIDC, and encrypted sync protocols guarantee GDPR and HIPAA compliance.]