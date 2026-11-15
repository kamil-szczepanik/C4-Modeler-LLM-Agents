## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Audit & Compliance Logger Sidecar securely captures, sanitizes, and routes compliance logs while enforcing regional data residency.

## Key Elements
- Log Ingestion Receiver (Fluentbit Core)
- Compliance Sanitizer & Masker (Go Custom Plugin / Filter)
- Regional Dispatcher (Fluentbit Output Plugin)
- Traceability Indexer (Go Sidecar Agent)
- Buffer & Resiliency Manager (Fluentbit Mem/Filesystem Buffer)

## Relationships
- App Containers -> Unix Domain Sockets (`in_syslog`) -> Log Ingestion Receiver
- Log Ingestion Receiver -> Go-routine channels -> Compliance Sanitizer & Masker
- Compliance Sanitizer & Masker -> Go function calls -> Traceability Indexer
- Traceability Indexer -> Filesystem I/O (Fluentbit Chunk Storage) -> Buffer & Resiliency Manager
- Buffer & Resiliency Manager -> Mutual TLS (TLS 1.3 over HTTPS) -> Regional GCP Storage / BigQuery (`europe-west3` or `us-central1`)

## Technology Stack
- Fluentbit & Go: Core log ingestion and custom sanitization/traceability plugins for high performance and low overhead
- Kubernetes (GKE): Deployment as a container sidecar in `europe-west3` and `us-central1`
- Unix Domain Sockets (`emptyDir`): Zero network overhead and secure local inter-process communication
- HTTPS / TLS 1.3 (Mutual TLS): Encrypted, region-locked data egress guaranteeing regulatory compliance

## Rationale
This architecture ensures strict GDPR, HIPAA, and EU MDR compliance by keeping EU and US health data strictly within regional boundaries and ensuring complete AI traceability. Furthermore, local Unix sockets and persistent disk buffering guarantee system reliability and zero log loss even over unstable rural internet connections.