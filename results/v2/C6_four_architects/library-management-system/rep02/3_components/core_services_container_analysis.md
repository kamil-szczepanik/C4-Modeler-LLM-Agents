## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals while strictly enforcing EU data residency. The architecture leverages a modular Java/Spring Boot core services container backed by cloud-native infrastructure.

## Key Elements
- **Core Services Container**: Java / Spring Boot container housing domain logic.
- **CatalogueComponent**: Spring Data JPA component managing physical and digital items (R-01).
- **CirculationComponent**: Component handling lending and circulation workflows.
- **SearchSyncComponent**: Spring Event Listener synchronizing search indexes.
- **CacheManagerComponent**: Spring Data Redis component for metadata caching.
- **DigitalAssetComponent**: Component managing digital asset references and storage URLs.
- **IdentityAdapter**: Spring Security OAuth2 Client for JWT validation.
- **PaymentAdapter**: Spring Cloud OpenFeign adapter for Stripe EU.
- **NotificationAdapter**: Adapter for SendGrid EU notifications.
- **IllNetworkAdapter**: Spring RestClient for Interlibrary Loan Network.
- **Apache Kafka EU-hosted**: Central event broker replacing RabbitMQ.
- **Database Container**: PostgreSQL EU region.
- **Search Service Container**: Elasticsearch / OpenSearch.
- **Redis Cache Container**: Redis caching layer.

## Relationships
- `API Gateway Container` -> `IdentityAdapter`: Forwards requests with bearer tokens [gRPC]
- `API Gateway Container` -> `CatalogueComponent`: Forwards validated requests [gRPC]
- `CatalogueComponent` -> `Database Container`: Executes queries [SQL over TCP]
- `CatalogueComponent` -> `CacheManagerComponent`: Reads/writes cache [RESP over TCP]
- `CacheManagerComponent` -> `Redis Cache Container`: Executes caching commands [RESP over TCP]
- `SearchSyncComponent` -> `Search Service Container`: Updates indexes [HTTP/REST over TLS]
- `CatalogueComponent` -> `Event Broker Container`: Publishes domain events [Kafka Protocol over TLS]
- `DigitalAssetComponent` -> `Digital Asset Storage Container`: Requests pre-signed URLs [HTTPS/REST S3 API]
- `PaymentAdapter` -> `Stripe EU`: Processes fines [HTTPS/REST]
- `NotificationAdapter` -> `SendGrid EU`: Sends alerts [HTTPS/REST]
- `CirculationComponent` -> `IllNetworkAdapter`: Coordinates loans [HTTPS/REST]

## Technology Stack
- **Java / Spring Boot**: Core enterprise framework for transaction boundaries and dependency injection.
- **Spring Data JPA**: Simplifies database persistence for cataloguing and circulation.
- **Apache Kafka**: Single unified event broker and asynchronous task router (eliminating RabbitMQ to prevent sprawl).
- **PostgreSQL**: Relational database ensuring strict EU data residency.
- **Redis**: In-memory caching layer to meet sub-800ms search and retrieval performance goals (R-05).
- **Spring Cloud OpenFeign**: Declarative REST client for external service integration.

## Rationale
This architecture balances strict EU data residency compliance with high performance by consolidating messaging onto Apache Kafka and utilizing Redis caching to achieve sub-800ms search responses (R-05). The modular Spring component design cleanly separates domain logic, infrastructure concerns, and external adapters for maintainability.