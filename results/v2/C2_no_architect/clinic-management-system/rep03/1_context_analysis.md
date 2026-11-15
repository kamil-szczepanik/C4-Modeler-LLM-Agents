## Overview
[The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability, regulatory compliance, and sub-second clinical workflows.]

## Key Elements
- **Users**: Front Desk Staff, Clinicians, Billing Officers, Patients, and Patient Portal Users.
- **Systems**: Clinic Management System, Lab Systems, Imaging Systems.
- **Containers**: On-Premises Kubernetes Cluster, Cloud Environment (`eu-central-1`).
- **Components**: Patient Registration Service, Scheduling Engine, EMR Service, Billing Service, Event Bus (Kafka/Debezium), Encrypted Gateways.

## Relationships
- **Front Desk / Clinicians / Billing Officers to CMS**: Interacts via TLS 1.3 and Multi-Factor Authentication (MFA).
- **CMS to Lab & Imaging Systems**: Integrates via HL7 FHIR APIs over encrypted protocols.
- **On-Prem-K8s to AWS (eu-central-1)**: Replicates asynchronously via Kafka/Debezium with field-level encryption for PHI.

## Technology Stack
- **Kubernetes (`on-prem-k8s`, `eu-central-1`)**: Deployed for hybrid orchestration ensuring 99.99% active-active availability.
- **Apache Kafka & Debezium**: Implements asynchronous, event-driven data pipelines to survive WAN dropouts.
- **AES-256 with Client-Side Envelope Encryption**: Secures data at rest, preventing cloud provider access.
- **TLS 1.3 & mTLS**: Secures all data in transit and hybrid boundary traffic.

## Rationale
[This hybrid architecture separates local clinic operations from cloud storage using an asynchronous event-driven model to ensure high availability and sub-second EMR performance. Strict zero-trust segmentation, field-level encryption, and break-glass protocols satisfy HIPAA and GDPR mandates without compromising clinical efficiency.]