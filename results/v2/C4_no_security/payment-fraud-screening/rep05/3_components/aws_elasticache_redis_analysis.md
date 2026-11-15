## Overview
This system provides real-time fraud screening for card-not-present payment authorizations and case management for suspicious transactions. It ensures strict PCI-DSS Level 1 compliance and sub-50ms decision latency within a fixed budget of 25,000 EUR per month.

## Key Elements
* Fraud Analysts and Compliance Officers
* Auditors and Regulators
* AWS API Gateway
* Fraud Scoring Engine (Go / Rust)
* Case Management & Rules Service (Node.js / Go)
* Audit & Evidence Worker (Go)
* AWS ElastiCache (Redis)
* Amazon SQS
* AWS S3 with Object Lock and Glacier Deep Archive

## Relationships
* Fraud Scoring Engine -> AWS ElastiCache (Redis): Queries real-time features using Redis Protocol (RESP) over TLS
* AWS API Gateway -> Fraud Scoring Engine: Routes payment authorization requests via HTTPS
* Fraud Scoring Engine -> Amazon SQS: Offloads audit events and case reviews asynchronously

## Technology Stack
* AWS API Gateway: Ingests incoming payment authorization requests
* Go / Rust: Implements high-throughput, low-latency Fraud Scoring Engine
* AWS ElastiCache (Redis): Provides sub-millisecond feature lookup using cache.m6g.large instances
* Amazon S3: Stores tamper-evident audit logs with Object Lock for 7 years
* Terraform: Automates infrastructure deployment for the 3-person engineering team

## Rationale
The architecture combines low-latency Redis caching with horizontally scalable Go/Rust microservices to meet the strict 50ms P99 latency requirement at 3,000 TPS. Managed AWS services and Infrastructure as Code maintain high availability and PCI-DSS compliance within the 25,000 EUR budget for a three-engineer team.