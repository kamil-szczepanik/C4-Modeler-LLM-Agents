## Overview
The Cross-Border Telehealth Platform provides video consultations, e-prescriptions, and an AI symptom checker for patients across the EU and US. It ensures strict data residency, regulatory compliance, and reliable cross-border health service delivery.

## Key Elements
* Patients and Licensed Clinicians (Users)
* Kong API Gateway/BFF (Container)
* Node.js E-Prescription Service (Container)
* Prescription API Controller (Component)
* Prescription Domain Service (Component)
* Gateway Integration Adapter (Component)
* Outbox Event Publisher (Component)
* Prescription Status Component (Component)
* GCP Cloud SQL (PostgreSQL) (Data Store)
* GCP Cloud Pub/Sub (Messaging)
* National E-Prescription Gateways and Pharmacy Networks (External System)

## Relationships
* Kong API Gateway -> Prescription API Controller: Routes e-prescription requests [gRPC / Anthos Service Mesh with mTLS]
* Prescription API Controller -> Prescription Domain Service: Invokes domain logic [In-process, Function Call]
* Prescription Domain Service -> Gateway Integration Adapter: Delegates external transmission [In-process]
* Gateway Integration Adapter -> National E-Prescription Gateways: Transmits prescriptions [HL7 FHIR / National Standards over mTLS]
* Prescription Domain Service -> Outbox Event Publisher: Persists events for asynchronous processing [In-process]
* Outbox Event Publisher -> GCP Cloud Pub/Sub: Publishes prescription events [GCP Pub/Sub API]
* Prescription Status Component -> GCP Cloud SQL (PostgreSQL): Manages state and metadata [PostgreSQL Protocol over TLS, CMEK encrypted]

## Technology Stack
* Node.js & TypeScript: Runtime and language for the e-prescription service ensuring rapid event processing
* Express.js / Fastify: Framework for the Prescription API Controller handling gRPC/HTTP traffic
* Prisma / TypeORM: ORM for database integration supporting secure regional queries
* GCP Cloud SQL (PostgreSQL): Relational database with region-segregated CMEK encryption for regional data residency
* GCP Cloud Pub/Sub: Messaging service providing asynchronous retries and dead-letter queue functionality

## Rationale
This architecture uses the Transactional Outbox Pattern and GCP Cloud Pub/Sub to guarantee reliable prescription delivery during intermittent network outages. Component-level decomposition and regional CMEK encryption ensure strict compliance with GDPR, HIPAA, and regional data residency constraints.