## Overview
- Solution: Library Management System providing catalogue management, circulation control, and self-service portals.
- Purpose: Deliver high-performance search (<800ms) and secure operations for public and academic libraries while enforcing strict EU-only data residency.

## Key Elements
- Library Patrons [person]
- Circulation Staff and Library Administrators [person]
- Identity Provider / SSO [externalSystem]
- Digital Content Providers [externalSystem]
- Notification Gateway [externalSystem]
- Observability & Logging Platform [externalSystem]
- Web Portal [container, React/TypeScript on Nginx]
- API Gateway [container, Envoy/Kong]
- Core Services API [container, Java/Spring Boot]
- Search & Catalogue Service [container, Elasticsearch/OpenSearch]
- Database [container, PostgreSQL with EU hosting]

## Relationships
- Library Patrons -> Web Portal (HTTPS/TLS 1.3)
- Circulation Staff and Library Administrators -> Web Portal (HTTPS/TLS 1.3)
- API Gateway -> Identity Provider / SSO (OIDC/SAML over HTTPS)
- Web Portal -> API Gateway (HTTPS / JSON over TLS 1.3)
- API Gateway -> Core Services API (gRPC over mTLS)
- API Gateway -> Search & Catalogue Service (gRPC over mTLS)
- Core Services API -> Database (PostgreSQL Wire Protocol over TLS 1.3)
- Search & Catalogue Service -> Database (PostgreSQL Wire Protocol over TLS 1.3)
- Core Services API -> Notification Gateway (Asynchronous HTTPS/REST webhooks over TLS 1.3)
- Core Services API -> Digital Content Providers (HTTPS/REST with mutual TLS)

## Technology Stack
- Frontend: React/TypeScript on Nginx for the Web Portal
- Routing & Edge: Envoy/Kong API Gateway with circuit breaking and OIDC validation
- Backend Logic: Java/Spring Boot for Core Services API
- Search Engine: Elasticsearch/OpenSearch for sub-800ms catalogue queries
- Primary Data Store: PostgreSQL with EU hosting and encrypted persistent volumes
- Infrastructure: Kubernetes with EU-hosted worker nodes, Istio/Linkerd service mesh, and Vault for secrets

## Rationale
- Separates patron-facing search workloads from core transactional operations to easily satisfy the sub-800ms performance SLA (R-05).
- Enforces EU-only data residency via dedicated regional deployments and encrypted storage to maintain compliance and security.