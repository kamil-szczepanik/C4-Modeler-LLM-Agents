## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient records, scheduling, and billing. It ensures high availability, strict regulatory compliance, and interoperability across clinical environments.

## Key Elements
- Patients, Clinical Staff, Hospital Administrators
- External Lab and Imaging Systems, Third-Party Insurance Clearinghouses
- Global Anycast Load Balancer and API Gateways (Kong)
- Patient Portal (React, Next.js SSR Engine, Node.js Express Portal Gateway, Auth Manager, Notification Dispatcher)
- EMR & Scheduling Service (Java Spring Boot)
- Billing & Insurance Claim Service (Python FastAPI)
- HL7 FHIR Interoperability Engine (Apache Camel)
- Database Tier (PostgreSQL with PgBouncer)
- Messaging & Audit Layer (Apache Kafka, FluentBit, S3)
- Infrastructure (Kubernetes, AWS eu-central-1, on-prem-k8s, Envoy sidecar)

## Relationships
- Global Anycast Load Balancer and API Gateways -> Patient Portal: Routes ingress traffic [HTTPS]
- Patient Portal -> EMR & Scheduling Service: Communicates backend calls [gRPC over mTLS]
- Patient Portal -> Billing & Insurance Claim Service: Communicates financial data [gRPC over mTLS]
- Patient Portal -> Notification Dispatcher: Dispatches async alerts [Apache Kafka]
- Portal Gateway -> Auth Manager: Handles session issuance [HTTPS / OAuth2/OIDC]
- HL7 FHIR Interoperability Engine -> External Lab Systems: Exchanges clinical data [HL7 FHIR REST APIs]

## Technology Stack
- Next.js & React: Delivers server-side rendered, mobile-responsive frontend views with sub-second performance.
- Node.js (Express): Powers the API gateway proxy and notification dispatcher for async event handling.
- Java Spring Boot: Implements high-throughput EMR and scheduling logic with strict concurrency controls.
- Python FastAPI: Handles billing and insurance claim workflows with rapid validation capabilities.
- PostgreSQL with PgBouncer: Provides robust relational data storage with AES-256 encryption at rest.
- Apache Kafka: Enables decoupled, asynchronous messaging for audit trails and notifications.
- Kubernetes & Envoy: Orchestrates active-active hybrid deployment across on-prem-k8s and AWS eu-central-1 with service mesh routing.

## Rationale
This architecture combines active-active Kubernetes clustering with AES-256 encryption and Kafka event-streaming to meet stringent HIPAA/GDPR standards and 99.99% availability. Modular gRPC and FHIR interfaces ensure low-latency performance and seamless clinical system interoperability.