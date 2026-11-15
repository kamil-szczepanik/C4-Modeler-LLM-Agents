## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing for medium-sized hospitals and clinics. It ensures strict HIPAA/GDPR compliance, 99.99% availability, and long-term data retention.

## Key Elements
- **Frontend Container**: TypeScript, React, Nginx/CDN single-page application.
- **Internal Components**: Authentication & Session Manager, Role-Based Router & Shell, Clinical EMR View Component, API Client Layer, Local Persistence Manager (IndexedDB), Cryptographic Vault Manager.
- **Edge Container**: Kong / Envoy.
- **Backend Services**: Clinical Service (Go), Scheduling Service (Node.js), Billing Service (Java / Spring Boot), Audit & Compliance Log Service (Go), Integration Service / FHIR Facade (Go).
- **Data & Infrastructure**: Apache Kafka / RabbitMQ, PostgreSQL, MongoDB, Redis, Encrypted S3-compatible Object Storage.
- **Personas**: Patient, Clinician / Doctor, Receptionist / Admin, Billing Specialist, Compliance / IT Auditor, Hospital Executive.

## Relationships
- **Patient, Clinician, Receptionist, Billing Specialist, Auditor, Executive** -> **Frontend Container**: Accesses role-based portals and workflows [HTTPS / JSON]
- **Frontend Container** -> **Edge Container**: Sends API requests [HTTPS / JSON over TLS 1.3]
- **Clinical EMR View Component** -> **Local Persistence Manager**: Reads/Writes encrypted drafts [IndexedDB / Web Crypto API]
- **Integration Service** -> **External Lab & Imaging Systems**: Interoperability data exchange [HL7 FHIR APIs]

## Technology Stack
- **Frontend**: TypeScript, React, Nginx, Global CDN for optimized client-side rendering and static asset delivery.
- **Security**: Web Crypto API for client-side encryption, OIDC/OAuth2 via Identity Provider for multi-factor authentication.
- **Backend**: Go, Node.js, and Java Spring Boot microservices chosen for domain-specific performance and reliability.
- **Databases & Messaging**: PostgreSQL, MongoDB, Redis, Apache Kafka / RabbitMQ supporting active-active resilience.
- **Deployment**: Kubernetes (`on-prem-k8s` and AWS `eu-central-1`) with non-root Nginx container hardening.

## Rationale
This hybrid architecture combines on-premises Kubernetes clusters with cloud infrastructure to satisfy strict data residency regulations and 99.99% availability requirements. Encrypted client-side storage and role-based access control ensure full HIPAA and GDPR compliance while maintaining sub-second EMR performance.