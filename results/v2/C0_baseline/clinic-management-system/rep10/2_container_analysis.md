## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR performance.

## Key Elements
- **Users & External Systems:** Patients, Clinicians, Administrative Staff, Billing Officers, Auditors, External Insurance Clearinghouses, External Labs/Imaging.
- **Frontend & Edge:** React/TypeScript Web Application, NGINX/Envoy API Gateway.
- **Core Containers:** EMR Service, Billing & Claims Service, Scheduling Service, Notification Service, Integration Service.
- **Data & Messaging:** PostgreSQL, Redis, RabbitMQ message broker, HashiCorp Vault.
- **Infrastructure:** Kubernetes (hybrid `on-prem-k8s` and `eu-central-1`), Istio Service Mesh.

## Relationships
- Patients & Staff access the **Web Application** via HTTPS through the **API Gateway**.
- **Web Application** communicates with microservices via REST/JSON over HTTPS.
- **EMR**, **Billing**, **Scheduling**, and **Notification** services communicate asynchronously via **RabbitMQ**.
- **Integration Service** connects via **HL7 FHIR APIs** to external lab systems.
- Inter-container traffic uses **mTLS (Istio)**.

## Technology Stack
- **Frontend:** React/TypeScript for responsive clinician UI.
- **API & Routing:** NGINX/Envoy for edge ingress, rate limiting, and JWT validation.
- **Backend Services:** Node.js/Go for EMR and Scheduling; Java/Spring Boot for Billing; Python/FastAPI for Notifications.
- **Data Stores:** PostgreSQL with AES-256 for persistent data; Redis for scheduling cache.
- **Messaging & Security:** RabbitMQ for events; HashiCorp Vault for secrets; Istio for service mesh.

## Rationale
The microservices architecture isolates high-volume billing and notification traffic from real-time clinical workflows to guarantee sub-second EMR performance and revenue protection. Hybrid Kubernetes deployment with active-active replication ensures 99.99% availability and stringent HIPAA/GDPR data protection standards.