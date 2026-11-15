## Overview
Clinic Management System provides patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, strict HIPAA/GDPR compliance, and sub-second performance across a hybrid cloud infrastructure.

## Key Elements
* Users: Patient, Clinic Receptionist/Staff, Clinician/Doctor, Billing Specialist, Compliance/IT Administrator
* External Systems: Insurance/Third-Party Payer Gateway, External Lab & Imaging Systems
* Containers: API Gateway, Patient Registration, Appointment Scheduling, EMR Service, Billing & Insurance Service
* Infrastructure: Kubernetes (`on-prem-k8s` and `eu-central-1`), Istio Service Mesh, Message Brokers

## Relationships
* Users to API Gateway: HTTPS with multi-factor authentication (MFA) and attribute-based access control (ABAC).
* EMR & Billing Services to External Systems: HL7 FHIR APIs and secure asynchronous retry queues.
* Cross-Cluster Communication: mTLS encrypted tunnels managed by Istio service mesh between `on-prem-k8s` and `eu-central-1`.

## Technology Stack
* Orchestration: Kubernetes (`on-prem-k8s`, `eu-central-1`) for active-active hybrid deployment and 99.99% uptime.
* Networking & Security: Istio Service Mesh, mTLS, Kubernetes NetworkPolicies, and Falco for zero-trust segmentation and runtime monitoring.
* Data & Observability: AES-256 with customer-managed keys (CMK) for data at rest, OpenTelemetry for distributed tracing, and tiered storage for 10-year retention.

## Rationale
This architecture uses active-active hybrid Kubernetes clusters paired with Istio service mesh to achieve strict 99.99% availability and data residency compliance. Comprehensive encryption, ABAC, and asynchronous queues protect sensitive patient data and ensure uninterrupted clinical and financial workflows.