## Overview
- Architectural summary for the Library Management System search service.
- Provides sub-800ms catalogue discovery with EU data residency compliance.

## Key Elements
- Search API Controller (Java / Spring WebFlux)
- Indexing Consumer (Java / Spring Kafka)
- Query Builder & Ranking Engine
- Search Data Store (OpenSearch)
- API Gateway (Nginx / Envoy)
- Message Broker (Kafka)
- Secrets Manager (HashiCorp Vault)

## Relationships
- API Gateway -> Search API Controller [HTTP/2 REST]
- Search API Controller -> Search Data Store [HTTP/JSON with Connection Pooling]
- Message Broker -> Indexing Consumer [Kafka Events]
- Indexing Consumer -> Search Data Store [Partial Document Updates]
- Search API Controller -> Secrets Manager [mTLS / Runtime Secret Injection via HashiCorp Vault]

## Technology Stack
- Java / Spring WebFlux: Asynchronous non-blocking control for low-latency queries.
- OpenSearch: Distributed EU-hosted search cluster meeting the <800ms performance SLA (R-05).
- Apache Kafka: Asynchronous event ingestion for near-real-time inventory indexing.
- HashiCorp Vault: Dynamic runtime injection of mTLS certificates and credentials.

## Rationale
- Decomposing the search container ensures high concurrency, strict EU data residency, and real-time faceted discovery.
- Robust security controls and circuit breaking guarantee resilience against resource exhaustion under academic peak loads.