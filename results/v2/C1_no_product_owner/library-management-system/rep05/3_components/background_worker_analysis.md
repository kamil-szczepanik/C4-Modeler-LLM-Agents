## Overview
The Background Worker is a Python/Celery container within the Library Management System that processes asynchronous tasks, batch operations, and external integrations. It ensures system performance by isolating heavy workloads from the core domain service while enforcing EU-only data residency.

## Key Elements
- Task Consumer (`Celery Worker`)
- Task Router (`Celery Router`)
- Data Access Layer (`SQLAlchemy`)
- External Integration Client (`HTTPX`)
- Async Event Broker (`RabbitMQ` / `Kafka`)
- Primary Database (`PostgreSQL`)
- External Systems (`Notification Service`, `National Library Registry`)

## Relationships
- Async Event Broker -> Task Consumer: Consumes asynchronous background tasks [Consumer subscription over mTLS with AMQP]
- Task Consumer -> Task Router: Dispatches incoming broker events based on task type [Internal Python routing]
- Task Consumer -> Data Access Layer: Reads/Writes task state and domain data [SQLAlchemy]
- Task Consumer -> External Integration Client: Triggers external notifications and syncs [Async HTTP/REST over TLS 1.3]
- Task Consumer -> Async Event Broker: Acknowledges task completion or routes poisoned messages to DLQ [AMQP/mTLS]

## Technology Stack
- **Python (FastAPI/Celery)**: Chosen for robust background task processing and ecosystem compatibility.
- **Pydantic**: Used for strict payload schema validation and sanitization to prevent injection attacks.
- **SQLAlchemy**: Provides secure database interaction meeting EU data residency constraints.
- **KEDA & Kubernetes**: Enables queue-specific auto-scaling based on individual queue depths.
- **Vault**: Ingests ephemeral secrets without local configuration files.

## Rationale
This architecture isolates resource-intensive background processing from user-facing services, ensuring <800ms search responses. Strict cryptographic, network, and security controls guarantee EU data residency and regulatory compliance.