## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and interoperability across hybrid cloud environments.

## Key Elements
- External Lab & Imaging Systems, Third-Party Health Apps
- Integration Service / FHIR Facade (Go container)
- FHIR API Gateway / Router (Go using `Gin` or `Fiber`)
- Resource Mapper & Validator (`go-fhir` models)
- Outbound/Inbound Client Pool
- DLQ Management Handler (Go background worker)
- Event Bus (Apache Kafka / RabbitMQ)
- Envoy sidecar & Kubernetes clusters (`on-prem-k8s`, `eu-central-1`)
- Encrypted S3-compatible Object Storage

## Relationships
- Edge Container -> Integration Service / FHIR Facade: Routes requests via internal mTLS [Internal gRPC and REST over mTLS]
- Integration Service / FHIR Facade -> External Lab & Imaging Systems: Exchanges lab and imaging interoperability data [HL7 FHIR APIs]
- FHIR API Gateway -> Resource Mapper & Validator: Internal function calls [Go structs]
- Resource Mapper & Validator -> Event Bus (Kafka): Publishes normalized clinical events and failed payloads [Async / Pub-Sub]
- DLQ Management Handler -> Event Bus (Kafka): Republishes corrected payloads [Kafka Producer]

## Technology Stack
- Go (with `Gin`/`Fiber`, `go-fhir`, and `sarama`/`segmentio/kafka-go`): Chosen for high performance, sub-second ingestion, and robust concurrency.
- Apache Kafka: Enables async event-driven architecture and Dead Letter Queue (DLQ) pattern for fault tolerance.
- Kubernetes & Envoy: Deployed across `on-prem-k8s` and `eu-central-1` to guarantee 99.99% active-active uptime and mTLS security.
- Encrypted S3-compatible Object Storage: Secures DLQ payloads with immutable object locking to meet 10-year audit retention mandates.
- SMART-on-FHIR OAuth2: Secures clinician and patient-access scopes for interoperability.

## Rationale
This architecture ensures robust interoperability through standardized HL7 FHIR APIs while meeting stringent HIPAA/GDPR security and 99.99% availability requirements. The hybrid cloud design, event-driven DLQ pattern, and Go-based facade provide scalable, fault-tolerant clinical data exchange.