## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Patients, Clinicians, Administrative Staff, Billing Officers, System Administrators
- **External Systems**: Insurance/Payer Gateways, External Lab/Imaging Systems, Identity Provider (IdP)
- **Containers**: API Gateway / Reverse Proxy (NGINX / Envoy), Clinical Web/Mobile App (React / React Native), Patient Portal App (Next.js), EMR & Scheduling Service (Node.js / NestJS), Billing Service (Java / Spring Boot), Integration & Interoperability Service (Apache Camel / Spring Boot), Audit & Compliance Service (Python / FastAPI), Data Tier (PostgreSQL with WORM Object Storage), Message Broker (Apache Kafka)
- **Message Broker Components**: Broker Cluster (Apache Kafka Core), Schema Registry (Confluent Schema Registry), MirrorMaker 2 Engine, Prometheus JMX Exporter, Dead Letter Queues (DLQ)

## Relationships
- *Clinical Web/Mobile App -> API Gateway / Reverse Proxy*: Routes client traffic via HTTPS / TLS 1.3
- *API Gateway / Reverse Proxy -> EMR & Scheduling Service*: Forwards authenticated requests via gRPC / HTTP/2
- *EMR & Scheduling Service / Billing Service -> Message Broker*: Publishes events via TLS 1.3 using Kafka TCP Protocol (`SASL_SSL`)
- *MirrorMaker 2 -> AWS MSK / Cloud Broker*: Replicates encrypted topic streams over mutual TLS (mTLS) across the hybrid boundary
- *Integration & Interoperability Service -> External Lab/Imaging Systems*: Exchanges clinical data via HL7 FHIR APIs over HTTPS

## Technology Stack
- **Languages & Frameworks**: Node.js / NestJS (EMR), Java / Spring Boot (Billing), Python / FastAPI (Audit), React / React Native & Next.js (Frontend)
- **Infrastructure & Orchestration**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) for hybrid container deployment
- **Message Broker**: Apache Kafka with Confluent Schema Registry and MirrorMaker 2 for event-driven durability and disaster recovery
- **Database & Storage**: PostgreSQL for transactional data, WORM Object Storage with AWS S3 Object Lock for 10-year retention
- **Security & Observability**: TLS 1.3, AES-256 at rest, OAuth2/OIDC via IdP, Prometheus JMX exporter, OpenTelemetry

## Rationale
This architecture uses an event-driven microservices pattern with Apache Kafka to decouple workloads, ensuring the <1s EMR response time and 99.99% availability requirements. Hybrid deployment with MirrorMaker 2 balances strict on-premises data control with scalable cloud resilience while strictly enforcing HIPAA and GDPR mandates.