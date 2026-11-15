## Overview
The Library Management System is a comprehensive platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. The architecture strictly enforces EU-only data residency and a 99th-percentile search response time under 800 ms.

## Key Elements
* Library Patrons, Librarians/Circulation Staff, and Library Administrators
* Library Management System (Central Software System)
* EU Identity Provider (IdP)
* EU Payment Gateway (e.g., Adyen EU or Stripe EU)
* EU Notification Service
* EU Cloud Infrastructure (AWS Frankfurt/Ireland or OVHcloud)
* Centralized Log & Metrics Aggregator (Datadog EU or Grafana Cloud EU)
* API Gateway

## Relationships
* Users to Library Management System via HTTPS/TLS 1.3
* Library Management System to EU Identity Provider via OIDC/OAuth2 over HTTPS
* Library Management System to EU Payment Gateway via REST/HTTPS
* Library Management System to EU Notification Service via HTTPS/SMTP
* Internal container-to-container communication secured via mutual TLS (mTLS)

## Technology Stack
* Cloud Infrastructure: AWS or OVHcloud (EU regions only) for hardware-level data residency
* Authentication: OpenID Connect (OIDC) with Multi-Factor Authentication (MFA)
* Security & Encryption: AES-256 with customer-managed keys (CMK) at-rest and TLS 1.3 in-transit
* Observability: Datadog EU or Grafana Cloud EU with distributed tracing
* Secrets Management: HashiCorp Vault or AWS Secrets Manager

## Rationale
This architecture ensures strict compliance with EU data residency regulations while meeting high-performance search SLAs through targeted infrastructure and security controls. Perimeter RBAC, API rate-limiting, and dedicated EU-hosted integrations guarantee robust security, auditability, and reliable circulation workflows.