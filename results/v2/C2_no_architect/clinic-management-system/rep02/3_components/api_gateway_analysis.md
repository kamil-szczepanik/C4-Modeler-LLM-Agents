## Overview
The Clinic Management System manages patient admissions, Electronic Medical Records (EMR), scheduling, and billing for medium-sized healthcare facilities. It is built as a high-availability, hybrid cloud architecture ensuring strict HIPAA and GDPR compliance.

## Key Elements
- Users: Patient, Clinic Receptionist/Staff, Clinician/Doctor, Billing Specialist, Compliance/IT Administrator
- External Systems: Insurance/Third-Party Payer Gateway, External Lab & Imaging Systems
- API Gateway: Kubernetes Ingress / Istio (Perimeter routing, TLS termination, WAF, and token exchange)
- Microservices: Patient Registration, Appointment Scheduling, EMR Service, Billing & Insurance Service (Spring Boot / Kubernetes)

## Relationships
- Patient, Staff, Doctor, Billing Specialist, Administrator -> API Gateway: Accesses services [HTTPS with MFA and ABAC]
- API Gateway -> Patient Registration: Routes registration traffic [Istio mTLS with W3C Trace Context]
- API Gateway -> Appointment Scheduling: Routes scheduling traffic [Istio mTLS with W3C Trace Context]
- API Gateway -> EMR Service: Routes EMR and clinical queries [Istio mTLS with W3C Trace Context]
- API Gateway -> Billing & Insurance Service: Routes billing payloads [Istio mTLS with W3C Trace Context]

## Technology Stack
- Kubernetes & Istio: Orchestrates container workloads and service mesh traffic with active-active multi-region deployment for 99.99% uptime.
- Spring Boot: Powers backend microservices for rapid development and clinical workload isolation.
- OAuth2/OIDC & JWT/PASETO: Manages perimeter token exchange and fine-grained ABAC claims enforcement.
- OpenTelemetry & Prometheus: Enables distributed tracing and real-time latency monitoring.

## Rationale
This hybrid microservices architecture meets the 99.99% availability requirement using active-active regional failover and Istio circuit breaking. Perimeter security controls like WAF, edge schema validation, and token exchange ensure rigorous HIPAA and GDPR compliance without compromising sub-second EMR performance.