## Overview
• The system is an AWS-hosted online bookstore built for 1M MAU, delivering catalog browsing, secure checkout, reviews, and personalized recommendations.
• The Checkout & Order Service processes secure financial transactions and fulfillment using a Go-based microservice architecture with ACID guarantees.

## Key Elements
• API Handler Component (Go)
• Order Management Component (Go)
• Payment Processing Component (Go)
• Fulfillment Integration Component (Go) with Shipping Rate & Estimation Sub-module
• Compliance Component (Go)
• Database Storage (Amazon Aurora PostgreSQL Global Database)
• Caching Layer (Amazon ElastiCache (Redis))
• Payment Gateway (External)
• Third-Party Shipping APIs (External)
• AWS Secrets Manager & AWS KMS

## Relationships
• API Gateway -> API Handler Component: HTTPS / gRPC with TLS 1.3
• Order Management Component -> Database Storage: PostgreSQL Protocol over TLS 1.3
• Payment Processing Component -> Payment Gateway: HTTPS / REST APIs with TLS 1.3
• Fulfillment Integration Component -> Third-Party Shipping APIs: HTTPS / REST APIs with TLS 1.3
• Fulfillment Integration Component -> Caching Layer: Redis Protocol

## Technology Stack
• Go: Selected for low memory footprint and high concurrency for peak transactional loads.
• Amazon Aurora PostgreSQL Global Database: Chosen for multi-region transactional persistence and ACID guarantees.
• Amazon ElastiCache (Redis): Used for sub-100ms caching of recommendations and shipping fallback rates.
• AWS KMS & AWS Secrets Manager: Enforces column-level PII encryption (AES-256) and dynamic credential rotation.
• OpenTelemetry & Prometheus: Deployed for distributed tracing and checkout latency monitoring.

## Rationale
• This architecture fulfills scalability, 99.95% availability, and OWASP security constraints using multi-region deployment and isolated third-party integrations.
• It ensures strict GDPR, CCPA, and PCI-DSS compliance through tokenization, anonymization components, and encrypted audit logging.