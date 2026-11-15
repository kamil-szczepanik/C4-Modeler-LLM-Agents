## Overview
The system screens card-not-present payment authorizations for fraud in real-time and provides case management for fraud analysts. It operates within AWS eu-west-1, adhering strictly to PCI-DSS Level 1 compliance and a 25,000 EUR monthly budget.

## Key Elements
- Payment Gateway / Acquirer Systems (External Actor)
- Fraud Analysts (Internal User)
- Card Networks / Token Vaults (External System)
- Audit / Compliance Archive (External Storage)
- ML Model / Rule Registry (External System)
- API Gateway / Ingress Service (AWS ECS Fargate / Envoy)
- Scoring Engine (Stateless microservice in Rust/Go)
- Case Management Backend (Node.js/Python API)
- Data & Event Tiers (Amazon DynamoDB, Amazon SQS / Kinesis)

## Relationships
- Payment Gateway -> API Gateway: Sends authorization requests via gRPC over HTTP/2.
- Scoring Engine -> Card Networks / Token Vaults: Resolves tokens via secure API over mTLS.
- Scoring Engine -> Audit / Compliance Archive: Streams audit logs asynchronously via HTTPS / TLS 1.3.
- Fraud Analysts -> Case Management Backend: Accesses case management via HTTPS.
- ML Engineers -> ML Model / Rule Registry: Pushes model and rule updates via HTTPS / REST API.
- Scoring Engine -> Payment Gateway: Sends circuit breaker signals via gRPC for fail-open fallback.

## Technology Stack
- AWS (eu-west-1): Cloud provider utilizing AWS PrivateLink for perimeter security within VPC Private Subnets.
- gRPC / Protocol Buffers: High-performance binary serialization to meet the sub-50ms P99 latency requirement.
- Rust / Go: Low-level stateless execution for the Scoring Engine to handle 3,000 TPS under tight latency bounds.
- Amazon DynamoDB: Low-latency NoSQL data store for real-time state and rules.
- Amazon SQS / Kinesis: Asynchronous event streaming for tamper-evident 7-year audit logs.

## Rationale
This architecture ensures strict sub-50ms P99 decision latency and PCI-DSS Level 1 compliance using lightweight AWS managed services. It respects the 25,000 EUR monthly budget and operational limits of a three-engineer team while satisfying 7-year auditability and high availability.