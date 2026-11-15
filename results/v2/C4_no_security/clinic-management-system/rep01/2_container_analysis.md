## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, strict regulatory compliance, and interoperability with external clinical systems.

## Key Elements
*   **Users:** Front Desk Receptionist, Clinician/Doctor, Billing Specialist, Patient, Compliance Officer.
*   **Clients:** Single-Page Application (SPA) / Mobile Client (React / TypeScript).
*   **Infrastructure / Gateway:** API Gateway (Kong or NGINX), Service Mesh (Istio / Linkerd).
*   **Microservices:** Patient & Scheduling Service, EMR Service, Billing & Claims Service, Integration Service, Audit & Compliance Service.
*   **Data & Caching:** PostgreSQL Clusters, Redis Enterprise.
*   **External Systems:** External Lab & Imaging Systems, Insurance Clearinghouse APIs, Identity Provider (IdP), SMS/Email Notification Gateway.

## Relationships
*   SPA to API Gateway: HTTPS / WSS
*   API Gateway to Services: gRPC over Istio mTLS
*   Integration Service to External Labs: HL7 FHIR over HTTPS
*   Services to IdP: OAuth2 / OIDC
*   Services to Data Layers: Encrypted internal connections (AES-256)

## Technology Stack
*   **Frontend:** React / TypeScript served via CDN for low-latency client performance.
*   **Backend Services:** Spring Boot (Java), Node.js / NestJS, Python / FastAPI, Go, and Apache Camel / Spring Integration for microservice separation.
*   **Databases & Caching:** PostgreSQL for primary persistence; Redis Enterprise for distributed caching and offline read resilience.
*   **Infrastructure & Orchestration:** Kubernetes (`on-prem-k8s` and AWS `eu-central-1`), ArgoCD for GitOps deployments.
*   **Security & Observability:** Istio service mesh (mTLS), Kong/NGINX (HTTPS/TLS 1.3), OpenTelemetry (OTel) sidecars, and automated air-gapped immutable backups.

## Rationale
This architecture uses container isolation and microservice boundaries to enforce least-privilege security (HIPAA/GDPR) while separating high-throughput EMR and billing workloads. A hybrid multi-primary mesh with active-active databases, Redis caching, and OpenTelemetry ensures 99.99% availability, local failover resilience, and <1s EMR response times.