## Overview
The Analytics & Audit Reporting Container provides heavy compliance reporting, operational analytics, and immutable audit logging for the Clinic Management System. It isolates resource-intensive reporting tasks to protect core electronic medical record (EMR) performance and ensure HIPAA/GDPR compliance.

## Key Elements
- **Users**: Clinic Administrators & Compliance Officers
- **Container**: Analytics & Audit Reporting Container
- **Core Technologies**: Python, Celery, Redis, Celery Beat, KEDA
- **Storage & Infrastructure**: Encrypted Object Storage (S3/MinIO), WORM Storage, Kubernetes (on-prem-k8s, eu-central-1)
- **Observability & Security**: OpenTelemetry, Datadog/Prometheus, Envoy / Istio Service Mesh

## Relationships
- **API Gateway -> Analytics & Audit Reporting Container**: Routes audit and reporting requests via gRPC / HTTPS with mTLS.
- **Analytics & Audit Reporting Container -> Background Workers**: Offloads heavy PDF/CSV export generation via Celery and Redis.
- **Analytics & Audit Reporting Container -> Object Storage**: Stores generated reports securely accessed via short-lived pre-signed URLs.
- **Analytics & Audit Reporting Container -> WORM Storage**: Streams immutable audit logs directly to tamper-proof storage.

## Technology Stack
- **Python**: Core application language for data aggregation and report generation.
- **Celery & Celery Beat**: Asynchronous background worker queue and distributed task scheduler for handling scheduled and heavy exports without request lifecycle starvation.
- **KEDA (Kubernetes Event-driven Autoscaling)**: Dynamically scales Python worker pods based on queue depth for high availability.
- **Object Storage (S3/MinIO) & WORM Storage**: Secures export files and enforces immutable retention for compliance.
- **OpenTelemetry & Datadog/Prometheus**: Provides distributed tracing and SLO monitoring for analytical queries.

## Rationale
This architecture offloads resource-intensive tasks from the core EMR to maintain sub-second P95 screen load performance. Furthermore, isolated asynchronous processing, strict RBAC, PII/PHI scrubbing, and WORM storage satisfy stringent HIPAA, GDPR, and 10-year data retention mandates.