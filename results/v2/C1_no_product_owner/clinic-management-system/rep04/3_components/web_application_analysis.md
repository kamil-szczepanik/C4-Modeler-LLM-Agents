## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for healthcare facilities. It ensures high availability, strict compliance with HIPAA and GDPR regulations, and low-latency clinical workflows.

## Key Elements
- **Users**: Patient/Client, Clinician/Medical Staff, Billing Admin
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **Containers**: API Gateway (Kong / Nginx on Kubernetes), Web Application (React / Next.js), Patient & Scheduling Microservice, EMR Microservice, Billing Microservice, Integration Service, PostgreSQL Database, WORM Audit Log Store, Event Broker (Apache Kafka / RabbitMQ), Istio Service Mesh
- **Web Application Internal Modules**: Patient Portal UI Module, Clinician Dashboard Module, Billing Console Module, Auth & Session Manager, State Management & API Client Module, Client-Side Routing & RBAC Guard

## Relationships
- Patients, Clinicians, Billing Administrators -> Web Application: Accesses portal via browser [HTTPS/TLS]
- Web Application -> API Gateway: Sends user requests [HTTPS/TLS with OAuth2/OIDC and mutual TLS]
- Auth & Session Manager -> Identity Provider: Validates sessions via [OpenID Connect / HTTPS]
- Clinician Dashboard Module -> API Gateway: Fetches EMR data via [gRPC-Web / HTTPS]

## Technology Stack
- **Frontend Framework**: React / Next.js for cross-platform UI and server-side rendering support.
- **Infrastructure & Orchestration**: Kubernetes (on-premise and AWS `eu-central-1`) with Istio Service Mesh (SPIFFE/SPIRE) for mTLS and traffic splitting.
- **Security & Storage**: PostgreSQL (Multi-AZ), WORM Storage with HSM-backed KMS, HTTP-only Secure SameSite=Strict cookies for token management.
- **Scalability**: KEDA (Kubernetes Event-driven Autoscaling) targeting HTTP concurrency metrics for 99.99% availability.

## Rationale
This hybrid architecture uses containerized microservices and Istio service mesh to meet strict HIPAA/GDPR data protection mandates and active-active 99.99% uptime requirements. Statically built UI modules deployed behind a CDN combined with gRPC-Web ensure sub-1-second P95 performance for critical EMR screens.