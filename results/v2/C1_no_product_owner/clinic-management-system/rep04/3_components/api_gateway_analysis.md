## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict security, and regulatory compliance across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
- **API Gateway (Kong / Nginx on Kubernetes):** Manages inbound traffic, TLS termination, and routing.
- **TLS Termination & Ingress Controller (Nginx/Kong Ingress):** Enforces TLS 1.3 and WAF policies.
- **Authentication & Authorization Plugin (Lua/Go with OIDC & Coraza/ModSecurity):** Validates JWTs, enforces RBAC, scope validation, and PHI masking.
- **Service Discovery & Upstream (Envoy / Kong Upstream):** Handles gRPC routing with circuit breakers.
- **Istio Service Mesh:** Secures internal service-to-service communication with SPIFFE/SPIRE.
- **Backend Microservices:** Patient & Scheduling, EMR, Billing, and Integration services (Node.js/Spring Boot).
- **Data Stores:** PostgreSQL (Multi-AZ) and WORM Audit Log Store with HSM-backed KMS.

## Relationships
- **Web Application -> API Gateway:** Sends user requests via HTTPS/TLS with OAuth2/OIDC.
- **External Systems -> API Gateway:** Connects via RFC 8705 OAuth2 mTLS / client certificate pinning.
- **API Gateway -> Microservices:** Routes internal traffic using gRPC over mTLS.
- **Authentication Plugin -> Identity Provider:** Validates tokens via HTTPS.

## Technology Stack
- **Kong API Gateway & Nginx Ingress:** Chosen for high-performance routing, active-active scaling, and pluggable architecture.
- **Coraza / ModSecurity:** Implemented as a WAF plugin for OWASP Top 10 injection prevention.
- **Istio Service Mesh:** Selected for zero-trust internal security using mTLS and SPIFFE/SPIRE.
- **GitOps (ArgoCD):** Utilized for declarative, reproducible configuration management across hybrid Kubernetes clusters.

## Rationale
This architecture uses an API Gateway pattern combined with a service mesh to meet stringent HIPAA and GDPR compliance mandates while maintaining 99.99% availability. Hybrid deployment via Kubernetes and robust rate-limiting, circuit-breaking, and WAF controls ensure low-latency performance and resilience against failures.