## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The Catalogue Service specifically manages physical and digital item cataloguing and search functionalities while enforcing strict EU-only data residency.

## Key Elements
- Library Patrons (Members), Librarians / Circulation Staff, Library Administrators
- External Identity Provider (IdP), Third-Party Payment Gateway, Digital Content Repositories
- Patron Portal (React.js SPA), Librarian Back-office (Next.js Web App)
- API Gateway (NGINX / Envoy)
- Catalogue Service (Java / Spring Boot) containing:
  - Item Controller & Service
  - Search & Indexing Engine
  - Facet & Recommendation Service
  - Digital Content Adapter
  - Event Publisher
- Circulation Service (Node.js / Express)
- Event Broker (Apache Kafka / RabbitMQ)
- PostgreSQL Database (EU-hosted)
- Elasticsearch (Elasticsearch EU-hosted)

## Relationships
- API Gateway -> Catalogue Service: Routes catalogue queries via mTLS using Istio Service Mesh
- Item Controller & Service -> PostgreSQL Database: Reads and writes catalogue data using Spring Data JPA and JDBC with AES-256 encryption
- Search & Indexing Engine & Facet & Recommendation Service -> Elasticsearch: Indexes search data and powers faceted navigation using Spring Data Elasticsearch and Elasticsearch Aggregations API with AES-256 encryption
- Event Publisher -> Event Broker: Publishes domain events via Spring Cloud Stream over TLS
- Digital Content Adapter -> Digital Content Repositories: Fulfills digital items using Spring WebClient over REST/LTI with Resilience4j circuit breakers

## Technology Stack
- Java / Spring Boot: Core runtime for the Catalogue Service providing robust enterprise capabilities
- PostgreSQL: Authoritative relational storage for item metadata secured with AES-256 encryption
- Elasticsearch: High-performance search and aggregation engine ensuring sub-800ms search responses (R-05)
- Spring Data JPA / Spring Data Elasticsearch: Data access layers for relational and search databases
- Resilience4j: Circuit breaker implementation for fault-tolerant external digital repository integrations
- Istio Service Mesh: Secures internal routing with mTLS

## Rationale
This architecture uses a dual-write pattern combining PostgreSQL for authoritative storage and Elasticsearch for high-performance search to meet the strict sub-800ms response time requirement. Furthermore, it enforces EU-only data residency and strict security controls, including AES-256 encryption, OAuth2/JWT RBAC, and PII-free event publishing.