## Overview
- Online Bookstore is a cloud-native e-commerce platform providing catalog browsing, secure multi-currency checkout, recommendations, and reviews.
- It delivers high scalability, global performance, and compliance for 1 million Monthly Active Users (MAU).

## Key Elements
- Database Container: Amazon Aurora PostgreSQL with multi-AZ, read replicas, and Aurora Global Databases.
- Catalog Schema Component: Relational tables with GiST/GIN indexes for books, authors, and categories.
- Order & Transactions Schema Component: ACID-compliant tables for carts, orders, and multi-currency pricing with TTL cleanup.
- Reviews & Recommendations Schema Component: Tables for user ratings and review texts.
- Audit & Compliance Component: Row-level security (RLS) and automated anonymization functions.
- Supporting Infrastructure: Amazon RDS Proxy and AWS Database Activity Streams.

## Relationships
- Catalog & Search Service -> Database: Reads and writes catalog data [PostgreSQL Protocol over TLS]
- Order & Checkout Service -> Database: Reads and writes order data [PostgreSQL Protocol over TLS]
- Recommendation & Review Service -> Database: Reads and writes review and recommendation data [PostgreSQL Protocol over TLS]
- Async Notification Service -> Database: Persists notification state [PostgreSQL Protocol over TLS]
- Database -> Amazon Kinesis: Streams audit logs for compliance [AWS Kinesis Protocol]

## Technology Stack
- Amazon Aurora PostgreSQL: Chosen for ACID compliance, multi-AZ high availability, and global replication.
- Aurora Global Databases: Deployed across `us-east-1`, `eu-west-1`, and `ap-southeast-1` to guarantee sub-2-second global page loads.
- Amazon RDS Proxy: Implemented to prevent connection exhaustion and mitigate thread exhaustion under high traffic.
- AWS KMS: Provides storage-level encryption with customer-managed keys for GDPR/CCPA compliance.
- PostgreSQL GiST/GIN Indexes: Speeds up keyword searches and catalogue queries.

## Rationale
- This architecture scales horizontally across multiple regions to support 1 million MAU with 99.95% uptime and sub-2-second page loads.
- It enforces strict security, encryption, and automated anonymization controls to meet GDPR and CCPA regulatory mandates.