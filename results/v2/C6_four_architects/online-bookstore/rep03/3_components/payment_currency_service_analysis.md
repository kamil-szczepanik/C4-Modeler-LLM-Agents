## Overview
The Online Bookstore system is a scalable e-commerce platform designed for browsing, purchasing, and reviewing physical and electronic books globally. It ensures high availability, strict security compliance, and multi-currency transaction processing.

## Key Elements
- **Payment Controller / API Endpoint**: ASP.NET Core Web API handling incoming routing requests.
- **Transaction Manager Component**: C# MediatR / Entity Framework Core managing payment execution and idempotency.
- **Stripe & PayPal Gateway Adapter**: C# HTTP Client abstracting third-party payment providers.
- **Currency Exchange Component**: .NET background service managing multi-currency conversions.
- **Payment Audit & Tokenization Component**: .NET Core security middleware handling PCI-DSS data sanitization.
- **Webhook Receiver Component**: ASP.NET Core Web API ingesting asynchronous payment provider events.
- **External Dependencies**: Stripe, PayPal, Amazon ElastiCache (Redis), Amazon RDS (PostgreSQL), and Amazon SQS.

## Relationships
- Payment Controller -> Transaction Manager: Invokes command handlers [In-process]
- Transaction Manager -> Stripe & PayPal Gateway Adapter: Executes payment calls [HTTPS Egress]
- Transaction Manager -> Payment Audit & Tokenization Component: Forwards sanitized records [In-process]
- Payment Audit & Tokenization Component -> Amazon RDS (PostgreSQL): Persists ledger and audit logs [ADO.NET / TLS]
- Currency Exchange Component -> Amazon ElastiCache (Redis): Reads/writes cached rates [Redis Protocol over TCP]
- Stripe/PayPal -> Webhook Receiver Component: Delivers asynchronous notifications [HTTPS Ingress]
- Webhook Receiver Component -> Amazon SQS: Publishes raw payment events [AWS SDK / HTTPS]

## Technology Stack
- **.NET Core**: Core framework providing high performance for financial services.
- **ASP.NET Core Web API**: Exposes REST endpoints for controllers and webhooks.
- **C# MediatR / Entity Framework Core**: Orchestrates transactions and data persistence.
- **Amazon ElastiCache (Redis)**: Caches real-time multi-currency exchange rates.
- **Amazon RDS (PostgreSQL)**: Persists ledger and PCI-DSS compliant audit logs.
- **Amazon SQS**: Queues asynchronous payment provider events securely.

## Rationale
This component architecture enforces strict PCI-DSS compliance and multi-currency support through isolated adapters and tokenization middleware. Utilizing .NET Core alongside AWS infrastructure guarantees secure, low-latency financial transactions meeting high availability requirements.