## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high-availability clinical workflows while adhering to strict HIPAA, GDPR, and 10-year data retention mandates.

## Key Elements
- Patients, Clinicians/Doctors, Receptionists/Admins, Billing Specialists, Compliance/IT Auditors
- Patient Portal App, Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- API Gateway (NGINX / Kong)
- Appointment Service (Node.js / Go) containing Appointment API Controller, Scheduling Engine, Waitlist Manager, and Notification Publisher
- EMR Service, Billing Container, Audit & Compliance Container, HL7 FHIR Interoperability Service
- PostgreSQL with Redis caching, Apache Kafka

## Relationships
- Patient Portal App -> API Gateway: Routes requests [HTTPS / REST / gRPC with mTLS]
- API Gateway -> Appointment Service: Routes scheduling requests [HTTPS / gRPC with mTLS]
- Appointment API Controller -> Scheduling Engine: Invokes core domain logic [In-Process]
- Scheduling Engine -> PostgreSQL: Executes atomic writes and resource clash checks [SQL/TCP with AES-256 and Redis Redlock]
- Scheduling Engine -> Notification Publisher: Publishes domain events and analytics tags [Kafka Producer]
- Notification Publisher -> Waitlist Manager: Triggers slot-freed events [In-Process / Event Handler]

## Technology Stack
- **Languages & Runtimes**: Node.js/TypeScript, Python (FastAPI), and Go chosen for high-concurrency, low-footprint microservices.
- **APIs & Protocols**: HTTPS, gRPC, and HL7 FHIR APIs for robust clinical interoperability.
- **Database & Caching**: PostgreSQL with AES-256 envelope encryption and Redis caching for distributed locking.
- **Messaging & Infrastructure**: Apache Kafka for asynchronous event publishing; Kubernetes (on-prem and eu-central-1) for multi-region active-active deployment.

## Rationale
This hybrid architecture guarantees 99.99% availability via active-active Kubernetes clusters and regional database replication. It enforces stringent HIPAA and GDPR compliance through TLS 1.3, AES-256 encryption, and RBAC controls.