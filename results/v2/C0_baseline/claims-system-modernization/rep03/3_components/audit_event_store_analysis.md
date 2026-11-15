## Overview
Modernizes a regional insurer's 30-year-old mainframe claims system via a hybrid cloud platform while ensuring zero data loss and continuity. Replaces legacy components incrementally over a 3-year migration window.

## Key Elements
- **Audit & Event Store**: Azure Cosmos DB container maintaining append-only immutability.
- **Event Ingestion API / Router**: Azure Functions / containerized gRPC/REST endpoint.
- **Immutability & Partition Manager**: Azure Cosmos DB native change feed and TTL policies partitioned by `ClaimID`.
- **Query & Compliance Facade**: Azure API Management backed by a Node.js/GraphQL microservice in Azure Container Apps.
- **Archival Worker**: Azure Functions timer-triggered background component.
- **Archive Storage**: Azure Blob Storage with Cool/Archive tiers and WORM policies.

## Relationships
- **Integration & Sync Service / Claims BFF** to **Event Ingestion API**: mTLS, gRPC over private endpoints.
- **Event Ingestion API** to **Immutability & Partition Manager**: Internal container network calls.
- **Archival Worker** to **Azure Blob Storage**: Change Feed protocol, HTTPS.
- **Customer Service Managers / Compliance Officers** to **Query & Compliance Facade**: OAuth2/JWT via corporate Active Directory, HTTPS/GraphQL.

## Technology Stack
- **Azure Cosmos DB**: Chosen for native append-only change feed, TTL, and horizontal scalability with minimal cloud expertise.
- **Azure Functions**: Serverless event routing and scheduled archival tasks for cost efficiency.
- **Azure Blob Storage**: Long-term cold storage with WORM policies to satisfy regulatory retention cost-effectively.
- **Azure API Management & Container Apps**: Secures and serves the query facade supporting pre-built executive dashboards.
- **Terraform**: Infrastructure as Code for reproducible hybrid deployments.

## Rationale
The hybrid architecture isolates complex legacy mainframe dependencies while leveraging managed cloud services to minimize operational overhead for a team with low cloud experience. Strict consistency configurations, VNet isolation, and immutable storage ensure regulatory compliance and zero data loss (R-04).