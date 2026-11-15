## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations at 3,000 TPS to protect merchant revenue while supporting case reviews and compliance, ensuring sub-50ms P99 latency. It is operated by a 3-engineer team within a €25,000 monthly AWS budget while maintaining PCI-DSS Level 1 compliance.

## Key Elements
- Payment Gateway / Core Processing System [externalSystem, context]
- External Cardholder Data Environment (CDE) / Tokenization Vault [externalSystem, context]
- AWS S3 Object Lock [externalSystem, context]
- Dynamic Rule & Model Registry [externalSystem, context]
- Fraud Analyst, Risk Manager, Compliance & Audit Officer [person, context]
- Scoring Engine Container [container, Rust/Tokio, AWS ECS Fargate]
- Case Management Container [container, Node.js/TypeScript, AWS ECS Fargate]
- Fallback Scoring Container [container, Python/FastAPI, AWS ECS Fargate]
- Audit Reporting Container [container, Node.js/TypeScript, AWS ECS Fargate]

## Relationships
- Payment Gateway / Core Processing System -> Scoring Engine Container (gRPC/REST over TLS 1.3 with mTLS and OAuth2/JWT)
- Scoring Engine Container -> External Cardholder Data Environment (CDE) / Tokenization Vault (Secure APIs)
- Scoring Engine Container -> Dynamic Rule & Model Registry (AWS KMS and ECDSA P-256)
- Scoring Engine Container -> AWS S3 Object Lock (AWS Firehose / S3 API)
- Scoring Engine Container -> Fallback Scoring Container (Internal HTTP/JSON via AWS Service Discovery)
- Fraud Analyst / Risk Manager -> Case Management Container (HTTPS Web UI)
- Compliance & Audit Officer -> Audit Reporting Container (HTTPS Web UI)
- Audit Reporting Container -> AWS S3 Object Lock (AWS SDK / S3 API)

## Technology Stack
- AWS ECS Fargate: Chosen for container compute to ensure predictable sub-50ms P99 latency and secure mTLS termination without Lambda cold-start overhead.
- Rust / Tokio: Chosen for the Scoring Engine to handle high-throughput (3,000 TPS) memory-efficient real-time processing.
- Node.js / TypeScript: Chosen for Case Management and Audit Reporting containers to accelerate UI-driven feature delivery.
- Python / FastAPI: Chosen for the Fallback Scoring Container for rapid execution of simplified heuristic rules during primary outages.
- AWS S3 Object Lock: Chosen for WORM-compliant storage guaranteeing 7-year tamper-evident auditability.

## Rationale
The containerized architecture separates the ultra-low-latency Rust scoring core from administrative workflows, satisfying strict performance and security isolation boundaries. Leveraging managed AWS services on ECS Fargate maintains high availability and PCI-DSS compliance within the 3-engineer operational capacity and fixed budget constraints.