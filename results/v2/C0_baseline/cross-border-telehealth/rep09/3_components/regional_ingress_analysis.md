## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency while ensuring high availability for rural, low-bandwidth users.

## Key Elements
* Patients and Licensed Clinicians (End Users)
* Compliance Officers and Auditors (Personas)
* Regional Ingress Container (GCP Cloud Armor, Global External HTTP(S) Load Balancer, Envoy Edge Proxy, Envoy WASM Route & Policy Enforcer)
* Downstream Containers (Flutter Frontend, Go/WebRTC Telehealth Service, Java/Spring Boot Prescription Service, Python/FastAPI AI Orchestrator, Keycloak Identity Service)
* External Systems (EU National E-Prescription Gateways, US Pharmacy Networks, AI Symptom Checker Engine)

## Relationships
* Patients & Clinicians -> Regional Ingress: Accesses platform features via HTTPS and WSS
* Compliance Officers -> Regional Ingress: Accesses audit logs and controls via HTTPS
* Global External HTTP(S) Load Balancer -> Envoy Edge Proxy: Forwards TCP/HTTPS streams via internal VPC
* Envoy Edge Proxy -> Route & Policy Enforcer (WASM): Invokes in-process synchronous inspection
* Route & Policy Enforcer -> Downstream Containers: Routes verified traffic via gRPC and mTLS (SPIFFE/SPIRE)

## Technology Stack
* GCP (europe-west3, us-central1): Cloud provider and target regions enforcing data residency
* Cloud Armor: Edge-level DDoS defense, adaptive rate limiting, and geo-detection
* Envoy Edge Proxy: TLS 1.3 termination, WebSocket upgrades, and traffic routing
* Envoy WASM Extension: Custom policy enforcement, JWT validation, and geo-pinning
* ArgoCD: GitOps-based regional configuration deployments
* Prometheus & OpenTelemetry: Observability and distributed tracing for latency tracking

## Rationale
This architecture uses edge-level geo-steering and regional ingress isolation to strictly enforce GDPR and HIPAA data residency constraints (R-05). Deploying Envoy with WASM and mTLS secures cross-border boundaries while supporting low-bandwidth optimization (R-06) and verifiable audit trails (R-07).