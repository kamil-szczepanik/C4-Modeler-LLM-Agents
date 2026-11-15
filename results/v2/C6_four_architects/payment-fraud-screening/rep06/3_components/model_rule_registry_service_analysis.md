## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud in under 50ms and provides case management for fraud analysts. It operates on AWS within a 25,000 EUR monthly budget, ensuring PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.

## Key Elements
- Fraud Analysts: Users reviewing suspicious payments via the Analyst UI
- Payment Gateway / Core Ledger: External system submitting payment authorizations
- Identity Provider / IdP: External authentication provider for users
- Compliance Archive / AWS S3 Object Lock: External tamper-evident storage for 7-year audit logs
- API Gateway / Envoy: Entry point handling TLS termination and routing (Envoy / HTTPS / TLS)
- Fraud Scoring Engine: Core evaluation container (Go / gRPC)
- Case Management Backend: Handles analyst reviews (Java / Spring Boot)
- Model & Rule Registry Service: Manages models and zero-downtime rule updates (Python / FastAPI / S3), comprising components: Registry API Controller, Model Compiler & Validator, Artifact Storage Manager, Distribution Coordinator, Metadata Repository Client, Hot Cache Manager, and Audit Event Emitter
- Analyst UI: Frontend interface (React / AWS S3 / CloudFront)
- Asynchronous Audit Worker: Processes immutable audit trails (Go / AWS Lambda)
- Redis Cluster / Amazon ElastiCache: Low-latency caching (Amazon ElastiCache Redis)
- PostgreSQL / Amazon Aurora: Relational data store (Amazon Aurora PostgreSQL)
- Amazon SQS / SNS: Asynchronous event messaging
- AWS Secrets Manager: Credential and secret management

## Relationships
- Payment Gateway / Core Ledger -> API Gateway / Envoy: Submits authorization requests [HTTPS / TLS]
- Analyst UI -> API Gateway / Envoy: Routes analyst actions and queries [HTTPS / TLS]
- API Gateway / Envoy -> Fraud Scoring Engine: Forwards real-time scoring requests [gRPC]
- API Gateway / Envoy -> Case Management Backend: Routes case management APIs [HTTPS / REST]
- Fraud Scoring Engine -> Model & Rule Registry Service: Fetches compiled models [gRPC / polling]
- Fraud Scoring Engine -> Redis Cluster / Amazon ElastiCache: Reads scoring context [Redis Protocol]
- Fraud Scoring Engine -> Asynchronous Audit Worker: Emits decision audit logs [Amazon SQS]
- Case Management Backend -> PostgreSQL / Amazon Aurora: Persists case data [SQL over TLS]
- Model & Rule Registry Service -> Compliance Archive / AWS S3 Object Lock: Stores immutable model artifacts [HTTPS / S3 API]
- Asynchronous Audit Worker -> Compliance Archive / AWS S3 Object Lock: Writes tamper-evident logs [HTTPS / S3 API]

## Technology Stack
- AWS (eu-west-1): Cloud provider and region ensuring regional compliance
- Go: Used for the Fraud Scoring Engine and Audit Worker for high-throughput, low-latency performance
- Python / FastAPI: Used for the Model & Rule Registry Service for rapid model and rule lifecycle management
- Java / Spring Boot: Used for the Case Management Backend for enterprise robustness
- React / AWS S3 / CloudFront: Provides a scalable, high-performance analyst frontend
- Amazon Aurora (PostgreSQL): Provides reliable, ACID-compliant transactional persistence
- Amazon ElastiCache (Redis): Delivers sub-millisecond caching for real-time scoring
- Amazon S3 Object Lock: Guarantees tamper-evident 7-year audit storage (R-06)

## Rationale
This architecture uses Go and Redis to meet stringent sub-50ms P99 latency requirements at high throughput (3,000 req/sec) within a fixed AWS infrastructure budget. Separation of immutable storage (S3 Object Lock) and decoupled asynchronous workers ensures PCI-DSS compliance and 7-year auditability while maintaining high system availability.