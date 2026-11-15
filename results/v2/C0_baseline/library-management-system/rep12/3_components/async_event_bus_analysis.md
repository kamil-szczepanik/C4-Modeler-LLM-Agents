## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It uses a secure, distributed event-driven architecture to ensure high-performance search and operational resilience.

## Key Elements
- **Event Broker Cluster:** Apache Kafka Brokers managing distributed commit logs
- **Schema Registry:** Confluent Schema Registry enforcing Avro/JSON payloads
- **Topic Manager / ACL Enforcer:** Handles topic creation and role-based access control via TLS client certificates
- **Kafka Connect:** Confluent Kafka Connect streaming data to external sinks
- **Core Domain Services:** Node.js / NestJS services publishing domain events
- **Notification Worker:** Node.js / NestJS worker consuming events via Consumer Groups
- **Search Engine:** Elasticsearch indexing catalogue items

## Relationships
- **Core Domain Services** -> **Event Broker Cluster**: Publishes domain events via TCP (Port 9092, mTLS)
- **Core Domain Services** -> **Schema Registry**: Validates event schemas prior to publishing via HTTPS (mTLS)
- **Event Broker Cluster** -> **Kafka Connect**: Streams domain changes to Search Engine via TLS
- **Notification Worker** -> **Event Broker Cluster**: Consumes events using Kafka Consumer Groups (mTLS)

## Technology Stack
- **Apache Kafka:** Selected over RabbitMQ for high-throughput event streaming and robust partition management
- **Confluent Schema Registry:** Ensures payload governance, backward compatibility, and GDPR minimization rules
- **mTLS & TLS 1.3:** Enforces strict authentication via client certificate SANs and secure in-transit data
- **AES-256 Encryption:** Secures all Kafka broker persistent volumes and Schema Registry storage within EU-hosted KMS
- **MirrorMaker 2:** Implements automated cross-AZ mirroring for disaster recovery

## Rationale
This architecture ensures strict compliance with EU-only data residency mandates while delivering sub-800ms search responses and reliable circulation workflows. Decentralized asynchronous messaging prevents blocking operations, guaranteeing high availability and operational resilience for library patrons and staff.