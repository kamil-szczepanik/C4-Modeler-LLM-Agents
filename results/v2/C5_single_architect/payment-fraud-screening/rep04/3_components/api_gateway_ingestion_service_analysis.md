## Overview
The API Gateway / Ingestion Service securely ingests, validates, sanitizes, and routes real-time payment authorization requests for fraud screening. It ensures strict PCI-DSS compliance and high-performance processing while maintaining strict latency and auditability constraints.

## Key Elements
- **API Gateway / Ingestion Service** (AWS API Gateway / ECS Fargate with Go)
- **Routing & Rate Limiting Filter** (Go component)
- **Data Sanitization & Tokenization Masking Component** (Go component)
- **Internal gRPC Client Router** (Go component)
- **Audit Logger & Telemetry Interceptor** (Go component)

## Relationships
- Payment Gateway / Core Ledger -> API Gateway / Ingestion Service: Sends authorization requests [HTTPS/REST (TLS 1.3)]
- Routing & Rate Limiting Filter -> Data Sanitization & Tokenization Masking Component: Hands off validated payloads [In-memory function call]
- Data Sanitization & Tokenization Masking Component -> Internal gRPC Client Router: Forwards sanitized payloads [In-memory function call]
- API Gateway / Ingestion Service -> Scoring Engine: Forwards requests for fraud evaluation [gRPC over mTLS]
- Audit Logger & Telemetry Interceptor -> Audit & Event Bus (Amazon MSK / Kafka): Emits telemetry and logs asynchronously [Kafka Protocol]

## Technology Stack
- **AWS API Gateway / ECS Fargate**: Selected for scalable container orchestration within budget.
- **Go**: Chosen for low memory footprint and high concurrency to achieve <50ms P99 latency.
- **gRPC over mTLS**: Used for fast, secure internal inter-container communication.

## Rationale
This architecture uses Go and Fargate to deliver high-throughput, low-latency processing required for 3,000 TPS under a 25,000 EUR monthly budget. Component-level tokenization and asynchronous auditing securely satisfy PCI-DSS Level 1 compliance and 7-year auditability.