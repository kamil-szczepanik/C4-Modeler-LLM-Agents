## Overview
The Library Management System provides cataloging, circulation, and self-service portals for public and academic libraries. Its Search Service delivers high-performance catalog queries adhering to strict EU data residency constraints.

## Key Elements
*   **Search Service**: Python container built with FastAPI and Elasticsearch.
*   **Search Controller**: FastAPI routing layer handling incoming queries.
*   **Query Builder**: Translates search parameters into Elasticsearch Query DSL.
*   **Index Synchronizer**: Listens for domain events to maintain index consistency.
*   **Elasticsearch Client**: Transport layer interfacing with the search cluster.
*   **Elasticsearch Cluster**: Storage and execution engine for catalog searches.
*   **RabbitMQ / Kafka**: Internal message broker for domain events.
*   **PostgreSQL Database**: Primary relational data store.

## Relationships
*   **API Gateway** -> **Search Controller**: Routes search queries `[gRPC]`
*   **RabbitMQ / Kafka** -> **Index Synchronizer**: Consumes domain events `[AMQP/TCP]`
*   **Index Synchronizer** -> **PostgreSQL Database**: Queries initial data `[TCP/JDBC]`
*   **Search Controller** -> **Query Builder**: Executes internal method calls `[In-process]`
*   **Query Builder** -> **Elasticsearch Client**: Translates Query DSL `[HTTP/JSON]`
*   **Elasticsearch Client** -> **Elasticsearch Cluster**: Transports queries `[TCP/REST]`
*   **Search Service** -> **Redis Cache**: Accesses frequent queries `[TCP]`

## Technology Stack
*   **Python (FastAPI)**: Selected for lightweight, high-throughput API routing.
*   **Elasticsearch**: Chosen to meet the 99th-percentile search response time under 800ms.
*   **RabbitMQ / Kafka**: Utilized for asynchronous, decoupled event consumption.
*   **PostgreSQL**: Serves as the durable system-of-record relational database.
*   **Redis**: Implemented to cache frequent catalogue queries.

## Rationale
This component architecture uses specialized search indexing and asynchronous event synchronization to guarantee sub-800ms response times. Deploying all components within EU-hosted infrastructure strictly satisfies data residency requirements.