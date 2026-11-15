## Overview
The system is an Amazon-style online bookstore designed to provide secure browsing, purchasing, reviews, and recommendations. The architecture leverages AWS-managed services to support high concurrency, multi-region availability, and strict compliance.

## Key Elements
- **Users**: Customers and Store Administrators
- **Frontend Container**: React SPA via AWS CloudFront and S3
- **API Gateway**: AWS API Gateway
- **Core Services**: Core E-Commerce, Recommendation Engine, Audit & Compliance, Integration, and Search & Analytics Services (Node.js/Python on Amazon ECS Fargate)
- **Data & Caching Containers**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch Service
- **Messaging & Eventing**: Amazon EventBridge, Amazon SQS/SNS, AWS Lambda
- **Database Components**: Relational Database Engine, Aurora Storage Volume, Read Replica Endpoint, Aurora Global Database Extension, PostgreSQL Audit (`pgaudit`), Connection Pooler (RDS Proxy), and Automated Backup Subsystem

## Relationships
- **React SPA -> AWS API Gateway**: HTTPS / WSS
- **AWS API Gateway -> ECS Fargate Services**: HTTP/gRPC via internal VPC
- **Core E-Commerce Service -> Connection Pooler (RDS Proxy)**: TCP/IP via TLS (PostgreSQL wire protocol)
- **Audit & Compliance Service -> Connection Pooler (RDS Proxy)**: TCP/IP via TLS
- **Connection Pooler -> Relational Database Engine**: Multiplexed TCP/IP via TLS
- **Aurora Global Database Extension -> Secondary Region Storage**: Asynchronous replication across AWS regions
- **Relational Database Engine -> Automated Backup Subsystem**: WAL streaming to Amazon S3

## Technology Stack
- **Frontend**: React, AWS CloudFront, Amazon S3 for global static content delivery
- **Compute**: Amazon ECS Fargate for serverless container orchestration
- **Primary Database**: Amazon Aurora PostgreSQL (PostgreSQL 15+) for ACID compliance and global replication
- **Caching & Search**: Amazon ElastiCache (Redis) for session management; Amazon OpenSearch Service for catalog search
- **Messaging**: Amazon EventBridge, SQS, and SNS for decoupled event-driven integration

## Rationale
This architecture ensures 99.95% uptime and scales horizontally to handle 1M MAU using ECS Fargate and Aurora Global Databases across multi-region AWS deployments. It meets GDPR and CCPA constraints via `pgaudit` extensions and robust encryption protocols.