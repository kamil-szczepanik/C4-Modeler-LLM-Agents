## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. It ensures 99.99% high availability, strict HIPAA and GDPR compliance, and seamless interoperability via HL7 FHIR APIs.

## Key Elements
- **Partition Manager & Replication Engine**: Kraft / ZooKeeper Consensus and Java component for leader election and ISR.
- **Kafka Request Handler & Produce/Consume API**: Java TCP Sockets component processing binary messaging.
- **Storage & Log Compaction Engine**: OS Page Cache / Java NIO with AES-256 for encrypted event retention.
- **MirrorMaker 2.0 Replication Agent**: Kafka Connect / Java component for cross-site hybrid replication.

## Relationships
- **Patient & EMR Service** -> **Kafka Request Handler**: Publishes EMR events via TCP / Kafka Protocol (SASL/TLS).
- **Billing & Integration Service** -> **Kafka Request Handler**: Consumes billing triggers via TCP / Kafka Protocol (SASL/TLS).
- **Partition Manager & Replication Engine** <-> **MirrorMaker 2.0**: Synchronizes state across regions via TCP / Kafka Protocol (TLS).

## Technology Stack
- **Kraft / ZooKeeper**: Chosen for reliable consensus and cluster coordination.
- **Java NIO / TCP**: Selected for high-throughput binary messaging performance.
- **AES-256 Encryption**: Implemented for HIPAA compliance on data at rest.
- **MirrorMaker 2.0**: Deployed for active-active multi-region hybrid disaster recovery.

## Rationale
This component architecture uses resilient replication and encrypted streaming to satisfy stringent regulatory mandates for PHI. The hybrid cloud design ensures uninterrupted 99.99% availability across on-prem-k8s and eu-central-1 regions.