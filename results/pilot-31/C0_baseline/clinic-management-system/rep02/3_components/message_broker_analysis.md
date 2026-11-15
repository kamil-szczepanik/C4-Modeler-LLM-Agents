## Overview
The Clinic Management System is a hybrid-cloud platform designed to manage patient records, scheduling, and billing. It utilizes an event-driven architecture to ensure high availability and strict data integrity for clinical operations.

## Key Elements
*   **Message Broker:** Apache Kafka (Federated deployment)
*   **Reconciliation Controller:** Custom service for DLQ monitoring and state correlation
*   **Schema Registry:** Enforces HL7 FHIR-compliant message structures
*   **WORM Storage:** Immutable destination for audit logs and historical data
*   **Infrastructure Management:** Terraform/Crossplane for automated provisioning

## Relationships
*   **Clinical Services -> Message Broker:** Publishes events via mTLS-secured asynchronous messaging.
*   **Message Broker -> WORM Storage:** Streams administrative and audit logs for compliance.
*   **Reconciliation Controller -> DLQ:** Monitors failed events and triggers notifications for clinical administrators.
*   **Services -> Schema Registry:** Validates all event payloads against FHIR standards before production.

## Technology Stack
*   **Apache Kafka:** Chosen for high-throughput, durable event streaming with `acks=all` and replication factor of 3.
*   **mTLS & ABAC:** Ensures encryption-in-transit and granular topic-level access control.
*   **Field-Level Encryption:** Protects sensitive PHI/PII at the application layer before ingestion.
*   **Terraform/Crossplane:** Standardizes deployment and configuration across hybrid on-prem and AWS environments.
*   **Tiered Storage:** Offloads historical logs to WORM storage to meet 10-year retention requirements.

## Rationale
This architecture prioritizes clinical data integrity and regulatory compliance by combining strict schema enforcement with immutable audit trails. The federated Kafka model and Reconciliation Controller ensure 99.99% availability while surfacing "silent failures" to maintain patient safety.