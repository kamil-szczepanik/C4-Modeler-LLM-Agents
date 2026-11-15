## Overview
The Clinic Management System is a hybrid cloud platform designed to streamline patient admissions, EMRs, scheduling, and billing for healthcare clinics. It ensures strict HIPAA/GDPR compliance, high availability, and rapid clinical data access.

## Key Elements
- **Users**: Patients, Clinical Staff, Administrative Staff, Compliance Officers
- **Containers**: API Gateway / BFF, Patient Portal, EMR & Scheduling Container, Billing & Claims Container, Analytics & Reporting Container, Data & Messaging Layer
- **API Gateway Components**: Edge Router & TLS Terminator, Auth & Policy Enforcement Filter, Persona-Specific BFF Routers
- **External Systems**: Lab & Imaging Systems, Payment Gateway & Insurance Clearinghouse, Regulatory & Auditing System

## Relationships
- Patients, Clinical Staff, Administrative Staff, Compliance Officers -> API Gateway / BFF [OAuth2/OIDC, mTLS, HTTPS/REST]
- API Gateway / BFF -> EMR & Scheduling Container [gRPC over HTTP/2, mTLS]
- API Gateway / BFF -> Billing & Claims Container [gRPC over HTTP/2, mTLS]
- Edge Router -> Auth & Policy Enforcement Filter [In-Memory Plugin Call, Lua/Wasm]
- Auth & Policy Enforcement Filter -> Persona-Specific BFF Routers [Internal Request Headers]

## Technology Stack
- **Kong / Envoy**: Chosen for edge routing, TLS termination, and low-latency in-memory plugin execution.
- **Node.js / TypeScript**: Powers the Patient Portal for rapid UI integration.
- **Java Spring Boot**: Used for EMR & Scheduling for robust enterprise scalability.
- **Python / FastAPI**: Powers Billing & Claims for fast API development.
- **PostgreSQL, Redis, Apache Kafka, Debezium**: Provides secure, ACID-compliant data persistence and real-time streaming.
- **gRPC over HTTP/2**: Ensures low-latency internal service-to-service communication.

## Rationale
This architecture uses a BFF pattern and gRPC communication to meet strict sub-second EMR load time requirements. Edge-enforced security and internal mTLS satisfy HIPAA and GDPR mandates while maintaining 99.99% availability.