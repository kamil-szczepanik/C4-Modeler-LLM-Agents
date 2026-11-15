## Overview
The Online Bookstore system is a scalable e-commerce platform providing catalog search, secure checkout, reviews, and recommendations for 1 million monthly active users. It uses an AWS-hosted microservices architecture to deliver sub-second search performance and multi-region availability.

## Key Elements
- Book Shopper & Store Administrator (Users)
- Catalog & Search Service (Spring Boot/Python)
- Amazon OpenSearch Container
- Search Engine Core (Apache Lucene)
- Ingest Pipeline (OpenSearch Ingest Node)
- Cluster Manager (OpenSearch Master Node)
- OpenSearch Dashboards (Web UI)
- AWS CloudWatch & Datadog
- Amazon S3

## Relationships
- Catalog & Search Service -> Ingest Pipeline: Index/Update book catalog documents [HTTPS / JSON]
- Catalog & Search Service -> Search Engine Core: Execute keyword and faceted search queries [HTTPS / JSON]
- Store Administrator -> OpenSearch Dashboards: View search analytics and manage index patterns [HTTPS / TLS]
- OpenSearch Dashboards -> Search Engine Core: Query internal indices for telemetry [REST / JSON over HTTPS]
- OpenSearch -> Amazon S3: Automated daily snapshots and cross-region backups [AWS SDK]

## Technology Stack
- Amazon OpenSearch Service: Managed search engine for sub-second keyword queries and faceted filtering
- OpenSearch Dashboards: Visualization UI for store analytics and index management
- Apache Lucene: Inverted-index storage powering the search engine core
- AWS KMS & IAM: Data encryption at rest and fine-grained access control for GDPR/CCPA compliance
- Terraform: Infrastructure as code for automated Blue/Green deployments

## Rationale
This architecture uses Amazon OpenSearch to meet sub-second performance goals under high scale while maintaining regional availability. Separation of cluster nodes and automated lifecycle policies ensure cost-effective compliance and operational resilience.