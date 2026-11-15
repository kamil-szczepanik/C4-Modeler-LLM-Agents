## Overview
The Library Management System is a comprehensive platform for public and academic libraries to catalogue physical and digital items, manage circulation, and provide self-service portals. It ensures secure, high-performance operations while enforcing EU data residency constraints.

## Key Elements
- **Users**: Library Patrons, Library Staff and Cataloguers, Library Administrators
- **External Systems**: Enterprise Identity Provider, Payment Gateway, Notification Service
- **Containers**: Envoy Proxy, Web Application Container (React with NGINX), Catalogue Service (Spring Boot), Circulation & Loan Service (Node.js/Express), Notification Service Worker (Python FastAPI), Search Indexer (Elasticsearch), Databases (PostgreSQL), Message Broker (RabbitMQ)
- **Envoy Proxy Components**: Listener Subsystem, HTTP Connection Manager (HCM), JWT Authentication Filter, Rate Limit Filter, Cluster Manager

## Relationships
- **Web Application Container -> Envoy Proxy**: Forwards web requests using HTTPS (TLS 1.3)
- **Envoy Proxy -> Catalogue Service**: Routes cataloguing requests via mTLS and gRPC/Protobuf
- **Envoy Proxy -> Circulation & Loan Service**: Routes circulation requests via mTLS and gRPC/Protobuf
- **Enterprise Identity Provider -> Envoy Proxy**: Issues JWTs validated at the edge

## Technology Stack
- **Envoy Proxy**: Edge API Gateway handling ingress, rate limiting, and TLS termination
- **xDS API**: Control plane for dynamic routing updates and canary deployments
- **OpenTelemetry**: Emits distributed tracing headers and asynchronous access logs
- **Kubernetes**: Deployment platform with HPA, PDBs, and strict resource limits

## Rationale
This architecture uses an Envoy Proxy with edge JWT validation and local JWKS caching to secure self-service portals while maintaining low latency. Asynchronous telemetry, token-bucket rate limiting, and robust cluster management safeguard the system's performance and meet strict search SLAs.