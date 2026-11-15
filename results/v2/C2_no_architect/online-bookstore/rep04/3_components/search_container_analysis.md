## Overview
The Online Bookstore search architecture provides scalable, sub-second book discovery for 1M MAU across physical and electronic inventories. It ensures multi-region availability, strict regulatory compliance, and robust security through managed AWS services.

## Key Elements
* Book Buyer (Primary Persona)
* Search Container (Amazon ECS on AWS Fargate)
* AWS OpenSearch Service (Managed Search Cluster)
* Amazon ElastiCache (Redis Caching Layer)
* Amazon SQS / SNS (Asynchronous Telemetry Pipeline)
* Analytics & CDP System (External System)
* AWS WAF & Amazon CloudFront (Edge Security)
* AWS Secrets Manager & AWS KMS (Security Services)

## Relationships
* Book Buyer -> AWS WAF & CloudFront: Submits keyword searches and faceted filters [HTTPS]
* AWS WAF & CloudFront -> Application Load Balancer: Routes validated search requests [HTTPS]
* Application Load Balancer -> Amazon ElastiCache: Checks cache for frequent search queries [Redis Protocol / TLS]
* Application Load Balancer -> Search Container: Forwards cache-miss search requests [HTTP/REST]
* Search Container -> AWS OpenSearch Service: Queries product catalogue and facets [HTTPS]
* Search Container -> Amazon SQS / SNS: Emits anonymous search telemetry and zero-result events [HTTPS]
* Amazon SQS / SNS -> Analytics & CDP System: Forwards telemetry asynchronously [HTTPS]
* Search Container -> AWS Secrets Manager & AWS KMS: Retrieves secrets and decrypts data [HTTPS]

## Technology Stack
* Amazon ECS on AWS Fargate: Runs the Search Container for elastic, serverless scalability (R-05).
* AWS OpenSearch Service: Provides managed, multi-AZ search capabilities with low-latency indexing and querying.
* Amazon ElastiCache (Redis): Caches frequent faceted searches to guarantee sub-second page loads on 3G (R-06).
* Amazon SQS / SNS: Decouples search telemetry ingestion to protect system uptime (R-07).
* AWS KMS & TLS 1.3: Encrypts all search queries and PII at rest and in transit for GDPR/CCPA compliance.
* AWS X-Ray & CloudWatch: Monitors distributed tracing and SLOs to maintain 99.95% availability (R-07).

## Rationale
This architecture decouples heavy search aggregations and telemetry processing using Redis caching and asynchronous SQS/SNS queues to achieve sub-second response times under high loads. Encrypted data pipelines, strict IAM roles, and multi-region Fargate deployments fulfill stringent scalability, performance, security, and availability requirements.