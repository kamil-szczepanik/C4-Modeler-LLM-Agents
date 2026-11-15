## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and the US. The Integration Service container routes e-prescriptions while strictly enforcing regional data residency and interoperability standards.

## Key Elements
- Integration Service: Container deployed on Google Kubernetes Engine (GKE) using Go.
- E-Prescription Router Component: Go component that orchestrates and routes prescription payloads.
- Data Residency Guard Component: Go component that validates regional routing rules and prevents cross-region data leaks.
- EU Adapter Component: Go component that translates models to National e-Prescription Standards.
- US Adapter Component: Go component that formats messages into HL7 FHIR.
- External Systems: EU National E-Prescription Gateways and US Surescripts / Pharmacy Clearinghouses.
- Audit & Traceability Ledger: Cloud Pub/Sub and BigQuery.

## Relationships
- E-Prescription Router -> Data Residency Guard: Validates regional routing rules [In-memory function call]
- Data Residency Guard -> EU Adapter: Dispatches EU-bound payloads [In-memory]
- Data Residency Guard -> US Adapter: Dispatches US-bound payloads [In-memory]
- Data Residency Guard -> Audit & Traceability Ledger: Emits routing audit events [Cloud Pub/Sub]
- EU Adapter -> EU National E-Prescription Gateways: Sends prescriptions [HTTPS / REST]
- US Adapter -> US Surescripts: Submits e-prescriptions [HL7 FHIR / HTTPS]

## Technology Stack
- Go: Chosen for the Integration Service and its internal components due to strong performance and network-bound routing capabilities.
- HL7 FHIR / HTTPS: Used for US prescription interoperability with Surescripts.
- National e-Prescription Standards / REST: Used for EU prescription interoperability.
- Cloud Pub/Sub: Used for asynchronous event emission to the audit ledger.

## Rationale
This architecture fits the requirements by isolating regional integration logic within dedicated adapters to satisfy local healthcare standards. Furthermore, the explicit Data Residency Guard enforces compliance with GDPR and HIPAA by guaranteeing region-locked data handling.