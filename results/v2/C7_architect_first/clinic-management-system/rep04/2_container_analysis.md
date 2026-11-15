## Overview
The Clinic Management System is a hybrid-cloud healthcare IT solution designed to manage patient admissions, EMRs, scheduling, and billing. It provides high availability, stringent compliance, and robust clinical workflows across medium-sized hospitals and clinics.

## Key Elements
* **Users**: Patient, Clinician/Doctor, Receptionist, Billing Staff
* **Containers**: API Gateway / Edge Proxy (NGINX/Envoy), Web Application Frontend (React/TypeScript), Patient Self-Service Portal, Core Clinical & EMR Service (Java/Spring Boot), Scheduling & Billing Service (Node.js/NestJS), Local Storage/Sync Daemon
* **Data & Storage**: PostgreSQL (with row-level encryption), Redis (Cache), Immutable Audit Log (AWS QLDB / Append-only Postgres)
* **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP), On-Premises Hardware Security Module (HSM)

## Relationships
* Users to API Gateway: HTTPS / WSS
* API Gateway to Web Application Frontend & Patient Portal: HTTPS
* API Gateway to Backend Services: gRPC over Istio Service Mesh
* Core Clinical & EMR Service to PostgreSQL & Audit Log: JDBC/TLS with mTLS
* Scheduling & Billing Service to Redis: TCP/TLS
* Scheduling & Billing Service to Payment Gateway / Insurance Clearinghouse: HTTPS/REST
* Inter-container hybrid boundary (`on-prem-k8s` to `eu-central-1`): Istio multi-primary service mesh with strict mTLS

## Technology Stack
* **Frontend**: React / TypeScript with IndexedDB and client-side AES-256 encryption for offline resilience
* **Backend Services**: Java / Spring Boot (Core Clinical & EMR) and Node.js / NestJS (Scheduling & Billing)
* **API & Communication**: NGINX / Envoy for edge proxy; gRPC for internal microservice communication
* **Data Layer**: PostgreSQL with row-level encryption; Redis for scheduling locks; AWS QLDB/Append-only Postgres for immutable audit logs
* **Infrastructure & Security**: Hybrid Kubernetes (`on-prem-k8s` and `eu-central-1`); Istio Service Mesh; On-Premises HSM for key management

## Rationale
This architecture uses a hybrid-cloud Kubernetes model with active-active multi-region deployment to satisfy the 99.99% availability and strict low-latency requirements. It enforces end-to-end security via AES-256 encryption, Istio mTLS, and HSM-backed key management to maintain mandatory HIPAA and GDPR compliance.