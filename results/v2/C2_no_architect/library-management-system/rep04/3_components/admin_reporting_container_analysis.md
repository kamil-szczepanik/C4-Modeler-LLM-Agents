## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for academic and public libraries. The Admin/Reporting Container handles administrative workloads, financial auditing, and data analytics while enforcing strict EU data residency.

## Key Elements
- Library Administrators, Financial Auditors, Library Data Analysts (Users)
- API Gateway (Kubernetes, OAuth2/OIDC, mTLS)
- Admin/Reporting Container (Kubernetes, EU-region)
- Core Circulation and Transactional Database (Kubernetes, EU-region clusters)
- Read-optimized Search Index (Elasticsearch, EU-hosted)

## Relationships
- Library Administrators -> Admin/Reporting Container [HTTPS (TLS 1.3)]
- Financial Auditors / Data Analysts -> Admin/Reporting Container [HTTPS (TLS 1.3)]
- API Gateway -> Admin/Reporting Container [mTLS]
- Admin/Reporting Container -> Core Circulation Database [Parameterized Queries, Read-Replicas]

## Technology Stack
- Kubernetes: Orchestrates containers with dedicated resource quotas and Horizontal Pod Autoscaling (HPA) for heavy reporting workloads.
- Prometheus: Tracks query execution times, export failure rates, and compliance metrics.
- Elasticsearch: Powers read-optimized search indices adhering to <800 ms performance goals.
- OAuth2/OIDC: Enforces Role-Based Access Control (RBAC) and data minimization principles.

## Rationale
This architecture isolates resource-intensive reporting workloads using dedicated Kubernetes nodes and asynchronous workers, protecting core patron circulation performance. Strict EU data residency constraints and role-based data masking ensure compliance with privacy regulations.