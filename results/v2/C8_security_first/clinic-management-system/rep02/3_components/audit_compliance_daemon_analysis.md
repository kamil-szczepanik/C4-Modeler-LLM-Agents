## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, high availability, and secure data retention.

## Key Elements
- Compliance Officers / Data Protection Officers (DPOs)
- Audit & Compliance Daemon (Go container)
- Ingestion Worker
- Immutable Log Engine
- Compliance Query API
- Report Generator
- Key Management Integrator
- Message Broker (NATS JetStream)
- WORM Storage (AWS S3 Object Lock / MinIO)

## Relationships
- Microservices -> NATS JetStream: Publishes cryptographically signed audit events [NATS/TCP, mTLS]
- Ingestion Worker -> NATS JetStream: Consumes audit streams and validates JWT scopes [NATS/TCP]
- Immutable Log Engine -> WORM Storage: Writes hash-chained audit logs [S3 API / HTTPS, Compliance Mode]
- Compliance Officers -> Compliance Query API: Requests audit reports and compliance certificates [HTTPS / REST, mTLS, OAuth2/OIDC]
- Report Generator -> Key Management Integrator: Verifies cryptographic chain-of-custody [gRPC / mTLS]

## Technology Stack
- Go: Chosen for low-overhead concurrency, cryptographic processing, and fast PDF generation.
- NATS JetStream: Selected for asynchronous event streaming, preventing backpressure and decoupling audit workflows.
- AWS S3 Object Lock / MinIO: Implemented in Compliance Mode to enforce tamper-proof 10-year data retention.
- Kubernetes: Utilized for pod sandboxing, resource quotas, and high-availability deployments.

## Rationale
This architecture ensures strict HIPAA and GDPR compliance by leveraging immutable WORM storage and decoupled asynchronous ingestion. It protects 99.99% system uptime while providing dedicated, secure query and reporting capabilities for compliance officers.