## Overview
The Online Bookstore is a scaled-down e-commerce platform that enables global users to browse, purchase, and review books with multi-region AWS infrastructure. Its core purpose is delivering a secure, performant, and highly available shopping experience supporting 1M MAU.

## Key Elements
- Observability & Synthetic Monitoring Container (AWS CloudWatch, AWS X-Ray)
- Core Domain Services (ECS / EKS, gRPC / REST)
- Automated Synthetic Canaries & Out-of-Band Probes
- Operations Personnel & On-Call Engineering Team

## Relationships
- Core Domain Services emit structured JSON logs and RED metrics to AWS CloudWatch via APM SDK wrappers over gRPC/REST.
- Synthetic Canaries execute periodic automated test scripts across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to validate regional user journeys.
- AWS CloudWatch evaluates composite alarms based on SLO burn rates, dispatching alerts to Operations Personnel.

## Technology Stack
- AWS CloudWatch & X-Ray: Native AWS monitoring, distributed tracing, and metric ingestion.
- Terraform / AWS CDK: Observability-as-Code for declarative, multi-region dashboard and alarm management.
- Dynamic Tail-Based Sampling: Controls cloud costs by capturing 100% of errors/slow transactions and a sample of healthy requests.
- Local Agent Buffering & Circuit Breakers: Prevents monitoring backpressure from crashing core application threads.

## Rationale
This architecture ensures 99.95% uptime and rapid incident response by combining automated SLO-based alerting with resilient, localized observability pipelines. Observability-as-code guarantees multi-region consistency across `us-east-1`, `eu-west-1`, and `ap-southeast-1` while strictly adhering to data residency constraints.