## Overview
The Clinic Management System is a hybrid cloud clinical IT platform designed to manage patient admissions, electronic medical records, scheduling, and billing. It provides high availability, stringent compliance, and seamless interoperability for medium-sized hospitals and clinics.

## Key Elements
- Clinic Staff and Patients
- Single Page Application (React)
- API Gateway (Edge Routing, OAuth2/OIDC)
- Patient Management, EMR, Scheduling, and Billing Microservices
- HL7 FHIR Integration Container (Apache Camel)
- Inbound FHIR Router, Data Mapper, Outbound Dispatcher, and FHIR Validation & Compliance Engine
- PostgreSQL Database, Redis Cache, Elasticsearch Audit Trail, Messaging Backbone (Apache Kafka)
- External Systems: Insurance Gateways, Lab and Imaging Systems, Identity Provider

## Relationships
- Single Page Application -> API Gateway: Manages user requests [HTTPS/REST]
- API Gateway -> Microservices: Routes internal API calls [gRPC/HTTP]
- HL7 FHIR Integration Container -> Lab and Imaging Systems: Communicates diagnostic data [HL7 FHIR APIs over HTTP/2, TLS 1.3]
- Inbound FHIR Router -> Data Mapper: Parses and forwards incoming payloads [Camel Direct Endpoints]
- Data Mapper -> FHIR Validation & Compliance Engine: Evaluates resource integrity [Camel Direct Endpoints]
- FHIR Validation & Compliance Engine -> Outbound Dispatcher: Queues validated payloads [Camel SEDA Queues]
- Outbound Dispatcher -> Messaging Backbone: Publishes integration events [Apache Kafka]
- Microservices -> PostgreSQL Database: Persists clinical data with AES-256 [SQL]

## Technology Stack
- React: Powers the Single Page Application for low latency EMR screens (<1s P95)
- Kubernetes: Orchestrates containers across on-prem-k8s and eu-central-1 for 99.99% active-active uptime
- Apache Camel & HAPI FHIR: Powers the HL7 FHIR Integration Container and Validation Engine for standard clinical interoperability
- PostgreSQL & Elasticsearch: Secures operational data (AES-256 at rest) and maintains HIPAA/GDPR audit trails
- Apache Kafka: Acts as the messaging backbone for decoupled, fault-tolerant event processing

## Rationale
This architecture uses an active-active hybrid Kubernetes deployment with containerized microservices to guarantee 99.99% availability and high performance. Apache Camel with HAPI FHIR ensures robust healthcare interoperability, while AES-256 encryption and immutable Elasticsearch audit trails satisfy strict HIPAA and GDPR compliance requirements.