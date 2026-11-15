## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides secure, highly available clinical workflows while ensuring strict HIPAA and GDPR compliance across hybrid cloud infrastructure.

## Key Elements
- Web Frontend & Patient Portal / Mobile App (User-facing clients)
- API Gateway (Ingress management, security enforcement, and routing)
- EMR Service & Billing / Claims Service (Core clinical and financial microservices)
- OpenTelemetry & Audit Logging sidecars (Observability and WORM audit trails)
- HashiCorp Vault (Dynamic Secrets Manager)
- Open Policy Agent (OPA) sidecar (Authorization engine)
- Infrastructure: on-prem-k8s cluster and AWS (eu-central-1)

## Relationships
- Web Frontend / Patient Portal -> API Gateway: Routes requests via HTTPS/TLS 1.3
- API Gateway -> EMR Service: Forwards internal requests via gRPC/REST over mTLS (SPIFFE/SPIRE)
- API Gateway -> Billing / Claims Service: Forwards billing requests via gRPC/REST over mTLS (SPIFFE/SPIRE)
- API Gateway -> OPA Sidecar: Evaluates Attribute-Based Access Control (ABAC) policies locally

## Technology Stack
- Kubernetes (on-prem-k8s and AWS eu-central-1): Hybrid container orchestration supporting active-active deployment
- OAuth2/OIDC & JWT: Edge authentication and token validation
- Open Policy Agent (OPA): Decentralized authorization and ABAC evaluation
- SPIFFE/SPIRE: Zero-trust workload identity and mTLS communication
- OpenTelemetry: Distributed tracing and observability sidecars
- ArgoCD: GitOps-based configuration management

## Rationale
This hybrid architecture uses active-active deployment, edge security controls, and decentralized policy caching to meet 99.99% availability and sub-second EMR performance. Zero-trust principles and strict cryptographic controls guarantee HIPAA and GDPR compliance while supporting scalable clinical operations.