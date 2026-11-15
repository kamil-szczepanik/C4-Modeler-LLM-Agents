## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and AI symptom checks for patients across the EU and US. It enforces strict regional data residency, regulatory compliance, and high availability on Google Cloud Platform (GCP).

## Key Elements
- Patients, Clinicians, Regional Pharmacists
- API Gateway (Google Cloud API Gateway)
- Core Services Container (Spring Boot / Java)
- AI Symptom Checker Container (Python / FastAPI)
- Integration Service Container (Node.js / TypeScript)
- Video Media Server (LiveKit / WebRTC)
- Cloud SQL (PostgreSQL) & Memorystore for Redis
- Cloud Storage & Google Cloud Pub/Sub
- Regional Identity Providers

## Relationships
- API Gateway -> Core Services Container: Routes backend requests [gRPC over mTLS]
- Core Services Container -> AI Symptom Checker Container: Sends inference requests [gRPC over mTLS]
- Core Services Container -> Integration Service Container: Dispatches events [Google Cloud Pub/Sub]
- Core Services Container -> Cloud SQL (PostgreSQL): Reads/writes relational data [JDBC / SQL via PgBouncer]
- Core Services Container -> Memorystore for Redis: Evaluates cached consent policies [Redis Protocol over TLS]
- Core Services Container -> Cloud Storage: Stores immutable audit logs [HTTPS / GCP API]

## Technology Stack
- **Languages/Frameworks:** Java / Spring Boot (Core Services), Python / FastAPI (AI Checker), Node.js / TypeScript (Integration Service), Flutter / TypeScript (Web & Mobile Apps)
- **Cloud Provider:** Google Cloud Platform (Regions: `europe-west3`, `us-central1`)
- **Infrastructure & Mesh:** Terraform, Helm, Istio (mTLS service mesh)
- **Data & Caching:** Cloud SQL (PostgreSQL with CMEK), Memorystore for Redis, Cloud Storage (append-only buckets with Object Retention Policies)
- **Resilience & Messaging:** Google Cloud Pub/Sub, Resilience4j (circuit breakers)

## Rationale
Independent regional deployments in `europe-west3` and `us-central1` ensure that EU health data strictly remains in the EU and US data in the US, satisfying GDPR and HIPAA constraints. Integrating dedicated consent caching, circuit breakers, and gRPC over mTLS guarantees low-latency availability and secure data handling for users with unstable rural internet connections.