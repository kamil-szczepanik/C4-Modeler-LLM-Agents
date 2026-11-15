## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It enforces strict regional data residency, HIPAA/GDPR compliance, and EU MDR traceability on GCP.

## Key Elements
* Patients & Clinicians (Users)
* Web & Mobile Client Apps (Flutter/React Native)
* API Gateway (Google Cloud API Gateway / Envoy)
* Core Telehealth Service (Go / gRPC & REST)
* Video Consultation Service (Mediasoup SFU on GCE)
* AI Symptom Checker Container (Python / FastAPI + PyTorch)
* Integration Service (Java / Spring Boot)
* Databases (Cloud SQL PostgreSQL & Cloud Storage)
* Infrastructure (Google Kubernetes Engine - GKE)
* Message Broker (Google Cloud Pub/Sub)
* External Systems (EU National e-Prescription Gateways, US Pharmacy Networks, Regional IdPs)

## Relationships
* Client Apps to API Gateway via HTTPS (TLS 1.3) and WebRTC
* API Gateway to Core Telehealth Service via gRPC over mTLS (Istio service mesh)
* Core Telehealth Service to Integration Service via Google Cloud Pub/Sub (regional topics)
* Integration Service to EU Gateways and US Pharmacy Networks via REST/SOAP
* AI Symptom Checker to Core Telehealth Service via internal gRPC

## Technology Stack
* Google Cloud Platform (`europe-west3`, `us-central1`) for regional data residency
* Google Kubernetes Engine (GKE) for zero-downtime container orchestration
* Istio Service Mesh for zero-trust mTLS and network policies
* Google Cloud Pub/Sub for asynchronous e-prescription messaging and resilience
* Cloud SQL PostgreSQL and Cloud Storage with CMEK for encrypted regional data persistence
* OpenTelemetry for distributed tracing and compliance auditability

## Rationale
This regionalized GCP architecture guarantees data residency compliance by isolating EU and US workloads. It ensures high availability for rural users through adaptive WebRTC streaming and resilient asynchronous messaging.