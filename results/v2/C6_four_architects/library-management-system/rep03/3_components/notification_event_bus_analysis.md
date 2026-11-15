## Overview
The Library Management System provides item cataloging, circulation management, and self-service portals for public and academic libraries. Its Notification & Event Bus uses Apache Kafka to enable decoupled, reliable, and secure asynchronous processing.

## Key Elements
- **Notification & Event Bus**: Apache Kafka container
- **Event Router (Topic Manager)**: Apache Kafka Brokers
- **Event Publisher Gateway**: Kafka Producer Client API (Java/Python)
- **Consumer Dispatcher**: Kafka Consumer Client API
- **Schema Registry**: Confluent Schema Registry
- **Dead Letter Queue (DLQ) Manager**: Kafka DLQ Topics
- **Kafka Connect Engine**: Confluent Kafka Connect
- **Access Control & TLS Terminator**: Kafka TLS/SASL Security Layer
- **Stream Processing Engine**: Apache Kafka Streams
- **Event Bus Metrics Exporter**: Prometheus JMX Exporter

## Relationships
- Core Domain Service -> Access Control & TLS Terminator: Kafka Wire Protocol over TLS
- Event Publisher Gateway -> Schema Registry: HTTP/REST
- Consumer Dispatcher -> DLQ Manager: Kafka Wire Protocol
- Kafka Connect Engine -> Notification Service: HTTPS
- Kafka Connect Engine -> Database: JDBC
- Event Router -> Stream Processing Engine: Kafka Wire Protocol
- Stream Processing Engine -> Reporting & Analytics Service: Kafka Wire Protocol
- Event Router -> Event Bus Metrics Exporter: HTTP/JMX
- Reporting & Analytics Service -> Event Bus Metrics Exporter: Prometheus Scrape Protocol

## Technology Stack
- **Apache Kafka**: Selected for EU-only data residency control and high-throughput event brokering.
- **Confluent Schema Registry**: Enforces Avro/JSON Schema contracts to prevent breaking changes.
- **Kafka TLS/SASL Security Layer**: Implements mTLS and SASL/SCRAM for secure internal communication.
- **Apache Kafka Streams**: Processes real-time event transformations locally.
- **Prometheus JMX Exporter**: Collects telemetry to meet 99th-percentile performance goals.

## Rationale
This architecture uses Apache Kafka and associated Confluent components to guarantee high-performance, secure, and compliant event-driven messaging within EU data boundaries. The modular component design ensures robust data governance, stream processing, and observability.