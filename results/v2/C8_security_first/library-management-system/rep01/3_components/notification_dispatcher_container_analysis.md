## Overview
[Library Management System Notification Dispatcher Container: A Go/Temporal service that reliably routes, renders, and dispatches multi-channel patron and staff notifications while enforcing strict EU data residency and PII protection.]

## Key Elements
- API Handler Component (Go)
- Notification Workflow Engine (Temporal SDK)
- Routing & Preference Resolver Component (Go)
- Template Engine Component (Go)
- External Connector Component (Go)
- External Notification Service

## Relationships
- API Handler -> Workflow Engine: Enqueues workflow [Temporal SDK / internal RPC]
- Workflow Engine -> Routing & Preference Resolver: Fetches channel preferences [Internal gRPC]
- Routing & Preference Resolver -> Template Engine: Passes localized context [In-memory]
- Workflow Engine -> Template Engine: Renders payload [In-memory]
- Workflow Engine -> External Connector: Dispatches message [Internal channel]
- External Connector -> External Notification Service: Sends alerts [HTTPS / REST, mTLS, OAuth2]

## Technology Stack
- Go: High-performance core language for all internal components
- Temporal SDK / Workflow Engine: Durable state management and retry policies
- Redis: Caching layer for patron preferences with fallback mechanisms
- HashiCorp Vault: Dynamic secret and OAuth2 token management
- OpenTelemetry: Distributed tracing and structured JSON logging

## Rationale
[This architecture guarantees high reliability and durability for critical library alerts through Temporal workflows and dead-letter queues. It strictly enforces EU data residency and GDPR compliance via PII sanitization, TLS 1.3, envelope encryption, and zero-trust internal mTLS.]