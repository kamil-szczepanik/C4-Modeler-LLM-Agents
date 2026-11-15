## Overview
The Library Management System is a solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. It guarantees strict EU-only data residency and high-performance catalog searches.

## Key Elements
*   **Users**: Patron, Librarian / Staff
*   **External Systems**: Payment Gateway, Notification Provider, Identity Provider, Digital Content Provider
*   **Containers**: Web Application (React, TypeScript, Nginx), API Gateway (Spring Cloud Gateway, Envoy), Core Domain Service (Java, Spring Boot), Search Service (Python, FastAPI, Elasticsearch), Async Event Broker (Apache Kafka), Background Worker (Python, Celery), Database (PostgreSQL)
*   **Async Event Broker Components**: Event Router / Topic Manager, Producer Ingress Handler, Consumer Egress Dispatcher, Schema Registry

## Relationships
*   Core Domain Service -> Producer Ingress Handler [Kafka Protocol]
*   Producer Ingress Handler -> Schema Registry [HTTP/REST]
*   Consumer Egress Dispatcher -> Schema Registry [HTTP/REST]
*   Consumer Egress Dispatcher -> Search Service [Kafka Protocol]
*   Async Event Broker -> Search Service [TCP/Kafka Protocol]

## Technology Stack
*   **React, TypeScript, Nginx**: Powers the Web Application container.
*   **Spring Cloud Gateway, Envoy**: Implements the API Gateway container.
*   **Java, Spring Boot**: Powers the Core Domain Service.
*   **Python, FastAPI, Elasticsearch**: Drives the Search Service container for sub-800ms 99th-percentile searches.
*   **Apache Kafka**: Deployed as a managed EU instance for the Async Event Broker to meet data residency constraints.
*   **Apache Avro**: Enforces schema validation and contract compatibility.

## Rationale
This event-driven, decoupled architecture leverages regional Apache Kafka deployment and Apache Avro validation to strictly enforce EU data residency. The specialized search stack ensures sub-800ms 99th-percentile performance requirements are met.