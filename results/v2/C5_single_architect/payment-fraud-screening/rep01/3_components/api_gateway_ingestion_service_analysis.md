## Overview
The Real-Time Payment Fraud Screening system processes card-not-present payment authorizations to detect fraud and manage analyst reviews. It ensures high-throughput, low-latency decision-making while maintaining PCI-DSS compliance on AWS.

## Key Elements
* API Gateway / Ingestion Service (Go container with Chi/Fiber)
* HTTP/gRPC Router Component (Go)
* Tokenization Proxy Component (Go)
* Scoring Orchestrator Component (Go)
* Event Publisher Component (Go, AWS SDK)
* Fraud Scoring Engine (Rust)
* Case Management Backend (Node.js / Java)
* Fraud Analyst UI (React, AWS S3 + CloudFront)
* Audit & Decision Store (PostgreSQL on AWS RDS)
* AWS SQS / SNS

## Relationships
* Payment Gateway / Acquirer -> API Gateway / Ingestion Service: Sends authorization requests [HTTPS/gRPC]
* HTTP/gRPC Router Component -> Tokenization Proxy Component: Forwards raw payload [Internal Memory]
* Tokenization Proxy Component -> Tokenization / Vault Provider: Strips PANs and tokenizes card data [mTLS / HTTPS]
* Scoring Orchestrator Component -> Fraud Scoring Engine: Invokes fraud scoring with 35ms timeout [gRPC]
* Event Publisher Component -> AWS SQS / SNS: Publishes transaction and decision payloads [AWS SDK batching over HTTPS]
* API Gateway / Ingestion Service -> Audit & Decision Store: Persists decisions [PostgreSQL protocol]

## Technology Stack
* Go (Chi/Fiber): Chosen for low memory footprint, concurrency, and sub-millisecond routing overhead to meet 3,000 TPS and 25k EUR budget constraints.
* gRPC: Utilized for low-latency internal communication between the API Gateway and Scoring Engine.
* AWS SDK: Used for efficient batch publishing to AWS SQS/SNS within cost limits.
* PostgreSQL on AWS RDS: Provides durable, relational storage for audit trails and decision logs.

## Rationale
This architecture uses Go microservices and gRPC to meet the stringent P99 < 50ms latency at 3,000 TPS within a 25,000 EUR monthly budget. Explicit timeouts, tokenization proxies, and strict component isolation ensure PCI-DSS Level 1 compliance and fault-tolerant availability.