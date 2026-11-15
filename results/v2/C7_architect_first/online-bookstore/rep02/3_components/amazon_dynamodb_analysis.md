## Overview
The Online Bookstore uses Amazon DynamoDB as a low-latency NoSQL datastore to manage high-throughput catalog, cart, and session operational data. It supports global active-active replication, strict data privacy compliance, and sub-10ms performance for 1M MAU.

## Key Elements
* Request Router / API Frontend
* Partition Router & Storage Nodes
* Storage Engine (B+-Tree & LSM-like indexing)
* Streams Processor (DynamoDB Streams)
* Global Tables (Multi-region active-active)

## Relationships
* Core E-Commerce Container -> Request Router: Reads/writes shopping cart & session state [HTTPS / DynamoDB API]
* Request Router -> Partition Router & Storage Nodes: Routes internal RPC requests [TCP / Consistent Hashing]
* Partition Router & Storage Nodes -> Storage Engine: Executes persistent B+-Tree updates [Local PCIe/SATA]
* Storage Engine -> Streams Processor: Triggers change data capture events [Internal Memory Buffers]
* Streams Processor -> Amazon SQS / SNS: Publishes item-level modification events [HTTPS / JSON]

## Technology Stack
* Amazon DynamoDB: Selected for predictable sub-10ms latency and high scalability.
* DynamoDB Streams: Used for asynchronous change data capture and event-driven integration.
* AWS KMS (CMK): Enforces encryption-at-rest with multi-region cryptographic isolation.
* DynamoDB Global Tables: Provides active-active multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.
* Terraform / CloudFormation: Ensures infrastructure as code and automated drift detection.

## Rationale
This architecture ensures 99.95% uptime and low-latency performance to meet strict page-load requirements. It satisfies GDPR and CCPA mandates through localized KMS encryption, Point-in-Time Recovery (PITR), and strict PII data minimization.