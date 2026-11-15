## Overview
The Staff Circulation & Cataloguing Container is a Kubernetes-based microservice within the Library Management System that provides circulation and cataloguing tools for library staff. It ensures secure, high-throughput item check-outs, returns, and catalog management while enforcing strict EU-only data residency.

## Key Elements
- Library Staff (Librarians, cataloguers, desk clerks)
- Staff Circulation & Cataloguing Container (Kubernetes Microservice)
- API Gateway Container
- In-Region APM and Log Aggregation Pipeline
- Audit and Compliance Trust Zone
- Internal Message Broker & Dedicated Batch Worker Pods

## Relationships
- API Gateway Container -> Staff Circulation & Cataloguing Container: Routes staff requests via mTLS over internal Kubernetes network policies
- Staff Circulation & Cataloguing Container -> In-Region APM and Log Aggregation Pipeline: Streams encrypted metrics via OpenTelemetry sidecars
- Staff Circulation & Cataloguing Container -> Audit and Compliance Trust Zone: Streams immutable audit events for check-outs, returns, and catalog modifications

## Technology Stack
- Kubernetes: Hosts container replicas with HPA rules and resource isolation for high availability
- Signed JWTs: Validates staff RBAC/ABAC permissions passed from the API Gateway
- Internal Message Broker: Decouples bulk MARC/ONIX metadata ingestion asynchronously with TLS encryption
- EU-Managed Encryption Keys: Secures persistent volumes and database storage for PII protection

## Rationale
This architecture ensures low-latency operations by utilizing database connection pooling, read replicas, and asynchronous worker patterns to meet the 2-second transaction SLA. Strict EU worker node pinning and encrypted storage satisfy regional data residency and security constraints.