## Overview
A cross-border telehealth platform providing video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. The system ensures regional data residency and strict compliance with GDPR, HIPAA, and EU MDR.

## Key Elements
- Patients and Licensed Clinicians (Users)
- React / Flutter Web and Mobile Apps Container
- Google Cloud API Gateway / Region Router
- Go / Spring Boot Core Telehealth Backends
- LiveKit / WebRTC SFU Video Media Servers
- Python / FastAPI + TensorFlow AI Symptom Checker
- Open Policy Agent (OPA) Consent Management Container
- Google Cloud SQL & Cloud Storage with Cloud KMS

## Relationships
- Patients & Clinicians -> React / Flutter Web and Mobile Apps via HTTPS and WebSockets
- React / Flutter Web and Mobile Apps -> Google Cloud API Gateway / Region Router via HTTPS
- API Gateway -> Go / Spring Boot Core Backends via gRPC and REST
- WebRTC Media Client Wrapper -> LiveKit / WebRTC SFU via WebRTC over UDP/TCP via Global TURN/STUN

## Technology Stack
- React & Flutter: Frontend web and mobile application frameworks for cross-platform UI.
- SQLCipher & Web Crypto API: Encrypted local storage for protecting PHI on client devices.
- LiveKit Client SDK: Manages adaptive bitrate video streaming for WebRTC.
- Google Cloud Platform (GCP): Cloud provider utilizing `europe-west3` and `us-central1` regions for data residency.
- OAuth 2.0 with PKCE & JWT: Secure authentication and short-lived session management.

## Rationale
This architecture enforces strict regional data boundaries and regulatory compliance for healthcare operations. Client-side encryption and offline-first capabilities maintain high availability and security for users with unstable internet connections.