## Overview
[The Clinic Management System manages patient admissions, EMR, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.]

## Key Elements
- Billing Officers (Users)
- Claim Submission Controller (Spring WebMVC)
- Clearinghouse Adapter (Spring Cloud OpenFeign)
- Billing Event Publisher (Apache Kafka)
- WORM Archival Service (Spring Batch / AWS S3)
- Billing Audit & Ledger Component (Spring Data JDBC / Axon Framework)
- Region-local PostgreSQL databases
- Third-Party Payment Gateway & Insurance Clearinghouse
- HashiCorp Vault

## Relationships
- Envoy API Gateway -> Claim Submission Controller: Routes requests via internal mTLS [Istio/Linkerd]
- Claim Submission Controller -> Third-Party Payment Gateway: Synchronous validation [REST over HTTPS]
- Billing Event Publisher -> Apache Kafka: Publishes financial events [Kafka Protocol with mTLS]
- WORM Archival Service -> AWS S3 / Object Storage: Archives records [HTTPS / S3 API with Object Lock]
- Clearinghouse Adapter -> HashiCorp Vault: Fetches dynamic API keys [HTTPS / Vault API]
- Billing Audit & Ledger Component -> Region-local PostgreSQL: Persists audit trails [Encrypted TCP / TLS 1.3]

## Technology Stack
- Java / Spring Boot: Core framework for microservices providing robust enterprise capabilities
- Spring Cloud OpenFeign & Resilience4j: Handles external clearinghouse communication with circuit breakers
- Apache Kafka: Asynchronous event streaming for billing and ledger lifecycles
- HashiCorp Vault: Dynamic secrets and cryptographic key management
- PostgreSQL: Relational storage with table partitioning and AES-256 encryption at rest
- AWS S3 / WORM Storage: Long-term compliant data retention (≥ 10 years)

## Rationale
[This architecture uses domain-driven component decomposition to isolate external third-party latency and maintain strict 99.99% system availability. It integrates robust cryptographic ledger auditing and WORM storage to satisfy strict HIPAA, GDPR, and 10-year financial data retention constraints.]