## Overview
The Library Management System is a comprehensive digital and physical cataloguing and circulation platform designed for public and academic libraries. It provides scalable self-service portals and staff management tools while strictly enforcing EU data residency constraints.

## Key Elements
- Patron Web App & Staff Portal (TypeScript/React SPAs)
- API Gateway (Nginx or Spring Cloud Gateway)
- Catalog & Search Service (Java/Spring Boot + Elasticsearch)
- Circulation Service (Java/Spring Boot + PostgreSQL)
- Notification & Integration Worker (Node.js/Python)
- Managed Kubernetes Cluster (EKS/AKS in EU-central)
- Internal Event Bus (Apache Kafka or RabbitMQ)

## Relationships
- Patron Web App & Staff Portal to API Gateway via HTTPS/REST and WebSockets
- API Gateway to backend microservices via internal gRPC
- Catalog & Search Service to Elasticsearch for search queries
- Circulation Service to PostgreSQL for transactional data and Payment Gateway for fine processing
- Circulation Service to Notification & Integration Worker via Apache Kafka/RabbitMQ

## Technology Stack
- TypeScript/React: Frontend single-page application delivery
- Java/Spring Boot: Microservice backend logic and APIs
- Elasticsearch: High-performance indexing for sub-800ms search compliance
- PostgreSQL: Relational storage for inventory and circulation data
- Kubernetes, Helm, ArgoCD: GitOps-driven deployment on EU-central infrastructure

## Rationale
This architecture isolates high-performance search and transactional circulation into dedicated microservices to meet strict performance metrics. Utilizing EU-hosted Kubernetes clusters, localized databases, and regional log aggregation ensures complete compliance with data residency mandates.