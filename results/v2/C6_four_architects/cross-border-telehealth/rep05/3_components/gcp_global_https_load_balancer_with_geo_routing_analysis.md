## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The architecture uses a globally distributed load balancer to enforce regional data residency and compliance.

## Key Elements
* Patients and Clinicians (Users)
* GCP Global External HTTP(S) Load Balancer (Frontend IP & SSL Termination)
* Google Cloud Armor (Security Policy Enforcer)
* GCP URL Map (Geo-Routing Engine & Geo-Header Injector)
* GCP Backend Services & Network Endpoint Groups (Regional Backend Selectors)
* GCP HTTP(S) Health Checks (Global Health Checker)
* EU Telehealth System (GCP `europe-west3`)
* US Telehealth System (GCP `us-central1`)

## Relationships
* Patients and Clinicians -> GCP Global External HTTP(S) Load Balancer [HTTPS/TLS 1.3]
* Frontend IP & SSL Termination -> Google Cloud Armor [Internal]
* Geo-Routing Engine -> Geo-Header Injector [Internal]
* Regional Backend Selectors -> EU Telehealth System [HTTPS/gRPC to `europe-west3`]
* Regional Backend Selectors -> US Telehealth System [HTTPS/gRPC to `us-central1`]
* Global Health Checker -> EU and US Telehealth Systems [HTTPS]

## Technology Stack
* GCP Global External HTTP(S) Load Balancer: Provides Anycast IP and global traffic distribution.
* Google Cloud Armor: Enforces WAF rules and rate limiting for security compliance.
* GCP URL Maps & Network Endpoint Groups: Routes traffic based on client geolocation headers.
* GCP HTTP(S) Health Checks: Monitors regional backend availability without violating data isolation.

## Rationale
This architecture leverages native GCP primitives to enforce strict regional data residency (R-05) by segregating EU and US traffic into distinct cloud regions (`europe-west3` and `us-central1`). Edge security and geo-routing ensure compliance with GDPR and HIPAA while maintaining high availability.