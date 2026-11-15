## Overview
[A real-time payment fraud screening system evaluates card-not-present payment authorizations for mid-size payment processors before approval, while providing case management tools for fraud analysts.]

## Key Elements
* Case Management & Admin Container (AWS ECS on Fargate)
* Amazon Aurora Serverless v2 (Relational database)
* Amazon RDS Proxy (Connection pooler)
* Amazon S3 with Object Lock (Tamper-evident audit storage)
* AWS Database Migration Service (CDC streaming)
* AWS Secrets Manager (Credential rotation)

## Relationships
* Case Management & Admin Container -> Amazon RDS Proxy: Queries and updates case data and relational workflows [TLS]
* Amazon RDS Proxy -> Amazon Aurora Serverless v2: Manages database connections [TLS]
* Amazon Aurora Serverless v2 -> Amazon S3 with Object Lock: Streams change data capture audit logs asynchronously via AWS Database Migration Service [TLS/HTTPS]
* Case Management & Admin Container -> AWS Secrets Manager: Fetches rotated database credentials [HTTPS/IAM]

## Technology Stack
* AWS ECS on Fargate: Runs containerized case management within a lean three-engineer team constraint
* Amazon Aurora Serverless v2: Provides relational storage for case management with strictly bounded ACUs to respect the 25,000 EUR monthly budget
* Amazon RDS Proxy: Prevents Fargate task scaling from exhausting database connections
* Amazon S3 with Object Lock: Delivers 7-year tamper-evident audit storage for PCI-DSS compliance without relational write contention
* AWS Database Migration Service: Streams CDC events off the primary database asynchronously

## Rationale
[Separating high-throughput audit streaming to S3 from relational case management in Aurora Serverless protects P99 latency targets and prevents budget overruns. Utilizing managed AWS services like RDS Proxy, Fargate, and Secrets Manager maintains PCI-DSS compliance while minimizing operational overhead for a three-engineer team.]