## Overview
Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. The system enforces strict EU-only data residency and high-performance search capabilities.

## Key Elements
- **Users**: Library Patrons, Librarians, Library Administrators
- **Containers**: Patron Self-Service Portal (React/TypeScript SPA), Librarian Workbench (.NET Core), Catalog API & Search Service (.NET Core), Integration Gateway (Kong/Envoy)
- **Librarian Workbench Components**: Inventory Management Module, Payment & Fee Module, Audit & Compliance Module, Notification & Messaging Module, ASP.NET Core Razor Pages / Blazor UI Layer
- **External Systems**: EU Identity Provider, EU Payment Gateway, EU Notification Service, Central Logging & Monitoring SIEM

## Relationships
- Librarian Workbench -> Catalog API & Search Service: gRPC over mTLS
- Librarian Workbench -> EU Payment Gateway: REST API over HTTPS with mTLS
- Librarian Workbench -> Central Logging & Monitoring SIEM: OpenTelemetry with PII sanitization
- Librarian Workbench -> EU Notification Service: AMQP over TLS / RabbitMQ
- Patron / Librarian -> Integration Gateway: HTTPS

## Technology Stack
- **Backend**: .NET Core / C# for modular monolith containers
- **Frontend**: React / TypeScript for SPA, ASP.NET Core Razor Pages / Blazor for Workbench UI
- **Database**: PostgreSQL with GIN indexes for search performance
- **Message Broker**: RabbitMQ with Dead-Letter Queues for asynchronous processing
- **Resilience**: Polly for retry and circuit-breaker patterns

## Rationale
The modular monolith architecture balances rapid delivery with strict EU data residency compliance. In-memory communication ensures high performance while maintaining domain boundaries for future scalability.