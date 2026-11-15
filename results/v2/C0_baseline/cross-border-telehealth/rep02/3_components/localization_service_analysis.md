## Overview
[The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for EU and US patients. The Localization Service manages regional i18n, medical glossaries, and compliance disclaimers under strict data residency mandates.]

## Key Elements
- Localization Controller (NestJS Controller)
- Translation Engine (Component)
- Regional Policy Provider (Component)
- Localization Cache (Google Memorystore Redis)
- Bundle Loader & Verifier (Component)
- GCP Cloud Storage WORM (External Storage)

## Relationships
- API Gateway -> Localization Controller: Routes localization requests [gRPC over mTLS]
- Localization Controller -> Translation Engine: Resolves localized strings [In-process / Function call]
- Localization Controller -> Regional Policy Provider: Fetches compliance text [In-process]
- Translation Engine & Regional Policy Provider -> Localization Cache: Reads cached bundles [Redis Protocol over TLS]
- Bundle Loader & Verifier -> Cloud Storage WORM (GCP): Downloads signed bundles [HTTPS / GCP SDK]

## Technology Stack
- Node.js with NestJS: Chosen for scalable, modular microservice architecture
- Google Memorystore (Redis): Isolated regional caching to enforce data residency
- GCP Cloud Storage WORM: Immutable, versioned storage for compliance bundles
- gRPC over mTLS: Secure, low-latency internal communication via SPIFFE/SPIRE

## Rationale
[Regionalized Redis instances and isolated GCP deployments guarantee GDPR and HIPAA compliance by ensuring EU data never leaves europe-west3. Dynamic bundle verification and cryptographic signing maintain EU MDR traceability and security without requiring full code redeployments.]