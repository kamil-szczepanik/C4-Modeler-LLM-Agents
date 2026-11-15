## Overview
The system is a hybrid insurance claims modernization platform that gradually replaces a 30-year-old mainframe system with a modern cloud architecture. It ensures zero claim loss and continuous processing during a multi-year migration.

## Key Elements
*   **Messaging Container**: Azure Service Bus with DLQs
*   **Claim Events Topic**: `topic/claims-events`
*   **Mainframe Sync Queue**: `queue/mainframe-sync`
*   **Notification Queue**: `queue/notifications`
*   **Schema Validation Filter**: Azure Schema Registry
*   **Dead-Letter Queue (DLQ) Manager**: Azure Functions
*   **Integration ACA Worker**: Azure Container Apps (Worker)

## Relationships
*   Claims Core Services -> Schema Validation Filter [AMQP]
*   Schema Validation Filter -> Claim Events Topic [AMQP]
*   Schema Validation Filter -> Mainframe Sync Queue [AMQP]
*   Claims Core Services -> Claim Events Topic [AMQP]
*   Mainframe Sync Queue -> DLQ Manager [AMQP]
*   Integration ACA Worker -> Mainframe Sync Queue [AMQP]

## Technology Stack
*   **Azure Service Bus**: Chosen for reliable asynchronous messaging and dead-letter queuing to guarantee R-04 compliance.
*   **Azure Schema Registry**: Enforces payload validation to prevent poison pills from crashing legacy systems.
*   **Azure Functions**: Automates DLQ triage and operational alerting for failed synchronization attempts.
*   **Bicep / Terraform**: Implements Infrastructure as Code to manage cloud resources despite team cloud experience limits.

## Rationale
This architecture decouples the modern cloud platform from the brittle legacy mainframe using managed queues and topics. It enforces strict resilience, schema validation, and routing patterns to support gradual claim-type migrations without exceeding mainframe constraints.