## Overview
The system is a Real-Time Payment Fraud Screening platform that screens card-not-present payment authorizations and manages suspicious payment reviews. It provides sub-50ms latency, PCI-DSS compliance, and 7-year tamper-evident auditability.

## Key Elements
- AWS Application Load Balancer (ALB)
- Listener Component (AWS ALB Listener)
- Routing Rules Engine
- Health Check & Circuit Breaker Component
- WAF & Security Filter Component (AWS WAF)
- Access Logging & Telemetry Component
- Target Group Manager
- Scoring Engine Container (Go, ONNX Runtime, AWS ECS Fargate)
- Case Management Backend Container (Node.js, TypeScript, AWS ECS Fargate)
- Tokenization Proxy Container (AWS Nitro Enclaves)
- Amazon DynamoDB
- Amazon S3 Object Lock

## Relationships
- Payment Gateway / Core Ledger -> Listener Component: Routes external authorization traffic [HTTPS/gRPC]
- Fraud Analysts -> Listener Component: Interacts with Case Management Backend [HTTPS]
- Listener Component -> WAF & Security Filter Component: Inspects headers and payloads [In-Memory]
- Listener Component -> Routing Rules Engine: Internal handoff [In-Memory]
- Routing Rules Engine -> Case Management Backend Container: Routes analyst traffic [HTTPS]
- Routing Rules Engine -> Scoring Engine Container: Forwards authorization traffic [gRPC over HTTP/2]
- Routing Rules Engine -> Tokenization Proxy Container: Forwards raw card payloads [gRPC over HTTP/2]
- Routing Rules Engine -> Access Logging & Telemetry Component: Emits metadata asynchronously [In-Memory/Queue]
- Routing Rules Engine -> Target Group Manager: Resolves backend ECS tasks [In-Memory]
- Target Group Manager -> Scoring Engine Container: Manages connection pools [gRPC over HTTP/2]
- Health Check & Circuit Breaker Component -> Scoring Engine Container: Performs active health probes [HTTP GET]
- Access Logging & Telemetry Component -> Amazon S3 Object Lock: Stores audit logs [HTTPS]

## Technology Stack
- AWS Application Load Balancer: Edge routing, TLS termination, and traffic splitting within infrastructure budget.
- AWS WAF: Managed security filtering for OWASP Top 10 protection to minimize operational toil for a 3-engineer team.
- gRPC over HTTP/2: Internal protocol for low-latency communication satisfying the P99 < 50ms requirement (R-04).
- Amazon S3 Object Lock: Tamper-evident immutable storage meeting the 7-year auditability constraint (R-06).
- AWS Nitro Enclaves: Isolated compute environment ensuring tokenized card data security for PCI-DSS Level 1 compliance.

## Rationale
This architecture uses managed AWS cloud services to maintain a fixed infrastructure budget of 25,000 EUR per month and support a three-engineer operational model. Asynchronous logging and gRPC protocols ensure strict sub-50ms latency (R-04) while meeting PCI-DSS Level 1 and 7-year auditability requirements.