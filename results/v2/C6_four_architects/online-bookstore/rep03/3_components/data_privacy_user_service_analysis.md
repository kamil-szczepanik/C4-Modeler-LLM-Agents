## Overview
The Online Bookstore system is a scalable e-commerce platform for purchasing physical and electronic books, featuring reviews and recommendations. The architecture ensures high availability, security, and global compliance for 1 million monthly active users.

## Key Elements
*   **Clients**: Customer, Store Administrator
*   **Edge & Gateway**: AWS CloudFront/Route 53, Amazon API Gateway
*   **Core Services**: Data Privacy & User Service (Python/FastAPI), Catalog & Search Service, Order & Checkout Service, Payment & Currency Service, Recommendation & Review Service, Admin & Content Management Service, Async Worker Service
*   Data Privacy Components: UserController, GDPRComplianceEngine, UserRepository, ConsentManager, DataEncryptionService, AuditLogger, AuthTokenVerifier, DataRetentionEnforcer, UserProfileCacheManager
*   **Databases & Storage**: Amazon RDS (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon OpenSearch, Amazon S3
*   **Messaging & Integration**: Amazon EventBridge & SQS, Stripe/PayPal, UPS/FedEx, Avalara, AWS SES/SNS, AWS Personalize, AWS Fraud Detector, AWS KMS

## Relationships
*   `Amazon API Gateway` -> `UserController` [gRPC / HTTPS over TLS]
*   `UserController` -> `AuthTokenVerifier` [In-process]
*   `UserRepository` -> `Amazon RDS (PostgreSQL)` [SQL / TCP]
*   `UserRepository` -> `AWS KMS` [AWS SDK / HTTPS]
*   `GDPRComplianceEngine` -> `Amazon EventBridge & SQS` [AMQP]
*   `GDPRComplianceEngine` -> `Amazon S3` [HTTPS]
*   `AuditLogger` -> `Amazon DynamoDB` [AWS SDK / HTTPS]
*   `UserProfileCacheManager` -> `Amazon ElastiCache (Redis)` [RESP / TCP]

## Technology Stack
*   **Python / FastAPI**: Core language and framework for the Data Privacy & User Service due to rich ecosystem.
*   **Amazon RDS (PostgreSQL)**: Relational database for transactional user records.
*   **Amazon DynamoDB**: NoSQL store for immutable audit logs and consent trails.
*   **Amazon ElastiCache (Redis)**: In-memory cache for high-performance non-sensitive profile reads.
*   **AWS KMS**: Field-level encryption for PII compliance.

## Rationale
The architecture combines microservices with managed AWS infrastructure to guarantee 99.95% uptime and sub-second performance. Strict data segregation and encryption mechanisms ensure complete GDPR and CCPA compliance.