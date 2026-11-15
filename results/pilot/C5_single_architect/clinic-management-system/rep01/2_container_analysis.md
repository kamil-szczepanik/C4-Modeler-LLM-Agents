## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized clinics. It ensures strict healthcare compliance, high availability, and interoperability with external clinical systems.

## Key Elements
- Clinic Staff and Patients (Actors)
- Single Page Application (React Frontend)
- API Gateway (Edge Routing & OAuth2/OIDC)
- Microservices: Patient Management, EMR, Scheduling, Billing
- Integration Layer: HL7 FHIR Integration Container (Apache Camel)
- Data Tier: PostgreSQL (AES-256), Redis (Caching), Elasticsearch (Audit Trail)
- Messaging Backbone: Apache Kafka
- External Systems: Insurance Gateways, Lab/Imaging Systems, Identity Provider

## Relationships
- Clinic Staff/Patients interact with SPA via HTTPS (TLS 1.3)
- SPA connects to API Gateway via HTTPS (OAuth2/OIDC)
- API Gateway routes requests to Microservices via gRPC (mTLS via Istio/Linkerd)
- Microservices persist data to PostgreSQL and cache states in Redis
- Microservices publish domain events to Apache Kafka
- HL7 FHIR Integration Container communicates with Lab/Imaging Systems using HL7 FHIR APIs

## Technology Stack
- React: Provides high-performance, responsive UI for clinical staff (< 1s P95 EMR load).
- Kubernetes (on-prem-k8s & AWS eu-central-1): Orchestrates containerized microservices for 99.99% active-active uptime.
- PostgreSQL: Provides relational storage with AES-256 encryption for HIPAA/GDPR compliance.
- Redis: Delivers low-latency in-memory caching for real-time appointment scheduling clash checks.
- Apache Kafka: Enables asynchronous, decoupled event-driven communication across services.
- Elasticsearch: Implements append-only, immutable storage for mandatory 10-year audit trails.
- Apache Camel: Standardizes internal data into HL7 FHIR resources for clinical interoperability.
- Istio / Linkerd: Secures hybrid cross-cluster traffic with mutual TLS (mTLS).

## Rationale
This hybrid microservices architecture leverages Kubernetes and an encrypted service mesh to guarantee 99.99% active-active availability across on-premise and cloud environments. Dedicated encryption, append-only audit logging, and FHIR translation layers seamlessly satisfy strict HIPAA, GDPR, and interoperability mandates.