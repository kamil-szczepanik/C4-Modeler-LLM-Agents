## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. It is architected as a cloud-native platform adhering to strict EU data residency constraints.

## Key Elements
* Library Patrons (Self-service users)
* Librarians/Catalogers (Inventory managers)
* Library Administrators (System configurers)
* Library Management System (LMS)
* EU Payment Gateway
* National Library Database

## Relationships
* Library Patrons to LMS via HTTPS/TLS 1.3 (OAuth2/OIDC)
* Librarians and Administrators to LMS via HTTPS/TLS 1.3 (MFA/RBAC)
* LMS to EU Payment Gateway via HTTPS/REST with mTLS
* LMS to National Library Database via SOAP/REST over HTTPS with mTLS

## Technology Stack
* AWS Frankfurt (EU region) for cloud infrastructure ensuring EU-only data residency
* TLS 1.3 and mTLS for secure data in transit
* AES-256 for data at rest and field-level PII encryption
* OAuth2, OIDC, and RBAC for authentication and authorization
* GitOps (ArgoCD) for deployment pipelines and container management
* OpenTelemetry for distributed tracing and SLO tracking

## Rationale
This architecture uses an EU-region cloud deployment and strict encryption protocols to meet legal data residency mandates. Additionally, centralized API gateways, mTLS, and distributed tracing ensure the system achieves secure operations and satisfies the <800ms search performance requirement.