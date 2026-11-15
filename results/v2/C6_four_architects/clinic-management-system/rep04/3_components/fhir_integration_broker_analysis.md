## Overview
The FHIR Integration Broker manages secure, bidirectional health data exchange for the Clinic Management System. It translates, routes, and audits clinical data between external lab systems and internal microservices.

## Key Elements
*   **FHIR REST Endpoint Listener**: Apache Camel REST DSL component exposing FHIR R4 APIs.
*   **HL7/FHIR Transformation Engine**: HAPI FHIR Java library mapping legacy formats to FHIR resources.
*   **Message Router & Enrichener**: Camel Content-Based Router inspecting resource types and enriching data.
*   **Kafka Event Publisher**: Camel Kafka Connector publishing standardized events.
*   **Security & Audit Interceptor**: Camel policy component enforcing OAuth2/JWT validation and audit logging.
*   **Outbound FHIR Dispatcher**: Camel HTTP4/Netty component pushing notifications and query responses.
*   **Dead Letter & Retry Handler**: Camel Dead Letter Channel capturing and retrying transient failures.

## Relationships
*   *API Gateway* sends requests via **HTTPS** to *FHIR REST Endpoint Listener*.
*   *FHIR REST Endpoint Listener* delegates requests via **In-JVM method calls** to *Security & Audit Interceptor*.
*   *Security & Audit Interceptor* writes compliance records via **gRPC/TLS** to the *Audit Log Service*.
*   *Outbound FHIR Dispatcher* transmits data to *External Lab & Imaging Systems* via **HTTPS (mTLS)**.
*   *Kafka Event Publisher* and *Dead Letter & Retry Handler* send messages via **Kafka Wire Protocol** to *Apache Kafka*.

## Technology Stack
*   **Apache Camel (Java on OpenJDK 17)**: Core integration framework providing robust Enterprise Integration Patterns.
*   **HAPI FHIR Java Libraries**: Native tooling for processing HL7 FHIR standards.
*   **Kubernetes**: Container orchestration platform ensuring high availability (99.99%).
*   **Apache Kafka**: Distributed event broker for reliable asynchronous message delivery.
*   **Redis Enterprise / Local DB**: Persistent backing for retry handling and state caching.

## Rationale
This architecture uses proven integration patterns to guarantee zero data loss and secure, fault-tolerant interoperability. It strictly fulfills HIPAA compliance, high availability, and HL7 FHIR standards across hybrid Kubernetes environments.