## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It guarantees regional data residency and regulatory compliance.

## Key Elements
- Patients and Licensed Clinicians
- API Gateway / Ingress (Envoy / GCP HTTPS Load Balancer)
- E-Prescription Integration Container (Node.js, TypeScript)
- Prescription Router Component
- EU National Gateway Adapter (`europe-west3`)
- US Pharmacy Network Adapter (`us-central1`, HL7 FHIR)
- Outbox Pattern / Reliability Component & Google Cloud Pub/Sub
- Data Tier (Cloud SQL PostgreSQL, Memorystore)
- External Gateways: National E-Prescription Gateways (EU), US Pharmacy Networks

## Relationships
- API Gateway -> E-Prescription Integration Container: Routes prescription requests via gRPC over mTLS
- Prescription Router -> EU National Gateway Adapter: Dispatches regional EU formats via outbound mTLS with pinned IPs and certificates
- Prescription Router -> US Pharmacy Network Adapter: Transmits HL7 FHIR payloads via outbound mTLS
- E-Prescription Integration Container -> Data Tier: Persists records using SQL with CMEK and transactional outbox tables
- E-Prescription Integration Container -> Google Cloud Pub/Sub: Publishes events for reliable delivery and OpenTelemetry observability

## Technology Stack
- Node.js & TypeScript: Powers the E-Prescription Integration Container for asynchronous, I/O-bound protocol mapping
- GCP Cloud SQL PostgreSQL: Provides robust relational data persistence with Customer-Managed Encryption Keys (CMEK)
- Google Cloud Pub/Sub: Implements reliable message queuing for the Transactional Outbox Pattern
- HL7 FHIR & EU National Standards: Ensure interoperability with US pharmacy networks and EU national e-prescription systems
- GCP Secret Manager & Certificate Authority Service: Securely manages and rotates dynamic mTLS credentials

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by enforcing regional data isolation across `europe-west3` and `us-central1`. The transactional outbox pattern and dedicated protocol adapters guarantee high availability and fault tolerance for cross-border prescription deliveries.