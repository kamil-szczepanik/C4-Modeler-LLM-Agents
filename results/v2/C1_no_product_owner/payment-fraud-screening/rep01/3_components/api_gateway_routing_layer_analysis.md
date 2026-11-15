## Overview
This system screens real-time payment authorizations for fraud to protect a mid-size payment processor. It evaluates requests for approval, decline, or manual review while providing case management for analysts.

## Key Elements
- Payment Gateway / Acquirer
- Card Networks & Tokenization Vault
- API Gateway & Routing Layer (AWS ALB + AWS WAF, Go Routing & Tokenization Proxy)
- Real-Time Scoring Service (Go container on Amazon ECS on EC2)
- Case Management Backend (Java Spring Boot container on Amazon ECS on Fargate)
- Data & Audit Stores (Amazon DynamoDB with AWS KMS, DynamoDB Streams, Amazon RDS PostgreSQL)
- Messaging & Eventing (Amazon SQS, SNS, Amazon EventBridge)

## Relationships
- Payment Gateway / Acquirer -> API Gateway & Routing Layer: Ingests authorization requests over HTTPS with mTLS and JWT [mTLS / HTTPS]
- API Gateway & Routing Layer -> Card Networks & Tokenization Vault: Resolves PAN to token [mTLS / HTTPS]
- API Gateway & Routing Layer -> Real-Time Scoring Service: Forwards scrubbed payloads for low-latency evaluation [gRPC over HTTP/2]
- Real-Time Scoring Service -> Data & Audit Stores: Persists audit logs and retrieves models [TLS / TCP]

## Technology Stack
- AWS ALB & AWS WAF: Edge termination and WAF filtering to meet P99 latency targets within budget.
- Go: Used for the Routing & Tokenization Proxy and Real-Time Scoring Service for minimal resource footprint and high performance.
- Java Spring Boot: Used for Case Management Backend.
- Amazon DynamoDB & RDS PostgreSQL: Persistent storage with AWS KMS encryption for tamper-evident audit trails.
- AWS Secrets Manager: Secure credential injection with automatic rotation.

## Rationale
The architecture uses AWS managed services and Go-based microservices to comfortably achieve the sub-50ms P99 latency requirement while strictly adhering to PCI-DSS Level 1 compliance. This lean design operates efficiently within the 25,000 EUR monthly budget and supports management by a three-engineer team.