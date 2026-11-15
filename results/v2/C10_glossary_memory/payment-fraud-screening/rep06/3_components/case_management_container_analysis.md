## Overview
The Case Management Container supports fraud analyst reviews, administrative workflows, and risk monitoring for card-not-present payment authorizations. It securely handles suspicious payment cases while strictly enforcing PCI-DSS Level 1 compliance and UI data masking.

## Key Elements
- Fraud Analyst (Person)
- Risk Manager (Person)
- Case UI Component (React / TypeScript SPA via AWS S3/CloudFront)
- Case API Component (Node.js / Express on AWS ECS Fargate)
- Case Ingestion Worker Component (Node.js / TypeScript on AWS ECS Fargate)
- Case Database Component (AWS Aurora Serverless v2 PostgreSQL)
- AWS SQS (Managed Message Queue)

## Relationships
- Fraud Analyst -> Case UI Component (HTTPS Web UI)
- Risk Manager -> Case UI Component (HTTPS Web UI)
- Fraud Analyst -> Case API Component (HTTPS / REST over TLS 1.3)
- Risk Manager -> Case API Component (HTTPS / REST over TLS 1.3)
- Case API Component -> Case Database Component (PostgreSQL Wire Protocol over TLS 1.3)
- Scoring Engine Container -> Case Ingestion Worker Component (AWS SQS over TLS 1.3 with AWS KMS)
- Case Ingestion Worker Component -> Case Database Component (PostgreSQL Wire Protocol over TLS 1.3)

## Technology Stack
- Node.js / TypeScript: Powers lightweight backend services and ingestion workers on AWS ECS Fargate.
- React / TypeScript: Delivers responsive single-page application dashboards served via AWS S3 and CloudFront.
- AWS Aurora Serverless v2 PostgreSQL: Provides cost-effective, auto-scaling relational storage for case reviews and audit logs.
- AWS SQS: Enables decoupled, asynchronous ingestion of suspicious transactions with Dead-Letter Queue support.
- AWS KMS: Secures data encryption at rest across storage and queuing layers.

## Rationale
This architecture fits the requirements by maintaining strict PCI-DSS Level 1 compliance through data masking and tokenized references without handling raw PANs. Additionally, managed serverless components keep operations maintainable for a three-engineer team within the €25,000 monthly budget.