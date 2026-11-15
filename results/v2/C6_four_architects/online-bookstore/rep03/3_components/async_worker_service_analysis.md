## Overview
The Async Worker Service is a Python-based background processing container that manages asynchronous workflows, data synchronization, and compliance tasks for the Online Bookstore. It ensures high availability, regulatory compliance, and system scalability by decoupling heavy workloads from synchronous user requests.

## Key Elements
- Task Consumer Component (Python/Celery or AWS Lambda)
- Workflow Orchestrator Component (Python / AWS Step Functions)
- Notification Dispatcher Component (Python)
- Data Synchronization Component (Python)
- GDPR/CCPA Compliance Purge Component (Python)
- Search Indexing Component (Python)
- Dead Letter Queue (DLQ) Handler Component (Python)

## Relationships
- Task Consumer -> Workflow Orchestrator: Triggers sagas [In-process Python function calls]
- Task Consumer -> GDPR/CCPA Compliance Purge Component: Triggers data deletion [In-process Python function calls]
- Task Consumer -> Search Indexing Component: Forwards catalogue updates [In-process Python function calls]
- Task Consumer -> DLQ Handler Component: Routes failed messages [SQS SDK / Exception Handling]
- Workflow Orchestrator -> Third-party Shipping APIs (UPS/FedEx): Requests shipment creation [HTTPS/REST]
- Workflow Orchestrator -> Avalara: Calculates and commits taxes [HTTPS/REST]
- Notification Dispatcher -> AWS SES/SNS: Sends notifications [AWS SDK / HTTPS]
- Data Synchronization Component -> Amazon RDS (PostgreSQL): Reads transactional state [PostgreSQL JDBC/TCP]
- GDPR/CCPA Compliance Purge Component -> Amazon RDS & DynamoDB: Anonymizes PII [SQL / AWS SDK]
- Search Indexing Component -> Amazon OpenSearch: Updates search indices [HTTPS / OpenSearch REST Client]
- DLQ Handler Component -> AWS SES/SNS: Alerts operations team [AWS SDK / HTTPS]

## Technology Stack
- Python: Core programming language for all worker components, chosen for rich ecosystem and developer familiarity.
- Amazon SQS & EventBridge: Event-driven message queuing for asynchronous task distribution and scalability.
- AWS SES/SNS: Notification delivery infrastructure for customer alerts and operational paging.
- Amazon OpenSearch: Search index synchronization target for catalogue browsing performance.
- PostgreSQL JDBC / AWS SDK: Protocols for secure database access and cloud service integration.

## Rationale
This component architecture ensures 99.95% uptime and high scalability (1M MAU) by isolating resource-intensive background tasks from user-facing services. It strictly enforces GDPR/CCPA compliance through a dedicated purge component and guarantees operational resilience via automated DLQ handling.