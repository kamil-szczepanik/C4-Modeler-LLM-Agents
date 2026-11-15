## Overview
The Library Management System is a comprehensive solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures strict EU-only data residency and sub-800ms search responses.

## Key Elements
- **Library Patrons, Librarians, and Administrators**: End-users and operators of the system.
- **External Systems**: External Identity Provider (IdP), Payment Gateway, Notification Service.
- **Web App / SPA**: React/TypeScript hosted on a CDN.
- **API Gateway**: Envoy/Kong.
- **Core Services Container**: Java/Spring Boot handling business logic.
- **Search Container**: Elasticsearch delivering fast search performance.
- **Audit Container**: Go-based security and audit event handler.
- **Message Broker (Apache Kafka)**: KRaft mode broker handling asynchronous events, retry topics, and Dead Letter Queues (DLQ).
- **Database**: PostgreSQL for persistent data storage.

## Relationships
- **Web App / SPA -> API Gateway**: HTTPS / REST / GraphQL.
- **API Gateway -> Core Services Container**: gRPC / REST [mTLS].
- **Core Services Container -> Message Broker**: Publishes domain events, retry messages, and DLQ payloads via Apache Kafka [mTLS, TCP].
- **Audit & Notification Services -> Message Broker**: Consumes domain and security events [mTLS, TCP].
- **Core Services -> Database**: JDBC / SQL [TLS].

## Technology Stack
- **Apache Kafka (KRaft mode)**: Selected for message brokering to provide persistent, append-only commit logs, strict ordering, and decentralized metadata management without ZooKeeper.
- **Java / Spring Boot & Spring Kafka**: Chosen for core business services and producer/consumer implementations.
- **Go**: Utilized for lightweight audit and alerting daemons.
- **Elasticsearch**: Deployed to achieve <800ms 99th-percentile search performance.
- **PostgreSQL**: Relational database for core transactional data.
- **Envoy/Kong**: API Gateway for routing and ingress control.

## Rationale
This architecture uses Apache Kafka in KRaft mode deployed across three EU availability zones to meet strict EU data residency and high-availability requirements. Decoupled asynchronous messaging with mTLS, AES-256 storage encryption, and DLQ patterns guarantee at-least-once delivery, data protection, and robust circulation resilience.