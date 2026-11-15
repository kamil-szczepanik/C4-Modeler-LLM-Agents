## Overview
[The Analytics Store container provides scalable storage, auditing, and business intelligence for transaction and fraud screening data. It enables cost-effective long-term analytics while strictly enforcing PCI-DSS compliance and data protection mandates.]

## Key Elements
[Data Lake Storage: Amazon S3 with Parquet format and Object Lock]
[Query Engine: Amazon Athena]
[Schema Catalog: AWS Glue Data Catalog]
[ETL Ingestion Worker: AWS Lambda (Python)]
[BI Dashboard Interface: Amazon QuickSight]
[Security Controls: AWS Lake Formation, AWS KMS]

## Relationships
[Audit Log Store (Aurora PostgreSQL) `--[Lambda PutObject (HTTPS)]-->` Data Lake Storage (Amazon S3)]
[Data Lake Storage (Amazon S3) `--[AWS Glue Crawler / Explicit Schema]-->` Schema Catalog (AWS Glue)]
[Schema Catalog (AWS Glue) `--[SQL (HTTPS)]-->` Query Engine (Amazon Athena)]
[Query Engine (Amazon Athena) `--[JDBC/ODBC (HTTPS)]-->` BI Dashboard Interface (Amazon QuickSight)]
[Fraud Analysts & Compliance Auditors `--[HTTPS via AWS Cognito]-->` BI Dashboard Interface (Amazon QuickSight)]

## Technology Stack
[Amazon S3: Immutable, cost-effective storage meeting the 7-year retention rule under budget]
[Amazon Athena: Serverless SQL query engine eliminating operational infrastructure overhead]
[Amazon QuickSight: Pay-per-session BI dashboarding layer empowering non-technical analysts]
[AWS Lambda: Serverless ETL execution enforcing automated PII masking without AWS DMS]
[AWS Lake Formation: Granular row and column-level access control for compliance]

## Rationale
[This serverless architecture operates well within the 25,000 EUR monthly budget and requires zero dedicated database administration for the 3-engineer team. S3 Object Lock and Lake Formation enforce strict tamper-evident auditing (R-06) and data protection (R-05).]