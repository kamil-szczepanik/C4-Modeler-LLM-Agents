## Overview
The system is a hybrid-cloud Clinic Management System designed to handle patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals. Its core purpose is to provide highly available, secure, and interoperable clinical IT operations while strictly maintaining HIPAA and GDPR compliance.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- **External Systems**: Insurance Payers/Clearinghouses, External Labs and Imaging Systems
- **Containers**: API Gateway (Istio, WAF), Patient Portal, Clinical Core (EMR, Scheduling, Billing Reconciliation), Notification & Reminder Container
- **Infrastructure**: Active-active multi-cluster Kubernetes (`on-prem-k8s` and `eu-central-1`) with eBPF-based collectors

## Relationships
- **Users -> API Gateway**: Secure access via HTTPS and OAuth2/MFA [mTLS via Istio]
- **API Gateway -> Patient Portal**: Routes authenticated portal traffic [mTLS via Istio]
- **API Gateway -> Clinical Core**: Routes workflow and transaction requests to internal services [mTLS via Istio]
- **API Gateway -> Notification & Reminder Container**: Routes notification events [mTLS via Istio]
- **External Systems -> API Gateway**: Integrates via HL7 FHIR APIs with schema validation [mTLS via Istio]

## Technology Stack
- **API Gateway / Service Mesh**: Istio with integrated WAF for ingress security, traffic routing, and canary deployments
- **Security & Identity**: Zero-Trust architecture with OAuth2 token exchange for short-lived JWTs/SPIFFE IDs and ABAC/RBAC
- **Deployment & Infrastructure**: Hybrid-cloud Kubernetes (`on-prem-k8s` and `eu-central-1`) managed via GitOps
- **Observability**: Asynchronous eBPF-based telemetry collection and immutable SIEM logging with automated PII/PHI masking

## Rationale
This architecture ensures 99.99% high availability through an active-active multi-cluster hybrid topology while maintaining strict sub-second performance for clinicians. The centralized Istio/WAF API Gateway enforces mandatory HIPAA/GDPR compliance, zero-trust security, and seamless interoperability via HL7 FHIR.