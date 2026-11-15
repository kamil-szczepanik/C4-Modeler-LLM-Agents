## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present transactions for a mid-size payment processor and provides a case management interface for fraud analysts.]

## Key Elements
* Fraud Analyst & Risk Manager (Persona)
* Compliance Auditor (Persona)
* Frontend SPA (React, AWS S3 / CloudFront)
* Case Management API (Node.js/Express, AWS ECS Fargate)
* Reporting Service (Node.js, AWS ECS Fargate)
* Amazon DynamoDB (On-Demand)
* Amazon Athena & Amazon S3 Object Lock

## Relationships
* Frontend SPA -> Case Management API & Reporting Service: User interactions and data queries [REST/HTTPS]
* Case Management API -> Amazon DynamoDB: Persists active case state [AWS SDK / HTTPS]
* Case Management API -> Amazon SQS / Kinesis: Dispatches audit events for archival [JSON / HTTPS]
* Reporting Service -> Amazon Athena: Aggregates false-positive metrics and analyst SLAs [AWS SDK / HTTPS]

## Technology Stack
* Node.js / Express: Lightweight runtime for APIs, matching team skill set
* React: Modern UI framework served via S3 and CloudFront for minimal infrastructure overhead
* Amazon DynamoDB (On-Demand): Serverless NoSQL storage eliminating database maintenance for a 3-engineer team
* Amazon Athena & S3 Object Lock: Provides scalable query capabilities and tamper-evident 7-year audit logs for PCI-DSS compliance
* AWS ECS Fargate: Container orchestration managed without server infrastructure overhead

## Rationale
[This architecture leverages serverless and managed AWS services (DynamoDB, Fargate, S3) to strictly operate within a 25,000 EUR monthly budget and a 3-engineer team constraint while meeting PCI-DSS Level 1 and 7-year auditability mandates.]