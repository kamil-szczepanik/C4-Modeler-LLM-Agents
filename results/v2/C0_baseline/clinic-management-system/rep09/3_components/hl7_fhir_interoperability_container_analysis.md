## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and HL7 FHIR interoperability.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, Compliance Officers
- External Identity Provider, External Labs & Imaging Systems, Insurance Claim Gateways
- Nginx Web App, API Gateway (Kong/Envoy)
- Core Clinical & EMR Container, Billing & Claims Container
- HL7 FHIR Interoperability Container (Node.js/Apache Camel)
- Patient Portal Container, Sync/Replication Container (Apache Kafka), Audit Sidecar Container (OpenTelemetry, HashiCorp Vault)
- Internal Components: FHIR API Router, SMART-on-FHIR Authorizer, FHIR Validation & Transformation Engine, Outbox Event Publisher, External TLS Client Connector, Circuit Breaker Proxy, PHI Sanitization Middleware

## Relationships
- Patient Portal & Nginx Web App -> API Gateway: HTTPS over TLS
- API Gateway -> HL7 FHIR Interoperability Container: gRPC over mTLS (Istio/Linkerd)
- HL7 FHIR Interoperability Container -> External Labs & Imaging Systems: HL7 FHIR APIs over TLS with mTLS
- FHIR API Router -> SMART-on-FHIR Authorizer: In-memory middleware
- External TLS Client Connector -> Circuit Breaker Proxy: In-memory invocation
- Validation & Transformation Engine -> Outbox Event Publisher: Internal message queue

## Technology Stack
- Hybrid Cloud: On-premise Kubernetes (`on-prem-k8s`) and AWS (`eu-central-1`) for active-active high availability
- Backend Runtimes: Node.js (Express/NestJS) and Apache Camel for integration pipelines
- Messaging & Integration: Apache Kafka for event-driven synchronization and DLQ handling; Resilience4j for circuit breaking
- Security & Compliance: AES-256 encryption at rest, OAuth2 / SMART-on-FHIR, OpenTelemetry, and HashiCorp Vault sidecar for secret/certificate rotation

## Rationale
This hybrid architecture uses cloud-native microservices, strict security boundaries, and robust integration patterns to guarantee 99.99% uptime, data protection, and seamless interoperability. Component isolation and active-active replication satisfy rigorous healthcare regulations and performance SLAs.