## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud within a sub-50ms latency window while providing case management for analysts. It operates within AWS (`eu-west-1`) to meet PCI-DSS Level 1 compliance and a 7-year tamper-evident audit requirement on a fixed budget.

## Key Elements
* **Payment Gateway / Acquiring System**: External actor submitting authorization requests.
* **Fraud Analyst & Risk Operations Manager**: Internal users reviewing cases and updating rules.
* **Real-Time Payment Fraud Screening System**: Core software system hosted on AWS.
* **AWS API Gateway / Envoy Proxy**: Edge layer handling mTLS termination and traffic routing.
* **AWS Fargate**: Containerized microservices executing fraud scoring and business logic.
* **AWS Cognito**: Managed Identity Provider handling OIDC/OAuth2 authentication and RBAC.
* **AWS S3 Object Lock**: Immutable storage backend configured in Compliance Mode for audit logging.
* **AWS KMS**: Cryptographic service managing envelope encryption and hardware-isolated keys.

## Relationships
* **Payment Gateway** to **AWS API Gateway**: Submits payment authorization requests via **gRPC over mTLS**.
* **Fraud Analysts** to **AWS Cognito / Web Frontend**: Authenticates via **OIDC/OAuth2 over HTTPS/REST**.
* **Core Fargate Services** to **AWS S3 Object Lock**: Archives scoring inputs and decisions via **AWS SDK (HTTPS)**.
* **External Fraud Intelligence Feeds** to **Core System**: Ingests risk data via **HTTPS/REST webhooks**.

## Technology Stack
* **AWS Fargate & API Gateway**: Chosen for serverless container orchestration to meet the 3,000 TPS at <50ms P99 SLA without managing Kubernetes.
* **gRPC over mTLS**: Selected for low-overhead, high-throughput service communication and PCI-DSS transport security.
* **AWS Cognito**: Offloads identity management to reduce operational toil for a 3-engineer team.
* **AWS S3 Object Lock (Compliance Mode)**: Implemented to mathematically guarantee 7-year immutability for regulatory auditability.
* **AWS KMS / CloudHSM**: Provides hardware-accelerated encryption and tokenization to minimize PCI-DSS scope.

## Rationale
This architecture leverages managed AWS services to remain strictly within the €25k monthly budget and operational capacity of a 3-engineer team while satisfying strict PCI-DSS Level 1 security and 7-year auditability mandates. Edge offloading and serverless compute guarantee sub-50ms latency at high throughput without requiring self-managed infrastructure.