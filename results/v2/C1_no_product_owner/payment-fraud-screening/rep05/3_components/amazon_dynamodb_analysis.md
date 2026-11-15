## Overview
Amazon DynamoDB serves as a low-latency feature store and append-only audit log store for real-time payment fraud screening. It enables sub-50ms fraud decisions while strictly maintaining PCI-DSS Level 1 compliance and a 7-year audit trail.

## Key Elements
* **`FeatureStore` Table:** DynamoDB table using Provisioned Capacity with Auto-Scaling, optimized for low-latency point reads.
* **`AuditLogs` Table:** DynamoDB table capturing append-only decision logs synced via DynamoDB Streams.
* **AWS VPC Endpoint (PrivateLink):** Secures data-in-transit between ECS containers and DynamoDB.
* **AWS KMS CMK:** Encrypts data at rest using Customer Managed Keys with automated rotation.
* **Terraform Modules:** Infrastructure-as-Code engine defining tables, auto-scaling, and endpoints.
* **Amazon CloudWatch:** Monitors `ReadThrottleEvents`, `SystemErrors`, and Contributor Insights.

## Relationships
* **Fraud Scoring Engine -> `FeatureStore`:** Executes single-digit millisecond `GetItem` and `BatchGetItem` calls via AWS SDK over HTTPS / VPC Endpoint.
* **`AuditLogs` -> Amazon S3 (Object Lock):** Streams tamper-evident decision logs asynchronously via DynamoDB Streams using AWS SDK.
* **Case Management App -> `FeatureStore` & `AuditLogs`:** Executes restricted `Query` operations via AWS SDK governed by ABAC IAM policies.
* **Amazon CloudWatch -> Amazon SNS / PagerDuty:** Triggers automated failover alerts on throttling or system errors.

## Technology Stack
* **Amazon DynamoDB:** Chosen for predictable single-digit millisecond latency at 3,000 TPS under fixed cost constraints.
* **Provisioned Capacity with Auto-Scaling:** Selected over On-Demand to prevent budget spikes while handling 3,000 TPS.
* **AWS Encryption SDK:** Implemented for client-side attribute-level encryption to satisfy PCI-DSS scope reduction.
* **AWS VPC Endpoints:** Mandated to ensure payment traffic bypasses the public internet.
* **Terraform:** Used for repeatable, version-controlled infrastructure deployment.

## Rationale
This architecture guarantees P99 latency below 50ms at 3,000 TPS through composite primary keys (`MerchantID#CustomerID`) and provisioned capacity. It respects the 25,000 EUR monthly budget and PCI-DSS Level 1 constraints via VPC isolation, AWS KMS encryption, and automated compliance auditing.