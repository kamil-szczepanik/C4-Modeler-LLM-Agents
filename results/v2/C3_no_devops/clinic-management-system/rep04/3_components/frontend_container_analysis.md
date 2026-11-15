## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability (99.99%), HIPAA/GDPR compliance, and 10-year data retention.

## Key Elements
- **Users**: Patient, Clinic Staff/Receptionist, Clinician/Doctor, Billing Specialist, System Administrator
- **Frontend Container**: React, TypeScript, Vite, CDN, Nginx Single Page Application
- **Frontend Components**: Routing & Shell Component, Authentication & Session Manager, Clinical & Administrative Feature Modules, API Client Service, Local Persistence & Sync Service (IndexedDB via Dexie.js, Web Crypto API)
- **Backend & Infrastructure**: API Gateway (Kong/Envoy, Istio), Core Services, EMR Service, Integration Service (HL7 FHIR APIs), Notification Service, Audit & Compliance Service (Kafka with TLS + SASL), PostgreSQL Database (AES-256), ClickHouse Database

## Relationships
- **Users -> Frontend Container**: Interact with UI workflows [HTTPS/WSS]
- **Frontend Container -> API Gateway**: Sends API requests and receives responses [HTTPS/WSS]
- **Routing & Shell Component -> Feature Modules**: Dynamically lazy-loads modules
- **Feature Modules -> API Client Service & Local Persistence**: Communicates with backend via API and manages offline encrypted drafts
- **Authentication & Session Manager -> External IdP**: Handles OIDC/OAuth2 authentication and MFA

## Technology Stack
- **Frontend**: React, TypeScript, Vite, Nginx, CDN, Axios/Fetch, Dexie.js for optimal bundle splitting and performance (<1s EMR load).
- **Security**: Web Crypto API for client-side IndexedDB encryption, OIDC/OAuth2, HttpOnly Secure cookies, strict Content Security Policy (CSP), HTTP Strict Transport Security (HSTS).
- **Integration & Data**: HL7 FHIR APIs, Apache Kafka (TLS + SASL), PostgreSQL with AES-256 encryption at rest, ClickHouse for analytics.

## Rationale
This architecture uses a React SPA with strict internal security components and client-side encryption to satisfy stringent HIPAA and GDPR privacy mandates. The hybrid cloud deployment model combined with microservices and local caching ensures sub-second EMR screen loads and 99.99% high availability.