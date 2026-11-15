## Overview
The Clinic Management System is a hybrid cloud platform designed for medium-sized hospitals and clinics to manage patient admissions, electronic medical records (EMR), scheduling, and billing. It provides high availability, stringent compliance, and offline-resilient clinical workflows.

## Key Elements
* Patients, Receptionists, Clinicians, Billing Specialists (Users)
* Identity Provider, Payment Gateway, Insurance Clearinghouse, Lab & Imaging Systems (External Systems)
* API Gateway (`Envoy / NGINX`)
* Web Application Container (`React / Next.js`)
* Clinical & EMR Core Container (`Spring Boot / Java`)
* Billing & Claims Container (`Node.js / Express`)
* HL7 FHIR Integration Container (`Apache Camel`)
* Edge Sync Container (`Go Daemon`)
* Primary DB (`PostgreSQL` with `Patroni` active-passive failover) and Audit Store

## Relationships
* Users interact with Web Application Container via HTTPS
* API Gateway routes requests to internal containers using TLS/JWT validation
* Clinical & EMR Core communicates internally via gRPC
* HL7 FHIR Integration Container connects to external Lab & Imaging Systems via HL7 FHIR APIs
* Billing & Claims Container connects to external payment gateways and insurance clearinghouses via HTTPS/REST
* Edge Sync Container synchronizes local on-prem EMR data with cloud tier via asynchronous transactional outboxes

## Technology Stack
* `React / Next.js`: Frontend SPA/SSR for responsive user interfaces
* `Spring Boot / Java`: High-performance internal EMR and scheduling services
* `Node.js / Express`: Lightweight billing and third-party integration management
* `PostgreSQL` with `Patroni`: Reliable relational data storage with automated failover
* `Apache Camel`: Integration engine for HL7 FHIR interoperability
* `Kubernetes` (`on-prem-k8s`, `eu-central-1`): Hybrid deployment orchestrator enforcing NetworkPolicies

## Rationale
Segregating patient-facing and internal clinical workloads into distinct containers enforces strict HIPAA/GDPR perimeter controls while scaling independently. Using an active-passive database failover strategy with an edge sync container guarantees 99.99% availability and offline clinical resilience.