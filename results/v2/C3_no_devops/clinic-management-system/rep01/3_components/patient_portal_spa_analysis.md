## Overview
The Clinic Management System manages patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It provides high availability, stringent security, and seamless interoperability across hybrid cloud environments.

## Key Elements
* Patients / Consumers, Clinic Staff, Healthcare Providers, Billing Specialists, and System Administrators
* Patient Portal (SPA) and Staff Dashboard (SPA)
* API Gateway (Kong / Envoy) and BFF Proxy Layer
* Core Clinical & Billing Services (Go / Java / Spring Boot, PostgreSQL, Kafka / RabbitMQ)
* Interoperability & Analytics Gateway Container (HAPI FHIR JPA Server, HL7 FHIR)
* External Identity Provider (IdP), Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse

## Relationships
* Patients -> Patient Portal (SPA): Accesses portal for admissions, records, and billing via HTTPS / WebSockets
* Patient Portal (SPA) -> BFF Proxy Layer / API Gateway: Sends API requests via HTTPS with httpOnly cookies
* API Gateway -> Core Clinical & Billing Services: Routes internal microservice calls via gRPC / HTTPS
* Core Clinical & Billing Services -> Interoperability & Analytics Gateway: Exchanges data via HL7 FHIR APIs and Kafka / RabbitMQ

## Technology Stack
* Frontend: React / TypeScript bundled via Vite, served statically via Nginx
* Backend: Go, Java, Spring Boot for core clinical and billing services
* Database & Messaging: PostgreSQL with AES-256 encryption at rest; Apache Kafka or RabbitMQ for asynchronous eventing
* Integration: HAPI FHIR JPA Server for HL7 FHIR interoperability
* Infrastructure: Kubernetes on-prem and AWS eu-central-1 (active-active)

## Rationale
This architecture ensures HIPAA and GDPR compliance through strict token management, robust audit logging, and encrypted data storage. The active-active hybrid cloud deployment guarantees 99.99% high availability and <1s EMR screen loads.