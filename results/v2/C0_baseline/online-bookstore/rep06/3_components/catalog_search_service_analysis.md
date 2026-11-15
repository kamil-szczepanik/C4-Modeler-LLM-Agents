## Overview
- The Catalog & Search Service is a containerized microservice that powers high-speed, typo-tolerant book discovery, faceted browsing, and keyword search.
- It delivers sub-2-second search responses for 1M MAU while enforcing strict security, GDPR/CCPA compliance, and 99.95% availability.

## Key Elements
- **Search & Browse Router**: Node.js/Go component handling gRPC input validation and sanitization.
- **OpenSearch Query Builder**: Component translating domain queries into AWS OpenSearch DSL.
- **Ingestion & Indexing Worker**: Component consuming event bus updates for bulk index synchronization.
- **AWS OpenSearch**: Managed search index storing denormalized documents with localized pricing.
- **AWS RDS PostgreSQL**: Primary relational database for catalogue persistence.
- **AWS EventBridge / SQS**: Messaging infrastructure with Dead Letter Queues for sync events.
- **AWS Secrets Manager**: Secure injection of database and search credentials.

## Relationships
- API Gateway -> Search & Browse Router: Routes catalogue queries via gRPC over HTTP/2 with mTLS.
- Search & Browse Router -> OpenSearch Query Builder: Delegates parsed queries via in-memory function calls.
- OpenSearch Query Builder -> AWS OpenSearch: Executes search queries via HTTPS/TCP.
- Ingestion & Indexing Worker -> AWS OpenSearch: Bulk updates index documents via HTTPS/TCP.
- Event Bus -> Ingestion & Indexing Worker: Consumes catalogue change events via HTTPS.

## Technology Stack
- **Node.js/Go**: Chosen for high-throughput, low-latency gRPC request handling.
- **AWS OpenSearch**: Selected for scalable, typo-tolerant full-text search and faceted filtering.
- **AWS ECS Fargate**: Provides serverless container orchestration with horizontal autoscaling.
- **AWS Secrets Manager**: Ensures secure credential storage without plain-text exposure.

## Rationale
- Denormalizing localized prices directly into AWS OpenSearch eliminates runtime inter-service calls, ensuring sub-2-second performance.
- Private subnet isolation, IAM RBAC, and AWS KMS encryption meet strict security, GDPR/CCPA compliance, and uptime requirements.