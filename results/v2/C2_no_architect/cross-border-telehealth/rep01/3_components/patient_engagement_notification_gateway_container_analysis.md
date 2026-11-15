## Overview
The Patient Engagement & Notification Gateway Container manages multi-channel patient communications, e-prescription dispatches, and delivery status feedback across regional deployments. It ensures secure, consent-validated, and localized message delivery while accommodating unstable rural connections.

## Key Elements
* **Patient Engagement & Notification Gateway Container:** Core service handling notifications, dispatches, and consent enforcement.
* **Regional GKE Clusters (`europe-west3`, `us-central1`):** Host regional gateway instances to enforce data residency.
* **Persistent Message Queues & DLQs:** GCP Pub/Sub instances managing asynchronous retries and failed message isolation.
* **Clinician Dashboard & Handoff Container:** Downstream consumer receiving asynchronous delivery status feedback events.
* **Third-Party SMS/Email Gateways:** External providers delivering masked notifications via deep links.

## Relationships
* **Clinician Dashboard -> Gateway Container:** Dispatches e-prescriptions and care notifications via HTTPS/TLS.
* **Gateway Container -> GCP Pub/Sub:** Publishes async delivery status feedback events and queues pending messages.
* **Gateway Container -> Third-Party SMS/Email Gateways:** Dispatches anonymized notification templates via HTTPS/OAuth 2.0.
* **Istio Service Mesh -> Gateway Container:** Enforces mTLS for all internal cluster traffic.

## Technology Stack
* **Google Cloud Platform (GCP):** Target cloud provider ensuring regional isolation in `europe-west3` and `us-central1`.
* **Google Kubernetes Engine (GKE):** Container orchestration platform utilizing Horizontal Pod Autoscalers driven by queue depth.
* **GCP Pub/Sub:** Asynchronous message bus and Dead Letter Queue provider for reliable retry handling.
* **GCP Cloud KMS & Secret Manager:** Provides regional customer-managed encryption keys and secure API credential storage.
* **Istio Service Mesh:** Enforces strict mTLS across internal container boundaries.
* **OpenTelemetry:** Standardizes distributed tracing and metric collection for SLA compliance.

## Rationale
Regionalizing the gateway inside GKE clusters strictly enforces GDPR and HIPAA data residency mandates. Asynchronous queuing and DLQs guarantee reliable delivery for rural patients with unstable connections without blocking clinician workflows.