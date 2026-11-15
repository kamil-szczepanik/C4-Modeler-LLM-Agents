## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, EMRs, scheduling, and billing. Its core purpose is to ensure high availability and HIPAA/GDPR compliance for medium-sized clinics and hospitals.

## Key Elements
- Patients, Clinicians, Administrative Staff, Billing Officers (Users)
- Clinic Management System (Software System)
- Insurance/Payer Gateways (External System)
- External Lab/Imaging Systems (External System)
- Identity Provider (IdP) (External System)
- Kubernetes On-Premises (`on-prem-k8s`) & AWS (`eu-central-1`) (Containers/Infrastructure)

## Relationships
- Users to Clinic Management System via HTTPS/TLS 1.3 with Multi-Factor Authentication
- Clinic Management System to Identity Provider via OIDC/OAuth2 for authentication
- Clinic Management System to Insurance/Payer Gateways via REST/JSON over HTTPS for claims
- Clinic Management System to External Lab/Imaging Systems via HL7 FHIR APIs (RESTful)
- Hybrid inter-cluster transport secured via encrypted IPSec VPN tunnels

## Technology Stack
- Kubernetes (`on-prem-k8s` and AWS `eu-central-1`): Active-active hybrid deployment ensuring 99.99% uptime
- AES-256: Enforces strict data-at-rest encryption for HIPAA/GDPR compliance
- OpenTelemetry: Unified observability pipeline tracking sub-second P95 EMR load times
- Edge-local caching proxies: Provides offline/degraded mode resilience during WAN outages

## Rationale
The hybrid architecture balances strict on-premises data control for clinical safety with AWS scalability for billing and analytics. This setup guarantees 99.99% availability and 10-year retention while maintaining robust compliance.