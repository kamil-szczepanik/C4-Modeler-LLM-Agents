## Overview
[The system is a real-time payment fraud screening platform for card-not-present transactions, designed to score authorization requests and manage suspicious payment reviews.]
[It ensures PCI-DSS compliance, 7-year auditability, and sub-50ms latency within a fixed AWS budget operated by a lean engineering team.]

## Key Elements
* Risk Manager & Compliance Auditor
* Case Management & Reporting Container (Node.js, AWS ECS Fargate)
* Amazon Athena (Athena Workgroups, Presto/Trino Query Engine, AWS Glue Data Catalog)
* Amazon S3 Object Lock

## Relationships
* Case Management & Reporting Container -> Athena Workgroups [HTTPS / AWS SDK]
* Athena Workgroups -> Presto/Trino Query Engine [Internal AWS Backbone]
* Presto/Trino Query Engine -> AWS Glue Data Catalog [Internal AWS Backbone]
* Presto/Trino Query Engine -> Amazon S3 Object Lock [SQL / AWS API]

## Technology Stack
* AWS ECS Fargate: Container hosting for low operational overhead.
* Amazon Athena: Serverless query engine for cost-effective ad-hoc auditing.
* AWS Glue Data Catalog: Schema registry with partition projection for performance and cost control.
* Amazon S3 Object Lock: Tamper-evident storage ensuring 7-year auditability.

## Rationale
[Serverless AWS components minimize infrastructure management for a 3-person engineering team while strictly enforcing budget limits.]
[Decoupled query routing via internal containers guarantees PCI-DSS compliance and robust audit capabilities.]