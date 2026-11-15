## Overview
The Real-Time Payment Fraud Screening system evaluates card-not-present payment authorizations for fraud at scale while enabling manual analyst reviews. It ensures low-latency decisions, strict PCI-DSS compliance, and tamper-evident auditing within a fixed budget and small team.

## Key Elements
- Payment Gateway / Acquirer Systems
- Fraud Scoring Engine (AWS ECS/Lambda)
- Case Management SaaS
- Third-Party Fraud Intelligence Feeds
- Identity Provider (AWS Cognito / Okta)
- Decision Audit Store (AWS S3 Object Lock & AWS KMS)

## Relationships
- Payment Gateway to Fraud Scoring Engine via gRPC/HTTPS for low-latency requests
- Fraud Scoring Engine to Third-Party Fraud Intelligence Feeds via HTTPS
- Fraud Scoring Engine to Case Management SaaS via secure REST APIs/Webhooks
- Fraud Scoring Engine to Audit Store via asynchronous log streaming with AWS KMS signing

## Technology Stack
- AWS eu-west-1: Target cloud region ensuring compliance and low latency
- Terraform/CDK: Infrastructure-as-code for zero-downtime deployments and GitOps
- AWS S3 Object Lock (Compliance Mode): Write-once-read-many storage for 7-year auditability
- AWS KMS: Cryptographic signing for tamper-evident decision logs
- gRPC / HTTPS: High-performance protocols for core scoring evaluation

## Rationale
The architecture separates high-throughput synchronous scoring from asynchronous case management to meet the P99 latency SLA. Offloading UI components to SaaS and utilizing managed AWS services ensures PCI-DSS compliance and operational feasibility for a three-person engineering team.