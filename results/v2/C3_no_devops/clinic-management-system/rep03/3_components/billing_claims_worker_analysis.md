## Overview
The Clinic Management System manages patient workflows, EMRs, and billing via a hybrid cloud architecture. The Billing & Claims Worker container processes insurance claims asynchronously to ensure high availability and financial resilience.

## Key Elements
- Claim Submission Queue Listener (.NET Core / RabbitMQ Client)
- Clearinghouse Integration Adapter (.NET Core / HttpClient with Polly)
- Reconciliation & State Manager (.NET Core / Entity Framework Core)
- Remediation Mapping Engine (.NET Core / Localized lookup cache)
- Alert Dispatcher (.NET Core / SignalR & RabbitMQ Publisher)
- Payment Gateway and Insurance Clearinghouse
- Frontend Container
- Audit Archive

## Relationships
- Claim Submission Queue Listener -> RabbitMQ: Consumes pending claim payloads [AMQP with mTLS]
- Clearinghouse Integration Adapter -> Payment Gateway and Insurance Clearinghouse: Submits claims and processes payments [HTTPS / REST with mTLS and strict egress filtering]
- Reconciliation & State Manager -> Remediation Mapping Engine: Parses clearinghouse responses [Direct C# Method Invocation]
- Alert Dispatcher -> API Gateway: Pushes enriched rejection alerts to Frontend [WSS / SignalR with JWT validation]
- Reconciliation & State Manager -> Audit Archive: Emits signed audit logs [Secure API / TLS]

## Technology Stack
- .NET Core: High-performance runtime for asynchronous worker components
- RabbitMQ: Message broker ensuring reliable, decoupled claim queueing
- Polly: Resiliency framework providing circuit-breaking and exponential backoff
- Entity Framework Core: ORM for managing local claim states securely
- SignalR: Real-time WebSocket protocol for instant UI alerts

## Rationale
This asynchronous component-based architecture isolates external clearinghouse dependencies to protect clinic cash flow during vendor outages. Granular error mapping and secure WebSocket dispatching minimize accounts receivable delays while enforcing strict HIPAA compliance.