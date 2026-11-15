## Overview
The Scheduling Service is a core container of the Clinic Management System responsible for managing patient appointment bookings and preventing resource clashes. It operates within a hybrid cloud architecture to support high availability and clinical compliance.

## Key Elements
- Patients and Administrative Users (External Actors)
- API Gateway (NGINX / Envoy)
- Scheduling Service (Go container with API Controller, Clash Service, and Broker Client components)
- PostgreSQL (Primary database with AES-256 encryption)
- Redis (Caching and distributed locking layer)
- RabbitMQ (Message broker for domain events)
- HashiCorp Vault (Secret management)

## Relationships
- API Gateway -> Scheduling Service: Routes REST requests over HTTPS / JSON
- Scheduling Service -> PostgreSQL: Executes queries via PostgreSQL Wire Protocol over TLS 1.3
- Scheduling Service -> Redis: Manages locks and caching via RESP over TLS
- Scheduling Service -> RabbitMQ: Publishes audit/domain events via AMQPS
- Scheduling Service -> HashiCorp Vault: Fetches credentials via API / TLS

## Technology Stack
- **Go**: Selected for low memory footprint, high concurrency, and sub-millisecond clash evaluation.
- **Redis & PostgreSQL**: Dual-layer locking mechanism to eliminate appointment race conditions and double-bookings.
- **RabbitMQ**: Asynchronous messaging for reliable event publishing and audit trailing.
- **HashiCorp Vault**: Secure, centralized secret management with dynamic credential rotation.

## Rationale
This architecture ensures 99.99% active-active hybrid availability by deploying stateless Go containers across on-premises Kubernetes and AWS `eu-central-1`. Strict adherence to mTLS, TLS 1.3, JWT scoping, and AES-256 fulfills HIPAA and GDPR compliance requirements.