## Overview
The Library Management System is a cloud platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It enforces strict EU-only data residency and sub-800ms search performance SLAs.

## Key Elements
- Library Patrons and Staff (Actors)
- Frontend SPA and Mobile App (React / React Native)
- API Gateway (Spring Cloud Gateway)
- Core Domain Services (Java / Spring Boot)
- Search Engine (Elasticsearch / OpenSearch)
- Database (PostgreSQL with Read Replicas)
- Async Message Broker (Apache Kafka / RabbitMQ)
- Notification Service (Java / Spring Boot)
- External Systems: Stripe EU, LDAP/SAML IdP, AWS S3 EU-Central, University SIS, Third-Party Delivery, RFID Gates

## Relationships
- Patrons/Staff -> Frontend SPA (HTTPS)
- Frontend SPA -> API Gateway (HTTPS)
- API Gateway -> Core Domain Services (HTTP/gRPC)
- Core Domain Services -> Search Engine (REST/TCP)
- Core Domain Services -> Database (JDBC/PostgreSQL Protocol)
- Core Domain Services -> Message Broker (AMQP/Kafka Protocol)
- Message Broker -> Notification Service (AMQP/Kafka Protocol)
- Notification Service -> External Email/SMS Provider (HTTPS/REST)
- LMS -> Payment Gateway, AWS S3, Delivery Service (HTTPS/REST)
- University SIS -> LMS (SFTP/HTTPS)

## Technology Stack
- Java/Spring Boot ecosystem: Chosen for enterprise maturity and robust microservices/modular monolith support.
- Elasticsearch/OpenSearch: Selected to meet the 99th-percentile search response time constraint of <800 ms.
- PostgreSQL (EU-Central): Provides reliable relational data storage with read replicas compliant with data residency rules.
- Apache Kafka/RabbitMQ: Enables decoupled, asynchronous event-driven workflows for notifications and indexing.
- AWS S3 EU-Central: Secures digital catalog asset storage within EU boundaries.

## Rationale
This architecture uses EU-hosted infrastructure and localized read replicas to strictly fulfill the data residency mandate. Additionally, utilizing an asynchronous message broker and dedicated search cluster ensures high-performance catalogue queries under peak academic circulation loads.