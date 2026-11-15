## Overview
Real-Time Payment Fraud Screening system screens card-not-present payment authorizations for fraud before approval and provides case management for analysts.

## Key Elements
* Modular Monolith Core Scoring Engine (AWS ECS Fargate)
* Internal Modules: Rule-Evaluation Module, ML-Scoring Module, Fail-Fast Validation Pipeline
* Supporting Infrastructure: AWS API Gateway, Tokenization Proxy Container, Amazon SQS, AWS S3 Object Lock, OpenTelemetry Sidecar

## Relationships
* Tokenization Proxy Container -> Modular Monolith Core Scoring Engine: Sends tokenized payment data via internal VPC network
* Modular Monolith Core Scoring Engine -> Amazon SQS: Asynchronously routes review cases via SQS API
* Modular Monolith Core Scoring Engine -> AWS S3 Object Lock: Writes tamper-evident audit logs via AWS SDK

## Technology Stack
* AWS ECS Fargate: Provides container orchestration within the 25k EUR budget
* Strategy Pattern & Atomic References: Enables zero-downtime hot-swapping of rules and models in memory
* ArchUnit: Enforces compile-time module boundaries and unidirectional data flow
* OpenTelemetry Sidecar (AWS Distro): Handles asynchronous metric flushing

## Rationale
The modular monolith architecture avoids network hops to meet the <50ms P99 latency target. Thread-safe in-memory hot-swapping and strict resource pooling ensure high throughput while operating within a fixed budget and small team.