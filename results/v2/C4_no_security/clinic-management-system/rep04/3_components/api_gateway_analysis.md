## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability, regulatory compliance, and high-performance clinical workflows across a hybrid cloud infrastructure.]

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists
- Identity Provider, Third-Party Payment Gateway, Insurance Clearinghouse, External Lab & Imaging Systems
- API Gateway Container (Envoy / NGINX) with internal components: TLS Termination, Auth Filter, Rate Limiter, Dynamic Router, QOS Filter, Circuit Breaker
- Web Application Container (React / Next.js)
- Clinical & EMR Core Container (Spring Boot / Java)
- Billing & Claims Container (Node.js / Express)
- HL7 FHIR Integration Container (Apache Camel)
- Edge Sync Container (Go Daemon)
- Primary DB & Audit Store (PostgreSQL with Patroni)
- Redis Cache Cluster

## Relationships
- Web Application Container -> API Gateway: Sends user requests via HTTPS [HTTPS]
- API Gateway -> Clinical & EMR Core Container: Routes validated, prioritized traffic [TLS / JWT / gRPC]
- API Gateway -> Billing & Claims Container: Routes validated requests [TLS / JWT / HTTP]
- Rate Limiter -> Redis Cache: Checks usage counters [gRPC / Redis Protocol, <2ms latency]

## Technology Stack
- Envoy / NGINX: Chosen for high-performance edge routing, TLS termination, and traffic management
- Redis Cluster: Selected for low-latency rate limiting and token bucket sync
- Spring Boot / Java: Powers the core EMR for robust enterprise reliability
- PostgreSQL with Patroni: Ensures high availability and secure 10-year audit trails
- Apache Camel: Standardizes HL7 FHIR interoperability with external labs

## Rationale
- The hybrid architecture combines on-premises Kubernetes and AWS `eu-central-1` to guarantee 99.99% active-active uptime.
- End-to-end TLS, JWT validation, and AES-256 encryption satisfy strict HIPAA and GDPR compliance mandates.