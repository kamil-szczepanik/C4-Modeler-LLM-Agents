## Overview
- Manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics.
- Ensures HIPAA and GDPR compliance with 99.99% high availability in a hybrid cloud environment.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators
- API Gateway / Reverse Proxy (Envoy / NGINX)
- Patient Portal App (React SPA / Node.js / CDN)
- Clinical Core Service (Java / Spring Boot)
- Billing & Integration Service (Go / Temporal.io)
- Administrative & Analytics Service (Python / FastAPI + Celery)
- Notification & Messaging Service (Node.js / Python)
- FHIR Integration Adapter
- Clinical Core Database (Encrypted SQL)
- External Systems: Payment Gateway, External Lab & Imaging Systems, Identity Provider (IdP)

## Relationships
- Patient, Staff, and Administrators -> API Gateway / Reverse Proxy via HTTPS (TLS 1.3) with adaptive MFA
- Clinic Management System -> Identity Provider (IdP) via OpenID Connect (OIDC) / OAuth2 over HTTPS
- API Gateway / Reverse Proxy -> Patient Portal App via HTTPS
- API Gateway / Reverse Proxy -> Clinical Core Service, Billing & Integration Service, Administrative & Analytics Service via HTTPS / mTLS
- Clinical Core Service -> Notification & Messaging Service via AMQP / Kafka over mTLS
- Billing & Integration Service -> Payment Gateway via Payment REST APIs over encrypted HTTPS
- FHIR Integration Adapter -> External Lab & Imaging Systems via HL7 FHIR APIs over encrypted HTTPS

## Technology Stack
- Java / Spring Boot for Clinical Core Service to ensure robust enterprise capabilities
- React SPA / Node.js / CDN for Patient Portal App for fast global delivery and secure session handling
- Go / Temporal.io for Billing & Integration Service for resilient workflows and claim processing
- Python / FastAPI + Celery for Administrative & Analytics Service to isolate compliance reporting
- Encrypted SQL for Clinical Core Database ensuring AES-256 at rest and 10-year data retention

## Rationale
- Hybrid cloud architecture utilizes on-premise Kubernetes and AWS eu-central-1 to meet data residency, strict security, and regulatory constraints.
- Microservices isolation combined with active-active deployment achieves the required 99.99% availability and high-performance EMR access.