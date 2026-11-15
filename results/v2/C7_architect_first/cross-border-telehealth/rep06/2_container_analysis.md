## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces regional data residency and regulatory compliance under GDPR and HIPAA.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Regional GKE Clusters (`europe-west3`, `us-central1`)
* API Gateway (Cloud Armor, Cloud Load Balancing)
* Core Telehealth Backend (Node.js, Express)
* AI Symptom Checker Service (Python, FastAPI)
* Video Media Router (Mediasoup SFU)
* Consent & Preference Management Service (Node.js, Express)
* Patient PWA & Clinician Dashboard Frontends (React, Cloud Storage, Cloud CDN)
* Data Tier (Cloud SQL PostgreSQL, Cloud Storage)

## Relationships
* Patient/Clinician PWA $\rightarrow$ API Gateway via HTTPS/WSS/WebRTC
* API Gateway $\rightarrow$ Core Backend, Consent Service via gRPC / mTLS
* Core Backend $\rightarrow$ Regional Data Tier via TCP/PostgreSQL
* AI Symptom Checker Service $\rightarrow$ Core Backend via gRPC / mTLS

## Technology Stack
* Google Cloud Platform: Selected for regional availability (`europe-west3`, `us-central1`) ensuring data residency.
* Node.js / Express & Python / FastAPI: Used for lightweight, asynchronous microservices and AI isolation.
* Mediasoup WebRTC SFU: Powers real-time video consultations in degraded network conditions (<300 kbit/s).
* Cloud SQL PostgreSQL & Cloud Storage: Provides region-isolated data storage encrypted with CMEK via Cloud KMS.
* Istio Service Mesh & Kubernetes NetworkPolicies: Enforces strict zero-trust mTLS and namespace isolation.

## Rationale
Regional GKE deployment guarantees that EU health data remains in the EU and US data in the US, meeting GDPR and HIPAA constraints. Isolated microservices and encrypted local caching ensure regulatory compliance, MDR traceability, and rural availability without compromising security.