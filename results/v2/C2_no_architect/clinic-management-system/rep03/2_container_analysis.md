## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for healthcare providers. It delivers high-availability clinical workflows while ensuring strict HIPAA and GDPR compliance.

## Key Elements
* Front Desk Staff, Clinicians, Billing Officers, Patients, Patient Portal Users
* External Lab Systems, External Imaging Systems
* Ingress Controller with OAuth2/OIDC & MFA
* Patient Registration Container
* Appointment Scheduling Container
* EMR Container with Asynchronous Audit Trail
* Billing & Insurance Claim Container
* HL7 FHIR Interoperability Engine
* PostgreSQL/MySQL Hybrid Databases (AES-256)
* WORM-Compliant Log Storage

## Relationships
* Users to Ingress Controller via HTTPS (TLS 1.3)
* Ingress Controller to Containers via mTLS (Istio Service Mesh)
* EMR & Registration Containers to Databases via TCP/AES-256
* HL7 FHIR Engine to External Lab/Imaging Systems via HTTPS/HL7 FHIR REST APIs
* Containers to WORM Storage via gRPC/TLS for Audit Logs

## Technology Stack
* Kubernetes (`on-prem-k8s`, AWS `eu-central-1`) for container orchestration and hybrid scaling
* Istio Service Mesh with Cilium/Falco for mTLS and eBPF runtime security
* PostgreSQL/MySQL with active-active asynchronous replication for data persistence
* OpenTelemetry, Prometheus, and Grafana for distributed tracing and P95 monitoring
* HashiCorp Vault / AWS Secrets Manager for encrypted secret management

## Rationale
Namespace segregation and Istio mTLS enforce Zero Trust boundaries, isolating critical EMR workloads from billing failures to guarantee 99.99% uptime. Asynchronous audit trails and WORM-compliant storage fulfill 10-year HIPAA and GDPR retention mandates without impacting sub-second P95 EMR performance.