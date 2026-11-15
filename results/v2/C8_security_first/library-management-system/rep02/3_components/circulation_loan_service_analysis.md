## Overview
The Circulation & Loan Service manages circulation, loan operations, and self-service portals for the Library Management System. It ensures secure, performant, and compliant handling of physical and digital item loans within the EU region.

## Key Elements
- **Circulation & Loan Service:** Node.js/Express container managing workflows, payments, and events.
- **Loan API Controller:** Express.js component handling gRPC routing and Zod schema validation.
- **Circulation Workflow Engine:** Node.js service layer managing transactional states, grace periods, and hold expiry.
- **Data Access Layer:** Repository component enforcing column-level encryption and least-privilege connection pooling.
- **Outbox Pattern Component:** Transactional outbox processor for reliable asynchronous messaging.
- **Event Publisher/Subscriber:** Component publishing domain events over AMQP to the Message Broker.
- **Payment Client:** Component encapsulating integration logic with the Payment Gateway over HTTPS with idempotency keys.
- **Circulation DB & Message Broker:** PostgreSQL database and RabbitMQ message broker.

## Relationships
- **Envoy Proxy -> Loan API Controller:** Routes gRPC/Protobuf requests with mTLS and forwarded JWT claims.
- **Data Access Layer -> Circulation DB:** Reads and writes encrypted circulation data using gRPC/Protobuf.
- **Event Publisher/Subscriber -> Message Broker:** Publishes and consumes domain events using AMQP.
- **Payment Client -> Payment Gateway:** Processes fine settlements using HTTPS with REST/JSON.

## Technology Stack
- **Node.js/Express & gRPC-Node:** Core runtime and API framework for low-latency request handling.
- **Zod:** Input validation library for request sanitization.
- **PostgreSQL & RabbitMQ:** Persistent storage and message broker supporting transactional outbox patterns.
- **Kubernetes (EU-region):** Container orchestration enforcing data residency, horizontal pod autoscaling, and resource governance.
- **OpenTelemetry:** Distributed tracing across gRPC boundaries.

## Rationale
This architecture uses an asynchronous event-driven design and transactional outbox pattern to guarantee zero-latency patron experiences and reliable event delivery. Strict EU container deployment, column-level encryption, and least-privilege access fulfill regulatory and high-performance requirements.