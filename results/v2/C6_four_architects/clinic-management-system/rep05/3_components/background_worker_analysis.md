## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and long-term data retention.

## Key Elements
- Task Dispatcher / Consumer (Python / Celery)
- Document Generator (Python / ReportLab)
- Audit Offloader (Python / boto3)
- Data Purger / Retention Manager (Python)
- Notification Dispatcher (Python)
- FHIR Sync Worker (Python / Celery)
- Worker Health & Metrics Agent (Python / Prometheus client)

## Relationships
- Task Dispatcher -> Message Broker [SASL/SCRAM over TLS]
- Task Dispatcher -> Primary Database [SQL over TLS]
- Task Dispatcher -> Notification Dispatcher / FHIR Sync Worker [In-process / Celery Task]
- Document Generator -> Audit & Archival Store [HTTPS]
- Audit Offloader -> Primary Database [SQL over TLS]
- Audit Offloader -> Audit & Archival Store [HTTPS]
- Notification Dispatcher -> SMS/Notification Gateway [HTTPS]
- FHIR Sync Worker -> FHIR Interoperability Service [gRPC / TLS]
- Worker Health & Metrics Agent -> Observability Agent [HTTP / Prometheus Scraping]

## Technology Stack
- Python / Celery: Powers stateless asynchronous task execution and worker distribution.
- ReportLab: Handles CPU-bound PDF generation for medical reports and invoices.
- SQLAlchemy / boto3: Manages secure database queries and object storage offloading.
- Prometheus Client: Exposes real-time worker metrics for observability.

## Rationale
This component-level architecture isolates resource-intensive asynchronous workloads within stateless Kubernetes worker pods, protecting core APIs. Secure protocols (TLS, gRPC, HTTPS) and dedicated offloaders ensure strict adherence to HIPAA compliance and 10-year data retention requirements.