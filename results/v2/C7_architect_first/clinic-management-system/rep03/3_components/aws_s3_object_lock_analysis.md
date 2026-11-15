## Overview
The Clinic Management System is a hybrid-cloud healthcare platform providing patient admissions, electronic medical records (EMR), scheduling, and billing. Its core purpose is to deliver secure, highly available, and compliant clinical IT operations for medium-sized hospitals and clinics.

## Key Elements
- **Users**: Doctors, Nurses, Receptionists, Billing Staff, Clinic Administrators, Patients, Compliance Officer
- **External Systems**: Identity Provider (IdP), External Labs & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- **Containers**: API Gateway (Nginx / Kong), Web Application SPA (React / TypeScript), Core Services (Node.js / Spring Boot), PostgreSQL, Redis, Apache Kafka, AWS S3 Object Lock
- **AWS S3 Components**: Object Ingestion API, Retention Enforcement Engine, Audit Logger, KMS Envelope Encryption Wrapper

## Relationships
- Web Application -> API Gateway: Manages user interactions [HTTPS]
- API Gateway -> Core Services: Routes client requests [REST / gRPC]
- Core Services -> PostgreSQL / Redis / Kafka: Persists transactional data, caches state, and streams events [TCP / AMQP]
- Core Services -> AWS S3 Object Lock: Stores immutable compliance data via KMS envelope encryption [HTTPS / AWS SDK over AWS PrivateLink]
- Core Services -> External Systems: Integrates via HL7 FHIR APIs [HTTPS]

## Technology Stack
- **Frontend**: React / TypeScript on Nginx for responsive SPA delivery
- **Backend**: Node.js / NestJS or Java / Spring Boot for scalable core services
- **Databases & Caching**: PostgreSQL (Active-Passive) for relational records; Redis for low-latency caching
- **Messaging**: Apache Kafka for asynchronous event streaming
- **Storage & Security**: AWS S3 Object Lock (WORM Compliance Mode) with AWS KMS for 10-year immutable retention and cryptographic GDPR erasure
- **Infrastructure**: Hybrid deployment across on-premise Kubernetes and AWS eu-central-1

## Rationale
This architecture uses active-passive replication and cloud-native WORM storage to guarantee 99.99% availability and strict 10-year medical data retention. Combining AWS S3 Object Lock with KMS cryptographic shredding resolves the conflict between HIPAA immutability and GDPR right-to-erasure mandates.