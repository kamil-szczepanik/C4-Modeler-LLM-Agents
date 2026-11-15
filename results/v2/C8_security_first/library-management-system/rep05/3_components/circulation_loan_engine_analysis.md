## Overview
[Library Management System container: Circulation & Loan Engine]
[Core purpose: Manages circulation workflows, patron loans, dynamic policies, and financial fine processing within EU boundaries]

## Key Elements
- Patron Self-Service Portal (Web/Mobile App)
- Staff Management Console
- Circulation & Loan Engine (Python / FastAPI / Pandas)
- Loan Workflow Controller
- Loan Policy Evaluator
- Fine & Payment Processor
- ILL Coordinator
- Notification Trigger Component
- Data Access Repository
- Primary PostgreSQL Database & Read-Replica
- Message Broker (RabbitMQ/Kafka)
- Payment Gateway
- Inter-Library Loan Networks

## Relationships
- Patron Self-Service Portal & Staff Management Console -> Loan Workflow Controller: gRPC over mTLS (TLS 1.3)
- Fine & Payment Processor -> Payment Gateway: REST/JSON over TLS 1.3
- ILL Coordinator -> Inter-Library Loan Networks: REST/JSON over TLS 1.3
- Notification Trigger Component & Components -> Message Broker: Async event publishing
- Data Access Repository -> PostgreSQL: SQLAlchemy ORM with encrypted queries

## Technology Stack
- Python (FastAPI): Core web framework for high-performance routing
- Pandas: Data processing for loan analytics
- SQLAlchemy & Pydantic: Data modeling, validation, and database abstraction
- PostgreSQL: Relational persistence with AES-256 encryption at rest
- RabbitMQ/Kafka: Asynchronous messaging and audit event streaming
- Kubernetes & KEDA: Container orchestration and queue-depth autoscaling
- HashiCorp Vault: Secure secret injection for payment credentials

## Rationale
[Modular FastAPI component separation ensures high-performance circulation processing while meeting strict EU data residency and audit requirements.]
[Robust security controls, encryption, and rate limiting protect PII and financial transactions against abuse.]