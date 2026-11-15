## Overview
[Component architecture for the Analytics & Reporting Service of the Library Management System, providing real-time operational widgets and compliant batch reports for administrators and librarians.]

## Key Elements
* Analytics & Reporting Service (Spring Boot Container)
* Report Query Engine (`Spring Data JPA / ClickHouse JDBC`)
* Data Anonymization Module (`Java`)
* Export Scheduler (`Spring Scheduler / Apache POI & OpenCSV`)
* Analytics REST Controller (`Spring MVC`)
* Dashboard Widget Provider (`Spring MVC / REST`)
* Query Caching Layer (`Spring Cache / Caffeine`)
* Managed Databases (`ClickHouse`)

## Relationships
* API Gateway -> Analytics REST Controller: Routes reporting requests [gRPC and internal REST, mTLS]
* Analytics REST Controller -> Report Query Engine & Dashboard Widget Provider: Delegates queries [In-process]
* Dashboard Widget Provider -> Query Caching Layer: Checks/stores aggregated metrics [In-process]
* Query Caching Layer -> Report Query Engine: Fallback for cache misses [In-process]
* Report Query Engine -> Managed Databases (ClickHouse): Executes analytical queries [TCP / Native Protocol, TLS]

## Technology Stack
* Spring Boot: Core container framework for REST APIs and scheduling
* ClickHouse: High-performance columnar database for analytics and reporting
* Spring Cache / Caffeine: In-memory caching layer for real-time dashboard widgets
* Apache POI & OpenCSV: Asynchronous generation of CSV and PDF report exports
* OpenTelemetry: Metrics and distributed tracing for observability

## Rationale
[This component-level architecture safely isolates resource-heavy analytical queries from real-time operational workflows while enforcing strict GDPR data anonymization and RBAC controls. The addition of an in-memory caching layer protects the ClickHouse database from high-volume dashboard polling within EU data residency constraints.]