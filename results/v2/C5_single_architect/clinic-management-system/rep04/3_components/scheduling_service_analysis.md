## Overview
The Scheduling Service manages high-concurrency patient appointment scheduling and resource clash checks within the Clinic Management System. It is implemented in Go to ensure low latency and high availability across hybrid cloud deployments.

## Key Elements
- API Handler / Controller (Go standard library / gRPC-go)
- Appointment Manager (Go domain logic)
- Resource Conflict Detector (Go with in-memory locks)
- Cache Repository (Go Redis Client)
- Database Repository (Go `pgx` driver)
- Event Publisher (Segmentio Kafka-go)
- External dependencies: Nginx / Envoy API Gateway, Redis Enterprise, Apache Kafka, PostgreSQL Primary Database

## Relationships
- API Gateway -> API Handler: Routes requests [HTTPS/REST and gRPC]
- API Handler -> Appointment Manager: Delegates requests [In-process Go interfaces]
- Appointment Manager -> Resource Conflict Detector: Validates availability [In-process]
- Resource Conflict Detector -> Cache Repository: Checks availability [TCP / Redis Protocol]
- Appointment Manager -> Database Repository: Persists state [In-process Go interfaces]
- Database Repository -> PostgreSQL Primary Database: Stores appointments [TCP / PostgreSQL Wire Protocol with AES-256]
- Appointment Manager -> Event Publisher: Dispatches events [In-process]
- Event Publisher -> Apache Kafka: Publishes domain events [TCP / Kafka Protocol]

## Technology Stack
- Go: Chosen for high concurrency and low memory footprint in scheduling operations
- gRPC-go: Facilitates efficient internal and gateway-to-service communication
- Redis Enterprise: Provides distributed caching for real-time availability checks
- PostgreSQL: Ensures ACID compliance and durable storage with AES-256 encryption
- Apache Kafka: Asynchronous event broker for cross-service integration

## Rationale
This component architecture uses Go and in-memory synchronization to achieve sub-second scheduling responses and high concurrency. Decoupled event publishing and robust persistence guarantee 99.99% availability and strict clinical data compliance.