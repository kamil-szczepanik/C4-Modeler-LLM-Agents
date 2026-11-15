## Overview
[The system is a real-time payment fraud screening platform that evaluates card-not-present authorizations and provides case management for analysts. Its core purpose is to prevent fraud while maintaining sub-50ms latency and strict PCI-DSS compliance.]

## Key Elements
- Payment Gateway / Acquirer
- Card Networks & Tokenization Vault
- AWS ALB / AWS WAF
- API Gateway & Ingress (Java / Spring Cloud Gateway)
- Real-Time Scoring Engine (Java / Spring Boot + ONNX)
- Case Management Backend (Node.js / TypeScript)
- Model & Rule Management Service (Python / FastAPI)
- Amazon Kinesis Data Streams
- Amazon Aurora PostgreSQL
- Amazon ElastiCache (Redis)

## Relationships
- Payment Gateway / Acquirer -> AWS ALB / AWS WAF: Sends payment authorizations [HTTPS / TLS 1.3]
- API Gateway & Ingress -> Real-Time Scoring Engine: Forwards scrubbed payloads [gRPC over HTTP/2]
- API Gateway & Ingress -> Card Networks & Tokenization Vault: Tokenizes PANs [HTTPS / mTLS]
- API Gateway & Ingress -> Amazon ElastiCache (Redis): Sliding window rate tracking [RESP protocol over TCP]
- API Gateway & Ingress -> Case Management Backend: Forwards authenticated requests [HTTP/2]

## Technology Stack
- AWS ALB / AWS WAF for edge security and PCI-DSS scoping
- Java / Spring Cloud Gateway for high-performance API routing
- gRPC over HTTP/2 for low-latency internal communication
- Amazon ElastiCache (Redis) for distributed rate limiting and circuit breaking via Resilience4j
- Spring Security OAuth2 Resource Server for JWT authentication

## Rationale
[This architecture satisfies PCI-DSS Level 1 compliance by isolating card data using external tokenization and edge security. It meets strict P99 latency requirements under 50 ms at 3,000 TPS through gRPC communication and distributed in-memory caching.]