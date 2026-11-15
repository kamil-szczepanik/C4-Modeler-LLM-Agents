## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records, scheduling, and billing securely. It guarantees high availability, strict HIPAA/GDPR compliance, and sub-second EMR performance.

## Key Elements
- Users: Receptionists, Clinicians, Billing Officers, Patients
- External Systems: External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouses, Identity Provider (IdP)
- Containers: API Gateway (Kong/Nginx), Patient-Facing UI (React/Next.js), Patient Portal, Clinical Core Services (Spring Boot), Interoperability Service (Apache Camel/Node.js), Billing & Claims Service (Spring Boot)
- Data Persistence: PostgreSQL (OLTP with AES-256 and column-level encryption)
- Message Broker: RabbitMQ / Kafka with DLQ
- Infrastructure: Hybrid deployment on-premise Kubernetes and AWS eu-central-1 via ArgoCD, Istio Service Mesh, and AWS S3 Glacier WORM vaults

## Relationships
- Patients & Staff access the system via HTTPS/TLS through the API Gateway (Kong/Nginx) validating JWTs.
- Patient-Facing UI communicates with backend containers via OAuth2 authorization code flow with PKCE.
- Clinical Core Services, Billing & Claims, and Interoperability services communicate internally using gRPC over mTLS.
- Interoperability Service connects to external Lab & Imaging systems via HL7 FHIR REST APIs using mTLS and SMART-on-FHIR scopes.
- Billing & Claims Service interacts with third-party clearinghouses asynchronously via RabbitMQ / Kafka message queues.

## Technology Stack
- API Gateway: Kong or Nginx for edge routing, WAF, rate-limiting, and JWT validation.
- Frontend: React / Next.js for the Patient-Facing UI container.
- Backend Services: Spring Boot (Java) for Clinical Core and Billing & Claims services.
- Integration: Apache Camel or Node.js for HL7 FHIR Interoperability service.
- Database: PostgreSQL with Crunchy Data Operator for active-active synchronous replication and AES-256 / column-level encryption.
- Messaging: Apache Kafka or RabbitMQ with persistent storage for asynchronous billing workflows.
- Infrastructure & Security: Kubernetes, ArgoCD, Istio Service Mesh, OpenTelemetry, HashiCorp Vault / AWS KMS, and S3 Glacier WORM storage.

## Rationale
This hybrid architecture isolates external-facing components like the Patient Portal and UI from internal clinical workflows, protecting the sub-second EMR performance target. Furthermore, active-active PostgreSQL clustering, gRPC communication over mTLS, and robust message queuing ensure 99.99% availability and rigorous HIPAA/GDPR compliance.