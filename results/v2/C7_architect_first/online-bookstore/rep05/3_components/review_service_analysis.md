## Overview
This architecture defines the Review Service component for the Online Bookstore, enabling secure customer reviews and 5-star ratings. It ensures high scalability, GDPR/CCPA compliance, and resilience through serverless moderation and distributed caching.

## Key Elements
- **Review API Controller**: Node.js/TypeScript Express/gRPC service handling authenticated review requests.
- **Review Data Access Component**: Node.js/TypeScript component managing persistence and cache invalidation.
- **Rating Aggregator Component**: Node.js/TypeScript component for asynchronous aggregate score recalculation.
- **Review Moderation Engine**: AWS Lambda function processing text for sentiment and compliance.
- **Data & Infrastructure**: Amazon Aurora PostgreSQL, AWS RDS Proxy, Amazon ElastiCache Redis, Amazon SQS with DLQs.

## Relationships
- **Amazon API Gateway -> Review API Controller**: Routes incoming gRPC traffic over HTTP/2 with mTLS via AWS App Mesh.
- **Review API Controller -> Order & Checkout Service**: Validates purchase history via gRPC calls.
- **Review API Controller -> Review Data Access Component**: Executes internal function calls.
- **Review Data Access Component -> Amazon ElastiCache (Redis)**: Caches queries and invalidates keys on writes/GDPR deletions.
- **Review Data Access Component -> AWS RDS Proxy**: Manages database connection pools securely.
- **AWS RDS Proxy -> Amazon Aurora PostgreSQL**: Executes JDBC/TLS over TCP queries with KMS encryption.
- **Review Moderation Engine -> Amazon SQS**: Processes moderation tasks asynchronously.

## Technology Stack
- **Node.js/TypeScript (Express/gRPC)**: Core runtime for review microservices ensuring rapid request handling.
- **AWS Lambda**: Serverless execution for moderation to handle load spikes without idle infrastructure cost.
- **Amazon Aurora PostgreSQL with AWS RDS Proxy**: Relational data store with connection pooling for high concurrency.
- **Amazon ElastiCache (Redis)**: In-memory cache to guarantee sub-second read performance.
- **AWS App Mesh & TLS 1.3**: Secures service-to-service communication with mTLS.

## Rationale
This architecture achieves 99.95% uptime and sub-2-second page loads by decoupling read-heavy workloads through Redis caching and serverless moderation. Strict JWT validation, rate limiting, and KMS encryption fulfill stringent GDPR/CCPA and OWASP security constraints.