## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention across a hybrid cloud infrastructure.

## Key Elements
- Patients, Receptionists, Physicians, and Billing Specialists
- API Gateway (Go), Patient Portal Frontend (Node.js), Physician EMR Frontend (React)
- EMR Backend (Java Spring Boot), Billing Service (Python)
- Apache Kafka (Event Broker)
- PostgreSQL & WORM Storage (Database)
- External Systems: Payment Gateways, Lab/Imaging Systems, Enterprise IDP

## Relationships
- API Gateway -> Physician EMR Frontend: Routes requests to physician frontend [HTTPS]
- Physician EMR Frontend -> EMR Backend: Communicates for EMR operations [gRPC-Web with mTLS]
- EMR Backend -> PostgreSQL & WORM Storage: Persists clinical data and audit trails [TCP/TLS]
- EMR Backend -> Lab and Imaging Systems: Interoperates via HL7 FHIR APIs [HTTPS/REST]

## Technology Stack
- React with Vite & Nginx Sidecar: Powers the Physician EMR Frontend for sub-second P95 performance
- Redux Toolkit & Encrypted IndexedDB: Manages state caching and secure draft persistence locally
- Java Spring Boot: Drives the high-performance EMR Backend services
- Apache Kafka: Handles asynchronous event streaming across microservices
- Web Crypto API: Secures cached PHI in browser storage per HIPAA/GDPR constraints

## Rationale
This hybrid architecture uses cloud-native technologies and active-active clustering to meet strict 99.99% availability and high-performance requirements. Strict encryption protocols and audit mechanisms guarantee compliance with healthcare security mandates.