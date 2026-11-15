## Overview
The AWS Glue & Athena system provides serverless data lake analytics and GDPR/CCPA compliance auditing for the online bookstore. It offloads heavy analytical workloads from operational databases to maintain high availability and performance.

## Key Elements
- AWS Glue Data Catalog (AWS Glue Data Catalog)
- AWS Glue ETL Jobs (Apache Spark on AWS Glue Serverless)
- Amazon Athena Query Engine (Presto/Trino-based Amazon Athena)
- S3 Data Lake (Amazon S3)
- Amazon Aurora Global Database (PostgreSQL)
- Amazon DynamoDB
- Compliance/Audit Lambda (AWS Lambda)
- Admin/Content Manager

## Relationships
- AWS Glue ETL Jobs -> Amazon Aurora Global Database [JDBC/TLS]
- AWS Glue ETL Jobs -> Amazon DynamoDB [AWS SDK / S3]
- AWS Glue ETL Jobs -> S3 Data Lake (Amazon S3) [S3 API / HTTPS]
- Amazon Athena Query Engine -> AWS Glue Data Catalog [Internal AWS API]
- Amazon Athena Query Engine -> S3 Data Lake (Amazon S3) [S3 API / HTTPS]
- Compliance/Audit Lambda -> Amazon Athena Query Engine [AWS SDK / HTTPS]
- Admin/Content Manager -> Amazon Athena Query Engine [JDBC/ODBC or AWS Console/HTTPS]

## Technology Stack
- AWS Glue: Serverless ETL processing and metadata cataloging for scalable data ingestion.
- Amazon Athena: Serverless interactive query service for fast ad-hoc analysis using standard SQL.
- Apache Parquet: Columnar storage format optimizing query performance and storage costs in S3.

## Rationale
This architecture ensures 99.95% uptime by isolating analytical reporting from operational databases serving 1M MAU. It also provides robust GDPR/CCPA compliance auditing through automated data discovery queries.