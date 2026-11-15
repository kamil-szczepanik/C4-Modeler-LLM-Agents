## Overview
The Data Routing / Compliance Proxy is an OCI-compliant container managing ingress traffic for the Library Management System, enforcing strict EU-only data residency and protecting performance SLAs. It routes requests between client portals and backend services while handling security, compliance, and traffic management.

## Key Elements
- Data Routing / Compliance Proxy (OCI-compliant Container)
- Redis Distributed Cache Container
- RabbitMQ / Kafka Asynchronous Message Broker Container
- Consul / Spring Cloud Config Centralized Configuration Store
- Monitoring and Telemetry Aggregator
- Downstream Services: Catalog Management, Circulation

## Relationships
- Client Portals to Data Routing / Compliance Proxy via HTTPS/REST
- Data Routing / Compliance Proxy to Redis Distributed Cache Container via RESP (REdis Serialization Protocol)
- Data Routing / Compliance Proxy to RabbitMQ / Kafka via AMQP/Kafka Protocol
- Data Routing / Compliance Proxy to Centralized Configuration Store via HTTP/gRPC

## Technology Stack
- OCI-compliant Container: Provides standard containerization and deployment flexibility.
- Redis Distributed Cache Container: Enables low-latency compliance rule lookups and distributed rate limiting.
- Consul / Spring Cloud Config: Facilitates dynamic, zero-downtime updates to routing tables and geo-IP lists.
- RabbitMQ / Kafka: Supports asynchronous dead-letter queue integration for non-blocking compliance auditing.

## Rationale
This architecture ensures strict adherence to EU-only data residency constraints through localized proxying and fail-closed security principles. Furthermore, integrating circuit breakers, Redis-backed rate limiting, and zero-copy data transfer guarantees that the 99th-percentile search response remains under 800 ms.