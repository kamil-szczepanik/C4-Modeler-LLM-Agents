## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces strict regional data residency, regulatory compliance, and resilient messaging for unstable connections.

## Key Elements
- EU Pub/Sub Topic Partition (`europe-west3`)
- US Pub/Sub Topic Partition (`us-central1`)
- Event Schema Registry
- Client Ingress Relay
- Regional Message Forwarders
- Dead Letter Queue (DLQ) & Retry Handler Component
- DLQ Monitoring & Alerting Component

## Relationships
- Web & Mobile Clients -> Client Ingress Relay via WebSocket/MQTT [WSS]
- Client Ingress Relay -> Regional Pub/Sub Topics via GCP Pub/Sub [gRPC]
- Core Telehealth & AI Services -> Event Schema Registry via [HTTPS/gRPC]
- Regional Pub/Sub Topics -> Regional Message Forwarders via [gRPC]
- Regional Pub/Sub Topics -> DLQ & Monitoring via [gRPC/HTTPS]

## Technology Stack
- GCP Pub/Sub: Asynchronous messaging backbone with regional partitioning for data residency.
- Apache Avro / JSON Schema: Payload validation enforced via Event Schema Registry.
- WebSocket / MQTT: Edge connectivity protocol for handling rural, low-bandwidth clients.
- Java / Go: Implementation languages for regional message forwarders and workers.
- Cloud Monitoring / Cloud Functions: Automated alerting for DLQ and poisoned messages.

## Rationale
Regional topic isolation and strict schema validation guarantee compliance with GDPR and HIPAA data residency and audit requirements. Edge relay buffering and dead-letter monitoring ensure continuous availability and resilience over unstable rural internet connections.