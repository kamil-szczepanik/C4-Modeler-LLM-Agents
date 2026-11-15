## Overview
The Library Management System is a cloud-native platform for public and academic libraries designed to catalogue items, manage circulation, and provide self-service portals with strict EU data residency. This summary focuses on the internal component architecture of the Circulation & Core Engine.

## Key Elements
- Circulation API & Auth Facade [component] (Go)
- Loan Management Component [component] (Go)
- Patron Policy Component [component] (Go)
- Audit & Event Dispatcher Component [component] (Go)
- API Gateway / BFF [container] (Nginx/Envoy)
- Primary Database [container] (PostgreSQL, EU-hosted)
- Notification Worker [container] (Async Worker)
- EU Compliance & Audit Logging Service [externalSystem]

## Relationships
- API Gateway / BFF -> Circulation API & Auth Facade [gRPC]
- Circulation API & Auth Facade -> Loan Management Component [In-Process Function Call]
- Circulation API & Auth Facade -> Patron Policy Component [In-Process Function Call]
- Loan Management Component -> Patron Policy Component [In-Process Function Call]
- Loan Management Component -> Primary Database [Postgres Wire Protocol over mTLS]
- Loan Management Component -> Audit & Event Dispatcher Component [In-Process Channel]
- Audit & Event Dispatcher Component -> Notification Worker [Async Message Queues (RabbitMQ/Redis)]
- Audit & Event Dispatcher Component -> EU Compliance & Audit Logging Service [Syslog/HTTPS]

## Technology Stack
- Go: Chosen for high-throughput concurrency and low latency in core circulation processing.
- PostgreSQL (EU-hosted): Persists transactional data with AES-256 encryption at rest and strict EU residency.
- RabbitMQ/Redis: Powers asynchronous message queues for non-blocking notifications and content syncing.
- gRPC: Ensures efficient internal and edge-to-service communication.

## Rationale
Decomposing the Go-based engine into specialized internal components cleanly separates security validation, business rules, and event dispatching to meet performance and strict EU compliance goals. In-process calls combined with asynchronous offloading protect user transaction speeds and ensure reliable audit logging.