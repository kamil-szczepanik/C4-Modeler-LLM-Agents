## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals, adhering to EU-only data residency constraints. This summary details the internal C4 architecture of its **Notification Service** container.

## Key Elements
* **Notification Router Component** (TypeScript): Ingress handler for gRPC requests with token scope validation and payload sanitization.
* **Delivery Consumer Component** (KafkaJS): Consumes asynchronous messages from the Managed Event Bus.
* **Template Engine Component** (Handlebars / TypeScript): Renders localized notification templates with ephemeral memory handling for PII.
* **Dispatch Adapter Component** (Node.js): Manages external channel egress with W3C Trace Context propagation.
* **Retry & Resilience Policy Engine Component** (Opossum / TypeScript): Implements circuit breaking and exponential backoff.
* **External Providers**: SendGrid and Twilio.

## Relationships
* API Gateway -> Notification Router: `gRPC over mTLS` with scope authorization
* Managed Event Bus -> Delivery Consumer: `Kafka Protocol (TCP/SSL)`
* Notification Router -> Template Engine: In-memory function call with string sanitization
* Delivery Consumer -> Template Engine: In-memory data passing (`Async/Await`)
* Template Engine -> Dispatch Adapter: In-memory data passing
* Dispatch Adapter -> External Providers (SendGrid, Twilio): `HTTPS / TLS 1.3` with egress whitelisting

## Technology Stack
* Node.js / TypeScript: Core container runtime chosen for asynchronous processing efficiency.
* Handlebars: Template engine for generating localized notifications.
* Opossum: Circuit breaker library for preventing cascading external failures.
* KafkaJS: Consumer library for event-driven background processing.
* Vault (via SPIFFE/SPIRE): Dynamic credential management for external APIs.

## Rationale
This decoupled, event-driven component architecture guarantees high resilience, fast response handling, and strict compliance with EU data residency regulations. Incorporating dedicated circuit breakers and ephemeral memory handling ensures high availability while preventing PII exposure during high-load notification spikes.