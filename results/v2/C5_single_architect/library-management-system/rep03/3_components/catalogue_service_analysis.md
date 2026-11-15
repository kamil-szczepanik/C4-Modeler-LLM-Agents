## Overview
The Catalogue Service is a core container of the Library Management System, responsible for cataloging physical and digital items for public and academic libraries. It provides high-performance search capabilities and strict EU-only data residency compliance.

## Key Elements
- **Catalogue Controller**: (Spring MVC) Exposes endpoints and translates gRPC requests.
- **Item Management Service**: (Spring Service) Encapsulates core cataloging business logic.
- **Search Indexing Service**: (Spring Service) Manages dual-write synchronization and query building.
- **Catalogue Repository**: (Spring Data JPA) Handles transactional persistence.
- **Digital Asset Adapter**: (Spring Component) Integrates with external content providers.
- **PostgreSQL**: Primary data store for item metadata.
- **Elasticsearch**: Search index engine for fast querying.
- **API Gateway**: Routes incoming traffic.
- **Digital Content Provider**: External system for digital assets.

## Relationships
- **API Gateway** -> **Catalogue Controller**: Routes catalog requests [gRPC over TLS]
- **Catalogue Controller** -> **Item Management Service**: Method calls [In-process]
- **Item Management Service** -> **Catalogue Repository**: JPA/Hibernate [JDBC over TCP]
- **Item Management Service** -> **Search Indexing Service**: Spring Application Events [In-process]
- **Item Management Service** -> **Digital Asset Adapter**: Method calls [In-process]
- **Search Indexing Service** -> **Elasticsearch**: Jest/Spring Data Elasticsearch [TCP]
- **Catalogue Repository** -> **PostgreSQL**: Reads and writes data [JDBC over TCP]
- **Digital Asset Adapter** -> **Digital Content Provider**: Imports metadata [REST/HTTPS over TLS]

## Technology Stack
- **Java / Spring Boot**: Core framework for robust, enterprise-grade microservices.
- **Spring MVC**: Exposes robust controller endpoints.
- **Spring Data JPA**: Simplifies relational database persistence and ACID transactions.
- **Elasticsearch**: Delivers sub-800ms 99th-percentile search performance (R-05).
- **PostgreSQL**: Ensures reliable, ACID-compliant metadata storage within EU boundaries.

## Rationale
This component architecture cleanly separates metadata ingestion, core catalog logic, and search indexing to meet demanding performance SLAs. Localized database and search clusters enforce the strict EU data residency constraint.