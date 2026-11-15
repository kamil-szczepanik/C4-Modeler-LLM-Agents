## Overview
## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The architecture enforces strict EU-only data residency and sub-second search responses.

## Key Elements
- **Catalogue Management Component**: Spring Data JPA / PostgreSQL service for item CRUD operations.
- **Search Query Component**: High-level REST client service executing low-latency searches against Elasticsearch.
- **Search Indexer Component**: Spring Kafka consumer handling asynchronous event synchronization with a Dead-Letter Queue (DLQ).
- **Apache Kafka (AWS MSK)**: Event streaming backbone deployed in Frankfurt (`eu-central-1`).
- **PostgreSQL & Elasticsearch**: Primary datastores encrypted with AWS KMS keys.

## Relationships
- API Gateway -> Catalogue Management Component: [gRPC with mTLS and JWT claims]
- API Gateway -> Search Query Component: [gRPC with mTLS]
- Search Indexer Component -> Apache Kafka (AWS MSK): Consumes domain events [Avro over mTLS with DLQ]
- Search Query Component -> Elasticsearch: Executes search queries [Internal VPC TCP with TLS 1.3]
- Catalogue Management Component -> Database: Reads/writes relational data [JDBC over Internal VPC TCP with TLS 1.3]

## Technology Stack
- **Java / Spring Boot**: Enterprise-grade framework for core service components.
- **Elasticsearch (Amazon OpenSearch)**: Delivers 99th-percentile search response < 800 ms.
- **Apache Kafka (AWS MSK)**: Asynchronous event messaging and item synchronization.
- **OpenTelemetry & Resilience4j**: Distributed tracing and circuit breaking for fault tolerance.
- **AWS Frankfurt (eu-central-1)**: Region enforcing EU-only data residency and KMS encryption.

## Rationale
Component decomposition isolates resource-intensive search queries from transactional catalog mutations to meet strict performance SLAs. Regional deployment in Frankfurt, TLS 1.3, and AWS KMS ensure compliance with EU data residency mandates.