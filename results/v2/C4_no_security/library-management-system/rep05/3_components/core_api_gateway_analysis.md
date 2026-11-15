## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries within the EU. The Core API Gateway routes and secures all traffic while enforcing strict performance SLAs.

## Key Elements
* Patrons, Librarians, and Administrators (Users)
* Patron Web Portal (React, Nginx)
* Staff Management Portal (Angular, Nginx)
* Core API Gateway (Spring Cloud Gateway, Spring Boot)
* Catalog & Search Service (Spring Boot, Elasticsearch)
* Circulation Service (Quarkus, PostgreSQL)
* Message Broker (RabbitMQ)
* State Store (Redis)
* Centralized Observability Platform

## Relationships
* Patron Web Portal -> Core API Gateway: Sends API requests [HTTPS REST/GraphQL]
* Staff Management Portal -> Core API Gateway: Sends API requests [HTTPS REST/GraphQL]
* Core API Gateway -> Catalog & Search Service: Routes search queries [gRPC]
* Core API Gateway -> Circulation Service: Routes transaction requests [gRPC]
* Core API Gateway -> RabbitMQ: Emits asynchronous telemetry events [AMQP]
* Core API Gateway -> Centralized Observability Platform: Ships metrics and logs [/actuator/prometheus]

## Technology Stack
* Spring Cloud Gateway: Chosen for reactive routing and robust filter ecosystem.
* Spring Security OAuth2: Provides stateless JWT validation against the Identity Provider.
* Resilience4j: Implements circuit breaking to prevent cascading downstream failures.
* Redis: Powers distributed rate-limiting within EU data residency constraints.
* gRPC: Ensures low-latency internal service communication (<800ms search SLA).
* RabbitMQ: Offloads asynchronous telemetry and usage metering events.

## Rationale
This architecture meets the strict <800ms search latency SLA by offloading analytics asynchronously and leveraging high-performance gRPC for internal routing. Centralizing security, rate-limiting, and tenant context propagation at the EU-pinned gateway ensures compliance and system resilience.