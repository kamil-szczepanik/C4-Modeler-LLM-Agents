## Overview
The Library Management System is a solution for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals with strict EU data residency. The API Gateway serves as the primary perimeter defense, handling traffic routing, security, and performance optimization.

## Key Elements
- **Users**: Library Patrons, Librarians / Circulation Staff, Library Administrators
- **Containers**: Web Frontend, API Gateway, Core Business Service, Search Service, Database, Notification Dispatcher, Audit Logging Service, Message Broker, Identity Provider, Payment Gateway
- **API Gateway Components**: Proxy Router, Authentication & Authorization Plugin, Rate Limiting Plugin, Response Caching Plugin, Log Transport Plugin

## Relationships
- Web Frontend -> API Gateway: Sends API requests [HTTPS/REST]
- Identity Provider -> API Gateway: Validates tokens / fetches JWKS [HTTPS/REST]
- API Gateway -> Core Business Service: Routes business requests [Internal REST/gRPC via mTLS]
- API Gateway -> Search Service: Routes search queries [Internal REST/gRPC via mTLS]
- API Gateway -> Audit Logging Service: Emits access logs [Async/gRPC via mTLS]

## Technology Stack
- **API Gateway**: Kong API Gateway for declarative configuration, Lua/Go plugins, rate limiting, and response caching.
- **Frontend**: React and TypeScript hosted on an EU-region CDN.
- **Backend Services**: Spring Boot (Java) for Core Business Service, Go for Audit Logging Service, Python/Celery for Notification Dispatcher.
- **Search & Storage**: Elasticsearch for search, PostgreSQL with AES-256 encryption-at-rest for primary storage, RabbitMQ / AWS SQS for message brokering.
- **Security Protocols**: TLS 1.3 for external traffic, strict mTLS for east-west traffic, OAuth2/JWT for authentication.

## Rationale
The architecture ensures high performance, meeting the <800ms search SLA through Kong's response caching and rate limiting. Centralizing security and token validation at the API Gateway enforces robust perimeter defense and compliance with EU data residency constraints.