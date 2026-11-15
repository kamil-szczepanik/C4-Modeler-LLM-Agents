## Overview
- The system is the Clinic Management System, managing patient admissions, EMRs, scheduling, and billing.
- The architecture isolates analytical workloads using the Administrative & Analytics Service to protect core transactional performance.

## Key Elements
- Hospital Administrator (person)
- Administrative & Analytics Service (container, Python / FastAPI + Celery)
- API Controller (component, FastAPI)
- Query & Reporting Engine (component, Python / SQLAlchemy)
- Compliance & Audit Worker (component, Celery)
- Analytics Data Store (component, Encrypted Document/Columnar Store)
- Clinical Core Database (container, Encrypted SQL read-only replicas)
- Identity Provider (IdP) (externalSystem, OIDC/OAuth2)

## Relationships
- Hospital Administrator -> Administrative & Analytics Service [HTTPS (TLS 1.3) via WAF with risk-based adaptive MFA]
- API Gateway / Reverse Proxy -> Administrative & Analytics Service [HTTPS / mTLS]
- API Controller -> Identity Provider (IdP) [OpenID Connect (OIDC) / OAuth2 over HTTPS]
- API Controller -> Query & Reporting Engine [In-process / Python Function Calls]
- Query & Reporting Engine -> Analytics Data Store [In-process / SQLAlchemy]
- Compliance & Audit Worker -> Clinical Core Database [Read-only replicas via encrypted SQL over mTLS]

## Technology Stack
- FastAPI: Exposes REST endpoints for administrative dashboards and report generation with low overhead.
- Celery: Handles asynchronous, long-running tasks for HIPAA/GDPR audit trail generation and data retention archiving.
- SQLAlchemy: Executes optimized read-only analytical queries against database replicas.
- Encrypted Document/Columnar Store: Caches aggregated metric summaries locally to meet P95 load NFRs.

## Rationale
- Isolates resource-intensive analytical and compliance reporting from core transactional services to maintain 99.99% availability.
- Enforces strict data masking, cryptographic erasure, and RBAC to satisfy HIPAA and GDPR compliance constraints.