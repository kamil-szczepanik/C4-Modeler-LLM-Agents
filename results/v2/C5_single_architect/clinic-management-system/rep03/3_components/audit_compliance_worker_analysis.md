## Overview
The Audit & Compliance Worker is a Go-based container within the Clinic Management System that asynchronously processes, sanitizes, and archives security and access events. It ensures strict HIPAA and GDPR compliance as well as a mandatory $\ge$ 10-year data retention period.

## Key Elements
- **Event Consumer Component**: Consumes raw security and access events.
- **Compliance Normalizer Component**: Validates, sanitizes, and structures event payloads against HIPAA/GDPR schemas.
- **Retention Policy Enforcer Component**: Applies data immutability flags and tagging.
- **Archival Exporter Component**: Batches and streams processed audit packages to long-term storage.
- **DLQ Handler Component**: Catches malformed or failed events to prevent audit data loss.

## Relationships
- *Event Consumer* --(reads)--> *Message Broker* [Kafka Protocol]
- *Compliance Normalizer* --(passes data)--> *Retention Policy Enforcer* [In-memory Go channels]
- *Compliance Normalizer* --(routes failures)--> *DLQ Handler Component* [In-memory Go channels]
- *Archival Exporter* --(writes)--> *Regulatory Archiving / Audit Storage* [HTTPS / S3 API]
- *DLQ Handler Component* --(publishes retry/alert)--> *Message Broker* [Kafka Protocol]

## Technology Stack
- **Go**: Selected for its lightweight concurrency model (goroutines) to handle high-throughput event streams with a minimal memory footprint.
- **`segmentio/kafka-go`**: Used for efficient message consumption from the Kafka broker.
- **AWS SDK**: Utilized for secure batching and streaming to cloud storage via S3 API.
- **Kafka Protocol**: Ensures reliable messaging communication.

## Rationale
This component-level architecture ensures absolute compliance resilience and high availability by securely processing and permanently archiving audit logs without dropping data. The decoupled design fulfills rigorous non-functional constraints including 99.99% uptime and long-term regulatory retention mandates.