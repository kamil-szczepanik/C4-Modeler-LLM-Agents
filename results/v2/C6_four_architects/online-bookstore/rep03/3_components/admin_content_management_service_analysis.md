## Overview
The Admin & Content Management Service provides secure administrative capabilities for managing inventory, compliance, and platform configurations for the Online Bookstore. It leverages a modular .NET Core architecture deployed on AWS to maintain strict security, scalability, and GDPR/CCPA compliance.

## Key Elements
- Store Administrators (Person)
- Amazon API Gateway (Container)
- Admin & Content Management Service (.NET Core Container)
- Catalog Administration Component (.NET Core)
- Content Moderation Component (.NET Core)
- IAM & RBAC Component (.NET Core)
- Data Privacy & Compliance Component (.NET Core)
- Shipping & Tax Configuration Component (.NET Core)
- CMS & Asset Management Component (.NET Core)
- Amazon RDS (PostgreSQL), Amazon S3, Amazon ElastiCache (Redis), Amazon EventBridge, Amazon OpenSearch (External Systems)

## Relationships
- Amazon API Gateway -> IAM & RBAC Component: Authenticates administrative tokens [HTTPS]
- Catalog Administration Component -> Amazon RDS (PostgreSQL): Manages inventory data [ADO.NET / TLS]
- Catalog Administration Component -> Amazon OpenSearch: Triggers index re-syncs [HTTPS / REST]
- Content Moderation Component -> Amazon EventBridge: Publishes moderation outcomes [AWS SDK / HTTPS]
- Data Privacy & Compliance Component -> Amazon RDS (PostgreSQL) / Amazon S3: Executes data export/erasure [ADO.NET / TLS]
- Shipping & Tax Configuration Component -> Amazon ElastiCache (Redis): Caches tax/shipping rules [RESP / TCP over TLS]
- CMS & Asset Management Component -> Amazon S3: Uploads static media assets [AWS SDK / HTTPS over TLS]

## Technology Stack
- .NET Core (.NET Core 8): Chosen for robust enterprise web API capabilities and strong typing
- ASP.NET Core Web API with MediatR: Provides clean CQRS separation for complex admin workflows
- Entity Framework Core & ADO.NET: Ensures reliable relational persistence with Amazon RDS (PostgreSQL)
- StackExchange.Redis: Enables low-latency caching of shipping and tax rules via Amazon ElastiCache
- AWS SDK for .NET: Facilitates native integration with Amazon S3, EventBridge, and SQS

## Rationale
This modular monolithic .NET Core architecture isolates administrative workloads while ensuring strict adherence to GDPR and CCPA compliance mandates. Leveraging managed AWS services and clean CQRS boundaries guarantees high availability, secure access control, and low-latency configuration management.