## Overview
The Clinic Management System is a clinical IT platform that handles patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent compliance, and low-latency interactions for healthcare providers.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers, Compliance Officers
- External Insurance/Clearinghouse System, External Laboratory & Imaging System
- Web Application (React / TypeScript)
- API Gateway (Envoy Proxy with WAF module)
- Microservices: EMR Service (Node.js / Go), Billing & Claims Service (Java / Spring Boot), Scheduling Service (Node.js / Go), Notification Service (Python / FastAPI), Integration Service (Java / Spring Boot)
- Infrastructure: PostgreSQL (AES-256), Redis, RabbitMQ Message Broker, HashiCorp Vault

## Relationships
- Web Application -> API Gateway: Client requests [HTTPS / REST]
- API Gateway -> EMR Service: Routes EMR traffic [mTLS / gRPC / HTTPS]
- API Gateway -> Billing & Claims Service: Routes billing requests [mTLS / gRPC / HTTPS]
- API Gateway -> Scheduling Service: Routes scheduling requests [mTLS / gRPC / HTTPS]
- Integration Service -> External Laboratory & Imaging System: Exchanges clinical data [HL7 FHIR APIs]

## Technology Stack
- Envoy Proxy: Edge ingress, routing, local JWT validation, and WAF protection for low latency and security.
- Redis: Global rate-limiting and priority queuing to protect EMR performance.
- HashiCorp Vault: Secure secret management and public key distribution for token validation.
- PostgreSQL: Primary datastore encrypted with AES-256 at rest for HIPAA/GDPR compliance.
- Kubernetes: Hybrid deployment across `on-prem-k8s` and `eu-central-1` supporting active-active 99.99% availability.

## Rationale
This hybrid, containerized architecture enforces strict security controls (mTLS, AES-256, WAF) and local token validation to satisfy HIPAA/GDPR compliance without violating the <1s EMR load time requirement. Active-active multi-region deployment on Kubernetes guarantees high availability (99.99%) for mission-critical clinical operations.