## Overview
The Online Bookstore Catalog & Search container provides scalable product browsing, keyword search, and real-time synchronization to support 1 million monthly active users. It processes high-volume read queries securely while maintaining sub-2-second page loads.

## Key Elements
*   **Catalog API Controller**: Node.js / Express component handling incoming HTTP browsing and filtering requests.
*   **Search Service Engine**: Node.js / TypeScript component executing sanitized domain queries.
*   **Caching Layer**: Amazon ElastiCache / Redis caching frequent queries and catalog metadata.
*   **Catalog Synchronization Consumer**: Node.js component processing asynchronous inventory and price updates.
*   **Amazon OpenSearch**: Managed search engine indexing catalog data.
*   **Amazon SQS / SNS**: Message bus for asynchronous event distribution.

## Relationships
*   **Catalog API Controller -> Caching Layer**: Internal Redis protocol via TCP
*   **Caching Layer -> Search Service Engine**: Fallback on cache miss via internal function calls
*   **Catalog API Controller -> Search Service Engine**: Internal function calls / gRPC
*   **Search Service Engine -> Amazon OpenSearch**: REST/HTTPS queries over TLS 1.3
*   **Message Bus -> Catalog Synchronization Consumer**: AMQP/HTTPS event consumption with payload signing (HMAC)
*   **Catalog Synchronization Consumer -> Caching Layer**: Redis pub/sub for event-driven cache invalidation

## Technology Stack
*   **Node.js / Express & TypeScript**: Core runtime for lightweight, high-throughput component execution.
*   **Amazon OpenSearch**: Scalable search engine chosen for full-text keyword search and fast filtering.
*   **Amazon ElastiCache (Redis):** In-memory cache implementing volatile-lru eviction to minimize search latency and offload OpenSearch.
*   **AWS IAM & AWS Secrets Manager:** Used for least-privilege task roles and secure Redis AUTH token rotation.

## Rationale
The component architecture uses Redis caching and OpenSearch separation to achieve high scalability and sub-2-second page loads for 1 million MAU. Security controls including TLS 1.3, IAM least-privilege, and input sanitization enforce OWASP Top-10 compliance.