## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict compliance, and interoperability across hybrid cloud environments.

## Key Elements
* Users: Patient, Clinic Receptionist/Staff, Clinician/Doctor, Billing Specialist, Compliance/IT Administrator
* External Systems: Insurance/Third-Party Payer Gateway, External Lab & Imaging Systems, External SMS/Email Gateways
* Containers: API Gateway, Patient Registration, Appointment Scheduling, EMR Service, Billing & Insurance Service, Identity Provider
* Infrastructure: Kubernetes clusters (`on-prem-k8s`), AWS Cloud (`eu-central-1`), RabbitMQ/Kafka Message Broker, Redis Cache, S3 Storage

## Relationships
* Patient, Staff -> API Gateway: Accesses system features via HTTPS [TLS 1.3, OAuth2/OIDC, MFA]
* API Gateway -> Patient Registration: Routes public and internal admission requests [Istio mTLS]
* Patient Registration -> RabbitMQ/Kafka: Dispatches asynchronous OTP and notification messages [AMQP]
* Patient Registration -> Redis: Enforces rate-limiting and session management [RESP]
* EMR Service -> External Lab & Imaging Systems: Exchanges clinical data [HL7 FHIR REST APIs]

## Technology Stack
* Backend: Spring Boot for containerized microservices ensuring rapid development and modular scalability
* Orchestration & Networking: Kubernetes (`on-prem-k8s`, `eu-central-1`) with Istio Service Mesh for mTLS, circuit breaking, and traffic routing
* Security: OAuth2/OIDC, JWT, AES-256 encryption at rest (with column-level encryption), and TLS 1.3 for HIPAA/GDPR compliance
* Messaging & Caching: RabbitMQ/Kafka for asynchronous resilience; Redis for high-speed rate-limiting
* Observability: Prometheus, Grafana, and FluentBit log shipping to encrypted AWS S3 for auditability

## Rationale
This hybrid architecture uses Kubernetes and Istio to guarantee 99.99% active-active uptime and secure traffic isolation for sensitive clinical workflows. Robust encryption, RBAC, and immutable audit logs satisfy strict HIPAA and GDPR regulations while maintaining sub-second performance.