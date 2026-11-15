## Overview
This architecture defines the internal components of the Amazon Aurora PostgreSQL container for the Online Bookstore, ensuring multi-region transactional integrity, scalability, and GDPR/CCPA compliance. It supports high availability across three AWS regions (`us-east-1`, `eu-west-1`, `ap-southeast-1`) while handling 1 million monthly active users.

## Key Elements
- Aurora PostgreSQL Writer Instance (Node)
- Aurora PostgreSQL Reader Instances (Replica Nodes)
- Aurora Storage Volume (Distributed Shared Storage with Aurora Global Databases)
- Row-Level Security (RLS) & Encryption Module
- Connection Pooler (PgBouncer integration)
- Logical Replication & CDC Engine
- Aurora Reader/Writer Endpoint Router

## Relationships
- Order & Checkout Service -> Aurora Reader/Writer Endpoint Router [Native Database Protocol / TCP over VPC]
- Catalog & Search Service -> Aurora Reader/Writer Endpoint Router [Native Database Protocol / TCP over VPC]
- Aurora Reader/Writer Endpoint Router -> Writer Instance & Reader Instances [TCP]
- Writer Instance -> Aurora Storage Volume [Distributed Storage Volume Protocol]
- Logical Replication & CDC Engine -> Amazon EventBridge / SQS [HTTPS / AWS SDK]
- Row-Level Security & Encryption Module -> AWS KMS [HTTPS / AWS API]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for managed multi-region relational persistence and high availability.
- PgBouncer: Provides connection pooling to prevent exhaustion during traffic spikes.
- Aurora Global Databases: Enables low-latency cross-region replication for global scalability.
- AWS KMS: Secures data at rest via envelope encryption for compliance.

## Rationale
This component architecture guarantees 99.95% uptime and sub-second multi-region replication through distributed storage and dedicated read/write routing. It satisfies strict GDPR/CCPA regulations via integrated row-level security and AWS KMS encryption.