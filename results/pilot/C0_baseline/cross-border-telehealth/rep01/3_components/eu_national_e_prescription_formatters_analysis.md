## Overview
- Spring Boot (Java) container component translating clinical data into national EU e-prescription formats.
- Ensures compliant cross-border prescription delivery to EU National E-Prescription Gateways while maintaining regional data residency.

## Key Elements
- EU National E-Prescription Formatters (Container)
- Template Engine Component (Spring Boot)
- Validation Engine Component (Spring Boot)
- Gateway Connector Component (Spring Boot)
- Go Clinical Workspace Service (Caller)
- EU National E-Prescription Gateways (External System)

## Relationships
- Go Clinical Workspace Service -> EU National E-Prescription Formatters: Invokes serialization [gRPC]
- EU National E-Prescription Formatters -> EU National E-Prescription Gateways: Sends formatted e-prescriptions [REST over HTTPS, mTLS, XMLDSig]
- EU National E-Prescription Formatters -> GCP Secret Manager: Retrieves X.509 client certificates [API]

## Technology Stack
- Java / Spring Boot: Chosen for robust enterprise security and HL7/XML parsing ecosystems (HAPI FHIR, Eclipse Projecteria).
- gRPC / Protocol Buffers: Provides high-throughput, type-safe internal communication with the Go Clinical Workspace Service.
- Resilience4j: Implements circuit breakers and backoff retries for unstable sovereign endpoints.
- OpenTelemetry & GCP Cloud Trace: Captures distributed tracing and compliance metrics.
- Kubernetes (GKE) & Istio: Enforces regional isolation in `europe-west3` and egress traffic control.

## Rationale
- Isolating national formatting logic into a modular Spring Boot architecture prevents regional schema updates from destabilizing the core telehealth platform.
- Strict mTLS, XML digital signatures (XMLDSig), and regional GCP deployment (`europe-west3`) satisfy EU MDR traceability and GDPR data residency mandates.