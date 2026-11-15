## Overview
The Patient Portal is a secure, highly available frontend container of the Clinic Management System that empowers patients with self-service registration and appointment scheduling. It ensures strict HIPAA and GDPR compliance while interacting seamlessly with core backend clinical services.

## Key Elements
* Patients / Consumers
* Patient Portal Container (Next.js, TypeScript)
* Patient Authentication Controller (NextAuth.js)
* Registration & Profile Manager (React Component)
* Appointment Self-Service UI (React Component)
* Localization & Preference Module (React Component)
* BFF (Backend-for-Frontend) API Router (Next.js API Routes)
* External Identity Provider (IdP)
* API Gateway / Reverse Proxy (Kong / NGINX Ingress)
* HashiCorp Vault

## Relationships
* Patient Auth Controller -> Identity Provider [HTTPS/OIDC]
* BFF API Router -> API Gateway / Reverse Proxy [HTTPS/REST via Istio mTLS]
* Frontend UI Components -> BFF API Router [Internal TypeScript Calls]
* Next.js Runtime -> HashiCorp Vault [Encrypted API]

## Technology Stack
* Next.js & React (TypeScript): Selected for server-side rendering, performance, and robust ecosystem support.
* NextAuth.js: Utilized for secure multi-factor authentication and token management.
* Istio Service Mesh: Deployed to enforce strict mTLS and zero-trust transport security.
* HashiCorp Vault: Implemented for secure runtime secret management.
* OpenTelemetry & Prometheus: Chosen for comprehensive distributed tracing and availability monitoring.

## Rationale
This architecture uses a BFF pattern with httpOnly cookies and Istio mTLS to strictly protect PHI against XSS and interception risks. Decoupling the frontend via a hybrid cloud setup with automated failover guarantees the required 99.99% availability and low-latency performance.