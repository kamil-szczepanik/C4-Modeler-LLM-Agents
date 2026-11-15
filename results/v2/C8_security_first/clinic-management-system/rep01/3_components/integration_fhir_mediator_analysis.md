## Overview
The Integration & FHIR Mediator securely standardizes and routes data exchanges between internal microservices and external clinical systems. It ensures HIPAA/GDPR compliance, high availability, and sub-second interoperability for the Clinic Management System.

## Key Elements
- Inbound Gateway Component (Apache Camel K / Java)
- Transformation Engine Component (Apache Camel / HAPI FHIR Java Library)
- Outbound Dispatcher Component (Apache Camel K Route)
- Audit & Compliance Logger Component
- Secret & Credential Management Store (HashiCorp Vault via CSI Secrets Store)
- Event Broker (Redpanda)
- Observability Stack (OpenTelemetry, Grafana Mimir/Tempo)

## Relationships
- External Lab & Imaging Systems invoke Inbound Gateway via HTTPS with mTLS and SMART-on-FHIR JWT tokens
- Inbound Gateway forwards payloads to Transformation Engine via internal gRPC/HTTP
- Outbound Dispatcher publishes domain events to Event Broker (Redpanda) using Kafka protocol
- Audit & Compliance Logger streams sanitized telemetry to Observability Stack via OpenTelemetry Protocol (OTLP)

## Technology Stack
- Apache Camel K / Java: Stateless serverless integration runtime for high availability and KEDA-driven autoscaling
- HAPI FHIR Java Library: Standardized parsing and schema validation of HL7 FHIR R4 resources
- HashiCorp Vault: Secure retrieval of external API keys and client certificates via CSI Secrets Store provider
- Redpanda: High-performance event broker supporting Kafka-backed Dead Letter Queues (DLQ)

## Rationale
This architecture guarantees 99.99% uptime and strict compliance through stateless, autoscaling serverless pods and secure cryptographic controls. It fulfills all healthcare interoperability mandates while delivering low-latency, resilient data transformation for clinicians.