## Overview
The FHIR Integration Broker is an internal container within the Clinic Management System responsible for mediating standardized healthcare data exchange. It ensures robust interoperability, security, and high availability for external lab and imaging systems.

## Key Elements
- FHIR Route Mediator (Apache Camel)
- HL7/FHIR Validator Component
- Data Anonymization & Security Filter
- FHIR Event Consumer (Apache Camel JMS/Kafka Consumer)
- API Gateway (Kong / Nginx)
- External Labs & Imaging Systems
- Message Broker (Kafka)
- Database Cluster (PostgreSQL)

## Relationships
- API Gateway -> FHIR Route Mediator: Forwards FHIR resource requests [mTLS / HTTPS]
- FHIR Route Mediator <-> HL7/FHIR Validator: Internal synchronous validation [Direct Java Route]
- FHIR Route Mediator -> External Labs & Imaging Systems: Dispatches standardized bundles [HL7 FHIR REST over HTTPS]
- Message Broker -> FHIR Event Consumer: Consumes asynchronous clinical domain events [AMQP / Kafka Protocol]
- FHIR Event Consumer -> HL7/FHIR Validator: Internal validation [Direct Java Route]
- FHIR Route Mediator -> Database Cluster: Persists transaction audit logs [JDBC over TLS]

## Technology Stack
- Apache Camel: Powers enterprise integration routing and mediation patterns
- Java: Underlying runtime for robust, enterprise-grade component execution
- Kafka: Enables asynchronous, decoupled clinical event processing for high availability
- PostgreSQL: Provides secure transactional audit log persistence
- mTLS / HTTPS: Secures network transport and client authentication

## Rationale
This architecture uses Apache Camel and Kafka to decouple synchronous API calls from asynchronous lab feeds, guaranteeing 99.99% availability. Dedicated validation and anonymization components strictly enforce HIPAA and GDPR compliance requirements.