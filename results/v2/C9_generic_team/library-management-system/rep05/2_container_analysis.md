## Overview
The Library Management System provides cataloging, circulation, and self-service portals for academic and public libraries. It ensures EU-only data residency and sub-800ms search responses.

## Key Elements
* Patrons, Staff, Librarians, and System Administrators
* API Gateway / BFF Container
* Web App & Core Transactional Service Containers
* Search Service Container (Elasticsearch/OpenSearch)
* Message Broker Container (RabbitMQ/Kafka)
* Distributed Cache Container (Redis)
* Worker / Background Task Container
* Observability Sidecars
* External Legacy ILS, Identity Providers, Payment Gateways, and WAF

## Relationships
* Patrons and Staff communicate via HTTPS to the API Gateway Container.
* API Gateway routes requests to Web App and Core Transactional Service via internal REST/gRPC.
* Core Transactional Service publishes events to Message Broker via AMQP/Kafka protocol.
* Search Service consumes events and indexes catalog data, serving queries via HTTP.
* Workers sync with Legacy ILS and ERP systems using scheduled batch protocols.

## Technology Stack
* Elasticsearch / OpenSearch: Chosen for the Search Service to meet the < 800 ms p99 latency requirement (R-05).
* Redis: Used as a distributed cache to maintain stateless application tiers and ensure fast data access.
* RabbitMQ or Kafka: Implemented as an Asynchronous Event Bus to decouple writes and maintain indexing consistency.
* Kubernetes: Orchestrator enforcing resource quotas, health checks, and strict EU-region deployments.

## Rationale
Decoupling search and background processing from core transactions protects system performance under load. Strict EU region hosting and stateless container designs ensure data residency compliance and scalability.