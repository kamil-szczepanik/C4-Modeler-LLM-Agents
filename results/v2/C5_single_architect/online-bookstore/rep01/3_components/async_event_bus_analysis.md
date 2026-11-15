## Overview
The Async Event Bus is a resilient, event-driven backbone for the Online Bookstore e-commerce system. It decouples microservices to handle 1 million monthly active users while ensuring reliable message delivery and external third-party integrations.

## Key Elements
- **Event Router / Ingestion Engine**: Amazon EventBridge Rules / Kafka Brokers
- **Event Topic / Stream Partition Manager**: Amazon MSK Topics
- **Dead Letter Queue (DLQ) Handler**: Amazon SQS + Lambda
- **Outbound Dispatcher**: AWS Lambda / EventBridge API Destinations
- **Schema Registry**: AWS Glue Schema Registry
- **External Entities**: Order & Checkout Container, Third-Party Shipping Provider, Notification Service

## Relationships
- **Order & Checkout Container** -> **Event Router**: Publishes events [JSON over TLS]
- **Event Router** -> **Schema Registry**: Validates event payloads [Internal gRPC/HTTPS]
- **Event Router** -> **Event Topic**: Routes events based on schema rules [Internal broker protocol]
- **Event Topic** -> **Outbound Dispatcher**: Triggers external integrations [Internal polling/push]
- **Event Topic** -> **Notification Service**: Streams domain events for customer alerts [SASL/SCRAM over TLS]
- **Async Event Bus** -> **Third-Party Shipping Provider**: Sends fulfillment requests [Webhooks / HTTPS APIs]

## Technology Stack
- **Amazon EventBridge / Amazon MSK**: Provides distributed event ingestion and ordered event log streaming to scale under heavy traffic loads.
- **AWS Glue Schema Registry**: Enforces strict JSON/Avro schemas to prevent malformed data pollution.
- **Amazon SQS + AWS Lambda**: Implements Dead Letter Queues for fault-tolerant failure recovery.
- **TLS / HTTPS**: Secures all transit channels for data protection and compliance.

## Rationale
This component architecture uses decoupled event-driven streaming to maintain sub-2-second page loads and 99.95% availability. Schema validation and DLQ handling guarantee data integrity and fault tolerance across distributed microservices.