## Overview
- The system is the Reviews & Ratings Container within the Online Bookstore, enabling customer reviews, 5-star ratings, author engagement, and content moderation.
- Its core purpose is to drive user-generated content, trust, and conversion rates while maintaining strict scalability, performance, and compliance standards.

## Key Elements
- **Reviews & Ratings Container**: AWS ECS / EKS microservice managing reviews, ratings, badges, and author responses.
- **Data Persistence**: Amazon Aurora PostgreSQL with Read Replicas and AWS KMS (AES-256) encryption.
- **Caching Layer**: Amazon ElastiCache Redis for vote deduplication, caching top reviews, and badges.
- **Messaging & Queueing**: Amazon SQS for asynchronous moderation and batch write-backs.
- **Observability & Auditing**: AWS CloudWatch and OpenTelemetry.

## Relationships
- **API Gateway Container -> Reviews & Ratings Container**: Routes HTTP/REST requests via service mesh using mTLS (AWS App Mesh).
- **Reviews & Ratings Container -> Amazon Aurora PostgreSQL**: Executes transactional reads/writes via JDBC/TLS.
- **Reviews & Ratings Container -> Amazon ElastiCache Redis**: Handles write-through caching and vote deduplication via RESP protocol.
- **Reviews & Ratings Container -> Amazon SQS**: Offloads asynchronous moderation events and batch vote persistence.
- **Reviews & Ratings Container -> AWS CloudWatch**: Streams operational logs, metrics, and immutable audit trails.

## Technology Stack
- **Compute**: AWS ECS / EKS for scalable container orchestration supporting 1M MAU.
- **Database**: Amazon Aurora PostgreSQL with Read Replicas for isolated query workloads and high availability.
- **Cache**: Amazon ElastiCache Redis for low-latency read caching and vote fraud prevention.
- **Messaging**: Amazon SQS for asynchronous moderation and decoupled database writes.
- **Security & Compliance**: AWS KMS, TLS 1.3, and JWT validation via IAM Identity Center for OWASP and GDPR/CCPA compliance.

## Rationale
- This architecture combines read-heavy caching with asynchronous write processing to sustain 99.95% uptime and <2s page loads under peak traffic.
- Dedicated read replicas, strict RBAC, and automated data erasure ensure robust security, scalability, and GDPR/CCPA compliance.