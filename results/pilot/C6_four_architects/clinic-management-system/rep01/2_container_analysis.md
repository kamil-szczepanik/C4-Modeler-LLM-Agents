## Overview
The Clinic Management System is a hybrid, highly available healthcare platform that securely processes patient admissions, electronic medical records, scheduling, and billing. It provides resilient, compliant, and sub-second clinical operations across on-premise Kubernetes clusters and AWS `eu-central-1`.

## Key Elements
* **Clients**: Progressive Web App (PWA) Client Container (Nginx, IndexedDB).
* **Ingress & Routing**: API Gateway Container (Kong/Envoy), Hybrid VPN Gateway Container (WireGuard).
* **Core Microservices**: Patient & EMR Service, Scheduling Service, Billing Service (Node.js, Docker, Kubernetes).
* **Integration & Processing**: HL7 FHIR Adapter Container, DICOM & Document Processing Container, Secure File Transfer Container (SFTP/FTPS, PGP).
* **Security & Compliance**: Tenant Context & Authorization Proxy Container (Open Policy Agent), Data Encryption & Key Management Container (PKCS#11, HSM), Audit & Compliance Sidecar Container.
* **Data & Messaging**: PostgreSQL Container cluster (CloudNativePG), Redis Container tier, Apache Kafka StatefulSet, RabbitMQ Container cluster, Elasticsearch Containers, ClickHouse Analytics Engine, MinIO Object Storage Gateway Container.
* **Observability & Mesh**: Envoy Service Mesh Container, Observability Collector Container (OpenTelemetry, Prometheus).

## Relationships
* **PWA Client Container** $\rightarrow$ **API Gateway Container**: Routes user actions and demographic payloads via HTTPS.
* **API Gateway Container** $\rightarrow$ **Core Microservices**: Dispatches routing and authenticates via OAuth2/OIDC.
* **Core Microservices** $\leftrightarrow$ **PostgreSQL / Redis / Elasticsearch**: Executes transactional queries, distributed locking, and EMR search via gRPC and SQL.
* **Core Microservices** $\leftrightarrow$ **Apache Kafka / RabbitMQ**: Publishes and consumes domain events using asynchronous messaging.
* **Core Microservices** $\leftrightarrow$ **HL7 FHIR Adapter Container**: Exchanges lab and imaging payloads with external health systems via HTTPS/REST.
* **Audit & Compliance Sidecar** $\rightarrow$ **WORM Object Storage**: Streams cryptographic audit logs via TLS 1.3.

## Technology Stack
* **Runtime & Orchestration**: Node.js/TypeScript, Docker, Kubernetes (hybrid on-prem-k8s and AWS `eu-central-1`) for scalable containerized workloads.
* **Databases & Caching**: PostgreSQL (CloudNativePG for multi-master replication), Redis Enterprise (active-active caching), Elasticsearch (CQRS read models), ClickHouse (analytics).
* **Messaging & Integration**: Apache Kafka (event sourcing), RabbitMQ (transient events), gRPC (internal RPC), HL7 FHIR (interoperability).
* **Security & Mesh**: Open Policy Agent (ABAC), Envoy Service Mesh (mTLS 1.3), WireGuard (hybrid VPN overlay), AES-256 (encryption at rest).

## Rationale
This architecture guarantees 99.99% uptime through active-active multi-region Kubernetes deployments, Redis clustering, and automated PostgreSQL failovers. Strict HIPAA and GDPR compliance is enforced via isolated OPA authorization proxies, local HSM key management, and dedicated WORM audit sidecars.