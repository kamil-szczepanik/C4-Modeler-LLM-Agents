## Overview
[The system provides real-time fraud screening for card-not-present payment authorizations, enabling secure automated decisions and analyst reviews. It ensures strict 7-year auditability and PCI-DSS compliance within a fixed budget.]

## Key Elements
- S3 Bucket (Data Partition)
- S3 Object Lock Policy Engine
- AWS Glue Data Catalog
- Athena Query Interface
- S3 Glacier Flexible Retrieval

## Relationships
- Risk / Compliance Officer -> Athena Query Interface: Queries historical audit logs [HTTPS/Console, SQL]
- Athena Query Interface -> S3 Bucket (Data Partition): Scans immutable audit records [AWS internal storage APIs]

## Technology Stack
- Amazon S3 Object Lock (Compliance Mode): Ensures tamper-evident 7-year retention for R-06 compliance
- AWS KMS: Encrypts audit data at rest using Customer Managed Keys with annual rotation
- Amazon Athena & AWS Glue Data Catalog: Enables serverless SQL querying over partitioned audit logs
- S3 Glacier Flexible Retrieval: Optimizes long-term storage costs to fit the 25,000 EUR monthly budget

## Rationale
[This architecture satisfies strict 7-year audit and PCI-DSS mandates while maintaining low operational overhead for a 3-engineer team. Cloud tiering and serverless querying balance cost constraints with rapid compliance retrieval capabilities.]