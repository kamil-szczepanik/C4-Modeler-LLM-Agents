## Overview
The Apache Superset Reporting Container provides secure business intelligence and analytical reporting for hospital administrators and clinical operations managers. It processes operational data while strictly enforcing HIPAA and GDPR compliance through internal isolation and access controls.

## Key Elements
- Superset Web Server & UI (Python/Flask)
- Superset Celery Worker (Python/Celery)
- Superset Metadata DB Connector (SQLAlchemy)
- Semantic Layer & RLS Engine (Python/SQLAlchemy)
- PostgreSQL Read-Replica
- Redis
- HashiCorp Vault

## Relationships
- Superset Web Server & UI -> Semantic Layer & RLS Engine: Applies data models and security filters [In-process Python Method Call]
- Superset Web Server & Celery Worker -> Redis: Manages broker/cache operations [Redis/TLS]
- Superset Celery Worker -> PostgreSQL Read-Replica: Executes sanitized analytical queries [JDBC/TLS]
- Semantic Layer & RLS Engine -> Go Audit Logging Container: Forwards dashboard data export events [HTTPS]

## Technology Stack
- Python/Flask & Celery: Chosen for robust web serving and asynchronous task management.
- SQLAlchemy: Provides flexible database abstraction and dynamic query modification.
- Redis: Used for secure, high-performance ephemeral caching and message brokering.
- HashiCorp Vault: Dynamic runtime injection of secrets to avoid plain-text storage.
- TLS 1.3: Secures all internal data in transit across the service mesh.

## Rationale
This architecture decouples heavy analytical workloads from core clinical services to protect the 99.99% system availability target. Furthermore, embedded Row-Level Security and strict audit logging satisfy stringent healthcare privacy mandates.