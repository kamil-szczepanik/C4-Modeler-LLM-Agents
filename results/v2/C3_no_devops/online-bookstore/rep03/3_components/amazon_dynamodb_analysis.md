## Overview
An Amazon DynamoDB data layer for the Online Bookstore manages shopping carts, user sessions, and browsing history with low-latency access. It ensures secure, high-performance data operations globally across multiple regions.

## Key Elements
* Shopping Cart Table (`CartTable`)
* Session & History Table (`UserActivityTable`)
* DynamoDB Streams (`ActivityStream`)
* Global Tables Replicator
* DynamoDB Accelerator (DAX)

## Relationships
* Core Microservices -> `CartTable` & `UserActivityTable`: CRUD operations via AWS SDK (HTTPS/TLS 1.3)
* `ActivityStream` -> Core Microservices / Recommendation Engine: Event consumption via Amazon Kinesis Adapter / AWS Lambda
* `CartTable` & `UserActivityTable` <-> Global Tables Replicator: Active-active multi-region replication via AWS backbone (Proprietary Protocol)
* Core Microservices -> DAX: In-memory read queries via AWS DAX SDK (TLS 1.3)

## Technology Stack
* Amazon DynamoDB: NoSQL database selected for predictable single-digit millisecond latency (R-02, R-06)
* AWS KMS: Customer-managed keys (CMK) with automatic rotation for encryption at rest
* DynamoDB Time-to-Live (TTL): Configured for 7-14 days to support GDPR/CCPA data minimization
* DynamoDB Global Tables: Multi-region replication in `us-east-1`, `eu-west-1`, and `ap-southeast-1` for 99.95% availability (R-07)
* DynamoDB Accelerator (DAX): In-memory caching for sub-millisecond read queries on user activity

## Rationale
This architecture uses DynamoDB to handle high-velocity cart and session data for 1M MAU without violating the 2-second page load limit. Comprehensive security controls, multi-region replication, and automated recovery ensure strict regulatory compliance and business continuity.