## Overview
The Online Bookstore system is a scalable e-commerce platform built to handle high-volume browsing, secure checkouts, and multi-region operations. It ensures ACID compliance, high availability, and strict GDPR/CCPA data privacy compliance across global markets.

## Key Elements
- **Primary DB Instance**: Handles write operations for orders and catalog updates.
- **Aurora Replicas (Read-Scale)**: 1-15 read-only nodes distributed across availability zones.
- **Amazon RDS Proxy**: Connection pooler intercepting requests from microservices.
- **Aurora Global Database Cluster**: Asynchronous cross-region replication layer across *us-east-1*, *eu-west-1*, and *ap-southeast-1*.
- **AWS Secrets Manager**: Manages and rotates database credentials.
- **AWS Backup**: Automated backup and retention policy manager.

## Relationships
- **Order & Checkout Service** -> **Amazon RDS Proxy**: Connects to proxy endpoint via [JDBC / TCP].
- **Catalog & Search Service** -> **Amazon RDS Proxy**: Connects to proxy endpoint via [JDBC / TCP].
- **Amazon RDS Proxy** -> **Primary DB Instance / Aurora Replicas**: Routes queries using [PostgreSQL Wire Protocol].
- **Primary DB Instance** -> **Aurora Global Database Cluster**: Performs cross-region storage replication via [AWS Aurora Storage Protocol].

## Technology Stack
- **Amazon Aurora PostgreSQL**: Selected for strict ACID compliance and high availability.
- **Amazon RDS Proxy**: Deployed to prevent connection exhaustion and accelerate failover.
- **Aurora Global Databases**: Implemented for low-latency multi-region reads and disaster recovery.
- **AWS Secrets Manager**: Integrated for credential rotation to meet OWASP NFRs.
- **AWS Backup**: Configured for 35-day retention supporting GDPR/CCPA compliance.

## Rationale
This architecture guarantees 99.95% uptime and handles 1M MAU through read-replica scaling and connection pooling. Furthermore, multi-region replication and Row-Level Security fulfill strict performance, scalability, and regulatory constraints.