## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It utilizes a containerized microservices architecture to deliver high-performance catalogue search and circulation features while strictly enforcing EU data residency.

## Key Elements
*   Clients: Web Frontend, Mobile App
*   Gateways: API Gateway Container, Data Routing / Compliance Proxy
*   Core Microservices: Catalog Management, Circulation, User Portals
*   Data & Caching: Elasticsearch / OpenSearch Search Container, Redis Distributed Cache Container, Isolated Microservice Databases
*   Infrastructure: Asynchronous Message Broker Container (RabbitMQ/Kafka), Centralized Configuration Store (Consul), Log/Metrics Collector Agent

## Relationships
*   Clients connect to the API Gateway Container via HTTPS/REST.
*   API Gateway routes traffic to Core Microservices via internal gRPC/REST.
*   Microservices query the Redis Distributed Cache Container and Elasticsearch Search Container via TCP.
*   Microservices publish/consume events via the Message Broker Container.
*   Log/Metrics Collector Agent forwards structured JSON logs to Monitoring via TLS.

## Technology Stack
*   OCI-compliant Container Images (Docker): Enables reproducible builds and packaging.
*   Elasticsearch / OpenSearch: Decouples search queries to meet the <800ms performance requirement.
*   Redis: Absorbs read spikes as a distributed cache and manages stateless session data.
*   Consul / Spring Cloud Config: Centralizes configuration to maintain immutable image builds.
*   Kubernetes: Orchestrates containers using explicit resource limits and health probes (`/healthz`).

## Rationale
Decoupling search, caching, and stateless microservices prevents resource starvation and ensures 99th-percentile search responses remain under 800ms. Explicit database isolation and EU-bound storage drivers guarantee compliance with the EU data residency constraint.