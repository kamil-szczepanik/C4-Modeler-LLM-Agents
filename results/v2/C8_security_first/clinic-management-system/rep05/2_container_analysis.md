## Overview
## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and strict EMR performance targets.

## Key Elements
- Users: Patient, Clinic Staff, Clinician, Billing Specialist
- External Systems: Enterprise Identity Provider (IdP), Insurance Claim Clearinghouse, Lab & Imaging Systems, Notification System
- Containers: Envoy Proxy API Gateway, OAuth2-Proxy / Keycloak Sidecar, EMR & Patient Service (Node.js/Fastify), Billing & Claims Service (Java Spring Boot), FHIR Interoperability Gateway (HAPI FHIR)
- Data & Messaging: PostgreSQL (CloudNativePG), Apache Kafka

## Relationships
- Users to API Gateway: HTTPS / TLS 1.3
- API Gateway to Identity & Access Proxy: Internal HTTP / mTLS
- Microservices to Microservices: gRPC over mTLS
- Billing & Claims Service to Insurance Claim Clearinghouse: Asynchronous queue-based integration via Apache Kafka
- Interoperability Gateway to External Lab & Imaging Systems: HL7 FHIR APIs

## Technology Stack
- Ingress & Routing: Envoy Proxy for TLS 1.3 termination and rate limiting
- Core Services: Node.js/Fastify for EMR/Patient workflows; Java/Spring Boot for Billing
- Interoperability: HAPI FHIR for HL7 FHIR standards compliance
- Persistence & Messaging: PostgreSQL with AES-256 encryption; Apache Kafka for asynchronous event streaming
- Infrastructure & Deployment: Kubernetes (`on-prem-k8s`, `eu-central-1`), ArgoCD, Cilium/Falco (eBPF security)

## Rationale
This architecture uses decoupled microservices, local message queuing, and isolated read replicas to achieve strict <1s EMR load performance and billing resilience during outages. Multi-region active-active deployments with asynchronous cross-site replication satisfy the 99.99% availability and 10-year data retention mandates.