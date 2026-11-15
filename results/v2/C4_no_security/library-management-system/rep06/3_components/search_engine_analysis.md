## Overview
The Search Engine container provides high-performance, real-time catalogue discovery for library patrons and staff. It ensures sub-800ms response times for complex queries while maintaining strict EU-only data residency.

## Key Elements
- Library Patrons and Library Staff (Users)
- Core API Application (Spring Boot / Java)
- Search Engine (OpenSearch)
- Message Broker (Kafka)
- APM and Synthetic Monitoring Tool / Centralized Log Aggregator
- Components: Search API & Routing Component, Query Execution & Scoring Engine, Index Management & Ingestion Component, Cluster Coordination & Storage Nodes

## Relationships
- Core API Application -> Search Engine: Executes catalogue searches via REST/gRPC over TLS
- Message Broker (Kafka) -> Index Management & Ingestion Component: Pushes real-time item catalogue updates via Kafka Protocol over TLS
- Search Engine -> APM / Log Aggregator: Exports telemetry, JVM metrics, and audit logs
- Search Engine -> EU-Region Object Storage: Performs automated snapshots for disaster recovery

## Technology Stack
- OpenSearch: Primary search and indexing technology for full-text search, fuzzy matching, faceting, and custom synonyms
- Kafka: Asynchronous message broker for decoupling ingestion from query execution
- REST over TLS / gRPC: Secure communication protocols for API routing and ingestion
- EU Cloud Managed Storage: Enforces EU-only data residency and encryption

## Rationale
Isolating OpenSearch with dedicated query and ingestion components guarantees the <800ms latency requirement (R-05) during peak loads. Asynchronous Kafka ingestion protects search performance from heavy bulk catalogue updates while satisfying EU data constraints.