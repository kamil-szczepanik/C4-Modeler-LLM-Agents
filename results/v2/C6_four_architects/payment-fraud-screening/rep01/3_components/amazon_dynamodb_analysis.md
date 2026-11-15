## Overview
The system is a real-time payment fraud screening platform that evaluates card-not-present payment authorizations and provides case management for fraud analysts. It is designed to process 3,000 transactions per second within strict PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
* Transaction Table (Amazon DynamoDB)
* Case Management Table (Amazon DynamoDB)
* Global Secondary Indexes (GSIs)
* DynamoDB Streams Processor (AWS Lambda)
* Client-Side Encryption Component (AWS Encryption SDK)
* Auto-Scaling Configuration

## Relationships
* Real-Time Scoring Engine -> Transaction Table: Reads and writes authorization data using `GetItem` and `PutItem` via AWS SDK [HTTPS]
* Case Management Backend -> Case Management Table & GSIs: Manages analyst workflows using `Query` and `UpdateItem` via AWS SDK [HTTPS]
* Case Management Table -> DynamoDB Streams Processor: Triggers event processing via DynamoDB Streams [AWS Internal Stream]
* DynamoDB Streams Processor -> Amazon S3 Object Lock: Streams tamper-evident audit logs via AWS SDK [HTTPS]

## Technology Stack
* Amazon DynamoDB: Selected for single-digit millisecond latency to meet the sub-50ms P99 requirement (R-04).
* AWS Encryption SDK: Utilized for client-side column-level encryption to satisfy PCI-DSS Level 1 compliance (R-05).
* DynamoDB Streams and AWS Lambda: Used for real-time change data capture to fulfill tamper-evident 7-year auditability (R-06).
* DynamoDB Auto-Scaling: Implemented with 70% target utilization to manage 3,000 TPS within the 25,000 EUR monthly budget.

## Rationale
This architecture leverages fully managed AWS serverless data services to deliver sub-50ms latency and strict PCI-DSS compliance at scale. The design minimizes operational overhead, allowing a three-engineer team to reliably operate and audit the system within a fixed budget.