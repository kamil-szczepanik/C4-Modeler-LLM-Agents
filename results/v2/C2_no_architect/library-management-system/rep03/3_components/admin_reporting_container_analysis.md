## Overview
The Admin & Reporting Container manages administrative functions, reporting, and sensitive analytical workloads for the Library Management System. It provides compliance auditing, collection analytics, and secure scheduled exports within the EU data residency boundary.

## Key Elements
- Admin & Reporting Container (Kubernetes, Microservice)
- Library Administrators (Primary Persona)
- API Gateway Container (Kubernetes, OAuth2/OIDC, TLS 1.3)
- In-Region APM and Log Aggregation Pipeline (External System)
- Audit and Compliance Trust Zone (External System)
- Ephemeral Object Storage (AWS S3 / compatible object store)
- Background Worker Queue (Celery / Temporal workflows)

## Relationships
- API Gateway Container -> Admin & Reporting Container: Routes administrative requests [mTLS over internal Kubernetes network policies]
- Admin & Reporting Container -> In-Region APM and Log Aggregation Pipeline: Streams encrypted metrics [OpenTelemetry sidecars]
- Admin & Reporting Container -> Audit and Compliance Trust Zone: Streams cryptographically signed audit logs [TLS 1.3]
- Admin & Reporting Container -> Ephemeral Object Storage: Streams generated export files [HTTPS with Customer-Managed Keys]

## Technology Stack
- Kubernetes: Orchestrates container deployment with dedicated worker node taints and tolerations for workload isolation
- Celery / Temporal: Manages asynchronous batch processing for resource-intensive reports and exports
- OpenTelemetry: Captures and streams container metrics and tracing data
- Prometheus: Monitors query execution times and triggers alerts for long-running operations

## Rationale
Dedicated node taints and asynchronous batch processing protect critical real-time microservices from resource exhaustion during heavy analytical queries. Strict RBAC, dynamic PII masking, DLP scanning, and CMK encryption ensure full compliance with EU data residency and security mandates.