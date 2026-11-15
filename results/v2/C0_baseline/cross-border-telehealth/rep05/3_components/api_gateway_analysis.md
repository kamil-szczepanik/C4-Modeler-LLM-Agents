## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The architecture enforces regional data residency and compliance using GCP regions (`europe-west3` and `us-central1`).

## Key Elements
* Patients and Licensed Clinicians (EU/US)
* Web & Mobile Client Apps (Flutter / React Native)
* API Gateway Container (Envoy / GCP Cloud Endpoints)
* Core Telehealth Service (Go / gRPC)
* AI Symptom Checker Service (Python / FastAPI on Cloud Run)
* Video Session Manager (Node.js)
* E-Prescription Integrator (Java / Spring Boot)
* Regional Data Storage & Audit Layer (Cloud SQL, BigQuery)
* Regional Identity Providers

## Relationships
* Web & Mobile Client Apps -> API Gateway: Connects via [HTTPS] with Anycast IP and Cloud Load Balancing
* API Gateway -> Regional Identity Providers: Validates authentication tokens via [OAuth 2.0 / OIDC, HTTPS]
* API Gateway -> Core Telehealth Service: Routes requests using [internal gRPC over HTTP/2, mTLS via SPIFFE/SPIRE]
* API Gateway -> AI Symptom Checker Service: Proxies requests with [W3C Trace Context and gRPC]
* API Gateway -> Video Session Manager: Routes control plane traffic using [gRPC]
* API Gateway -> E-Prescription Integrator: Routes prescription requests using [gRPC]

## Technology Stack
* Envoy Proxy: Deployed as the API Gateway for geo-routing, TLS termination, and traffic shaping.
* GCP Cloud Load Balancing: Utilizes Anycast IPs to reduce connection setup latency for rural users.
* gRPC over HTTP/2: Powers low-latency internal communication between the API Gateway and backend microservices.
* WASM / Lua Filters: Custom Envoy filters used for consent metadata extraction and context handling.
* SPIFFE / SPIRE: Implements Zero Trust mTLS for secure service-to-service communication.

## Rationale
This architecture ensures strict GDPR and HIPAA compliance by isolating regional data traffic while supporting robust security controls. Envoy filters, Anycast routing, and dedicated traffic segregation guarantee high availability and low-latency performance for users on unstable network connections.