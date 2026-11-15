## Overview
The Real-Time Payment Fraud Screening System screens card-not-present payment authorizations at 3,000 TPS to protect merchant revenue while supporting case reviews and compliance, ensuring sub-50ms P99 latency. It provides a dedicated audit reporting architecture that securely indexes and queries 7-year WORM-compliant transaction logs for compliance officers and risk managers.

## Key Elements
* Compliance & Audit Officer [person]
* Risk Manager [person]
* Audit Reporting Container [container] (Node.js / TypeScript, AWS ECS Fargate)
* Audit UI Component [component] (Express.js / React SSR)
* Query & Aggregation Component [component] (TypeScript)
* S3 Access Component [component] (AWS SDK for JavaScript)
* Regulatory Exception Component [component] (TypeScript)
* AWS S3 Object Lock [externalSystem]

## Relationships
* Compliance & Audit Officer -> Audit UI Component: Interacts for secure dashboards and export packages [HTTPS]
* Risk Manager -> Audit UI Component: Monitors portfolio risk metrics and aggregated reports [HTTPS]
* Compliance & Audit Officer -> Regulatory Exception Component: Attaches compliance sign-offs and overrides [HTTPS]
* Query & Aggregation Component -> AWS S3 Object Lock: Queries historical decisions and Parquet-compacted data via Athena [AWS SDK / Athena / S3 API]
* Regulatory Exception Component -> AWS S3 Object Lock: Writes immutable exception sidecar objects [AWS SDK / S3 API]
* S3 Access Component -> AWS S3 Object Lock: Retrieves WORM-compliant logs securely [AWS SDK / S3 API]

## Technology Stack
* Node.js / TypeScript: Powers the Audit Reporting Container runtime for rapid UI and API development
* AWS ECS Fargate: Runs serverless containers within a strict €25,000 monthly infrastructure budget
* AWS S3 Object Lock & Glacier: Provides tamper-evident WORM storage for 7-year auditability with automated lifecycle transitions
* AWS Athena & Apache Parquet: Enables cost-effective, high-performance querying over partitioned historical audit data
* AWS KMS: Secures encryption-at-rest (`SSE-KMS`) for sensitive audit data, queries, and sidecar metadata

## Rationale
This architecture uses serverless AWS services and columnar storage (Parquet/Athena) to meet strict 7-year auditability and PCI-DSS compliance requirements while staying within budget. Component decomposition and role-based access control isolate sensitive compliance sign-offs and ensure secure, low-latency reporting for auditors.