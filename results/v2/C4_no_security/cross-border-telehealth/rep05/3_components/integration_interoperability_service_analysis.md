## Overview
The Cross-Border Telehealth Platform provides secure video consultations, e-prescriptions, and an AI symptom checker for patients in the EU and US. It enforces strict regional data residency, GDPR/HIPAA compliance, and interoperability with regional healthcare standards.

## Key Elements
- Patients and Licensed Clinicians (Users)
- External Pharmacies, National Health/Insurance Systems, Identity Providers (External Systems)
- API Gateway / BFF (Envoy / Cloud Endpoints)
- Integration & Interoperability Service (Apache Camel / Spring Integration container)
- API Router & Transformer Component
- US FHIR Connector Component & EU National Standard Connector Component
- Audit & Logging Interceptor & Dead-Letter Queue (DLQ) Handler
- Regional Relational Database (Google Cloud SQL PostgreSQL) & Regional Data Warehouse (BigQuery)

## Relationships
- API Gateway / BFF -> Integration & Interoperability Service: Routes integration requests via [gRPC / REST]
- API Router & Transformer -> US / EU Connectors: Delegates payloads via [Direct Java Method Calls]
- US FHIR Connector -> External Pharmacies: Transmits prescriptions using [REST / TLS]
- EU National Standard Connector -> National Health Systems: Transmits prescriptions using [REST/SOAP / TLS]
- Connectors -> DLQ Handler: Captures failed delivery messages via [GCP Pub/Sub]
- Audit & Logging Interceptor -> BigQuery: Streams scrubbed compliance logs via [gRPC / TLS]

## Technology Stack
- Google Cloud Platform (GCP): Target cloud provider utilizing `europe-west3` and `us-central1` regions for strict data residency.
- Apache Camel / Spring Integration: Powers message routing and format translation in the interoperability service.
- Java / Spring Boot: Implements dedicated US and EU regional connector components.
- GCP Pub/Sub: Manages dead-letter queues and asynchronous message retries for failed delivery requests.
- OpenTelemetry & BigQuery: Provides secure telemetry, PAI/PHI log scrubbing, and regional audit logging.

## Rationale
The modular decomposition of the Integration & Interoperability Service isolates frequent, independent updates to EU national e-prescription standards from US operations, minimizing blast radius. GCP regional deployments and Pub/Sub dead-letter queues ensure strict GDPR/HIPAA data residency compliance and robust handling of unstable network conditions.