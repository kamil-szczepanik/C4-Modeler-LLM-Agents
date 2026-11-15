## Overview
The Online Bookstore system is a scalable, globally-distributed e-commerce platform designed to provide catalogue browsing, secure checkout, reviews, and personalized book recommendations. It meets strict multi-region performance, availability (99.95%), and compliance (GDPR/CCPA) requirements across AWS regions.

## Key Elements
* **Frontend**: React / TypeScript Single Page Application hosted on AWS CloudFront and AWS S3
* **Edge Security**: AWS API Gateway with AWS WAF
* **Compute Layer**: Node.js and Python FastAPI microservices running on AWS ECS Fargate
* **Database Layer**: Amazon Aurora PostgreSQL Global Database spanning `us-east-1`, `eu-west-1`, and `ap-southeast-1`
* **Caching & Messaging**: Amazon ElastiCache Redis, Amazon SQS, and Amazon SNS with Dead Letter Queues
* **Security & Governance**: AWS Secrets Manager, AWS KMS, Amazon GuardDuty RDS Protection, and AWS Backup

## Relationships
* **React SPA -> AWS CloudFront**: Serves static assets globally over HTTPS [TLS 1.3]
* **AWS CloudFront -> AWS API Gateway**: Routes client API requests over HTTPS [TLS 1.3]
* **Core E-Commerce Service -> Connection & Auth Proxy Component**: Authenticates and routes database transactions over TLS 1.3 [PostgreSQL Wire Protocol]
* **Primary DB Cluster -> Secondary DB Clusters**: Replicates transactional data cross-region via dedicated AWS backbone infrastructure
* **Primary DB Cluster -> Regional Storage Subsystem**: Persists encrypted transaction logs locally using region-bound AWS KMS CMKs

## Technology Stack
* **Cloud Infrastructure**: AWS multi-region deployment (`us-east-1`, `eu-west-1`, `ap-southeast-1`) managed via Terraform/AWS CDK for reproducible environments
* **Database**: Amazon Aurora PostgreSQL Global Database for sub-10ms regional reads and automated multi-region failover
* **Security**: AWS KMS for region-bound data encryption at rest, IAM database authentication, and TLS 1.3 for all in-transit data
* **Observability & Resilience**: Amazon CloudWatch, AWS Fault Injection Simulator (FIS) for chaos engineering, and Amazon GuardDuty RDS Protection

## Rationale
This multi-region AWS architecture guarantees 99.95% uptime and sub-2-second page loads globally by bringing read replicas closer to users while centralizing writes. Strict encryption, IAM-based access control, and region-bound backups ensure full compliance with GDPR and CCPA data sovereignty mandates.