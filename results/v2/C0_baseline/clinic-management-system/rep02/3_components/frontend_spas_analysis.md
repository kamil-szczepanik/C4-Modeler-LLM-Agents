## Overview
The Frontend SPAs container provides a responsive, role-tailored user interface for patients, clinicians, and administrative staff within the Clinic Management System. It delivers optimized clinical workflows while strictly enforcing security, data privacy, and high-availability standards.

## Key Elements
- Role-Based UI Modules (React, Redux Toolkit)
- API Client Layer (Axios, in-memory OIDC state)
- Telemetry & Monitoring Module (OpenTelemetry, RUM)
- Nginx Web Server (Static asset serving, strict CSP headers)
- Envoy API Gateway

## Relationships
- Patient, Clinician, Receptionist, Billing Specialist, Hospital Administrator -> Frontend SPAs: Accesses portals and workflows [HTTPS (TLS 1.3)]
- Frontend SPAs -> Envoy API Gateway: Authenticates and fetches data [HTTPS / REST & GraphQL / JSON]

## Technology Stack
- React with Redux Toolkit: Provides lazy-loaded, role-tailored feature bundles to meet performance requirements.
- Nginx: Serves immutable static assets with strict Content Security Policy headers and TLS 1.3 encryption.
- OpenTelemetry: Captures Real User Monitoring data and tracks P95 load times.
- In-memory OIDC State: Secures authentication tokens without vulnerable browser storage.

## Rationale
This architecture separates UI presentation from authorization enforcement to ensure strict HIPAA and GDPR compliance. It optimizes client-side performance to maintain EMR screen loads below one second.