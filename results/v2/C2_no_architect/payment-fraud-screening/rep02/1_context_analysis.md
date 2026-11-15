## Overview
The Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud at 3,000 TPS while maintaining PCI-DSS Level 1 compliance. It provides real-time scoring, audit logging, and case management for fraud analysts within a fixed budget.

## Key Elements
* Cardholder / End Customer
* Fraud Operations Analyst
* Risk Manager / Quant
* Fraud Ops Team Lead / Administrator
* API Gateway (AWS API Gateway + WAF)
* Fraud Screening Engine (AWS ECS Fargate with ONNX runtimes)
* Case Management Web UI
* Event Streaming (AWS Managed Kafka - MSK)
* Audit Storage (AWS S3 with Object Lock and KMS)

## Relationships
* Cardholder sends payment authorizations to API Gateway via HTTPS/TLS 1.3
* API Gateway routes payloads to Fraud Screening Engine over internal TLS/AWS VPC
* Fraud Screening Engine publishes decision audit logs to AWS S3 via AWS SDK
* Fraud Operations Analyst accesses Case Management UI via HTTPS with OIDC/OAuth2
* Risk Manager updates fraud models in ECS Fargate via internal API

## Technology Stack
* AWS ECS Fargate: Container orchestration to minimize operational overhead for a 3-engineer team
* AWS API Gateway & AWS WAF: Edge routing and DDoS/bot mitigation at 3,000 TPS
* ONNX Runtimes: Lightweight model execution to achieve sub-50ms P99 latency
* AWS S3 with Object Lock: Tamper-evident 7-year audit logging for regulatory compliance
* AWS KMS & Secrets Manager: Envelope encryption, tokenization, and secure credential rotation

## Rationale
The architecture combines fully managed AWS services to fit within a 25,000 EUR monthly budget and operate reliably with a 3-person team. High-throughput performance and stringent PCI-DSS Level 1 security requirements are met via lightweight container runtimes, isolated VPCs, and immutable audit logging.