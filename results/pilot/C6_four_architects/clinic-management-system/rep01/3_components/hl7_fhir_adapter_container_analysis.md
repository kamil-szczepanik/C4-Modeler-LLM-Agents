## Overview
[The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare clinics, ensuring HIPAA and GDPR compliance with 99.99% availability. The HL7 FHIR Adapter Container securely transforms and exchanges clinical payloads with external health systems.]

## Key Elements
- API Router & Validator (Express.js, Node.js)
- FHIR Resource Mapper (TypeScript classes)
- Outbound TLS Client (Axios, HTTPS/mTLS)
- Audit Logger Interceptor (gRPC)
- HL7 Validation Engine (fhir validator-wrapper)
- Retry & Dead-Letter Queue Manager (BullMQ, Redis)
- mTLS Ingress Terminating Proxy (Envoy sidecar)
- Payload Sanitization & PII Redaction (Regex-based)
- FHIR Subscription Manager (WebSockets, gRPC, RabbitMQ)
- Bulk Data Import/Export Processor (JSONStream, KafkaJS, Apache Kafka)
- Rate Limiting & Throttling Interceptor (Bottleneck)
- Schema Version Negotiation Middleware (Semantic versioning)
- Circuit Breaker Pattern Manager (Opossum)
- Token Exchange & Claims Verifier (OAuth2/JWT, ABAC)
- Terminology Mapping Engine (Redis, LOINC, SNOMED-CT)
- Metrics & Tracing Interceptor (OpenTelemetry SDK)
- Asynchronous Webhook Dispatcher (Express.js, HMAC-SHA256, AMQP/RabbitMQ)
- Payload Compression & Decompression Middleware (Node.js zlib)
- DLQ Purge & Replay Worker (Cron, Notification Service)
- FHIR Bundle Splitting Processor (Node.js)

## Relationships
- Patient & EMR Service -> API Router & Validator: Exchanges clinical payloads [HTTPS/REST]
- API Router & Validator -> FHIR Resource Mapper: Forwards validated payloads [In-memory]
- FHIR Resource Mapper -> Outbound TLS Client: Transmits transformed FHIR resources [HTTPS/mTLS]
- Outbound TLS Client -> External Lab, Imaging, and HIE Systems: Exchanges health data [HTTPS/REST]
- Audit Logger Interceptor -> Audit & Compliance Sidecar Container: Dispatches audit events [gRPC]
- FHIR Subscription Manager -> RabbitMQ Cluster: Distributes real-time events [gRPC/AMQP]
- Bulk Data Import/Export Processor -> Apache Kafka StatefulSet: Streams large bundles [KafkaJS]
- Asynchronous Webhook Dispatcher -> RabbitMQ Cluster: Offloads webhook payloads [AMQP]

## Technology Stack
- Node.js & TypeScript: Core application runtime and type safety for reliable container logic
- Express.js: Lightweight HTTP routing for REST APIs and webhook ingestion
- BullMQ & Redis: Resilient message queuing, caching, and retry management
- Apache Kafka: High-throughput streaming for bulk FHIR data processing
- Envoy & OpenTelemetry: Edge cryptographic termination and end-to-end distributed tracing

## Rationale
[This modular internal container architecture guarantees high availability, secure HIPAA-compliant data interoperability, and robust fault tolerance during external network anomalies. Leveraging streaming parsers and caching layers ensures optimal performance meeting the <1s P95 EMR requirement.]