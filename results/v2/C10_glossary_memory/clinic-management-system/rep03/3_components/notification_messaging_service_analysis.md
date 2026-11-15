## Overview
• Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics using a hybrid cloud architecture.
• Ensures HIPAA and GDPR compliance, 99.99% high availability, and secure multi-factor authentication across all clinical and administrative workflows.

## Key Elements
• Clinic Management System
• Patient, Receptionist / Front Desk, Clinician / Doctor, Billing Specialist, Hospital Administrator
• Payment Gateway, External Lab & Imaging Systems, Identity Provider (IdP)
• API Gateway / Reverse Proxy (Envoy / NGINX), Patient Portal App (React SPA / Node.js / CDN)
• Clinical Core Service (Java / Spring Boot), Billing & Integration Service (Go / Temporal.io)
• Administrative & Analytics Service (Python / FastAPI + Celery), Notification & Messaging Service (Node.js / Python)
• FHIR Integration Adapter, Clinical Core Database (Encrypted SQL)

## Relationships
• Patient / Staff -> API Gateway / Reverse Proxy via HTTPS (TLS 1.3) with risk-based adaptive MFA
• Clinic Management System -> Identity Provider (IdP) via OpenID Connect (OIDC) / OAuth2 over HTTPS
• Clinical Core Service & Billing & Integration Service -> Notification & Messaging Service via AMQP / Kafka over mTLS
• Billing & Integration Service -> Payment Gateway via Payment REST APIs over encrypted HTTPS
• FHIR Integration Adapter -> External Lab & Imaging Systems via HL7 FHIR APIs over encrypted HTTPS
• Administrative & Analytics Service -> Clinical Core Database via Read-only replicas using encrypted SQL over mTLS

## Technology Stack
• Kubernetes (on-prem-k8s and eu-central-1): Hybrid multi-region deployment ensuring 99.99% active-active availability
• Java / Spring Boot & Go / Temporal.io: Backend core and integration services for robust asynchronous processing and reliable state management
• Python / FastAPI & Node.js: Lightweight analytics, patient portals, and notification ingestion
• AES-256 and mTLS: Strict data encryption at rest and secure transport across all microservice boundaries to satisfy HIPAA/GDPR constraints

## Rationale
• The hybrid cloud Kubernetes architecture combined with active-active regional placement guarantees the required 99.99% uptime and low-latency performance.
• Strict adherence to AES-256 encryption, mTLS transport, and HL7 FHIR interoperability standards fulfills complex HIPAA, GDPR, and clinical integration mandates.