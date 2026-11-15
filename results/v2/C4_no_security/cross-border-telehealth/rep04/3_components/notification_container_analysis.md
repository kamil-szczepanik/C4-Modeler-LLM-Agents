## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system ensures regional data compliance, high availability in low-connectivity areas, and traceable AI outputs.

## Key Elements
- Patients (EU & US) and Licensed Clinicians
- Web/Mobile Client (Flutter / React Native)
- API Gateway (Cloud Endpoints / Envoy)
- Core Telehealth Backend (Node.js / Go)
- AI Symptom Checker & Consent Management Services
- Notification Container (Node.js / TypeScript) with internal components: Notification Router, Template Engine, Dispatcher Adapters, Delivery Status Tracker, and User Notification Preferences
- External Services: Twilio (SMS/Push) and SendGrid (Email)

## Relationships
- API Gateway -> Notification Container: Routes notification requests via gRPC [gRPC]
- Notification Router Component -> User Notification Preferences Component: Queries user channel settings [Local DB query]
- Notification Container -> Twilio: Triggers SMS and push alerts [HTTPS / API]
- Notification Container -> SendGrid: Triggers email alerts [HTTPS / API]

## Technology Stack
- Node.js (TypeScript): Implements the Notification Container logic for efficient async I/O.
- GCP Cloud SQL PostgreSQL: Stores regional delivery status and user preference read-models to satisfy data residency.
- GCP Pub/Sub: Handles asynchronous event-driven preference synchronization across regions.
- Twilio & SendGrid: Manages multi-channel outbound messaging via HTTPS APIs.

## Rationale
Regional container isolation and zero-PHI payloads guarantee strict GDPR and HIPAA compliance while preventing cross-border data leakage. Integrated retry queues and fallback channels maintain communication reliability for rural patients with unstable connections.