## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations to detect fraud and routes suspicious transactions for analyst review. It ensures high performance, PCI-DSS compliance, and 7-year auditability within fixed resource constraints.

## Key Elements
- **Payment Analysts & Compliance Auditors:** End users reviewing cases and compliance data.
- **Payment Gateway / Acquirer:** External system initiating transactions.
- **API Gateway / Ingestion Service:** Go-based container handling initial requests.
- **Fraud Scoring Engine:** Rust-based container providing low-latency fraud decisions.
- **Case Management Backend:** Node.js/Java container managing analyst workflows.
- **Fraud Analyst UI:** React application hosted on AWS S3 and CloudFront.
- **Audit & Decision Store:** PostgreSQL on AWS RDS for persistent, tamper-evident logs.
- **AWS SQS / SNS:** Serverless messaging service featuring Amazon SNS Audit Topic, Amazon SQS Case Routing Queue, and Dead-Letter Queues (DLQ).

## Relationships
- **API Gateway / Ingestion Service -> AWS SNS Audit Topic:** Publishes raw events asynchronously via AWS SDK (HTTPS/TLS 1.3).
- **AWS SNS Audit Topic -> Audit & Decision Store (PostgreSQL):** Persists immutable audit logs via AWS Lambda (HTTPS).
- **Fraud Scoring Engine -> AWS SQS Case Routing Queue:** Pushes review-required cases using AWS SDK (SQS SendMessage) with SSE-KMS.
- **AWS SQS Case Routing Queue -> Case Management Backend:** Consumes messages using AWS SDK (SQS Long Polling).

## Technology Stack
- **Go:** Used for the API Gateway / Ingestion Service to ensure high-throughput processing.
- **Rust:** Used for the Fraud Scoring Engine to guarantee sub-50ms P99 latency.
- **PostgreSQL on AWS RDS:** Stores audit logs and transactional data with encryption for 7-year compliance.
- **AWS SQS / SNS:** Serverless messaging for decoupling and asynchronous processing within the 3-engineer team capacity.
- **AWS S3 and CloudFront:** Hosts the React-based Fraud Analyst UI.

## Rationale
This AWS serverless and containerized architecture meets the strict <50ms P99 latency and PCI-DSS Level 1 compliance requirements while operating within a €25,000 monthly budget. Utilizing fully managed AWS services minimizes operational overhead, allowing a lean team of three engineers to maintain high availability and auditability.