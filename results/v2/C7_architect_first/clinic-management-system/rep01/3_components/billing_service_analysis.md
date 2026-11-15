## Overview
The Billing Service is a containerized microservice within the Clinic Management System that manages patient financial transactions, insurance claims, and payment processing. Its core purpose is to ensure secure, highly available, and compliant financial operations for medium-sized clinics.

## Key Elements
- Billing API Controller & Patient Billing Portal API (FastAPI)
- Invoice & Ledger Engine (Python)
- Claims Processor & Insurance Reconciliation Engine (Python/Celery)
- Payment Integrator (Python/HTTPX)
- Billing Data Repository (PostgreSQL with SQLAlchemy ORM)
- Idempotency State Store (Distributed Redis)
- External Payment Gateway & Insurance Clearinghouse
- Istio Service Mesh & HashiCorp Vault

## Relationships
- API Gateway / Edge Proxy -> Billing API Controllers: Routes incoming traffic [mTLS/gRPC/HTTPS]
- Billing Controllers -> Invoice & Ledger Engine: Delegates business logic [In-Memory / Python Function Calls]
- Claims Processor & Payment Integrator -> Payment Gateway & Insurance Clearinghouse: Submits claims and processes payments [HTTPS]
- Billing Services -> Billing Data Repository: Interfaces for data persistence and ledger updates [SQLAlchemy Connection Pooling]

## Technology Stack
- FastAPI & Python: Chosen for high-performance asynchronous API endpoints and rapid development.
- PostgreSQL: Provides relational data integrity and supports 10-year financial retention mandates.
- Celery & Redis: Decouples asynchronous claims processing and powers the idempotency state store.
- Istio Service Mesh: Enables multi-cluster failover and active-active resilience across hybrid environments.
- HashiCorp Vault: Secures financial PII/PHI with AES-256 encryption at rest.

## Rationale
This architecture uses active-active multi-cluster deployment and asynchronous workers to achieve 99.99% availability and fault tolerance during clearinghouse outages. Strict encryption, OAuth2 RBAC, and idempotency controls ensure full HIPAA compliance and zero financial data loss.