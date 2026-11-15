## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, regulatory compliance (GDPR/HIPAA/MDR), and fault-tolerant operations for unstable connections.

## Key Elements
* Patients and Licensed Clinicians (End Users)
* Offline-First Patient Mobile/Web App
* API Gateway / Region Router (GCP / HTTPS / WebSockets)
* Core Business Logic & Video Consultation Containers (GCP Regional Containers / WebRTC)
* FHIR/E-Prescription Adapter Containers (Anti-Corruption Layer, Circuit Breakers, Bulkheads)
* Consent Management & Traceability Logging Containers (OpenTelemetry / GCP Memorystore)
* External Systems: US HL7 FHIR Providers, EU National E-Prescription Gateways, Regional Pharmacy Networks

## Relationships
* Offline-First Patient Mobile/Web App -> API Gateway / Region Router: Routes requests [REST/gRPC / Idempotency Keys]
* API Gateway / Region Router -> Core Business Logic & Video Consultation Containers: Forwards regional traffic [HTTPS / WebSockets]
* Core Business Logic & Video Consultation Containers -> FHIR/E-Prescription Adapter Containers: Requests prescriptions and lookups [Internal API / gRPC]
* FHIR/E-Prescription Adapter Containers -> US HL7 FHIR Providers: Exchanges clinical data [REST/FHIR]
* FHIR/E-Prescription Adapter Containers -> EU National E-Prescription Gateways: Routes e-prescriptions [National Protocols]
* FHIR/E-Prescription Adapter Containers -> Regional Pharmacy Networks: Coordinates fulfillment [REST/HTTPS]

## Technology Stack
* Google Cloud Platform (GCP): Target cloud provider for scalable regional deployments
* GCP Regions `europe-west3` and `us-central1`: Enforces strict EU/US data residency compliance
* WebRTC: Enables low-bandwidth, degraded-mode video consultations for unstable rural connections
* OpenTelemetry: Emits structured metrics, distributed tracing, and symptom-checker traceability logs
* GCP Pub/Sub: Acts as the event-driven integration bus across distributed services
* GCP Memorystore: Provides low-latency regional caching and session management
* GCP Secret Manager: Manages externalized configuration and environment-agnostic runtime secrets

## Rationale
Containerizing adapters with an Anti-Corruption Layer isolates volatile external US and EU healthcare protocols from core business logic. Regional deployment isolation and resilience patterns (Circuit Breakers, Bulkheads, DLQs) guarantee strict compliance with GDPR/HIPAA while ensuring high availability during unstable network conditions.