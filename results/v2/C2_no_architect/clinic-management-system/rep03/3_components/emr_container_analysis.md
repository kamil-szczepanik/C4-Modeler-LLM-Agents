## Overview
The Clinic Management System is a hybrid-cloud healthcare platform designed to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent security, and interoperability for medium-sized hospitals and clinics.

## Key Elements
- Users: Front Desk Staff, Clinicians, Billing Officers, Patients, Patient Portal Users
- External Systems: Lab Systems, Imaging Systems
- Core Containers: Ingress Controller, Patient Registration, Appointment Scheduling, EMR, Billing & Insurance Claim
- Interoperability Engine: HL7 FHIR Interoperability Engine
- Infrastructure & Storage: PostgreSQL/MySQL Hybrid Databases, WORM-Compliant Log Storage, Istio Service Mesh, HashiCorp Vault, Kubernetes (`on-prem-k8s`, `eu-central-1`)

## Relationships
- Ingress Controller -> EMR Container: Routes authenticated traffic [mTLS via Istio Service Mesh]
- HL7 FHIR Interoperability Engine -> EMR Container: Ingests external lab and diagnostic reports [HTTPS/REST via mTLS]
- EMR Container -> PostgreSQL/MySQL Hybrid Databases: Persists and retrieves encrypted medical records [TCP/AES-256]
- EMR Container -> WORM-Compliant Log Storage: Sends cryptographically signed asynchronous audit logs [gRPC/TLS]

## Technology Stack
- Container Orchestration: Kubernetes with ArgoCD for GitOps deployments to guarantee zero-downtime upgrades and 99.99% uptime.
- Networking & Security: Istio Service Mesh for mTLS, OAuth2/OIDC for RBAC JWT claims, HashiCorp Vault for secrets management.
- Observability & Monitoring: OpenTelemetry sidecars, Prometheus, and KEDA with Kubernetes Horizontal Pod Autoscalers (HPA).
- Runtime & Compliance: Cilium Tetragon for eBPF-based runtime security, LUKS for encrypted ephemeral local volumes, and PostgreSQL/MySQL for hybrid persistence.

## Rationale
This architecture uses microservices on Kubernetes across hybrid clusters (`on-prem-k8s` and `eu-central-1`) to achieve 99.99% availability and <1s P95 EMR load times. Strict security controls, including AES-256 encryption, WORM-compliant auditing, and zero-trust pod standards, ensure full HIPAA and GDPR compliance.