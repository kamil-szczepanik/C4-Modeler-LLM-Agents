## Overview
The Clinic Management System is a hybrid-cloud clinical IT solution managing patient admissions, EMRs, scheduling, and billing. It ensures high availability, strict HIPAA/GDPR compliance, and low-latency performance.

## Key Elements
- **Users**: Patient, Clinician / Staff, Hospital Administrator
- **External Systems**: External Lab & Imaging Systems, Insurance Payment Gateways, Identity Provider (IdP), SMS / Notification Gateway
- **Containers**: API Gateway (NGINX/Envoy), Web Application (React/TypeScript), Core Clinic Service (Java/Spring Boot), Scheduling Service (Go), Billing Service (Node.js), Integration Service (Apache Camel/Spring Integration), Event Broker (Apache Kafka/RabbitMQ), PostgreSQL Database (PostgreSQL with AES-256), Redis Cache (Redis)
- **Redis Components**: Redis Master Node (v7.x), Redis Replica Nodes, Distributed Lock Manager (Redlock)

## Relationships
- **Web Application -> API Gateway**: Routes client requests [HTTPS / REST]
- **API Gateway -> Core Clinic Service / Scheduling Service / Billing Service**: Dispatches microservice requests [gRPC / REST]
- **Core Clinic Service -> PostgreSQL Database**: Persists clinical and patient data [JDBC / TLS]
- **Core Clinic Service -> Redis Cache**: Caches frequent EMR queries for <1s load times [RESP / TLS over TCP]
- **Scheduling Service -> Redis Master Node**: Acquires distributed appointment locks using Redlock [RESP / TLS over TCP]
- **Redis Master Node <-> Redis Replica Nodes**: Handles high availability replication [RESP / TCP]
- **Integration Service -> External Lab & Imaging Systems**: Exchanges health data [HL7 FHIR / REST]

## Technology Stack
- **Frontend**: React / TypeScript for responsive UI
- **Backend**: Java (Spring Boot) for core clinical logic, Go for concurrent scheduling, Node.js for billing
- **Databases & Caching**: PostgreSQL with AES-256 encryption at rest; Redis Engine v7.x for caching and distributed locks
- **Messaging**: Apache Kafka / RabbitMQ for event-driven workflows
- **Integration & Gateway**: Apache Camel / Spring Integration; NGINX / Envoy API Gateway
- **Infrastructure**: Hybrid deployment across on-premises Kubernetes and AWS (eu-central-1)

## Rationale
The hybrid architecture combines on-premises Kubernetes control with cloud scalability to meet stringent HIPAA/GDPR compliance and 10-year data retention mandates. Active-active components, Redis replication, and PostgreSQL clustering ensure 99.99% high availability and sub-second EMR response times.