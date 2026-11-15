## Overview
The Library Management System is a cloud-native platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It is deployed strictly within EU data centers to meet data residency constraints.

## Key Elements
- **Library Patron**: End-user accessing self-service portals.
- **Librarian / Staff**: Internal user managing cataloging and circulation.
- **Library Management System**: Core platform comprising Web Frontend, API Gateway, and Core Services.
- **Web Frontend**: React and TypeScript Single-Page Application.
- **API Gateway**: Spring Cloud Gateway.
- **Core Services**: Domain-driven Spring Boot microservices (Catalog, Circulation, User Management).
- **Primary Database**: PostgreSQL 16 with PgBouncer.
- **Search Index**: Elasticsearch / OpenSearch cluster.
- **Cache Layer**: Redis in-memory data store.
- **Message Broker**: Apache Kafka.
- **External Systems**: Stripe EU (Payment Gateway), SendGrid EU (Notification Service), EU Identity Provider (OIDC/Keycloak/Auth0), National Library Registry, and Interlibrary Loan (ILL) Network.

## Relationships
- **Patron / Librarian -> Web Frontend**: Accesses UI via HTTPS/TLS 1.3.
- **Web Frontend -> API Gateway**: Routes requests via HTTPS.
- **API Gateway -> Core Services**: Forwards internal requests via REST/gRPC.
- **Core Services -> Primary Database**: Persists relational data via JDBC/TCP.
- **Core Services -> Search Index**: Queries catalog metadata via REST/TCP.
- **Core Services -> Cache Layer**: Reads/writes hot-spot data via RESP/TCP.
- **Core Services -> Message Broker**: Publishes asynchronous events via Kafka protocol.
- **Library Management System -> External Systems**: Integrates with Stripe (REST/HTTPS), SendGrid (REST/HTTPS), National Registry (OAI-PMH), IdP (OIDC/HTTPS), and ILL Network (ISO 18626/HTTPS).

## Technology Stack
- **Java 21 & Spring Boot**: Core language and framework for robust backend microservices.
- **React & TypeScript**: Modern frontend technology for responsive patron and staff UIs.
- **PostgreSQL 16**: Relational storage ensuring ACID compliance for circulation data.
- **Elasticsearch / OpenSearch**: Dedicated search cluster meeting the <800ms 99th-percentile search performance requirement.
- **Redis**: Low-latency caching for sessions and frequent catalog reads.
- **Apache Kafka**: Asynchronous event-driven decoupling for notifications and audit logs.

## Rationale
The microservices architecture with a dedicated search index and cache layer ensures high performance, meeting the strict search latency requirement. Strictly pinning all cloud components, databases, and third-party SaaS integrations to EU regions satisfies the mandatory data residency constraint.