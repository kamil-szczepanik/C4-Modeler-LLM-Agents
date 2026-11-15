## Overview
- An AWS-hosted multi-region online bookstore providing catalogue browsing, secure checkout, reviews, and recommendations.
- Built to handle 1 million monthly active users with sub-second performance and high availability.

## Key Elements
- **Catalogue Service** (Node.js / Express): Manages catalogue data and keyword search.
- **Catalogue API Router** (Express Router): Handles incoming REST endpoints.
- **Search Component** (Node.js / OpenSearch SDK): Executes low-latency queries.
- **Inventory & Pricing Component** (Node.js / Sequelize ORM): Manages relational book data.
- **Catalogue Sync Worker** (Node.js background process): Synchronizes updates.
- **Amazon Aurora PostgreSQL** (Amazon Aurora PostgreSQL): Relational data store.
- **Amazon OpenSearch** (Amazon OpenSearch): Search engine.
- **Amazon SQS** (Amazon SQS): Event queue for synchronization.

## Relationships
- Catalogue API Router -> Search Component [In-Process Function Call]
- Catalogue API Router -> Inventory & Pricing Component [In-Process Function Call with JWT validation]
- Search Component -> Amazon OpenSearch [TLS/TCP]
- Inventory & Pricing Component -> Amazon Aurora PostgreSQL [TLS/TCP]
- Catalogue Sync Worker -> Amazon OpenSearch [TLS/TCP using bulk ingestion APIs]
- Catalogue Sync Worker -> Amazon SQS [HTTPS]

## Technology Stack
- **Node.js / Express**: Core runtime for Catalogue Service for fast asynchronous I/O.
- **Amazon OpenSearch**: Offloads keyword search to ensure sub-second response times.
- **Amazon Aurora PostgreSQL**: Multi-region relational storage for durable persistence.
- **Amazon SQS**: Asynchronous event queue for reliable change data capture ingestion.
- **AWS Secrets Manager**: Dynamic credential retrieval for security compliance.

## Rationale
- Decomposing the catalogue service protects database performance and ensures sub-second search under heavy load.
- Asynchronous synchronization guarantees eventual consistency and high availability across distributed multi-region infrastructure.