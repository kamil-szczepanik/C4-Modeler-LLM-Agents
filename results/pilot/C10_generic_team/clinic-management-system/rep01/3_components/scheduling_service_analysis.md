## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers high availability and stringent compliance with HIPAA and GDPR regulations.

## Key Elements
* API Gateway (HTTPS, TLS 1.3, OpenAPI)
* Scheduling Service (Microservice, Domain-Driven Design)
* Caching Layer (Redis with distributed locks and lease keys)
* Message Brokers (Persistent Message Queues with Dead-Letter Routing)
* EMR Service & Billing Service (Microservices)
* Storage Tier (WORM storage for immutable audit logs)
* Infrastructure (Hybrid: on-prem-k8s and AWS eu-central-1)

## Relationships
* API Gateway -> Scheduling Service: Routes booking requests [REST, gRPC over TLS]
* Scheduling Service -> Caching Layer: Queries and manages time-slot reservations [In-memory Redis Protocol]
* Scheduling Service -> Message Brokers: Publishes asynchronous state change events [Persistent Queues, Saga Pattern]
* Scheduling Service -> WORM Storage: Streams immutable audit logs asynchronously [Secure Stream]

## Technology Stack
* Kubernetes: Container orchestration for hybrid cloud deployment, supporting OCI-compliant containers with liveness/readiness probes.
* Redis: Caching and distributed lock management for resource clash prevention and concurrency control.
* OpenTelemetry: Distributed tracing across the API gateway, caching layer, and message brokers.
* Pact: Contract testing framework for validating microservice interactions.

## Rationale
This architecture combines active-active hybrid Kubernetes deployments, Redis distributed locks, and the Saga pattern to meet strict 99.99% availability and data consistency requirements. Asynchronous event-driven messaging and WORM audit logging ensure HIPAA and GDPR compliance without impacting real-time clinical performance.