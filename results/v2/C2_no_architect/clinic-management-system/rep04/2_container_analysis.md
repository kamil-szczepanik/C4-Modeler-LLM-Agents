## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, EMRs, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability for clinical workflows.

## Key Elements
* **Users:** Patients, Receptionists, Clinicians, Billing Specialists, and Hospital Administrators.
* **Containers:** Patient Portal, Clinical Core (EMR, Scheduling, Billing Reconciliation), Notification & Reminder Container, and API Gateway.
* **External Systems:** Insurance Payers/Clearinghouses, External Labs, and Imaging Systems.
* **Infrastructure:** Hybrid Kubernetes (`on-prem-k8s` and AWS `eu-central-1`), Istio Service Mesh, and ArgoCD.

## Relationships
* **Patients** access the **Patient Portal** via HTTPS/OAuth2.
* **API Gateway** routes traffic to internal containers using **mTLS** via **Istio**.
* **Clinical Core** communicates with **External Labs and Imaging Systems** via **HL7 FHIR APIs**.
* **Billing Reconciliation** interfaces with **Insurance Payers/Clearinghouses** via secure HTTPS with dead-letter queues.

## Technology Stack
* **Orchestration & GitOps:** Kubernetes (`on-prem-k8s`, `eu-central-1`) with ArgoCD for zero-downtime progressive delivery.
* **Security & Auth:** OAuth2/OIDC, short-lived JWTs, HashiCorp Vault for secrets, Cosign for image signing, and WAF at the ingress.
* **Networking & Mesh:** Istio Service Mesh enforcing mutual TLS (mTLS) and Kubernetes NetworkPolicies for namespace isolation.
* **Observability & Storage:** OpenTelemetry for distributed tracing, AES-256 encryption at rest with WORM audit logging.

## Rationale
Namespace isolation and mTLS enforce zero-trust boundaries, satisfying strict HIPAA and GDPR compliance mandates. Active-active hybrid deployment strategies and asynchronous data pipelines guarantee 99.99% availability and low-latency EMR performance.