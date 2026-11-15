## Overview
[Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The system ensures strict regional data residency, regulatory compliance, and high availability across unstable connections.]

## Key Elements
- Patients and Clinicians (Users)
- Web Application (React) and Mobile App (Flutter)
- Ingress Layer (Google Cloud DNS, Google Cloud Armor, Google Cloud Certificate Manager, Google Cloud Global HTTPS Load Balancer with Regional Backend Multiplexer, and Ingress Access Logging)
- API Gateway (Google Cloud API Gateway)
- Core Services (Core Telehealth Service, Video Consultation Service, AI Symptom Checker Service, Consent Management Service, E-Prescription & Interoperability Gateway, Audit & Compliance Logging Service)
- Data and Messaging (Google Cloud Pub/Sub, Google Cloud SQL for PostgreSQL)

## Relationships
- Patients/Clinicians -> Ingress Layer: Accesses platform [HTTPS/WSS via Google Cloud DNS geo-routing]
- Edge Security & WAF -> Global HTTPS Load Balancer: Passes filtered traffic [Internal GCP Network]
- SSL/TLS Termination Component -> Regional Backend Multiplexer: Forwards decrypted traffic [Internal Proxy Routing]
- Global HTTPS Load Balancer -> API Gateway (`europe-west3` / `us-central1`): Proxies regionally segregated ingress traffic [mTLS over Internal GCP VPC]
- Edge Security & WAF / Global HTTPS Load Balancer -> Ingress Access Logging Component: Emits security events and access logs [Cloud Pub/Sub / Cloud Logging]

## Technology Stack
- Google Cloud Platform (GCP): Primary cloud provider operating in `europe-west3` and `us-central1` regions for strict data residency.
- Google Cloud DNS: Provides geo-routing to direct EU traffic to `europe-west3` and US traffic to `us-central1`.
- Google Cloud Armor: Edge security and WAF providing OWASP Top 10 protection and rate-limiting.
- Google Cloud Global HTTPS Load Balancer: Terminates TLS 1.3, handles WebSocket upgrades, and utilizes Regional Backend Multiplexing.
- LiveKit: Manages video consultations with support for degraded network modes.

## Rationale
[This architecture enforces strict regional data residency for GDPR and HIPAA compliance by routing EU and US traffic to isolated GCP regions via dedicated load balancer multiplexing. Edge security, mTLS communication, and comprehensive access logging ensure system accountability and resilience for rural users.]