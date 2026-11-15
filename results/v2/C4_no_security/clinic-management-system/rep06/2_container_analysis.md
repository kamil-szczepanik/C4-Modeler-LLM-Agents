## Overview
The Clinic Management System manages patient admissions, electronic medical records (EMR), scheduling, and billing for healthcare facilities. It provides high availability, strict regulatory compliance, and localized hybrid cloud deployment.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers
- API Gateway / Reverse Proxy (NGINX / Envoy)
- Clinical Web/Mobile App (React / React Native)
- Patient Portal App (Next.js)
- EMR & Scheduling Service (Node.js / NestJS)
- Billing Service (Java / Spring Boot)
- Integration & Interoperability Service (Apache Camel / Spring Boot)
- Audit & Compliance Service (Python / FastAPI)
- Data Tier (PostgreSQL with WORM Object Storage)
- Message Broker (Apache Kafka)
- External Systems: Insurance Gateways, Lab/Imaging Systems, Identity Provider (IdP)

## Relationships
- Clinical Web App -> API Gateway via HTTPS/WSS
- Patient Portal App -> API Gateway via HTTPS
- API Gateway -> EMR Service, Billing Service, and Integration Service via gRPC / REST
- EMR Service -> Audit & Compliance Service via gRPC / Kafka
- Integration Service -> External Lab/Imaging Systems via HTTPS/FHIR
- Billing Service -> Apache Kafka for asynchronous event publishing

## Technology Stack
- Node.js / NestJS: Chosen for the EMR & Scheduling Service to handle rapid domain logic execution.
- Java / Spring Boot: Selected for the Billing Service to ensure robust transactional integrity.
- PostgreSQL: Utilized for primary transactional data with AES-256 encryption at rest.
- Apache Kafka: Deployed for asynchronous event-driven decoupling of billing workloads.
- Kubernetes: Used across on-prem-k8s and AWS eu-central-1 for container orchestration.
- Cilium/Istio: Enforces mTLS across the hybrid network topology.

## Rationale
Decoupling clinical workloads from billing via Apache Kafka guarantees high availability (99.99%) for critical patient care operations. Localized regional database isolation avoids WAN latency penalties, ensuring EMR screen loads remain under 1 second.