## Overview
[The system is a real-time payment fraud screening platform that evaluates payment authorizations and manages suspicious transactions. Its core purpose is to prevent fraud, enforce PCI-DSS compliance, and provide low-latency risk decisions.]

## Key Elements
* Payment Gateway / Processing Engine
* API Gateway (AWS Regional ALB with AWS WAF)
* Envoy Proxy Sidecar
* Fraud Scoring Engine
* Tokenization Vault
* Amazon Redis
* Amazon Aurora PostgreSQL

## Relationships
* Payment Gateway / Processing Engine -> API Gateway: Submits payment authorizations via HTTPS (REST/JSON)
* API Gateway -> Tokenization Vault: Sanitizes PANs and retrieves payment tokens via HTTPS (REST/JSON)
* API Gateway -> Envoy Proxy Sidecar: Routes sanitized requests via internal VPC Link
* Envoy Proxy Sidecar -> Fraud Scoring Engine: Forwards payloads via gRPC over TLS (mTLS)
* API Gateway -> Amazon Redis: Evaluates sliding-window rate limits via Redis protocol

## Technology Stack
* AWS ALB & AWS WAF: Managed edge security and rate limiting to prevent card-testing attacks within budget
* Amazon Redis: Low-latency distributed cache supporting high-throughput sliding-window rate limiting
* gRPC over TLS (mTLS): High-performance internal communication protocol guaranteeing sub-50ms P99 latency
* AWS Certificate Manager (ACM) Private CA: Automated certificate lifecycle management for strict mTLS compliance

## Rationale
[This architecture uses AWS managed edge services and gRPC to meet the strict sub-50ms latency at 3,000 TPS under a 25,000 EUR monthly budget. Edge tokenization and zero-logging ensure PCI-DSS Level 1 compliance while operating with a three-engineer team.]