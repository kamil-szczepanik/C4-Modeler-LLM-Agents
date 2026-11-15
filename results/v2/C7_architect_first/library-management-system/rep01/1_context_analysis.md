## Overview
The Library Management System is a cloud-native platform designed for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and high-performance search SLAs.

## Key Elements
- **Library Patrons & Staff:** End-users accessing self-service portals and administrative workflows.
- **Library Management System:** Core cloud-native platform handling cataloguing, circulation, and search.
- **CDN / Edge Layer:** Cloudflare or AWS CloudFront with EU-only POPs.
- **Identity Provider:** Keycloak or Auth0 EU instance supporting OIDC and MFA.
- **External Payment Gateway:** EU-compliant vendor for processing fines and fees.
- **National Library Database:** EU-compliant source for bibliographic data imports.
- **Centralized Observability Platform:** APM and distributed tracing system.

## Relationships
- Library Patrons & Staff -> CDN / Edge Layer: HTTPS (TLS 1.3)
- CDN -> Library Management System: HTTPS/REST
- Library Management System -> Identity Provider: OIDC
- Library Management System -> External Payment Gateway: HTTPS/REST (EU endpoints via DPAs)
- Library Management System -> National Library Database: HTTPS/REST (EU endpoints via DPAs)

## Technology Stack
- **Compute & Orchestration:** EU-region Kubernetes (AWS/Azure/GCP EU-Central) for scalable container management.
- **Backend Services:** Java/Spring Boot or Node.js for modular microservices.
- **Security & Compliance:** HashiCorp Vault or AWS Secrets Manager for secret management; WAF for DDoS protection.
- **Infrastructure Provisioning:** Terraform (Infrastructure-as-Code) for immutable deployments and preventing configuration drift.

## Rationale
This architecture ensures strict compliance with EU-only data residency mandates through localized cloud deployment, dedicated edge routing, and verified vendor DPAs. Furthermore, it guarantees sub-800ms search performance and high availability via edge caching, Kubernetes orchestration, and centralized observability.