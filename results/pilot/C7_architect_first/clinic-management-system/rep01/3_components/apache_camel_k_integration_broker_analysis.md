## Overview
[Component-level architecture for the Apache Camel K Integration Broker managing interoperability and secure health data exchange. It ensures real-time, resilient communication between internal clinical services and external medical systems.]

## Key Elements
* FHIR Transformer Component (Quarkus runtime using `camel-fhir` for clinical data mapping and validation)
* Routing Slip Manager (Camel Enterprise Integration Pattern engine managing asynchronous message flows)
* Kafka Consumer Component (Ingests events from Apache Kafka via reactive connectors using TCP/SASL)
* HTTPS/REST Dispatcher Component (Manages outbound traffic to external labs using TLS 1.3 and mTLS)

## Relationships
* Apache Camel K Integration Broker -> Apache Kafka: Ingests asynchronous events [TCP/SASL]
* HTTPS/REST Dispatcher Component -> Third-Party Lab and Imaging Systems: Exchanges health data [HTTPS with TLS 1.3 and mTLS]
* Routing Slip Manager -> FHIR Transformer Component: Direct in-memory exchanges for data transformation [`direct://` endpoints]
* HashiCorp Vault -> HTTPS/REST Dispatcher Component: Injects ephemeral client certificates for authentication [Secure API]

## Technology Stack
* Quarkus: Underlying runtime chosen for fast startup and low memory footprint in Kubernetes
* Apache Camel K (`camel-fhir`, `camel-kamelet`): Integration framework for parsing HL7 resources and abstracting connectors
* HashiCorp Vault: Secret management for dynamic mTLS certificate injection
* OpenTelemetry & Prometheus: Distributed tracing and metrics collection for SLA monitoring

## Rationale
[This component architecture guarantees the 99.99% availability SLA and HIPAA/GDPR compliance through isolated Kubernetes namespaces, circuit breakers, and encrypted data handling. It ensures reliable, sub-second interoperability with external clinical systems to protect patient safety and hospital revenue streams.]