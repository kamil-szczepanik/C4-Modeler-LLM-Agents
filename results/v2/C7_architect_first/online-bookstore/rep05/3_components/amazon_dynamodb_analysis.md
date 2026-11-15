## Overview
An Amazon DynamoDB-backed NoSQL tier powers the catalog, search, and recommendation features of a globally distributed, multi-region online bookstore. It ensures high availability, strict regulatory compliance, and low-latency performance for millions of users worldwide.

## Key Elements
- **Catalog Table Store**: Stores book metadata, inventory counts, and categories partitioned by `BookID`.
- **Search Index Accelerator**: Maintains Global Secondary Indexes (GSIs) and DynamoDB Streams for faceted keyword/author searches and analytics.
- **Global Table Replica Manager**: Manages active-active multi-region replication across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Relationships
- Catalog Service -> Catalog Table Store: Reads/writes book details and stock levels [DynamoDB API over HTTPS via VPC Endpoint]
- Recommendation Service -> Catalog Table Store: Queries co-purchase patterns and GSI projections [DynamoDB API over HTTPS via VPC Endpoint]
- Catalog Table Store -> AWS KMS: Encrypts data at rest using Customer Managed Keys [AWS internal API]
- Catalog Table Store -> DynamoDB Streams: Emits item updates for downstream analytics [AWS internal IPC]

## Technology Stack
- **Amazon DynamoDB Standard Tables**: Chosen for sub-10ms metadata lookups and schema-less merchandising flexibility.
- **DynamoDB Global Tables**: Selected for active-active multi-region replication supporting global users.
- **AWS KMS**: Utilized for Customer Managed Keys to enforce GDPR and CCPA data protection mandates.
- **AWS PrivateLink / VPC Endpoints**: Ensures all traffic routes securely without crossing the public internet.

## Rationale
This architecture uses DynamoDB Global Tables and VPC Endpoints to achieve 99.95% availability, sub-second multi-region replication, and strict GDPR/CCPA compliance. On-demand capacity and GSIs absorb traffic spikes while delivering fast, faceted search capabilities.