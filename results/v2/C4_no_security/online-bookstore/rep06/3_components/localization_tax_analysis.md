## Overview
The Localization & Tax component manages multi-currency pricing, regional tax calculations, and compliance rules for the Online Bookstore platform. It ensures resilient, low-latency financial transactions across global markets using AWS infrastructure and robust caching strategies.

## Key Elements
- **LocalizationController**: Spring MVC RestController exposing gRPC endpoints for internal communication.
- **TaxRuleResolver**: Spring component encapsulating regional tax classifications and B2B exemptions.
- **TaxCalculationEngine**: Spring component managing external tax queries and Resilience4j circuit breakers.
- **CurrencyConverter**: Spring component handling multi-currency conversion with hourly refresh.
- **Amazon ElastiCache (Redis)**: Regional distributed cache for exchange rates and tax jurisdictions.
- **Tax & Currency Provider**: External API for real-time exchange rates and tax rates.

## Relationships
- **API Gateway -> LocalizationController**: Routes internal traffic via VPC links [gRPC]
- **LocalizationController -> TaxRuleResolver -> TaxCalculationEngine**: Executes internal logic [In-process Java method calls]
- **TaxCalculationEngine -> Tax & Currency Provider**: Queries exchange rates and tax info [HTTPS]
- **TaxCalculationEngine -> Amazon S3**: Streams scrubbed audit logs [AWS Kinesis Firehose]

## Technology Stack
- **Spring Boot / Java**: Core application framework for modular component design.
- **Resilience4j**: Implements circuit breakers and fallbacks to prevent third-party API outages from blocking checkout.
- **Amazon ElastiCache (Redis)**: Provides multi-region distributed caching for sub-millisecond local latency.
- **AWS ECS Fargate**: Hosts containerized services with zero-downtime rolling updates via AWS CodeDeploy.
- **Amazon S3 & Kinesis Firehose**: Secures immutable, PII-scrubbed audit logging for financial compliance.

## Rationale
This architecture guarantees 99.95% uptime and sub-millisecond internal performance by decoupling third-party dependencies through regional Redis caching and Resilience4j circuit breakers. It strictly satisfies multi-currency and global tax compliance requirements without risking checkout availability.