## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data isolation to comply with GDPR and HIPAA mandates.

## Key Elements
- Patients and Clinicians (Users)
- Global HTTPS Load Balancer with Geo-routing (GCP)
- EU Telehealth System (GCP europe-west3)
- US Telehealth System (GCP us-central1)
- Regional Pharmacy Networks and Health Information Exchanges (HIEs)
- AI Model Provider / Inference Service
- WebRTC/SFU Media Relay

## Relationships
- Patients & Clinicians to Global Load Balancer via HTTPS and WebRTC
- Global Load Balancer to Regional Systems via Regional Routing
- Regional Systems to Pharmacy Networks and HIEs via mTLS, REST, HL7 FHIR, and national gateways
- Regional Systems to AI Model Provider via mTLS and HTTPS
- EU Telehealth System to US Telehealth System via mTLS and gRPC for consent-driven queries

## Technology Stack
- Google Cloud Platform (GCP) with regions europe-west3 and us-central1 for data residency
- GCP Cloud Armor and VPC Service Controls for security isolation
- TLS 1.3 and mutual TLS (mTLS) for secure communication
- HL7 FHIR for US interoperability and national standards for EU e-prescriptions
- WebRTC with adaptive bitrate streaming for low-bandwidth availability

## Rationale
The multi-region GCP architecture guarantees that EU health data remains in Europe and US data in the US, fulfilling GDPR and HIPAA constraints. Geo-routing, adaptive WebRTC streaming, and isolated regional services ensure high availability and compliance across diverse network conditions.