## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It utilizes a secure, event-driven architecture to guarantee reliable, low-latency processing while maintaining strict EU-only data residency.

## Key Elements
- **Patron Self-Service Portal**: Web/Mobile application for patron self-service.
- **Staff Management Console**: Web interface for library staff.
- **Search & Catalogue Service**: Java / Spring Boot, Elasticsearch container for catalog management.
- **Circulation & Loan Engine**: Python (FastAPI / Pandas) container handling loan transactions.
- **Analytics & Reporting Service**: Python (FastAPI / Pandas) container for reporting.
- **Notification Engine**: Go container for asynchronous alerts.
- **Message Broker**: RabbitMQ/Kafka cluster containing Exchange & Routing Engine, Persistent Storage & Log Manager, Connection & ACL Manager, DLQ & Retry Manager, and Analytics Event Router.
- **Primary Database**: PostgreSQL with read-replicas.

## Relationships
- Patron Self-Service Portal -> EU-bound API Gateway: Submits user requests [HTTPS/REST]
- Circulation & Loan Engine -> Message Broker (Exchange & Routing Engine): Publishes domain events [AMQP/Kafka over TLS 1.3]
- Notification Engine -> Message Broker: Consumes events asynchronously [AMQP/Kafka]
- Message Broker -> Analytics & Reporting Service: Streams anonymized domain events [AMQP/Kafka over TLS 1.3]
- Notification Engine -> Message Broker (DLQ & Retry Manager): Routes unacknowledged or poisoned messages [AMQP/Kafka]

## Technology Stack
- **Message Broker**: RabbitMQ (3-node quorum queues) or Apache Kafka (3-broker KRaft cluster) for high availability and at-least-once delivery.
- **Security Protocols**: TLS 1.3 for data in transit, mTLS, SASL/SCRAM-SHA-512, and AES-256 disk encryption for EU data residency compliance.
- **Database**: PostgreSQL with read-replicas for robust transactional integrity.
- **Search Engine**: Elasticsearch to meet the 99th-percentile search response time under 800 ms.
- **Infrastructure**: Kubernetes StatefulSet with automated multi-AZ cloud storage replication in the EU region.

## Rationale
This event-driven microservices architecture guarantees sub-200ms messaging latency and high availability to support peak traffic without performance degradation. Strict security isolations, encryption standards, and data residency controls fully satisfy EU compliance and privacy mandates.