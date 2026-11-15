## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics, ensuring HIPAA and GDPR compliance.]
[The architecture provides high availability (99.99%) and sub-second EMR performance using a hybrid cloud deployment.]

## Key Elements
- Patients, Clinicians/Doctors, Receptionists/Admins, Billing Specialists, Auditors
- API Gateway (NGINX / Kong)
- EMR Service (Go) containing EMR API Controller, Access Policy Enforcer, Clinical Record Manager, Audit Trail Interceptor, Data Access Layer, Local Emergency Cache
- Appointment Service, Billing Container, Audit & Compliance Container, HL7 FHIR Interoperability Service
- PostgreSQL with Redis caching
- Apache Kafka with Dead Letter Queues (DLQs)
- External Systems: Patient Portal App, IdP, External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse

## Relationships
- API Gateway -> EMR Service: Routes requests via HTTPS / gRPC with mTLS
- EMR API Controller -> Access Policy Enforcer: Evaluates ABAC rules in-process
- Access Policy Enforcer -> Clinical Record Manager: Forwards validated requests in-process
- Clinical Record Manager -> Data Access Layer: Executes SQL / Redis queries
- EMR Service -> PostgreSQL: Reads and writes records via PostgreSQL protocol with Redis caching
- EMR Service -> Apache Kafka: Publishes EMR events asynchronously via Kafka protocol

## Technology Stack
- Go: Used for EMR API Controller and Clinical Record Manager for high throughput and low-latency P95 performance (<1s)
- PostgreSQL & Redis: Used for secure data storage and hot-record caching to meet high availability and performance goals
- Apache Kafka: Used for reliable asynchronous event streaming with DLQs
- HashiCorp Vault: Used for zero-downtime secret rotation and dynamic X.509 certificate issuance for mTLS

## Rationale
[The hybrid microservices architecture balances on-premise security needs with cloud scalability to meet strict HIPAA, GDPR, and 99.99% uptime constraints.]
[Decomposing the EMR Service into Go-based components with robust caching and encryption guarantees sub-second performance without compromising data integrity.]