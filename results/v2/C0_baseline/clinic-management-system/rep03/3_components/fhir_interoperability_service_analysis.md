## Overview
The Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, high availability (99.99%), and long-term data retention across hybrid cloud environments.

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Officers, Patients, Regulatory Auditors
- **External Systems**: Identity Provider, External Lab & Imaging Systems, Third-Party Payment Gateway & Insurance Clearinghouse, Centralized SIEM & Observability Platform, Global Traffic Manager / Anycast DNS, Distributed Network Interconnect / SD-WAN
- **Containers**: React Single-Page Application (SPA) / React Native Mobile Client, Envoy API Gateway / Edge Proxy, EMR & Scheduling Service, Billing & Claims Service, FHIR Interoperability Service (HAPI FHIR, Java), Region-local PostgreSQL databases, Localized Apache Kafka/RabbitMQ message brokers, AWS S3 / on-prem object storage (WORM), HashiCorp Vault
- **FHIR Interoperability Components**: FHIR API Controller (HAPI FHIR REST Framework, Java), Transformation Engine (Apache Camel, Java), Async Event Dispatcher (Spring Cloud Stream / Kafka Client)

## Relationships
- Envoy API Gateway / Edge Proxy -> FHIR Interoperability Service: Routes interoperability requests securely [Internal mTLS via Istio/Linkerd]
- FHIR API Controller -> Transformation Engine: Validated FHIR payload [Java interface]
- Transformation Engine -> Localized PostgreSQL: Atomic outbox write [JDBC / SQL]
- Async Event Dispatcher -> Localized Apache Kafka/RabbitMQ: Publishes outbox events [Kafka protocol / W3C Trace Context]
- FHIR Interoperability Service -> HashiCorp Vault: Retrieves secrets dynamically [HTTPS / Vault API]
- FHIR Interoperability Service -> External Lab & Imaging Systems: Exchanges lab and imaging data [HL7 FHIR over HTTPS, TLS 1.3]

## Technology Stack
- **Frontend**: React, React Native, CDN for UI delivery
- **Backend Services**: Node.js, Java / Spring Boot, HAPI FHIR Framework, Apache Camel for enterprise integration
- **Messaging & Persistence**: Apache Kafka, RabbitMQ, PostgreSQL with transactional outbox pattern, AWS S3 / WORM Object Storage for 10-year retention
- **Security & Infrastructure**: Kubernetes (on-prem-k8s, eu-central-1), Envoy, HashiCorp Vault, OAuth 2.0 / OIDC with SMART-on-FHIR scopes, AES-256 at rest, TLS 1.3 in transit
- **Observability**: OpenTelemetry with W3C Trace Context, Centralized SIEM

## Rationale
The hybrid architecture utilizes Kubernetes and active-active replication to guarantee the required 99.99% uptime and low-latency performance. HAPI FHIR with strict schema validation, OAuth2, and AES-256 encryption fulfills interoperability (HL7 FHIR) and regulatory compliance (HIPAA/GDPR).