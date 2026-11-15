## Overview
The Interoperability Service securely manages HL7 FHIR exchanges for the Clinic Management System. It ensures high availability, HIPAA/GDPR compliance, and seamless integration with external diagnostic partners.

## Key Elements
- **API Gateway (.NET Core YARP):** Handles inbound TLS termination, mTLS validation, rate limiting, and request routing.
- **FHIR Transformer Engine (Apache Camel / .NET worker):** Performs asynchronous message translation and JSON schema validation.
- **Integration Queue (RabbitMQ):** Buffers inbound and outbound payloads with envelope encryption (AES-256) and DLQ support.
- **Outbound Dispatcher (.NET Core HttpClient):** Manages outbound notifications using Polly circuit breakers and exponential backoff.
- **Audit & Compliance Interceptor (.NET Middleware):** Captures metadata and invokes the Audit Logger Sidecar.
- **External Lab & Imaging Systems:** Third-party diagnostic partners.

## Relationships
- **API Gateway -> FHIR Transformer:** Forwards validated requests [In-process / gRPC with mTLS metadata]
- **FHIR Transformer -> Integration Queue:** Queues asynchronous payloads [AMQP]
- **FHIR Transformer -> Outbound Dispatcher:** Passes processed payloads [In-process / gRPC]
- **Outbound Dispatcher -> External Lab & Imaging Systems:** Sends FHIR notifications [HTTPS / mTLS]
- **API Gateway -> Audit Interceptor:** Logs ingress requests [In-process middleware]

## Technology Stack
- **.NET Core & Apache Camel:** Chosen for high-throughput microservices and robust enterprise integration patterns.
- **RabbitMQ:** Selected for asynchronous buffering and reliable queueing during partner outages.
- **YARP (.NET):** Utilized for high-performance ingress routing and rate limiting.
- **Polly:** Implemented for resilient circuit breaking and exponential backoff retry logic.
- **AES-256 & cert-manager:** Deployed for message-level encryption and automated certificate lifecycle management.

## Rationale
This architecture guarantees 99.99% uptime and strict HIPAA/GDPR compliance through resilient queuing, strict network isolation, and automated cryptographic controls. It securely processes external clinical data without compromising core system performance.