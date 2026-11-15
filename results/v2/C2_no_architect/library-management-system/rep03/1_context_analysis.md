## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
* Library Patrons, Library Staff, and Library Administrators (User Personas)
* Library Management System (Primary Context boundary)
* EU Cloud Infrastructure Boundary (AWS Frankfurt/Ireland)
* External Identity Provider (IdP)
* In-Region APM and Log Aggregation Pipeline (Prometheus/Grafana or EU-hosted ELK)
* Audit and Compliance Trust Zone

## Relationships
* Patrons to Self-Service Portal via HTTPS (TLS 1.3) and OAuth 2.0 / OIDC
* Staff and Administrators to Circulation/Cataloguing tools via TLS 1.3 and OAuth 2.0 / OIDC with MFA
* System telemetry to In-Region APM via encrypted local pipelines
* All system components strictly contained within EU-hosted cloud infrastructure

## Technology Stack
* Cloud Infrastructure: EU-hosted cloud providers (AWS Frankfurt/Ireland or EU-sovereign clouds) for EU-only data residency compliance
* Security Protocols: TLS 1.3 for data in transit; AES-256 for data at rest; mTLS for digital asset integrations
* IAM & Access: OAuth 2.0 / OIDC with Role-Based Access Control (RBAC) and MFA
* Observability & Analytics: Prometheus/Grafana or EU-hosted ELK for in-region telemetry and <800ms search latency tracking (R-05)
* Audit & Compliance: WORM (Write-Once-Read-Many) storage controls with automated retention limits

## Rationale
The architecture strictly enforces EU data residency and GDPR compliance using single-region EU hosting and in-region observability pipelines. It guarantees performance (R-05) and security through TLS 1.3, AES-256, and isolated audit zones.