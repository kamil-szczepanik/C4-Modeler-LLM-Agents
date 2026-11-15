## Overview
[The Analytics & Event Tracking Container manages real-time telemetry ingestion, data masking, and analytical processing for the Online Bookstore. It powers personalized customer recommendations and administrative sales insights while ensuring GDPR and CCPA compliance.]

## Key Elements
- Customers and Bookstore Administrators
- Ingestion API (Node.js / AWS API Gateway)
- Stream Processor (AWS Kinesis / Apache Flink)
- Data Firehose (AWS Kinesis Data Firehose)
- Reporting & Insights API (Node.js / AWS Lambda)
- Data Stores (AWS S3 / Snowflake)

## Relationships
- Single Page Application -> Ingestion API: Sends clickstream and search events [HTTPS / JSON]
- Ingestion API -> Stream Processor: Forwards scrubbed events [AWS Kinesis]
- Stream Processor -> Async Event Bus: Publishes real-time user actions [Amazon EventBridge]
- Data Firehose -> Data Stores (S3/Snowflake): Persists aggregated analytics [S3/Snowflake Bulk Load]
- Bookstore Administrator -> Reporting & Insights API: Queries dashboards [HTTPS / JSON]
- Reporting & Insights API -> Data Stores (Snowflake): Executes analytical queries [JDBC / Snowflake SQL]

## Technology Stack
- Node.js & AWS Lambda: Lightweight serverless execution for APIs
- AWS API Gateway & Kinesis: Scalable real-time event ingestion and stream processing
- Snowflake & AWS S3: High-performance data warehousing for historical analytics
- AWS KMS: Customer-managed encryption keys for data-at-rest protection

## Rationale
[This architecture ensures high scalability to support 1 million monthly active users while maintaining strict security controls. Edge data masking and rigorous IAM policies guarantee full compliance with GDPR and CCPA mandates.]