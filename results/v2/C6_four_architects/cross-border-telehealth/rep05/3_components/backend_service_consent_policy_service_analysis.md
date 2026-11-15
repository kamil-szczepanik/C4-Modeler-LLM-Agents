## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. The system enforces strict regional data residency and compliance using GCP infrastructure.

## Key Elements
- API Router & Controller Component
- Consent & Policy Engine Component
- FHIR & E-Prescription Domain Component
- Audit & Traceability Logger Component
- Data Residency Router Component
- AI Traceability & Logging Interceptor Component
- E-Prescription Translation Adapter Component

## Relationships
- API Router & Controller -> Consent & Policy Engine: Evaluates access permissions via in-memory gRPC
- API Router & Controller -> Data Residency Router: Determines target region for data mutations via in-process method calls
- Data Residency Router -> Cloud SQL: Enforces regional connection pools via JDBC over TLS
- FHIR & E-Prescription Domain -> E-Prescription Translation Adapter: Hands off clinical orders via in-process calls
- E-Prescription Translation Adapter -> Integration Adapter Container: Dispatches formatted prescriptions via gRPC
- AI Traceability & Logging Interceptor -> Cloud Storage (WORM): Writes immutable audit logs via HTTPS/Storage API

## Technology Stack
- Spring Boot / FastAPI: Implements API routing and control logic
- Open Policy Agent (OPA) + Java/Python: Enforces GDPR and HIPAA consent rules
- HAPI FHIR / Spring Data: Manages clinical data models and standards
- Spring Cloud / Custom Middleware: Handles regional routing for data-locality compliance
- Spring AOP / Python Middleware: Captures AI symptom checker inputs and model versions
- Apache Camel: Translates clinical models into regional e-prescription formats

## Rationale
This architecture ensures strict compliance with GDPR, HIPAA, and EU MDR by isolating data residency and consent management within dedicated regional GKE components. It maintains rigorous traceability for AI recommendations and seamless clinical interoperability across international jurisdictions.