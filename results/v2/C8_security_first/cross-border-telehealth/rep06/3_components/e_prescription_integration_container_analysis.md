## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It ensures strict data residency, regulatory compliance, and high availability across unstable internet connections.

## Key Elements
* **Patients & Licensed Clinicians**: Primary end-users of the telehealth platform.
* **API Gateway & Gateway-Backend (BFF)**: Built with Go and Envoy Proxy.
* **E-Prescription Integration Container**: Built with Node.js and Express, containing Prescription Router, National Gateway Adapter, Prescription State & Event Manager, and Prescription Outbox & Retry Processor.
* **AI Symptom Checker Container**: Built with Python and FastAPI.
* **Data & Messaging Storage**: Cloud SQL (PostgreSQL), Google Cloud Storage (WORM enabled), Cloud Pub/Sub, and regional Memorystore (Redis).
* **External Systems**: National e-Prescription Gateways (EU) and US Pharmacy Networks (HL7 FHIR).

## Relationships
* **API Gateway & BFF -> E-Prescription Integration Container**: Routes e-prescription requests via mTLS over gRPC/REST.
* **National Gateway Adapter -> National e-Prescription Gateways & US Pharmacy Networks**: Dispatches prescriptions using HL7 FHIR and REST over mTLS.
* **Prescription State & Event Manager -> Cloud SQL**: Persists audit logs and states using the PostgreSQL Protocol.
* **Prescription State & Event Manager -> Cloud Pub/Sub**: Publishes lifecycle events for the BFF via gRPC over TLS.

## Technology Stack
* **Go & Envoy Proxy**: Powers the API Gateway and BFF for performant routing.
* **Node.js & Express**: Powers the E-Prescription Integration Container for asynchronous event handling.
* **Python & FastAPI**: Used for the AI Symptom Checker Container to handle machine learning workflows.
* **PostgreSQL & Redis (BullMQ)**: Manages relational data and transactional outbox queues.
* **GCP (europe-west3, us-central1)**: Provides regional cloud infrastructure, GKE Confidential Computing, Cloud HSM, and Cloud KMS to enforce data residency.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data storage and compute workloads within specific GCP regions. Furthermore, the inclusion of transactional outbox patterns, circuit breakers, and regional encryption guarantees high availability and data sovereignty for cross-border telemedicine.