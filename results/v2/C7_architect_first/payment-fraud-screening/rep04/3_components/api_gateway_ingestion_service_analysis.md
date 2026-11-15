## Overview
The API Gateway / Ingestion Service securely ingests, validates, and routes real-time payment authorization requests while enforcing strict security controls, latency SLAs, and PCI-DSS compliance. It serves as the primary ingress point for the Real-Time Payment Fraud Screening system on AWS.

## Key Elements
* **Container:** API Gateway / Ingestion Service (Go, AWS ECS Fargate)
* **Component:** HTTP Ingestion Handler (`net/http`)
* **Component:** Rate Limiter & Circuit Breaker (Custom middleware)
* **Component:** gRPC Client (`grpc-go`)
* **Component:** Audit Dispatcher (Asynchronous worker pool)
* **Sidecar:** FluentBit log redaction sidecar

## Relationships
* **Payment Gateway -> API Gateway / Ingestion Service:** Sends payment authorizations [HTTPS/JSON via AWS ALB with TLS 1.3]
* **API Gateway / Ingestion Service -> Fraud Scoring Engine:** Forwards sanitized authorization requests [gRPC over HTTP/2 with mTLS via AWS VPC security groups]
* **API Gateway / Ingestion Service -> Audit & Event Store:** Asynchronously writes tamper-evident decision inputs and metadata [HTTPS / AWS SDK with HMAC-SHA256]

## Technology Stack
* **Go:** Selected for superior memory footprint and CPU efficiency to maintain <50 ms P99 latency at 3,000 TPS.
* **AWS ECS Fargate:** Provides serverless container orchestration within a 3-engineer team constraint and €25,000 monthly budget.
* **AWS Application Load Balancer & AWS WAF:** Terminates TLS 1.3, provides ingress traffic protection, and enforces PCI-DSS network isolation.
* **AWS Secrets Manager:** Injects runtime secrets securely without static credentials in container images.

## Rationale
This architecture leverages Go and Fargate to achieve high-throughput, low-latency processing within budget and staffing constraints. Comprehensive security controls, non-blocking asynchronous logging, and circuit breakers ensure PCI-DSS Level 1 compliance and fault-tolerant merchant availability.