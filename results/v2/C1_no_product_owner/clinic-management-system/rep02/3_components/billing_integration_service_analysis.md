## Overview
The Clinic Management System provides comprehensive patient admissions, electronic medical records, scheduling, and billing capabilities for healthcare facilities. It operates within a hybrid cloud environment, ensuring strict HIPAA and GDPR compliance with high availability.

## Key Elements
- **API Gateway / Reverse Proxy**: Envoy proxy routing incoming traffic.
- **Service Mesh**: Istio handling mTLS, circuit breaking, and egress policies.
- **Billing & Integration Service**: Python/FastAPI container managing external systems and billing.
- **Internal Components**: API Router, FHIR Translation Engine, Payment & Claims Processor, Integration Event Publisher, and Billing Data Access Repository.
- **External Systems**: External Lab & Imaging Systems, Payment Gateways, and Insurance Clearinghouses.
- **Data & Infrastructure**: PostgreSQL with Patroni, NATS / RabbitMQ and AWS Kafka, WORM-compliant S3 / MinIO, and HashiCorp Vault.

## Relationships
- **Envoy -> Billing & Integration Service**: Routes incoming REST/gRPC traffic over Istio mTLS [gRPC over Istio mTLS].
- **Billing & Integration Service -> External Lab & Imaging Systems**: Integrates via HL7 FHIR [HTTPS / HL7 FHIR].
- **Billing & Integration Service -> Payment Gateways & Insurance Clearinghouses**: Processes claims and payments asynchronously [HTTPS with strict egress filtering].
- **Billing & Integration Service -> NATS / RabbitMQ and AWS Kafka**: Publishes and consumes events using DLQs [TLS 1.3].
- **Billing Data Access Repository -> PostgreSQL with Patroni**: Reads and writes relational data with AES-256 encryption [Encrypted SQL connections].
- **Billing & Integration Service -> HashiCorp Vault**: Injects API keys, client certificates, and ephemeral OAuth tokens at runtime [TLS].

## Technology Stack
- **Python / FastAPI**: Chosen for high asynchronous performance and robust schema validation.
- **Pydantic & SQLAlchemy**: Used for strict HL7 FHIR payload validation and data mapping.
- **Istio & Envoy**: Ensures mTLS, circuit breaking, and strict IP/FQDN egress filtering.
- **Kafka / RabbitMQ / NATS**: Manages asynchronous decoupling, event-driven updates, and Dead Letter Queues.
- **PostgreSQL with Patroni & S3/MinIO**: Provides high availability relational storage and WORM-compliant audit logging.
- **HashiCorp Vault**: Secures runtime secrets and rotates ephemeral OAuth tokens.

## Rationale
This architecture ensures 99.99% high availability through active-active deployments, asynchronous queue decoupling, and Kafka-based auto-scaling. It satisfies strict HIPAA, GDPR, and PCI-DSS mandates via end-to-end mTLS, AES-256 encryption, HashiCorp Vault secret management, and WORM-compliant auditing.