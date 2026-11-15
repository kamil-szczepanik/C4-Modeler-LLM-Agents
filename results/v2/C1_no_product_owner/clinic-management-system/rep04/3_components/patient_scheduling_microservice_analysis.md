## Overview
The Clinic Management System manages patient admissions, Electronic Medical Records (EMR), scheduling, and billing for healthcare providers. It features a high-availability, hybrid-cloud architecture compliant with HIPAA and GDPR regulations.

## Key Elements
- **Users**: Patient/Client, Clinician/Medical Staff, Billing Admin
- **External Systems**: External Lab & Imaging Systems, Payment Gateway / Insurance Clearinghouse, Identity Provider (IdP)
- **Containers**: API Gateway (Kong/Nginx), Web Application (React/Next.js), Patient & Scheduling Microservice, EMR Microservice, Billing Microservice, Integration Service, PostgreSQL Database, WORM Audit Log Store, Apache Kafka / RabbitMQ Event Broker, Istio Service Mesh
- **Components (Patient & Scheduling Microservice)**: PatientController, SecurityEnforcer / AuthInterceptor, SchedulingService, AppointmentRepository, NotificationPublisher, EventPayloadMasker

## Relationships
- API Gateway -> Patient & Scheduling Microservice: Routes internal requests [gRPC over mTLS]
- PatientController -> SecurityEnforcer: Interception / Authorization [In-memory]
- PatientController -> SchedulingService: Local method invocation
- SchedulingService -> AppointmentRepository: JDBC / TLS [AES-256 Encryption]
- SchedulingService -> NotificationPublisher: Asynchronous publish [Kafka Producer API]
- NotificationPublisher -> EventPayloadMasker: Sanitizes payload [In-memory]
- Patient & Scheduling Microservice -> PostgreSQL Database: Persists relational data [AES-256 Encryption]
- Patient & Scheduling Microservice -> WORM Audit Log Store: Streams audit logs [Direct Stream]

## Technology Stack
- **Languages & Frameworks**: Spring Boot / Java 21 for microservices, React / Next.js for web applications
- **Infrastructure & Orchestration**: Kubernetes (on-prem-k8s and eu-central-1), Istio Service Mesh with SPIFFE/SPIRE for mTLS
- **Databases & Storage**: PostgreSQL (Multi-AZ), WORM Storage with HSM-backed KMS
- **Messaging & Resilience**: Apache Kafka / RabbitMQ, Resilience4j for circuit breaking
- **Security**: OAuth2/JWT for RBAC, Jakarta Bean Validation, HashiCorp Vault / AWS Secrets Manager for secrets

## Rationale
This architecture uses microservices on a hybrid Kubernetes platform with Istio service mesh to achieve the required 99.99% active-active availability and strict network isolation. Field-level masking, WORM storage, and AES-256 encryption ensure strict HIPAA and GDPR compliance without compromising sub-second performance targets.