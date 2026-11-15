## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, electronic medical records, scheduling, and billing for medium-sized hospitals and clinics. It delivers 99.99% availability, strict HIPAA/GDPR compliance, and sub-second EMR performance across on-premises Kubernetes and AWS (`eu-central-1`).

## Key Elements
* **Users:** Patients, Clinicians/Staff, Hospital Administrators
* **External Systems:** Identity Provider (IdP), Insurance Gateway, External Lab & Imaging Systems, Notification Gateway, Cloud Backup (AWS S3 Glacier)
* **Containers:** API Gateway, Web Frontend, Core Services Container, EMR Service, Database Layer, Integration Worker, Event Broker, Audit Log Store, Key Management Service (KMS), Background Job Scheduler, Global Load Balancer, Observability & Monitoring Collector

## Relationships
* **Web Frontend** interacts with **API Gateway** via HTTPS/WSS
* **API Gateway** communicates with **Core Services** and **EMR Service** via gRPC over mTLS
* **Core Services & EMR Service** interact with **Database Layer** using encrypted PostgreSQL wire protocol
* **Core Services** and **Integration Worker** stream messages via **Event Broker** using Kafka over TLS
* **Core Services & EMR Service** communicate with **Background Job Scheduler** via gRPC over mTLS
* **All Containers** access **Key Management Service** via HTTPS/REST with client certificate authentication
* **All Containers** export telemetry data to **Observability & Monitoring Collector** via gRPC/OTLP over TLS

## Technology Stack
* **API Gateway:** Kong/Envoy for TLS termination, rate limiting, and JWT validation
* **Web Frontend:** React/TypeScript served via Nginx/CloudFront
* **Core Services:** Java/Spring Boot for patient registration, scheduling, and billing
* **EMR Service:** Node.js/TypeScript for sub-second EMR performance and audit trails
* **Database Layer:** PostgreSQL with multi-master replication and AES-256 encryption at rest
* **Integration Worker:** Apache Camel/Python for asynchronous HL7 FHIR messaging
* **Event Broker:** Apache Kafka for asynchronous decoupling across hybrid clusters
* **Audit Log Store:** PostgreSQL Append-Only tables backed by AWS S3 Glacier / MinIO for 10-year retention
* **Key Management Service:** HashiCorp Vault / AWS KMS for envelope encryption and key separation
* **Background Job Scheduler:** Temporal.io for orchestrating complex clinical and insurance workflows
* **Global Load Balancer:** AWS Route 53 / Envoy Global for active-active multi-region health checks and geo-routing
* **Observability Collector:** OpenTelemetry / Prometheus / Grafana Loki for aggregated metrics, traces, and logs

## Rationale
This hybrid container architecture separates critical workloads like EMR and billing to guarantee sub-second performance and stringent HIPAA/GDPR compliance. Active-active multi-region deployment via Kafka, Temporal, and PostgreSQL replication fulfills the 99.99% uptime constraint.