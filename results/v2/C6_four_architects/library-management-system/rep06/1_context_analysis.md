## Overview
The Library Management System is a comprehensive digital solution for public and academic libraries to catalogue items, manage circulation, and provide self-service portals. The architecture enforces strict EU-only data residency and sub-800ms search performance through dedicated containerization and event-driven synchronization.

## Key Elements
* **Actors:** Patron, Librarian, Library Administrator
* **External Systems:** External Payment Gateway, Digital Content Providers, Notification Service, Integrated Library System (ILS) / Legacy Data Source
* **Containers:** Web App / Self-Service Portal, API Gateway, Core Backend Services, Search Engine, Async Worker, Operational Database & Cache

## Relationships
* Patron / Librarian / Library Administrator -> API Gateway [HTTPS]: Routes UI and API traffic
* Web App -> API Gateway [HTTPS/REST]: Fetches application data
* Library Management System -> External Payment Gateway [HTTPS/REST]: Processes fines
* Library Management System -> Digital Content Providers [HTTPS/REST]: Fetches digital assets
* Library Management System -> Notification Service [HTTPS/REST]: Dispatches alerts via EU endpoints
* Library Management System -> ILS / Legacy Data Source [Z39.50 / HTTPS]: Synchronizes bibliographic records
* Core Backend Services -> Search Engine [TCP/REST]: Updates search index via event streams
* Core Backend Services -> PostgreSQL / Redis [TCP]: Handles transactional persistence and session caching

## Technology Stack
* **Frontend:** React / Next.js hosted on an EU Content Delivery Network (CDN)
* **API Gateway:** Kong or Nginx handling single entry-point routing
* **Backend:** Java 17 / Spring Boot using gRPC for low-latency internal communication
* **Search Engine:** OpenSearch or Elasticsearch for sub-800ms catalog queries (R-05)
* **Asynchronous Messaging:** Apache Kafka or Redis streams for decoupled event-driven indexing
* **Persistence:** PostgreSQL (OLTP) and Redis (Cache) deployed in EU-Central
* **Infrastructure:** Docker containers deployed via Kubernetes within EU regions

## Rationale
Separating the core transactional database from a dedicated search engine via an event stream guarantees sub-800ms search performance under heavy catalog query loads. Deploying all cloud infrastructure, databases, and third-party SaaS integrations strictly within EU regions ensures absolute compliance with the mandatory data residency constraint.