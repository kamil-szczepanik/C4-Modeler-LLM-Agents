## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations for a mid-size payment processor in AWS (eu-west-1). Its core purpose is to score 3,000 TPS under 50 ms P99 latency, manage fraud analyst reviews, and ensure PCI-DSS Level 1 compliance with 7-year tamper-evident auditability.]

## Key Elements
* **End Customer:** Cardholder initiating transactions
* **Payment Gateway:** External client submitting payment authorizations via HTTPS
* **API Gateway & AWS WAF:** Ingress management enforcing TLS 1.3, rate-limiting, and velocity-based risk throttling
* **Scoring Engine:** Stateless microservice container running on AWS ECS/Fargate for real-time fraud evaluation
* **Case Management UI:** Internal web application for fraud analysts using OIDC/OAuth2 and hardware-backed MFA
* **Audit & Storage Layer:** Amazon S3 with Object Lock (Compliance Mode) and KMS-envelope encryption for 7-year retention

## Relationships
* **Payment Gateway to API Gateway:** Submits authorization requests via HTTPS (TLS 1.3)
* **API Gateway to Scoring Engine:** Forwards payload for real-time evaluation via mTLS
* **Scoring Engine to Audit & Storage Layer:** Writes tamper-evident decisions, model versions, and inputs via AWS SDK
* **Fraud Analyst to Case Management UI:** Reviews suspicious payments via HTTPS without accessing raw PAN data

## Technology Stack
* **AWS ECS/Fargate:** Container orchestration for stateless scoring microservices, avoiding serverless cold starts to maintain <50ms P99 latency
* **Amazon S3 with Object Lock:** Provides tamper-evident, cost-optimized 7-year audit log retention using compliance mode and lifecycle tiering
* **AWS API Gateway & AWS WAF:** Handles fail-open circuit breakers, rate-limiting, and velocity-based throttling during outages
* **AWS Certificate Manager (ACM) Private CA:** Secures internal microservice communication using mutual TLS (mTLS)

## Rationale
[This architecture meets strict performance and compliance demands using fully managed AWS services to fit the €25,000/month budget and operational limits of a 3-person engineering team. It enforces PCI-DSS boundaries, secure tokenization, and fail-open resilience while preserving tamper-evident 7-year auditability.]