## Overview
[The Data & Audit Stores container provides secure, low-latency feature storage, relational case management, and tamper-evident 7-year audit logging for the Real-Time Payment Fraud Screening system on AWS.]

## Key Elements
* Audit & Decision Log Store (Amazon DynamoDB with AWS KMS and DynamoDB Streams)
* Feature Store (Amazon DynamoDB)
* Case Management Database (Amazon RDS PostgreSQL)
* Audit Archival Worker (AWS Lambda)
* Long-Term Audit Archive (Amazon S3 Glacier Flexible Retrieval with S3 Object Lock)

## Relationships
* Real-Time Scoring Service -> Feature Store: Read/write fraud features via DynamoDB SDK (HTTPS/TLS 1.3)
* Real-Time Scoring Service -> Audit & Decision Log Store: Appends immutable decision records via DynamoDB API (HTTPS/TLS 1.3)
* Case Management Backend <-> Case Management DB: Relational data persistence via PostgreSQL JDBC (TLS 1.3)
* Audit & Decision Log Store -> Audit Archival Worker: Streams change records via DynamoDB Streams (Internal AWS Event Source)
* Audit Archival Worker -> Long-Term Audit Archive: Writes tamper-evident archives via S3 API (HTTPS/TLS 1.3)

## Technology Stack
* Amazon DynamoDB: Selected for feature and audit storage to achieve sub-50ms P99 latency.
* Amazon RDS PostgreSQL: Selected for case management to handle complex relational analyst workflows.
* Amazon S3 Glacier: Selected for 7-year audit retention with S3 Object Lock (Compliance Mode) to meet budget and compliance constraints.
* AWS Lambda: Selected for serverless audit stream processing with minimal operational overhead.
* AWS KMS: Selected for customer-managed encryption keys to ensure strict data protection.

## Rationale
[This architecture satisfies PCI-DSS Level 1 compliance and sub-50ms latency requirements through isolated AWS data stores and managed services. It respects a €25,000 monthly budget and a 3-engineer team constraint by leveraging serverless archival pipelines.]