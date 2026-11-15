## Overview
[Real-Time Payment Fraud Screening Platform] provides card-not-present fraud scoring and analyst case management for a mid-size payment processor. It screens payment authorizations in real-time while maintaining strict compliance, auditability, and cost constraints.

## Key Elements
* Fraud Analyst & Risk Manager (Users)
* Payment Gateway / Acquirer, Corporate Identity Provider (IdP), Card Tokenization Provider, Notification Gateway (External Systems)
* API Gateway (AWS API Gateway - HTTP APIs)
* Scoring Engine Container (Go, ONNX runtime, Amazon ECS on AWS Fargate)
* Case Management Container (Next.js / Node.js, Amazon ECS on AWS Fargate)
* Amazon RDS PostgreSQL (Database)
* Amazon S3 WORM Bucket & Model Bucket (Amazon S3 with WORM Object Lock & Versioning)
* Amazon SQS / EventBridge (Messaging/Events)
* Amazon Athena & S3 Data Lake (Analytics)

## Relationships
* API Gateway -> Scoring Engine Container [HTTPS/REST]
* API Gateway -> Case Management Container [HTTPS/REST]
* Scoring Engine Container -> Amazon RDS PostgreSQL [TCP/PostgreSQL protocol]
* Scoring Engine Container -> Amazon S3 WORM Bucket & Model Bucket [HTTPS (TLS 1.3), AWS IAM SigV4, VPC Gateway Endpoints]
* Case Management Container -> Amazon RDS PostgreSQL [TCP/PostgreSQL protocol]
* Amazon Athena & S3 Data Lake -> Amazon S3 WORM Bucket & Model Bucket [SQL queries, HTTPS]

## Technology Stack
* AWS (eu-west-1): Target cloud provider ensuring managed scalability and low latency.
* Go & ONNX Runtime: Powers the Scoring Engine for high performance and sub-50ms P99 latency.
* Next.js / Node.js: Powers the Case Management interface for analysts.
* Amazon RDS PostgreSQL: Relational storage for application data and case workflows.
* Amazon S3 (WORM Object Lock & Versioning): Secure, immutable storage meeting the 7-year audit requirement.
* Terraform: Infrastructure-as-Code for automated, drift-free deployments managed by a 3-person team.

## Rationale
[The microservices and serverless-leaning AWS architecture delivers sub-50ms P99 latency at 3,000 requests per second while strictly adhering to the €25,000 monthly budget. Immutable S3 storage and strict IAM boundaries ensure PCI-DSS Level 1 compliance and 7-year tamper-evident auditability.]