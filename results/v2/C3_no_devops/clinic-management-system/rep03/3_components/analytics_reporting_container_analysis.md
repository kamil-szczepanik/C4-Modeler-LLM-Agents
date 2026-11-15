## Overview
The Clinic Management System is a hybrid cloud platform designed to manage patient admissions, EMR, scheduling, and billing for medium-sized healthcare facilities. It ensures high availability, strict HIPAA/GDPR compliance, and seamless interoperability.

## Key Elements
* **Users**: Patients, Clinicians, Administrative Staff, Billing Officers, Regulatory Auditors, Clinic Managers, Hospital Executives
* **External Systems**: Enterprise Identity Provider, External Lab/Imaging Systems, Payment Gateway/Insurance Clearinghouse, Audit Archive
* **Containers**: API Gateway (Kong/Nginx), Frontend Container (Next.js/Node.js), Clinical Core Container (Node.js/Java Spring Boot), Scheduling & Resource Engine (Python/Go with Redis), Interoperability Service (Apache Camel/HAPI FHIR), Billing & Claims Worker (.NET Core with RabbitMQ), Analytics & Reporting Container
* **Analytics Components**: Dashboard & Visualization UI (Apache Superset), Query & Semantic Layer (Superset SQL Lab), Analytical Data Store (ClickHouse), CDC Ingestion Worker (Debezium + Kafka Connect), Report Export Service, Notification & Scheduling Worker (Celery/Node.js)

## Relationships
* **Users to API Gateway**: Access via HTTPS/WSS with Multi-Factor Authentication (OIDC).
* **API Gateway to Containers**: Routes internal traffic using mTLS across hybrid infrastructure (on-prem-k8s and eu-central-1).
* **Interoperability Service to External Labs**: Communicates via HL7 FHIR APIs over HTTPS.
* **CDC Ingestion Worker to Databases**: Streams asynchronous transactional data from primary PostgreSQL to ClickHouse and Read-Only PostgreSQL Replica.
* **Report Export Service to Audit Archive**: Streams immutable audit logs over TLS.

## Technology Stack
* **Frontend**: Next.js / Node.js for responsive role-based UI and dashboard templates.
* **Backend Core**: Java Spring Boot / Node.js / .NET Core for clinical, billing, and scheduling workflows.
* **Analytics**: Apache Superset for visualization, ClickHouse for sub-second time-series analytical queries.
* **Ingestion & Messaging**: Debezium, Kafka Connect, and RabbitMQ for asynchronous event-driven data streaming.
* **Security & Infrastructure**: AES-256 encryption at rest, mTLS in transit, OIDC/MFA for authentication, deployed on Kubernetes.

## Rationale
This architecture uses an event-driven, decoupled design with CDC to isolate analytical workloads from the clinical core, guaranteeing sub-second EMR performance and 99.99% availability. Hybrid cloud deployment and robust security controls ensure strict adherence to HIPAA, GDPR, and 10-year data retention mandates.