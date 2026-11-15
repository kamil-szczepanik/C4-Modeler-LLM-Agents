## Overview
The system is a real-time payment fraud screening platform that evaluates 3,000 card-not-present authorizations per second in AWS (`eu-west-1`). It provides automated risk scoring, case management for analysts, and a secure 7-year tamper-evident audit trail while adhering to strict PCI-DSS Level 1 compliance.

## Key Elements
* **Users:** Fraud Analysts reviewing flagged transactions via the Case Management UI.
* **External Systems:** Payment Gateway integrating via REST APIs.
* **Containers:** Ingestion Edge Proxy, Stateless Scoring Microservice, and Case Management Backend.
* **Storage & Caching:** Amazon ElastiCache (feature store), Amazon S3 with Object Lock (audit logs).
* **Infrastructure Services:** AWS ECS Fargate, AWS KMS, AWS CodePipeline, Amazon CloudWatch.

## Relationships
* Payment Gateway invokes Ingestion Edge Proxy via HTTPS/REST.
* Ingestion Edge Proxy queries Amazon ElastiCache for user/card feature vectors via Redis protocol.
* Scoring Microservice performs in-memory ONNX scoring and publishes audit records to Amazon S3 using AWS KMS encryption via HTTPS.
* Fraud Analysts access Case Management Backend via HTTPS.

## Technology Stack
* **Compute:** AWS ECS Fargate for stateless microservices to minimize operational toil.
* **Scoring Runtime:** ONNX runtimes loaded in memory for sub-50ms P99 latency.
* **Caching:** Amazon ElastiCache for sub-millisecond feature lookup.
* **Audit Storage:** Amazon S3 Object Lock with AWS KMS envelope encryption for 7-year tamper-evident compliance.
* **Deployment & IaC:** Terraform and AWS CodePipeline for automated blue/green deployments and infrastructure reproducibility.
* **Observability:** Amazon CloudWatch and AWS X-Ray with correlation IDs for tracing without infrastructure bloat.

## Rationale
The architecture prioritizes "boring technology" and fully managed AWS services to fit the operational capacity of a 3-person team. Strict data boundary isolation and automated S3 compliance controls satisfy PCI-DSS and 7-year audit rules within a €25,000 monthly budget.