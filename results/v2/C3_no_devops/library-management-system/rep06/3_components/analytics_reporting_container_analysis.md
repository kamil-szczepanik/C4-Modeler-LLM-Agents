## Overview
The Library Management System is a comprehensive solution for cataloguing items, managing circulation, and providing self-service portals with strict EU data residency. The Analytics & Reporting Container processes administrative metrics while strictly isolating and protecting patron PII.

## Key Elements
- Library Patrons, Librarians, Library Administrators
- API Gateway (Nginx/Kong)
- Analytics & Reporting Container (Python / FastAPI)
- Report Orchestrator Component (FastAPI Router)
- Aggregation & Analytics Engine Component (Pandas / NumPy)
- Data Anonymization Component
- Export Generation Component (ReportLab / WeasyPrint)
- Alert Evaluation Component
- Databases (Read-optimized PostgreSQL replica)
- Message Broker (Apache Kafka / RabbitMQ)

## Relationships
- API Gateway -> Report Orchestrator: Routes reporting requests [gRPC over mTLS]
- Report Orchestrator -> Data Anonymization: Passes raw query results [In-memory]
- Data Anonymization -> PostgreSQL Replica: Fetches read-only data [SQL over TLS]
- Aggregation & Analytics Engine -> Export Generation: Passes processed data [In-memory]
- Aggregation & Analytics Engine -> Alert Evaluation: Streams computed metrics [In-memory]
- Alert Evaluation -> Message Broker: Publishes anomaly events [AMQP/Kafka over TLS]

## Technology Stack
- Python / FastAPI: High-performance asynchronous backend for the reporting container.
- Pandas / NumPy: Efficient in-memory data processing for analytics and trend calculations.
- ReportLab / WeasyPrint: Dedicated libraries for generating secure CSV and PDF exports.
- PostgreSQL Replica: Read-optimized database isolating heavy analytical queries from core circulation.
- Apache Kafka / RabbitMQ: Asynchronous message broker for publishing inventory anomaly alerts.

## Rationale
This architecture decouples heavy analytical processing and export rendering from core transactional services to protect performance and maintain search latency. Strict data anonymization, role-based access control, and Frankfurt-hosted infrastructure ensure compliance with EU data residency and privacy mandates.