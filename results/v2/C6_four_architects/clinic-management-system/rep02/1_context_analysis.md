## Overview
The Clinic Management System is a hybrid cloud platform designed to handle patient registration, scheduling, electronic medical records (EMR), and billing for medical clinics. It guarantees HIPAA/GDPR compliance, 99.99% availability, and strict 10-year data retention.

## Key Elements
- **Users & Actors**: Doctors, Nurses, Receptionists, Billing Officers, and Patients.
- **External Systems**: External Lab/Imaging Systems, Insurance Clearinghouses, Payment Gateway (Stripe-like), Identity Provider (Keycloak/Azure AD), and Notification Service (Twilio/AWS SES).
- **Containers**: API Gateway (Kong/NGINX), Core Clinical & EMR Service (Spring Boot), Scheduling & Billing Service (Node.js), FHIR Integration Broker (Python/FastAPI), Notification Worker (Go).
- **Data & Storage**: PostgreSQL, Redis, Apache Kafka, MinIO/AWS S3.
- **Components (Core EMR)**: Patient Demographic Controller, EMR Management Component, Audit Trail Logger, Data Access Repository.

## Relationships
- Users/Patients to API Gateway: HTTPS (TLS 1.3), OpenID Connect (OIDC).
- API Gateway to Internal Containers: gRPC over mTLS.
- CMS to External Lab/Imaging & Clearinghouses: HL7 FHIR over REST/HTTPS.
- CMS to Payment Gateway & Notification Provider: REST/HTTPS.
- Services to Data Stores: PostgreSQL wire protocol, Redis protocol, Kafka protocol, S3 API, all secured via mTLS and AES-256 at rest.

## Technology Stack
- **Frontend/Gateway**: NGINX/Kong for TLS termination and OIDC validation.
- **Backend Services**: Java (Spring Boot) for core EMR, Node.js for scheduling/billing, Python for FHIR, Go for notifications.
- **Databases & Caching**: PostgreSQL with active-active replication for primary data, Redis for <1s P95 read latency.
- **Messaging & Storage**: Apache Kafka for event bus, MinIO/AWS S3 for object storage and immutable audit logs.
- **Infrastructure**: Hybrid deployment across on-premise Kubernetes and AWS `eu-central-1`.

## Rationale
The hybrid architecture distributes workloads across on-premise Kubernetes and cloud infrastructure to meet stringent HIPAA/GDPR data residency mandates. Active-active PostgreSQL replication, Kafka messaging, and Redis caching ensure 99.99% availability and high-performance EMR access.