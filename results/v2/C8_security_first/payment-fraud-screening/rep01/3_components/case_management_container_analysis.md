## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations in the cloud before approval and provides case management tools for fraud analysts. It operates on AWS within a strict compliance, budget, and team size framework.

## Key Elements
* Fraud Analysts & Risk Managers
* AWS API Gateway (HTTP APIs)
* Scoring Engine Container (Go, ONNX runtime, Amazon ECS on Amazon Fargate)
* Case Management Frontend (Static SPA on Amazon S3 and Amazon CloudFront)
* Case Management Backend (Node.js API on Amazon ECS on Amazon Fargate)
* Amazon RDS PostgreSQL
* Amazon S3 WORM Bucket & Model Bucket
* Amazon SQS / Amazon EventBridge
* External Systems: Payment Gateway / Acquirer, Corporate Identity Provider (IdP), Card Tokenization Provider, Notification Gateway

## Relationships
* Payment Gateway / Acquirer -> AWS API Gateway: Submits authorization requests [HTTPS]
* AWS API Gateway -> Scoring Engine Container: Routes scoring requests [HTTP/JSON]
* AWS API Gateway -> Case Management Backend: Routes analyst requests [HTTPS]
* Case Management Frontend (S3/CloudFront) -> Case Management Backend: Invokes REST API [HTTPS]
* Case Management Backend -> Amazon RDS PostgreSQL: Reads and writes case data, prioritizations, and audits [TLS]
* Case Management Backend -> Amazon S3 WORM Bucket: Streams tamper-evident audit logs [AWS SDK / HTTPS]
* Case Management Backend -> Amazon SQS / Amazon EventBridge: Publishes asynchronous events [AWS SDK]
* Case Management Backend -> Notification Gateway: Dispatches operational alerts [HTTPS]

## Technology Stack
* AWS Cloud (eu-west-1 region): Selected to meet regional compliance and infrastructure requirements.
* Amazon ECS on AWS Fargate: Runs containerized services without managing underlying servers, fitting the 3-engineer constraint.
* Node.js & Next.js (Static SPA): Powers the analyst UI decoupled from the backend for optimized cost and performance.
* Go & ONNX Runtime: Powers the high-performance scoring engine to achieve sub-50ms P99 latency.
* Amazon RDS PostgreSQL: Stores relational case data and transactional records securely.
* Amazon S3 WORM Bucket (Object Lock): Ensures tamper-evident, 7-year auditability for regulatory compliance.

## Rationale
This architecture balances stringent PCI-DSS Level 1 security and 7-year auditability with high-performance real-time scoring. Decoupling the static SPA frontend from the lean Fargate backend optimizes operational efficiency for a three-engineer team within the 25,000 EUR monthly budget.