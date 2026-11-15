## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent security, and strict regulatory compliance for healthcare operations.

## Key Elements
- Users: Doctors, Nurses, Receptionists, Billing Specialists
- Containers: Web Application Frontend, API Gateway, Core Services Container, EMR & Audit Service, Billing & Insurance Integration Worker, Async Message Broker, PostgreSQL Primary DB, WORM-compliant storage
- Components (Billing & Insurance Integration Worker): Claim Consumer Component, Claim Transformation Component, Clearinghouse Adapter Component, Audit & Reconciliation Logger Component
- External Systems: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Enterprise Identity Provider, Third-Party Notification Service

## Relationships
- Claim Consumer -> Claim Transformation: Passes raw payload [In-memory]
- Claim Transformation -> Clearinghouse Adapter: Passes formatted claim [HTTPS]
- Clearinghouse Adapter -> Payment Gateway / Insurance Clearinghouse: Submits encrypted claims [HTTPS / REST, TLS 1.3]
- All components -> Audit & Reconciliation Logger: Emits audit logs [SQL / TLS]
- Integration Worker -> Async Message Broker: Consumes claims events [AMQP / Kafka]

## Technology Stack
- Frontend: React / TypeScript served via CDN/Nginx
- Gateway/Core: Kong / Nginx API Gateway, Node.js / Java Spring Boot Core Services
- Integration Worker: Node.js with KafkaJS (consumer), TypeScript (transformation), Axios with Opossum circuit breaker (adapter)
- Database & Storage: PostgreSQL Primary DB with AES-256 encryption, WORM-compliant storage

## Rationale
This architecture ensures 99.99% high availability and active-active multi-region resiliency to meet demanding hospital uptime requirements. Encrypted storage, TLS 1.3, and robust audit logging guarantee strict HIPAA and GDPR compliance while maintaining sub-second EMR performance.