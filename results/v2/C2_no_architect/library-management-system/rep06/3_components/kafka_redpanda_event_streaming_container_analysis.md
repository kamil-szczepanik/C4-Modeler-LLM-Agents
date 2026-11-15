## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service patron portals. It uses a high-performance, EU-compliant event-driven architecture to ensure real-time inventory visibility and sub-800ms search responses.

## Key Elements
* **Users:** Library Patrons, Librarians/Circulation Staff, Library Administrators
* **External Systems:** EU-hosted Identity Provider (IdP), CDN/WAF Edge Services, Digital Content Vendors / Third-Party E-Resource Providers
* **Containers:** API Gateway (Istio Service Mesh / Kubernetes Gateway), Patron Portal (Web Frontend / Backend Service), Circulation & Cataloguing Container (Java / Microservice), Elasticsearch Container (Elasticsearch), Kafka/Redpanda Event Streaming Container (Apache Kafka / Redpanda), Audit & Event Tracking Container (Microservice), Reporting/Analytics Container (Analytics Service), PostgreSQL Database (Primary/Read Replica)

## Relationships
* **Circulation & Cataloguing Container -> Kafka/Redpanda Event Streaming Container:** Publishes operational and transactional events using the Kafka Protocol [Kafka Protocol]
* **Kafka/Redpanda Event Streaming Container -> Audit & Event Tracking Container:** Consumes event streams using the Kafka Protocol [Kafka Protocol]
* **Patron Portal -> API Gateway:** Routes self-service requests via HTTPS/TLS 1.3 [HTTPS]
* **API Gateway -> Circulation & Cataloguing Container:** Forwards authenticated microservice calls via gRPC/mTLS [gRPC]

## Technology Stack
* **Event Streaming:** Redpanda (C++ thread-per-core architecture) chosen for superior throughput and tail latency over JVM-based Kafka
* **Search Engine:** Elasticsearch chosen to guarantee 99th-percentile search responses under 800ms
* **Primary Database:** PostgreSQL with read replicas for reliable transactional persistence
* **Gateway & Mesh:** Istio Service Mesh / Kubernetes Gateway for secure traffic management and routing
* **Security & Storage:** TLS 1.3 for encryption-in-transit, client-side field-level encryption for PII, topic-level ACLs, and EU-compliant object storage with SSE-KMS for tiered storage

## Rationale
This architecture ensures strict compliance with EU-only data residency mandates while delivering real-time inventory visibility for librarians and instant UI updates for patrons. The high-performance Redpanda and Elasticsearch components guarantee sub-800ms response times and robust system resilience.