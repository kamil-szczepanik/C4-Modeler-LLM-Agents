## Overview
The Clinic Management System is a hybrid-cloud clinical IT solution designed to manage patient registration, scheduling, Electronic Medical Records (EMR), and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- FHIR Interoperability Service (.NET container)
- Security Enforcement Middleware
- FHIR API Controller (ASP.NET Core)
- Resource Transformer Engine
- HL7 Client Adapter (HttpClient / Polly)
- Audit & Compliance Interceptor
- External Lab & Imaging Systems
- OpenTelemetry Collector
- RabbitMQ
- HashiCorp Vault

## Relationships
- API Gateway -> Security Enforcement Middleware: gRPC over mTLS [SPIFFE/SPIRE]
- Security Enforcement Middleware -> FHIR API Controller: Method calls [In-process]
- FHIR API Controller -> Resource Transformer Engine: Method calls [In-process]
- Resource Transformer Engine -> HL7 Client Adapter: Method calls [In-process]
- HL7 Client Adapter -> External Lab & Imaging Systems: HL7 FHIR over HTTPS [REST/JSON]
- HL7 Client Adapter -> RabbitMQ: Failed payload streaming [AMQP]
- Audit & Compliance Interceptor -> OpenTelemetry Collector: Telemetry with PHI masking [OTLP over gRPC]

## Technology Stack
- .NET / ASP.NET Core: High-performance framework for building the FHIR service container.
- Polly: Provides circuit breaking, bulkhead patterns, and retry policies for resilient outbound calls.
- HashiCorp Vault: Securely injects and rotates mTLS client certificates for external lab authentication.
- RabbitMQ: Dead Letter Queue (DLQ) for capturing failed outbound lab payloads to ensure zero data loss.
- OpenTelemetry Collector: Centralized observability for distributed tracing and Prometheus metrics.

## Rationale
This architecture uses micro-segmentation, zero-trust patterns, and resilient .NET components to guarantee secure, compliant, and highly available clinical data exchange. Strict isolation, automated secrets management, and robust error-handling mechanisms satisfy both regulatory mandates and rigorous uptime targets.