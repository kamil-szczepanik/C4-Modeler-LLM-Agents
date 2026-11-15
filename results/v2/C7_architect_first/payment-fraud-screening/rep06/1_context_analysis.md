## Overview
[The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations for fraud at scale and supports case management for analysts. It operates within strict PCI-DSS Level 1 compliance constraints and a fixed AWS infrastructure budget.]

## Key Elements
* Payment Gateway / Acquirer Systems (External Software System)
* Real-Time Payment Fraud Screening System (Target Software System)
* Fraud Analysts (Person)
* Data Scientists / Risk Managers (Person)
* Card Networks / Tokenization Providers (External Software System)
* Regulatory / Compliance Auditors (Person/System)
* AWS ECS on Fargate, AWS Global Accelerator, AWS Secrets Manager, and S3 Object Lock (Containers / Infrastructure)

## Relationships
* Payment Gateway -> Fraud Screening System: Submits payment authorizations via HTTPS / REST (<50ms SLA)
* Fraud Analysts -> Fraud Screening System: Reviews suspicious cases via HTTPS with OIDC/OAuth2 and MFA
* Data Scientists / Risk Managers -> Fraud Screening System: Updates scoring models and rules via HTTPS with IAM authentication
* Fraud Screening System -> Card Networks / Tokenization Providers: Resolves tokens via HTTPS / REST with mTLS

## Technology Stack
* AWS ECS on Fargate: Runs containerized microservices within a single region (`eu-west-1`) to fit the €25,000 monthly budget
* AWS Global Accelerator: Ensures predictable, low-latency routing for high-throughput traffic
* S3 Object Lock (Compliance Mode): Enforces tamper-evident, 7-year retention for audit logs and decision inputs
* AWS Secrets Manager: Manages database credentials, JWT signing keys, and model encryption keys with automatic rotation
* ArgoCD: Enforces GitOps and automated canary deployments for zero-downtime model updates

## Rationale
[This architecture uses a single-region AWS Fargate deployment with managed services to meet strict performance and PCI-DSS requirements without exceeding the 25,000 EUR monthly budget. It balances sub-50ms latency SLAs and immutable 7-year auditability with the operational capacity of a three-engineer team.]