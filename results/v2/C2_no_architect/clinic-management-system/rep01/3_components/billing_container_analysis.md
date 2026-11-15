## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient records, scheduling, billing, and regulatory compliance. It ensures high availability, strict security, and robust interoperability for clinical workflows.

## Key Elements
- Billing Container (Microservice handling financial records, claim submission, and patient ledger queries)
- Event Broker (Apache Kafka for asynchronous message processing and decoupled claim pipelines)
- PostgreSQL Databases (Primary data store with Patroni/etcd for active-passive replication)
- HashiCorp Vault (Secrets management and AES-256 key retrieval)
- Immutable Audit Storage Sink (Tamper-evident storage for financial and security audit logs)
- Insurance Clearinghouses (External third-party systems for claim processing)
- Analytics & Reporting Container (Consumes sanitized financial events for revenue cycle dashboards)

## Relationships
- Billing Container -> Event Broker: Publishes and consumes financial events asynchronously via Apache Kafka
- Billing Container -> PostgreSQL Databases: Reads and writes financial data using SQL with Active-Passive Replication
- Billing Container -> Insurance Clearinghouses: Submits claims and tracks statuses using secure HTTPS REST APIs with TLS 1.3
- Billing Container -> HashiCorp Vault: Retrieves AES-256 keys and rotates database credentials securely
- Billing Container -> Immutable Audit Storage Sink: Synchronously emits tamper-evident financial audit logs

## Technology Stack
- Kubernetes (on-prem-k8s and eu-central-1): Manages container deployment, autoscaling via HPA based on Kafka consumer lag
- Apache Kafka / RabbitMQ: Powers asynchronous claim pipelines, dead-letter queues (DLQ), and idempotency
- HashiCorp Vault: Secures dynamic credential rotation and AES-256 application-layer data encryption
- TLS 1.3 / mTLS (SPIFFE/SPIRE): Secures all pod-to-pod and external communication channels

## Rationale
This architecture ensures 99.99% availability by decoupling synchronous external clearinghouse bottlenecks through asynchronous event-driven queues. It strictly satisfies HIPAA, GDPR, and PCI-DSS mandates via end-to-end encryption, mTLS, RBAC, and immutable audit trails.