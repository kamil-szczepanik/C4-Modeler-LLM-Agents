## Overview
[The Core Telehealth Service is a Spring Boot application running on GCP, providing secure, region-isolated clinical consultations, e-prescriptions, and AI symptom checks.]

## Key Elements
* Patients and Licensed Clinicians (Users)
* Core Telehealth Service (Spring Boot / Java Container)
* Consent & Policy Enforcement Engine
* Consultation Session Manager
* Clinical Core Orchestrator
* Event-Driven Sync & Outbox Dispatcher
* Cloud SQL (PostgreSQL), Cloud Pub/Sub, and GCP Cloud KMS

## Relationships
* Web & Mobile Clients -> Core Telehealth Service: HTTPS / gRPC with mTLS via GCP Service Mesh
* Core Telehealth Service -> Cloud SQL (PostgreSQL): Encrypted JDBC connections via Cloud KMS
* Core Telehealth Service -> Cloud Pub/Sub: Application-layer encrypted asynchronous messaging for offline sync

## Technology Stack
* Spring Boot / Java: Chosen for robust enterprise architecture and dependency injection
* Google Cloud Platform (GCP): Selected for regional isolation (`europe-west3` and `us-central1`)
* Cloud KMS: Utilized for application-layer envelope encryption and column-level security
* Spring Data JPA & Cloud Pub/Sub: Implements the Transactional Outbox pattern for rural network resilience

## Rationale
[This architecture enforces strict data residency and zero-trust security controls to comply with GDPR and HIPAA. It ensures reliable, offline-first continuity of care for rural patients without compromising regulatory integrity.]