## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The architecture enforces strict regional data residency while ensuring high availability and compliance with GDPR and HIPAA.

## Key Elements
* Anycast IP Frontend (`HTTP/2`, `gRPC`)
* Cloud Armor Security Policy Engine
* URL Map & Redirect Component
* Region-Selection Edge Service (Cloud Storage/Cloud CDN)
* Regional Backend Services (`europe-west3`, `us-central1`)
* Regional API Gateways (Kong / GCP API Gateway)

## Relationships
* Web Applications -> Global External HTTP(S) Load Balancers: Sends user requests [HTTPS]
* Native Mobile Apps -> Global External HTTP(S) Load Balancers: Sends user requests [HTTPS / gRPC]
* Global External HTTP(S) Load Balancers -> Regional API Gateways: Routes traffic to regional deployment zones [HTTPS]
* Global External HTTP(S) Load Balancers -> Region-Selection Edge Service: Routes ambiguous or unrouted requests to static edge assets [HTTPS]

## Technology Stack
* GCP Global External HTTP(S) Load Balancer: Terminates TLS 1.3 globally and executes geo-routing policies.
* Google Cloud Armor: Mitigates DDoS attacks and enforces WAF and geo-access rules.
* Terraform: Automates CI/CD validation pipelines for infrastructure and routing policy updates.
* Cloud Logging and Cloud Monitoring: Captures observability metrics, security logs, and latency SLOs.

## Rationale
This architecture ensures strict compliance with GDPR and HIPAA by deterministically routing regional data to dedicated GCP regions while providing graceful edge fallbacks for ambiguous client connections. It maintains high availability for rural patients through resilient edge caching and automated backend failover.