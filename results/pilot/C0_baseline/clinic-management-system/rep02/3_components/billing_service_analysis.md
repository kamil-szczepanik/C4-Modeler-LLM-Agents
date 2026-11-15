## Overview
The Billing Service is an internal Python container within the Clinic Management System that automates financial transactions, insurance claims, and reconciliation. It ensures high-availability billing operations, PCI-DSS compliance, and secure data retention for healthcare facilities.

## Key Elements
* ClaimProcessor (Python, FastAPI): Validates incoming claims and handles RBAC/OAuth2 entry points
* PaymentOrchestrator (Python, Celery, Redis): Manages asynchronous payment tasks and gateway retries
* InvoiceManager (Python, SQLAlchemy): Executes double-entry bookkeeping and persistence
* ReconciliationEngine (Python, Kubernetes CronJob): Performs batch financial reconciliation
* External Payment Gateways: Process credit card and insurance transactions over HTTPS

## Relationships
* ClaimProcessor -> InvoiceManager: Invokes internal Python function calls for invoice creation
* ClaimProcessor -> PaymentOrchestrator: Dispatches asynchronous jobs via Celery broker over mTLS
* PaymentOrchestrator -> External Payment Gateways: Processes payments via REST/JSON over HTTPS
* InvoiceManager & ReconciliationEngine -> PostgreSQL: Persists and queries data using encrypted TCP (AES-256)
* Billing Service Components -> Redis: Manages task queues via TLS and SCRAM-SHA-512

## Technology Stack
* Python: Core programming language for rapid development of domain logic
* FastAPI: High-performance framework for REST endpoints and schema validation
* Celery & Redis: Asynchronous task queue and broker for resilient payment retries
* SQLAlchemy ORM: Manages database transactions and double-entry bookkeeping patterns
* PostgreSQL: Relational database providing encrypted storage for financial ledger data

## Rationale
This architecture uses an asynchronous, component-based Python design to decouple real-time claim validation from resource-heavy payment retries. This ensures 99.99% availability and strict HIPAA/PCI-DSS security compliance across hybrid cloud deployments.