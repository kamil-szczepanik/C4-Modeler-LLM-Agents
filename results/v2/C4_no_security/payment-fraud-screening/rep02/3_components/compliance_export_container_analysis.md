## Overview
The Compliance Export Container provides scheduled, automated generation of standardized CSV and JSON audit trails to satisfy 7-year regulatory retention and PCI-DSS compliance. It operates within a cost-effective, serverless architecture managed by a three-engineer team.

## Key Elements
* Compliance Export Container (AWS Lambda)
* Athena Query Orchestrator (Python / boto3)
* Schema Formatter Component (Python / Pandas)
* Presigned URL Notifier
* Amazon Athena
* Audit & Feature Store (Amazon S3 with Object Lock)
* Amazon S3 Compliance Bucket
* Amazon SNS & Amazon SQS DLQ
* Amazon EventBridge

## Relationships
* Compliance Export Container -> Amazon Athena: Executes scheduled audit queries [HTTPS / AWS SDK]
* Compliance Export Container -> Audit & Feature Store: Queries tamper-evident compliance logs [Amazon Athena]
* Compliance Export Container -> Amazon S3 Compliance Bucket: Writes formatted CSV/JSON audit reports [HTTPS / AWS SDK]
* Compliance Export Container -> Amazon SNS: Publishes export status and secure download links [AWS SDK]
* Amazon EventBridge -> Compliance Export Container: Triggers scheduled compliance exports [Cron / AWS Events]
* Compliance Export Container -> Amazon SQS DLQ: Captures unhandled execution failures for analysis [AWS SDK]

## Technology Stack
* AWS Lambda: Serverless execution environment chosen to maintain the fixed €25k/month infrastructure budget.
* Amazon Athena: Serverless query service used to process heavy 7-year compliance datasets without always-on compute.
* Python with boto3 and Pandas: Lightweight runtime and data manipulation libraries selected for streaming and formatting query results within memory limits.
* Amazon S3 Object Lock: Tamper-evident storage ensuring immutable audit logs for regulatory compliance.

## Rationale
Serverless execution via AWS Lambda and Amazon Athena eliminates idle infrastructure costs, fitting the strict €25k/month budget for a three-engineer team. Scoping exports to standardized CSV/JSON packages via automated streaming prevents memory bottlenecks while fulfilling strict PCI-DSS and 7-year auditability mandates.