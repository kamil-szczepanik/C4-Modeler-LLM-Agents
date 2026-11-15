## Overview
The Billing Service is a core component of the Clinic Management System designed to handle financial transactions, insurance claim processing, and patient billing. It ensures HIPAA/GDPR compliance and 99.99% availability through a hybrid cloud architecture.

## Key Elements
*   **Invoice Manager (FastAPI):** Handles RESTful CRUD operations and patient-facing billing logic.
*   **Claim Processor (Celery/RabbitMQ):** Asynchronous worker for Clearinghouse Gateway interactions.
*   **Payment Orchestrator:** Manages state machines for installment plans and PCI-DSS compliant payment processing.
*   **Statement Generator (Jinja2):** Produces itemized patient statements and PDFs.
*   **PostgreSQL:** Primary database with row-level security (RLS) and TDE.
*   **S3 Glacier:** Long-term immutable storage for 10-year data retention.

## Relationships
*   **Clinical API Gateway -> Billing Service:** gRPC with mTLS for secure service-to-service communication.
*   **Billing Service -> Clearinghouse Gateway:** Outbound calls protected by Resilience4j circuit breakers.
*   **Billing Service -> Payment Gateway:** Tokenized API communication via PCI-DSS compliant trust zone.
*   **Billing Service -> Audit Log Service:** Real-time, cryptographically signed event streaming.

## Technology Stack
*   **Language:** Python (FastAPI) for high-performance service logic.
*   **Observability:** OpenTelemetry for distributed tracing across hybrid on-prem/cloud boundaries.
*   **Infrastructure:** Kubernetes (k8s) with Service Mesh for mTLS and cross-site traffic routing.
*   **Security:** ABAC for role-based authorization, TDE for data at rest, and tokenization for payment instruments.

## Rationale
The architecture uses asynchronous processing and component decoupling to maintain high availability and performance during high-latency financial workflows. Hybrid deployment and multi-region replication ensure the system meets strict 99.99% uptime and 10-year data retention compliance requirements.