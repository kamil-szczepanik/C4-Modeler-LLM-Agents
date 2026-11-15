## Overview
[Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud, providing case management for suspicious payments while ensuring PCI-DSS Level 1 compliance.]

## Key Elements
* AWS Application Load Balancer (ALB) with AWS WAF and AWS Shield
* Listener & TLS Terminator Component
* Path-Based Routing Router Component
* Authentication/Authorization Filter Component
* Rate Limiting & Throttling Filter Component
* Telemetry & Tracing Injector Component
* Edge Request Sanitization Component
* Scoring Engine (AWS ECS Fargate, Rust)
* Case Management App (AWS ECS Fargate, Node.js/Python, React SPA)
* Model & Rule Management Service (AWS ECS Fargate)
* Amazon Aurora PostgreSQL
* Identity Provider (IdP)

## Relationships
* Payment Gateway -> API Gateway / ALB: Sends payment authorizations [Synchronous REST/gRPC, mTLS, TLS 1.3]
* API Gateway / ALB -> Scoring Engine: Forwards payment authorizations [Synchronous gRPC, mTLS]
* API Gateway / ALB -> Case Management App: Routes review cases [Synchronous HTTP/1.1]
* API Gateway / ALB -> Model & Rule Management Service: Forwards rule updates [Synchronous REST, mTLS]
* API Gateway / ALB -> Amazon CloudWatch / Prometheus: Streams access logs and metrics [Asynchronous HTTPS/gRPC]

## Technology Stack
* AWS Application Load Balancer: Provides low-latency, cost-effective edge routing within budget constraints
* AWS WAF & AWS Shield: Enforces edge request sanitization, DDoS protection, and schema validation
* AWS ECS Fargate: Runs containerized microservices without server management overhead
* Rust: Powers the Scoring Engine for high throughput and sub-50ms P99 latency
* Amazon Aurora PostgreSQL: Stores tamper-evident transaction logs and audit data

## Rationale
[This architecture leverages AWS managed services and ECS Fargate to meet the strict €25,000 monthly budget while maintaining sub-50ms P99 latency at 3,000 TPS. Edge security components and mTLS enforcement satisfy PCI-DSS Level 1 compliance and 7-year tamper-evident auditability requirements.]