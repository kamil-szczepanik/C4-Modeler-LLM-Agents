## Overview
The Clinic Management System is a hybrid cloud platform designed to securely manage patient admissions, electronic medical records, appointment scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, clinical performance, and strict compliance with HIPAA and GDPR regulations.

## Key Elements
- Patients, Clinicians, Receptionists, Billing Specialists, and Hospital Administrators (User Personas)
- External Identity Provider (IdP), External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse
- Envoy API Gateway
- Frontend SPAs (React / Nginx)
- Domain Microservices (Spring Boot on Kubernetes): Patient Registry, Scheduling, EMR, Billing
- Integration Service (Node.js)
- Decoupled Data Tier (AWS RDS in `eu-central-1` and enterprise-grade on-premise clusters)
- Istio Service Mesh with OpenTelemetry sidecars
- WORM Storage for 10-year audit retention

## Relationships
- Users to Frontend SPAs via HTTPS (TLS 1.3)
- Frontend SPAs to Envoy API Gateway via HTTPS / REST / JSON
- Envoy API Gateway to Domain Microservices via gRPC over mTLS (Istio)
- Domain Microservices to Decoupled Data Tier via encrypted database drivers (AES-256)
- Integration Service to External Lab & Imaging Systems via HL7 FHIR APIs
- Core Services to External Identity Provider via OAuth2/OIDC

## Technology Stack
- Kubernetes (on-prem-k8s and AWS `eu-central-1`): Provides hybrid orchestration and active-active deployment capabilities
- Spring Boot & Node.js: Powers core domain microservices and integration layers for rapid request handling
- React & Nginx: Delivers responsive static UI containers for clinical and administrative workflows
- Envoy & Istio: Manages ingress routing, rate limiting, circuit breaking, and strict mTLS service mesh security
- PostgreSQL (AWS RDS & on-prem): Ensures secure, encrypted relational data storage with AES-256 at rest
- ArgoCD: Automates zero-downtime progressive deployments with canary analysis

## Rationale
This architecture decouples stateful data from application pods to eliminate split-brain risks and maintain 99.99% availability in a hybrid environment. Service mesh segmentation, strict mTLS, and WORM storage natively satisfy rigorous HIPAA, GDPR, and 10-year audit retention mandates without sacrificing sub-second EMR performance.