## Overview
- The system is a Clinic Management System designed for medium-sized hospitals and clinics to handle patient records, scheduling, and billing securely.
- The core purpose of the Scheduling Service container is to manage patient and resource bookings with real-time conflict prevention while ensuring high availability.

## Key Elements
- Patients and Receptionists / Admins (Users)
- Edge Container (Kong / Envoy)
- Scheduling Service (Node.js Container)
- API Router Component (Express.js / Fastify)
- Booking Engine Component (Node.js)
- Availability Cache Component (Redis Cluster)
- Notification Dispatcher Component
- Databases (PostgreSQL)
- Event Bus (Apache Kafka)

## Relationships
- Edge Container -> API Router Component: Routes requests via mTLS [gRPC and REST over mTLS]
- API Router Component -> Booking Engine Component: Delegates requests [In-process TypeScript interfaces]
- Booking Engine Component -> Availability Cache Component: Acquires distributed locks and checks availability [TCP with TLS, `rediss://`]
- Booking Engine Component -> Databases: Persists booking data [TLS-encrypted PostgreSQL connections]
- Notification Dispatcher Component -> Event Bus: Publishes domain events [Apache Kafka using `kafkajs` over TLS]

## Technology Stack
- Node.js & TypeScript: Chosen for rapid iteration on complex scheduling logic and calendar calculations.
- Redis Cluster: Implements Redlock for distributed locking to prevent resource clashes and double-bookings.
- PostgreSQL: Provides ACID-compliant relational data storage for appointment records.
- Apache Kafka: Handles asynchronous event publishing for notifications and analytics.
- Kubernetes (Hybrid): Ensures active-active high availability (99.99%) across on-prem-k8s and eu-central-1.

## Rationale
- This architecture isolates calendar logic and leverages Redis Redlock to prevent race conditions during peak concurrency, fulfilling stringent uptime and performance requirements.
- Hybrid cloud deployment and robust event-driven components ensure HIPAA compliance, high availability, and seamless interoperability.