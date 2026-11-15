## Overview
[The Amazon Athena & S3 Data Lake container provides serverless analytics and immutable storage for compliance auditing, risk reporting, and fraud trend analysis. It securely ingests transaction logs to satisfy 7-year audit mandates while keeping operational costs within the fixed infrastructure budget.]

## Key Elements
* Amazon Kinesis Data Firehose
* Amazon S3 Data Lake Storage (Raw and Curated Zones with S3 Object Lock)
* AWS Glue Data Catalog
* Amazon Athena Query Engine
* AWS Lake Formation

## Relationships
* Scoring Engine & Case Management Containers -> Amazon Kinesis Data Firehose: Ingests transaction logs [HTTPS / AWS SDK]
* Amazon Kinesis Data Firehose -> Amazon S3 Data Lake Storage: Batch-writes logs in Apache Parquet format [S3 API]
* AWS Glue Data Catalog -> Amazon S3 Data Lake Storage: Maintains schema definitions [Internal AWS API]
* Amazon Athena Query Engine -> AWS Glue Data Catalog: Reads metadata for query execution [Internal AWS API]
* Risk Managers & BI Tools -> Amazon Athena Query Engine: Executes compliance audits and trend queries [JDBC/ODBC / HTTPS]

## Technology Stack
* Amazon S3: Chosen for cost-effective, durable storage with Object Lock compliance mode for immutable 7-year audit retention.
* Amazon Kinesis Data Firehose: Selected for near-real-time streaming ingestion and automated conversion to Apache Parquet format.
* AWS Glue Data Catalog: Utilized for automated schema discovery and cataloging of analytical datasets.
* Amazon Athena: Chosen for serverless, pay-per-query SQL execution minimizing idle infrastructure costs.
* AWS Lake Formation: Deployed to enforce column-level data masking and fine-grained access control for PCI-DSS compliance.

## Rationale
[This architecture satisfies PCI-DSS Level 1 and 7-year audit requirements through immutable S3 Object Lock and strict Lake Formation access controls. It respects the €25,000 monthly budget by leveraging serverless Athena queries and Parquet storage optimization.]