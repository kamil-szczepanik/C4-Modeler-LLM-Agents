## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It ensures high availability, strict compliance, and clinical interoperability across distributed environments.

## Key Elements
- **Users:** Doctors, Nurses, Receptionists, and Billing Staff.
- **External Systems:** Identity Provider (IdP), Payment Gateway, Insurance Clearinghouse, and External Lab & Imaging Systems.
- **Containers:** Edge API Gateway (Envoy/Kong), On-Premises Core Service (Java/Spring Boot), Cloud EMR & Billing Services (Node.js/Python), Service Mesh Bridge (Istio/Linkerd), and Audit Log Service.
- **Components (On-Premises Core):** Admission Controller, Scheduling Engine, FHIR Interoperability Adapter, Security & Authorization Interceptor, Data Access Repository (Hibernate/JPA), and Event Publisher Component.

## Relationships
- **Users to Edge API Gateway:** HTTPS/TLS with OIDC token validation.
- **Edge API Gateway to On-Premises Core / Cloud Services:** gRPC over TLS and REST/HTTPS.
- **On-Premises Core to External Lab Systems:** HL7 FHIR over REST/TLS.
- **On-Premises Core to Cloud Services:** Apache Kafka streaming via Service Mesh Bridge with mTLS.
- **Services to Databases:** JDBC over TLS with AES-256 encryption.

## Technology Stack
- **Hybrid Cloud:** `on-prem-k8s` for local admissions and scheduling; AWS `eu-central-1` for cloud EMR and billing services, ensuring data residency and high availability (≥ 99.99%).
- **Backend & Persistence:** Java/Spring Boot and Node.js/Python microservices; PostgreSQL/MySQL with AES-256 encryption at rest; Redis for in-memory clash checks.
- **Security & Interoperability:** OpenID Connect (OIDC) via external IdP for MFA; Istio/Linkerd service mesh for zero-trust mTLS; HL7 FHIR APIs for clinical integration.

## Rationale
This hybrid architecture localizes sensitive patient admissions and low-latency scheduling on-premises to guarantee data privacy and high availability. Simultaneously, it leverages cloud elasticity for EMR and billing while enforcing strict HIPAA and GDPR compliance via end-to-end encryption.