## Overview
Real-Time Payment Fraud Screening is a scalable, low-latency financial service that screens card-not-present payment authorizations and provides case management tools for fraud analysts. It ensures PCI-DSS compliance, strict auditability, and sub-50 ms decision latencies within a fixed 25,000 EUR monthly AWS budget.

## Key Elements
- **Fraud Analyst & Risk Officer / Fraud Operations Manager**: Human users managing cases and rules.
- **Web Application (React SPA, AWS S3, CloudFront)**: Frontend container comprising Case Triage Dashboard, Rule Authoring Studio, and Audit & Compliance Viewer.
- **Case Management Backend (Node.js / Spring Boot)**: Backend container processing case workflows and rule publishing.
- **API Gateway (Envoy)**: Entry point handling routing, security enforcement, and token management.
- **Real-Time Scoring Engine (Go, ONNX Runtime, AWS ECS Fargate)**: High-performance container scoring transaction payloads.
- **Storage Tier**: AWS Aurora PostgreSQL and Amazon ElastiCache (Redis) for state and caching.
- **Audit Log Worker (Go) & Amazon SQS**: Asynchronous components ensuring tamper-evident logging.

## Relationships
- **Fraud Analyst / Risk Officer -> Web Application**: Interacts via browser [HTTPS].
- **Web Application -> API Gateway (Envoy)**: Sends API requests via [REST/GraphQL over HTTPS].
- **API Gateway -> Case Management Backend & Real-Time Scoring Engine**: Routes internal traffic via [gRPC/REST over TLS].
- **Scoring Engine -> Amazon Aurora PostgreSQL / Redis**: Reads scoring models and writes audit logs via [TCP/TLS].

## Technology Stack
- **React & Tailwind CSS**: Chosen for rapid UI development and low overhead for a 3-engineer team.
- **AWS S3 & CloudFront**: Cost-effective static hosting with global edge distribution for the SPA.
- **Go & ONNX Runtime**: High-throughput, low-latency processing meeting the P99 < 50 ms constraint.
- **Node.js / Spring Boot**: Robust backend frameworks for case and rule management logic.
- **AWS Aurora PostgreSQL & ElastiCache Redis**: Managed data tiers ensuring reliability, speed, and compliance.

## Rationale
The architecture combines serverless frontend distribution with containerized microservices on AWS ECS Fargate to balance high throughput with minimal operational overhead. This design strictly meets PCI-DSS Level 1 and auditability requirements while operating comfortably within the 25,000 EUR monthly budget for a 3-engineer team.