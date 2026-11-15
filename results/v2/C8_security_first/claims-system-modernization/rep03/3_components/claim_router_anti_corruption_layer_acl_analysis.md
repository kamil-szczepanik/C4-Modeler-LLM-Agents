## Overview
[The system is a modern hybrid claims processing platform designed to gradually replace a 30-year-old COBOL/DB2 mainframe system. Its core purpose is to enable online claim submission and adjuster workflows while migrating claim types incrementally without data loss.]

## Key Elements
- [ASP.NET Core Minimal APIs / API Endpoint Component]
- [Routing Engine Component (.NET 8 with Polly)]
- [Translation / Mapper Component (AutoMapper / strongly typed record mappings)]
- [Outbox Dispatcher Component]
- [Mainframe Adapter Component]
- [Azure Container Apps]
- [Azure App Configuration]
- [Azure Service Bus]
- [Azure Key Vault]
- [Azure App Insights / OpenTelemetry]

## Relationships
- [ASP.NET Core Minimal APIs -> Routing Engine Component: Forwards validated JSON/REST payloads via in-process method calls]
- [Routing Engine Component -> Mainframe Adapter Component: Routes un-migrated legacy claims via mTLS over dedicated ExpressRoute / IPsec VPN tunnel]
- [Routing Engine Component -> Azure App Configuration: Evaluates real-time feature flags via HTTPS REST APIs]
- [Translation / Mapper Component -> Mainframe Adapter Component: Translates modern JSON payloads into fixed-width COBOL copybooks]
- [Outbox Dispatcher Component -> Azure Service Bus: Publishes reliable events using AMQP protocol]
- [Claim Router / ACL -> Azure Key Vault: Retrieves secrets and rotation policies using Managed Identities over HTTPS]

## Technology Stack
- [.NET 8: High-performance framework utilized for building scalable cloud-native microservices]
- [Polly: Resilience and fault-handling library used for circuit breakers, timeouts, and retries]
- [Azure App Configuration: Managed service used for dynamic feature flagging and zero-downtime routing]
- [Azure Service Bus: Messaging broker ensuring at-least-once delivery and event consistency]
- [OpenTelemetry: Standardized observability framework for distributed tracing and payload log-redaction]

## Rationale
[This architecture effectively isolates modern services from mainframe latency and instability using circuit breakers and local caching to meet strict performance targets. It leverages managed Azure services to compensate for the team's low cloud experience while ensuring secure, zero-downtime, incremental migration.]