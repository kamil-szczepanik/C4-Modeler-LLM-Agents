## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and strict data retention policies.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
- **Clients**: React Single-Page Application (SPA) / React Native Mobile Client
- **Edge Layer**: Envoy API Gateway / Edge Proxy
- **Core Services**: EMR & Scheduling Service (Node.js/Java), Billing & Claims Service (Java), FHIR Interoperability Service (HAPI FHIR)
- **Data & Messaging Tier**: Region-local PostgreSQL databases, localized Apache Kafka/RabbitMQ message brokers, AWS S3 / on-prem object storage (WORM)
- **Infrastructure & Security**: Kubernetes (`on-prem-k8s`, `eu-central-1`), Istio/Linkerd Service Mesh, HashiCorp Vault, Centralized SIEM

## Relationships
- Clients interact with the Envoy API Gateway via HTTPS/TLS 1.3 using OAuth2/OIDC validation.
- Envoy routes requests to internal containers using internal mTLS via Istio/Linkerd.
- EMR and Billing services connect to region-local PostgreSQL instances via encrypted TCP.
- FHIR Interoperability Service communicates asynchronously with backend services via Apache Kafka/RabbitMQ using W3C Trace Context headers.
- Services retrieve secrets dynamically from HashiCorp Vault.

## Technology Stack
- **Frontend**: React and React Native delivered via CDN for optimized client rendering.
- **Backend**: Node.js/TypeScript and Java/Spring Boot containers optimized for sub-second responses.
- **Database & Storage**: PostgreSQL for regional operational storage; S3-compatible object storage with WORM policies for 10-year audit retention.
- **Messaging**: Apache Kafka or RabbitMQ for asynchronous, decoupled data exchanges.
- **Infrastructure & Security**: Kubernetes orchestrated via ArgoCD, Istio/Linkerd for mTLS, HashiCorp Vault for secrets management, and OpenTelemetry for observability.

## Rationale
The hybrid architecture utilizes region-local primary databases and asynchronous messaging to prevent wide-area network latency, ensuring sub-second EMR load times and 99.99% availability. Strict container isolation, mTLS, AES-256 encryption, and immutable audit logs satisfy rigorous HIPAA, GDPR, and financial compliance mandates.