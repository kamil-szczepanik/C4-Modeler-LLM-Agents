## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations to prevent fraud and provides a review interface for suspicious transactions. It ensures sub-50ms latency, strict PCI-DSS compliance, and 7-year auditability on AWS within a fixed budget.

## Key Elements
- Fraud Analysts: Primary users reviewing suspicious transactions.
- Fraud Analyst UI: React SPA hosted via Amazon S3 and Amazon CloudFront.
- API Gateway & Ingress: Java / Spring Cloud Gateway managing incoming traffic.
- Real-Time Scoring Engine: Java / Spring Boot + ONNX service scoring transactions.
- Case Management Backend: Node.js / TypeScript service managing analyst workflows.
- Model & Rule Management Service: Python / FastAPI service for zero-downtime updates.
- Audit Worker & Supporting Datastores: Node.js/Python workers, Amazon Kinesis, Amazon Aurora PostgreSQL, and Amazon ElastiCache (Redis).

## Relationships
- Fraud Analysts -> Fraud Analyst UI: Accesses case management workflows and web UI [HTTPS]
- Fraud Analyst UI -> Case Management Backend: Fetches cases and submits review decisions [HTTPS / JSON REST]
- Fraud Analyst UI -> Model & Rule Management Service: Sends rule update payloads [HTTPS / JSON REST]
- Fraud Analyst UI -> API Gateway & Ingress: Transmits secured requests and audit telemetry [HTTPS / JSON REST]

## Technology Stack
- Frontend: React SPA, Zustand, Tailwind CSS, TanStack Table, Axios (hosted on Amazon S3 / CloudFront) for a lightweight, serverless UI.
- Backend Services: Java / Spring Boot, Node.js / TypeScript, and Python / FastAPI to balance high performance and rapid development.
- Data & Streaming: Amazon Aurora PostgreSQL, Amazon ElastiCache (Redis), and Amazon Kinesis Data Streams for reliable persistence, caching, and event streaming.
- Cloud Platform: AWS (eu-west-1 region) to leverage managed services within the fixed budget.

## Rationale
This serverless and managed container architecture minimizes operational overhead for a three-engineer team while easily meeting peak performance and strict PCI-DSS Level 1 security requirements. AWS managed services ensure high availability and robust audit trails within the 25,000 EUR monthly budget.