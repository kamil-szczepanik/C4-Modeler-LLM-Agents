## Overview
The Clinic Management System is a hybrid-cloud healthcare platform providing patient registration, EMR, scheduling, billing, and FHIR interoperability. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance.

## Key Elements
- Users: Patients, Clinical Staff, Administrative Staff, Billing Officers, Compliance Administrators
- External Systems: Web Browsers, Patient Mobile App, Lab & Imaging Systems, Payment Gateway, Identity Provider, SIEM
- Frontend Containers: React SPA, Node.js Mobile BFF
- Gateway & Security: Nginx/Kong API Gateway, Istio/Linkerd Service Mesh
- Core Containers: Java/Spring Boot Clinical Services, Python/FastAPI Billing, Java HAPI FHIR Interoperability, Go Notification Worker, Python Compliance Worker
- Data & Messaging: PostgreSQL, Apache Kafka, S3-compatible Tiered Storage

## Relationships
- Web/Mobile Clients to API Gateway/BFF via HTTPS/OAuth2
- Internal Services to Core Clinical Services via gRPC over mTLS
- Core Services to Kafka via TCP for asynchronous event publishing
- Billing and Interoperability Containers to External Systems via REST/HL7 FHIR
- Compliance Worker to S3 Tiered Storage via HTTPS with AES-256

## Technology Stack
- Frontend: React SPA, Node.js / Express for mobile BFF
- Backend Services: Java / Spring Boot (Clinical/FHIR), Python / FastAPI (Billing/Compliance), Go (Notifications)
- Messaging & Integration: Apache Kafka for event-driven decoupling
- Database & Storage: PostgreSQL with AES-256 encryption; S3-compatible tiered storage for long-term retention
- Infrastructure & Security: Hybrid Kubernetes (on-prem-k8s and AWS eu-central-1), Nginx/Kong, Istio/Linkerd Service Mesh, ArgoCD, OpenTelemetry

## Rationale
The asynchronous event-driven architecture using Kafka decouples third-party dependencies to protect 99.99% uptime and sub-second EMR performance. Separating compliance and interoperability workloads into dedicated containers maintains core clinical performance while satisfying 10-year retention and strict HIPAA/GDPR requirements.