## Overview
This system screens real-time card-not-present payment authorizations for fraud and provides case management tools for fraud analysts. It ensures sub-50ms decision latency while maintaining strict PCI-DSS Level 1 compliance and 7-year auditability.

## Key Elements
- Real-Time Payment Fraud Screening System
- Fraud Analyst
- Risk & Compliance Officer
- Merchant / Payment Gateway
- Payment Processing Core / Acquirer
- Identity Provider (IdP)
- AWS Audit & Compliance Store
- Notification / Alerting Service
- AWS CloudWatch / Observability Platform
- CI/CD & Model Registry Pipeline
- Decision API Container (Go, AWS Fargate)
- Scoring Engine Container (Python, FastAPI, AWS Fargate)
- Case Management Portal Container (AWS Fargate)
- Amazon Aurora PostgreSQL (Amazon Aurora PostgreSQL)

## Relationships
- Merchant / Payment Gateway -> Real-Time Payment Fraud Screening System (gRPC / HTTPS)
- Fraud Analyst -> Real-Time Payment Fraud Screening System (HTTPS (TLS 1.3))
- Real-Time Payment Fraud Screening System -> AWS Audit & Compliance Store (HTTPS / S3 API)
- Real-Time Payment Fraud Screening System -> Notification / Alerting Service (API)
- Payment Processing Core / Acquirer -> Real-Time Payment Fraud Screening System (mTLS)
- Merchant / Payment Gateway -> Decision API Container (gRPC / HTTPS)
- Decision API Container -> Scoring Engine Container (Internal VPC gRPC / mTLS)
- Fraud Analyst -> Case Management Portal Container (HTTPS (TLS 1.3))
- Case Management Portal Container -> Identity Provider (IdP) (OIDC / OAuth2)
- Scoring Engine Container -> AWS Audit & Compliance Store (HTTPS / S3 API)

## Technology Stack
- Go: Chosen for the Decision API Container to ensure high-performance and low-latency authorization checks.
- Python & FastAPI: Powers the Scoring Engine Container for rapid ML model inference.
- AWS Fargate: Runs all containers serverlessly to stay within the 25,000 EUR monthly budget and minimize operational overhead for a 3-engineer team.
- Amazon Aurora PostgreSQL: Stores transactional case data, utilizing read replicas and RDS Proxy to maintain the P99 <50ms latency SLA.
- pgAudit: Native PostgreSQL extension utilized for mandatory compliance logging.

## Rationale
The serverless Fargate and managed Aurora PostgreSQL architecture minimizes operational overhead for a three-engineer team while strictly enforcing PCI-DSS Level 1 security. Microsecond-optimized Go and Python runtimes combined with RDS Proxy guarantee sub-50ms decision latency at 3,000 TPS within a 25,000 EUR monthly budget.