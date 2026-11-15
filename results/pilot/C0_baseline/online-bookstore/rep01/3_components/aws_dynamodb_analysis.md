## Overview
AWS DynamoDB and DynamoDB Accelerator (DAX) serve as the high-velocity catalogue, reviews, and recommendation storage tier for the Online Bookstore. They provide single-digit millisecond latency and multi-region replication to support global scaling and high-throughput traffic.

## Key Elements
* AWS DynamoDB Core Tables: Primary storage for catalogue, reviews, and recommendations.
* DynamoDB Accelerator (DAX): In-memory caching layer for high-velocity queries.
* DynamoDB Table Partitions: Logical data partitions managed via consistent hashing.
* DynamoDB Global Secondary Indexes (GSIs): Optimized indexes for flexible keyword searches.
* DynamoDB Streams: Change data capture mechanism for asynchronous event propagation.

## Relationships
* ECS Fargate Go Microservices -> AWS DAX: Reads and writes cached catalogue and recommendation data [Proprietary DAX protocol over TLS 1.3, AWS SigV4].
* ECS Fargate Go Microservices -> AWS DynamoDB: Executes fallback data reads and writes [HTTPS/TLS 1.3, AWS SigV4].
* AWS DynamoDB -> AWS DynamoDB Global Tables: Replicates data across `us-east-1`, `eu-west-1`, and `ap-southeast-1` [AWS private backbone, TLS].
* AWS DynamoDB Streams -> Amazon SNS: Propagates change events [AWS internal triggers].

## Technology Stack
* AWS DynamoDB: Fully managed NoSQL database chosen for auto-scaling and single-digit millisecond latency.
* DynamoDB Accelerator (DAX): In-memory cache chosen to reduce read latency to microseconds for popular book listings.
* AWS KMS: Used with customer-managed keys (CMK) for mandatory AES-256 storage and transit encryption.
* AWS IAM: Enforces fine-grained access control using SigV4 signing and `dynamodb:LeadingKeys`.

## Rationale
This architecture ensures 99.95% availability, sub-2-second page loads, and 1M MAU scalability by offloading high-velocity catalogue lookups to in-memory DAX caching. Multi-region Global Tables and strict AWS security controls satisfy global compliance and disaster recovery requirements.