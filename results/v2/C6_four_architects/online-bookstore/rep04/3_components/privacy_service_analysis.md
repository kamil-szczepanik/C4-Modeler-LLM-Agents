## Overview
[The Online Bookstore system is an Amazon-style e-commerce platform designed to support physical and electronic book sales, recommendations, and reviews. Its core purpose is to provide a compliant, high-performance retail experience with global multi-currency support.]

## Key Elements
* Consent Controller & Middleware Component (Node.js/TypeScript)
* DSAR Orchestrator Component (Node.js/TypeScript)
* Data Redaction Component (Node.js/TypeScript)
* Compliance Reporting Component (Node.js/TypeScript)
* Amazon API Gateway
* Amazon ECS Fargate
* Amazon DynamoDB
* Amazon Aurora PostgreSQL
* Amazon S3
* Amazon SQS & SNS

## Relationships
* API Gateway -> Consent Controller: Routes incoming privacy requests [gRPC / HTTP/2]
* Consent Controller -> Amazon DynamoDB: Persists and queries user consent preferences [AWS SDK / HTTPS]
* DSAR Orchestrator -> Amazon SQS / SNS: Coordinates async data export and erasure workflows [AWS SDK / HTTPS]
* DSAR Orchestrator -> Amazon S3: Stores user data export packages [AWS SDK / HTTPS]
* Data Redaction Component -> Amazon Aurora PostgreSQL: Purges and anonymizes PII [pg / TLS]
* Compliance Reporting Component -> Amazon S3: Archives tamper-proof audit trails [AWS SDK / HTTPS]

## Technology Stack
* Node.js (TypeScript): Standardized runtime for all Privacy Service components to eliminate polyglot overhead and ensure lightweight execution
* Amazon ECS Fargate: Container orchestration platform for scalable, serverless microservice deployment
* Amazon DynamoDB: Low-latency NoSQL data store for user consent tokens and preferences
* Amazon Aurora PostgreSQL: Relational database for transactional records and structured audit histories
* Amazon S3: Secure object storage for data export packages and long-term regulatory audit logs
* Amazon SQS / SNS: Event-driven messaging backbone for asynchronous workflow decoupling

## Rationale
[This architecture fits the requirements by standardizing on a single, efficient Node.js runtime inside Amazon ECS Fargate, eliminating polyglot container bloat. It leverages AWS managed data stores and event-driven messaging to achieve strict GDPR/CCPA compliance, low latency, and high availability.]