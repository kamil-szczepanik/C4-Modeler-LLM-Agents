## Overview
This architecture defines the Catalog & Search container for the Online Bookstore, handling high-performance keyword search and product metadata management. It ensures sub-2-second page loads for 1M MAU while maintaining strict GDPR/CCPA compliance across three global AWS regions.

## Key Elements
- **Catalog API Controller**: Spring MVC component exposing endpoints for browsing and metadata retrieval.
- **Search Engine Service**: Spring Data component handling fuzzy matching and auto-complete via Amazon OpenSearch.
- **Product Metadata Repository**: Spring Data JPA component managing book details and inventory via PostgreSQL.
- **Review & Rating Aggregator**: Spring service for aggregating customer ratings.
- **Catalog Management Service**: Spring service processing admin-initiated updates.
- **Sync & Resilience Pipeline**: Debezium with AWS MSK (Kafka) for asynchronous Change Data Capture.

## Relationships
- API Gateway -> Catalog API Controller: Routes inbound requests [gRPC over mTLS via AWS App Mesh]
- Search Engine Service -> Amazon OpenSearch: Queries indices [HTTPS / REST]
- Product Metadata Repository -> PostgreSQL: Reads/Writes transactional data [JDBC / TCP]
- Catalog Management Service -> AWS MSK / Kafka: Publishes catalog change events [TCP]

## Technology Stack
- **Spring Boot**: Core framework for microservice components due to enterprise robustness.
- **Amazon OpenSearch**: Search engine selected for sub-second fuzzy matching and auto-complete.
- **PostgreSQL**: Relational database chosen for ACID-compliant transactional data integrity.
- **AWS MSK (Kafka) & Debezium**: Event streaming and CDC selected for decoupled, resilient data synchronization.
- **Terraform & ArgoCD**: Infrastructure-as-Code and GitOps for multi-region consistency across `us-east-1`, `eu-west-1`, and `ap-southeast-1`.

## Rationale
Decoupling the administrative write path from the buyer read path prevents bulk publisher updates from degrading storefront performance. Asynchronous CDC replication ensures high availability (99.95%) and low-latency global search capabilities.