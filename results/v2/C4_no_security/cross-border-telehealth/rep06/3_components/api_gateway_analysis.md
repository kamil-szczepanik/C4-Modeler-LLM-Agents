## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It ensures strict regional data residency, regulatory compliance, and resilience for unstable network connections.]

## Key Elements
* Patients (EU/US) and Clinicians/Pharmacists
* GCP Global External HTTP(S) Load Balancing
* Regional API Gateway instances (`europe-west3` and `us-central1`)
* API Gateway Internal Components: Routing & Regional Geo-Dispatcher, Auth & Scope Validator, Resilience Proxy
* Core Telehealth Service, AI Symptom Service, Consent & Identity Container
* Third-Party Video Infrastructure and Redis Cache

## Relationships
* Patients / Clinicians -> GCP Load Balancing -> Regional API Gateway instances [HTTPS / WebSockets]
* Routing & Regional Geo-Dispatcher -> Core Telehealth Service / AI Symptom Service [gRPC / REST]
* Auth & Scope Validator -> Consent & Identity Container [gRPC]
* Resilience Proxy -> Redis [TCP]

## Technology Stack
* GCP Cloud Endpoints / API Gateway: Manages unified routing and API security.
* GCP Global External HTTP(S) Load Balancing: Enforces geographic routing and data residency.
* Redis: Powers low-latency rate limiting and token caching for degraded networks.
* OpenTelemetry / Prometheus / Cloud Monitoring: Provides distributed tracing, observability, and SLO alerting.
* Terraform / ArgoCD: Implements GitOps-based zero-touch deployment and canary releases.

## Rationale
[Two physically isolated regional API Gateway instances enforce strict GDPR and HIPAA data residency requirements. Internal component decomposition and Redis-backed caching maintain low-latency session validation and high availability for rural patients with unstable connections.]