## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It ensures high availability, HIPAA/GDPR compliance, and long-term data retention.

## Key Elements
- Patients & Clinicians (Primary Users)
- Notification Service Container (Python / FastAPI)
- API Router Component (FastAPI)
- Event Consumer Component (Python background worker)
- Notification Orchestrator Component (Python core logic)
- Channel Adapters Component (Twilio SDK / SendGrid SDK / Firebase Admin)
- Preference Manager Component (Python module)
- Retry & State Store Component (Redis / PostgreSQL)
- RabbitMQ (Message Broker)
- HashiCorp Vault (Secrets Management)
- WORM Storage (Audit Logging)

## Relationships
- API Gateway -> API Router: Routes notification requests [REST / JSON over HTTPS via mTLS]
- Event Consumer -> RabbitMQ: Consumes asynchronous tasks [AMQP]
- Notification Orchestrator -> Preference Manager: Queries communication flags [In-process call]
- Notification Orchestrator -> Retry & State Store: Manages persistent retries and DLQ [TCP / Redis Protocol with TLS and AES-256]
- Notification Orchestrator -> Channel Adapters: Abstracts dispatch [In-process call]
- Channel Adapters -> External Providers (Twilio/SendGrid): Delivers SMS, Email, and Push [HTTPS / TLS 1.3]
- Notification Orchestrator -> WORM Storage: Ships audit logs [HTTPS]

## Technology Stack
- Python / FastAPI: Enables rapid service delivery and asynchronous execution.
- RabbitMQ: Provides reliable message brokering for asynchronous event processing.
- Redis / PostgreSQL: Stores persistent retry states and dead-letter queues with AES-256 encryption.
- HashiCorp Vault: Secures dynamic secrets and API keys with automated rotation.
- Twilio, SendGrid, & Firebase: External adapters for multi-channel notification delivery.

## Rationale
This architecture decouples notification processing to guarantee 99.99% system availability and prevent third-party provider outages from disrupting core clinic workflows. It strictly enforces HIPAA and GDPR compliance by excluding PHI from external payloads and securing long-term audit logs in WORM storage.