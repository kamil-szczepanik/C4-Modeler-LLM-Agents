## Overview
[The Feature Cache provides ultra-low-latency data storage for transactional and velocity features used in real-time card-not-present fraud screening. It ensures sub-50 ms P99 decision latency while maintaining strict PCI-DSS Level 1 compliance and budget constraints.]

## Key Elements
* Amazon DynamoDB: Serverless primary data store for transactional features and velocity metrics.
* Feature Data Access Component: Go-based application layer utilizing the AWS SDK for optimized batch reads and writes.
* TTL Manager Component: DynamoDB Time-To-Live feature for automatically expiring stale transactional records.
* In-Process Go Cache: Local, short-TTL memory cache inside the Real-Time Scoring Service for static features.
* AWS Key Management Service (KMS): Customer-managed keys securing data encryption-at-rest.

## Relationships
* Real-Time Scoring Service -> Feature Data Access Component: Retrieves and updates features via VPC Endpoints using HTTPS/gRPC.
* Feature Data Access Component -> Amazon DynamoDB: Executes encrypted data read/write queries over AWS VPC infrastructure.
* Real-Time Scoring Service -> In-Process Go Cache: Fetches static cached features via internal application memory access.
* Amazon SNS/SQS -> In-Process Go Cache: Delivers event-driven cache invalidation messages for velocity updates.

## Technology Stack
* Amazon DynamoDB: Chosen for predictable single-digit millisecond performance and zero server management overhead.
* Go (AWS SDK): Selected for high-performance data serialization and low memory footprint in the scoring pipeline.
* AWS KMS (CMK): Enforced to meet strict PCI-DSS Level 1 encryption and auditability requirements.
* In-Process Go Cache: Implemented to reduce network overhead without introducing dedicated cache cluster costs.

## Rationale
[This architecture combines serverless DynamoDB with an in-process Go cache to satisfy the strict sub-50 ms latency and 7-year tamper-evident audit requirements. It avoids dedicated caching clusters like DAX, successfully keeping operational complexity low for a three-engineer team while strictly respecting the 25,000 EUR monthly infrastructure budget.]