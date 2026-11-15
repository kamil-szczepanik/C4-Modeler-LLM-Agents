## Overview
The Clinic Management System manages patient admissions, EMRs, scheduling, and billing for clinical environments. It provides a hybrid-cloud architecture ensuring 99.99% availability, HIPAA/GDPR compliance, and low-latency EMR performance.

## Key Elements
- **Users**: Patients, Receptionists, Clinicians, Billing Specialists, Hospital Administrators
- **External Systems**: Insurance Payers/Clearinghouses, External Labs and Imaging Systems, Twilio, SendGrid
- **Containers**: Patient Portal, API Gateway, Clinical Core, Notification & Reminder Container
- **Infrastructure**: on-prem-k8s, eu-central-1, Kafka/RabbitMQ message broker, Vault operator

## Relationships
- **Patient Portal -> API Gateway**: Routes client traffic via HTTPS and OAuth2
- **API Gateway -> Notification & Reminder Container**: Routes notification traffic via mTLS using Istio
- **Notification & Reminder Container -> External Gateways**: Dispatches messages via TLS 1.3 with client certificate pinning

## Technology Stack
- **Orchestration**: Kubernetes (on-prem-k8s and eu-central-1) for high availability and autoscaling
- **Communication & Mesh**: Istio for mTLS and egress filtering; TLS 1.3 for secure transport
- **Messaging**: Kafka or RabbitMQ with TLS in transit, AES-256 at rest, and DLQs for async processing
- **Security & Secrets**: Vault operator for credential rotation; JWT/OAuth2 for RBAC; OpenTelemetry for PII-masked tracing

## Rationale
The hybrid-cloud Kubernetes architecture with active-active regional deployment guarantees the required 99.99% uptime and high performance. Strict cryptographic controls, PII scrubbing, and consent verification satisfy rigorous HIPAA and GDPR regulatory mandates.