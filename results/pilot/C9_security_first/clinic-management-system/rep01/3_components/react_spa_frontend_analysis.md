## Overview
The Clinic Management System is a hybrid cloud clinical IT solution designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures HIPAA/GDPR compliance, a 99.99% uptime availability, and a 10-year data retention policy.

## Key Elements
- Patients, Receptionists, Clinicians, Billing Specialists (Users)
- React SPA Frontend (Container: React, CDN/Nginx)
- Authentication Context, Routing & Layout Engine, EMR Workspace Module, Scheduling & Billing Views, API Client Layer (Frontend Components)
- NGINX/Kong API Gateway (Container)
- Patient Service, Scheduling Service, EMR Service, Billing Service (Containers: Java, Spring Boot, gRPC)
- Apache Camel Integration Service, Distributed PostgreSQL Database, Apache Kafka Event Broker
- Third-Party Lab & Imaging Systems, External Payment Gateways, Insurance Clearinghouses (External Systems)

## Relationships
- Users -> React SPA Frontend: Access portal, manage admissions, update EMR, and process bills [HTTPS/WSS, OAuth2/OIDC, MFA]
- React SPA Frontend -> NGINX/Kong API Gateway: Sends API requests and queries [HTTPS/WSS, TLS 1.3, JWT]
- NGINX/Kong API Gateway -> Microservices (Patient, Scheduling, EMR, Billing): Routes internal gRPC calls [gRPC, mTLS]
- Apache Camel Integration Service -> Third-Party Lab & Imaging Systems: Interoperates via HL7 FHIR APIs [HTTPS/REST, HL7 FHIR]

## Technology Stack
- React with TypeScript: Powers the SPA Frontend with modular code-splitting and lazy loading for optimized performance.
- IndexedDB with AES-GCM: Provides HIPAA-compliant client-side encrypted state persistence for offline resilience.
- Nginx & Geo-Distributed CDN: Delivers static assets and enforces strict Content Security Policy (CSP) headers.
- Java & Spring Boot: Powers backend microservices communicating via gRPC.
- PostgreSQL & Apache Kafka: Handles active-active distributed persistence and event streaming.

## Rationale
The architecture decouples clinical microservices behind an API Gateway while utilizing a high-performance React frontend to meet strict sub-second EMR load requirements. Hybrid deployment and geo-distributed CDN caching guarantee 99.99% availability and robust HIPAA/GDPR compliance across regions.