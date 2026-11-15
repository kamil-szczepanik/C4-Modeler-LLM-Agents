## Overview
The Clinic Management System is a hybrid-cloud healthcare platform providing patient registration, EMR, scheduling, and billing. It ensures HIPAA/GDPR compliance, 99.99% availability, and sub-second EMR screen loads.

## Key Elements
- Patients, Clinicians, and Billing Staff (Users)
- Next.js Single Page Application (Frontend Container)
- Go API Gateway (Backend Routing)
- Java Spring Boot Microservices (Business Logic)
- Apache Camel K Integration Broker & Apache Kafka (Integration/Streaming)
- Multi-master PostgreSQL Cluster & Redis Enterprise (Data Layer)
- External IdP, Payment Gateways, Lab/Imaging Systems (External Systems)

## Relationships
- Patients, Clinicians, Billing Staff -> Next.js Single Page Application: Manages clinical workflows via HTTPS/JSON
- Next.js Single Page Application -> Go API Gateway: Routes frontend requests via HTTPS/JSON with mTLS
- Go API Gateway -> Java Spring Boot Microservices: Internal RPC/REST communication
- Java Spring Boot Microservices -> PostgreSQL & Redis: Data persistence with AES-256 encryption
- Apache Camel K -> Third-Party Lab/Imaging Systems: HL7 FHIR interoperability

## Technology Stack
- Next.js / React App Router: Frontend framework utilizing RSCs and TypeScript for sub-second P95 loads
- TanStack Query & Zustand: Server-state caching and client-side ephemeral state management
- Go & Java Spring Boot: High-performance backend services and API gateway
- PostgreSQL & Redis: Multi-master persistence and high-availability caching with AES-256 at rest
- OpenTelemetry & Global Multi-CDN: Real-user monitoring, tracing, and edge failover across hybrid regions (`eu-central-1` and on-prem Kubernetes)

## Rationale
The hybrid architecture combines resilient on-premises Kubernetes and cloud infrastructure with active-active replication to guarantee 99.99% availability. Strict edge security, HttpOnly cookies, and strict RBAC enforce HIPAA and GDPR mandates while meeting high-performance clinical requirements.