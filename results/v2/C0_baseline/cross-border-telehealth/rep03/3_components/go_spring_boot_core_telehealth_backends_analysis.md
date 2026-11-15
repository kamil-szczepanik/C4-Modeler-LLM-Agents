## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. It enforces strict regional data residency, GDPR/HIPAA compliance, and resilience for rural connectivity.

## Key Elements
* React / Flutter Web and Mobile Apps
* Google Cloud API Gateway / Region Router
* Go Consultation & API Gateway Pod (Go)
* Spring Boot Integration & Transformation Pod (Spring Boot)
* LiveKit / WebRTC SFU Video Media Servers
* Python / FastAPI + TensorFlow AI Symptom Checker Container
* Open Policy Agent (OPA) Consent Management Container
* E-Prescription Integration Service
* Google Cloud SQL & Cloud Storage (with Cloud KMS)
* Regional Identity Providers (IDP) and External Payment Gateways

## Relationships
* Google Cloud API Gateway / Region Router -> Go Consultation & API Gateway Pod: Routes traffic [gRPC over Istio mTLS mesh]
* Go Consultation & API Gateway Pod -> Spring Boot Integration & Transformation Pod: Mediates clinical workflows [gRPC over Istio mTLS mesh]
* Go Consultation & API Gateway Pod -> LiveKit / WebRTC SFU Video Media Servers: Initiates video session streams [WebRTC]
* Go Consultation & API Gateway Pod -> Python / FastAPI + TensorFlow AI Symptom Checker Container: Requests symptom analysis [gRPC over Istio mTLS mesh]
* Go Consultation & API Gateway Pod -> Open Policy Agent (OPA) Consent Management Container: Evaluates fine-grained consent [gRPC over Istio mTLS mesh]
* Spring Boot Integration & Transformation Pod -> E-Prescription Integration Service: Dispatches e-prescriptions [REST, HL7 FHIR]
* Go & Spring Boot Pods -> Google Cloud SQL & Cloud Storage: Queries regional databases and stores encrypted PHI/PII [SQL / HTTPS]

## Technology Stack
* GCP (europe-west3, us-central1): Target cloud provider ensuring regional data residency.
* Go: Powers high-concurrency API routing and real-time consultation workflow orchestration.
* Spring Boot: Powers complex HL7 FHIR and national e-prescription format transformations.
* Python / FastAPI + TensorFlow: Hosts the AI symptom checker container for traceable medical outputs.
* Open Policy Agent (OPA): Evaluates dynamic, purpose-based patient consent.
* LiveKit / WebRTC SFU: Delivers low-latency video streaming in degraded network conditions.
* Google Cloud KMS: Manages application-layer envelope encryption for sensitive patient data.

## Rationale
Decoupling the lightweight Go orchestrator from the JVM-based Spring Boot transformer prevents heavy batch workloads from degrading real-time video sessions in rural areas. Synchronous gRPC over Istio mTLS combined with OPA and regional Cloud SQL isolation guarantees strict compliance with HIPAA, GDPR, and EU MDR audit requirements.