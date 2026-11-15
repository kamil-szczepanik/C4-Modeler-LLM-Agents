## Overview
The Clinic Management System is a hybrid cloud platform managing patient admissions, electronic medical records, scheduling, and billing for medium-sized healthcare facilities. It ensures HIPAA/GDPR compliance, 99.99% uptime, and secure interoperability.

## Key Elements
* API Gateway Container (Single entry point with TLS 1.3, Envoy Proxy)
* Core Domain Containers (Microservices for clinical, billing, and scheduling workflows)
* Read-Model / Query Container (CQRS pattern optimized data retrieval)
* Distributed Caching and Rate-Limiting Store (Redis)
* Asynchronous Message Broker (Apache Kafka / RabbitMQ)

## Relationships
* Patients, Practitioners, Administrators -> API Gateway Container: HTTPS, TLS 1.3
* API Gateway Container -> Core Domain Containers: mTLS
* API Gateway Container -> Read-Model / Query Container: mTLS
* API Gateway Container <-> Distributed Caching and Rate-Limiting Store: TCP / Redis Protocol

## Technology Stack
* Envoy Proxy: Powers the API Gateway for secure routing and sidecar communication.
* Redis: Provides distributed caching and rate-limiting state management to support horizontal scaling.
* TLS 1.3 / mTLS: Secures external client entry and internal microservice communication.
* OpenAPI / Swagger: Enforces edge schema validation and declarative routing.
* Prometheus: Exposes metrics for operational visibility and uptime tracking.

## Rationale
The hybrid architecture utilizes a secure, horizontally scalable API Gateway backed by Redis to meet strict 99.99% availability and low-latency performance requirements. Strict mTLS transport security and edge schema validation guarantee compliance with HIPAA and GDPR data protection mandates.