## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability and stringent compliance with HIPAA and GDPR regulations.

## Key Elements
- **Users:** Patients, Clinic Staff/Receptionists, Healthcare Providers, Billing Specialists, System Administrators
- **Containers:** Patient Portal (SPA), Staff Dashboard (SPA), API Gateway (Kong/Envoy), Core Clinical & Billing Services, Interoperability & Analytics Gateway Container
- **External Systems:** Identity Provider (IdP), Lab & Imaging Systems, Payment Gateway, Regulatory Registry
- **Data & Infrastructure:** PostgreSQL Database, Apache Kafka / RabbitMQ Event Broker, Kubernetes (on-prem-k8s & AWS EKS), Istio Service Mesh

## Relationships
- Patients & Staff interact with SPAs via HTTPS/REST and WebSockets.
- API Gateway routes traffic to Core Clinical and Interoperability containers using mTLS via Istio.
- Interoperability Container connects to Lab & Imaging Systems via HL7 FHIR over HTTPS.
- Core and Interoperability services persist data to PostgreSQL and exchange events via Kafka using TLS 1.3.

## Technology Stack
- **Frontend:** Nginx-served Single Page Applications for Patient Portal and Staff Dashboard.
- **Gateway & Routing:** Kong or Envoy for API Gateway; HAPI FHIR JPA Server for HL7 interoperability.
- **Backend & Messaging:** Go or Java/Spring Boot for core microservices; Apache Kafka / RabbitMQ for asynchronous event messaging.
- **Data & Security:** PostgreSQL with AES-256 encryption and row-level controls; OAuth 2.0 / OIDC for authentication; Istio for mTLS service mesh.

## Rationale
This hybrid architecture isolates critical clinical workloads while maintaining 99.99% active-active availability across on-premises and AWS environments. Dedicated security boundaries and encryption standards ensure compliance with HIPAA and GDPR data protection mandates.