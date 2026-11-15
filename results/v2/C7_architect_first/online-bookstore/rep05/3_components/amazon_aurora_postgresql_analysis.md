## Overview
- Scaled-down Amazon-style e-commerce site for buying physical and electronic books with recommendations and reviews.
- Designed to handle 1M MAU with 99.95% availability, multi-currency support, and strict GDPR/CCPA compliance.

## Key Elements
- **Users**: Customers and Admins.
- **External Systems**: Global Edge Layer, Stripe/PayPal, FedEx/UPS, SendGrid/AWS SES, Fixer/Open Exchange Rates.
- **Containers**: React Single Page Application, Amazon API Gateway, ECS Fargate Microservices, Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon ElastiCache Redis.
- **Database Components**: Writer Node, Reader Node, Connection Pooler (AWS RDS Proxy), Distributed Storage Volume.

## Relationships
- Order & Checkout Service -> RDS Proxy: Transacts orders [PostgreSQL Wire Protocol / TLS over TCP/5432]
- Notification Service -> RDS Proxy: Reads/writes notification state [PostgreSQL Wire Protocol / TLS over TCP/5432]
- Review Service -> RDS Proxy: Reads/writes ratings [PostgreSQL Wire Protocol / TLS over TCP/5432]
- RDS Proxy -> Writer Node / Reader Node: Routes traffic [Internal Routing]
- Writer Node -> Storage Subsystem: Replicates data [Storage Replication]

## Technology Stack
- AWS Aurora PostgreSQL (Multi-AZ cluster, Global Databases): Ensures high availability, multi-region durability, and transactional integrity.
- AWS RDS Proxy: Manages connection spikes and prevents max-connection exhaustion from ECS Fargate.
- AWS IAM Database Authentication & Secrets Manager: Eliminates hardcoded credentials and secures fallback root accounts.
- Terraform: Provisions immutable, repeatable infrastructure across target regions.

## Rationale
- Multi-AZ Aurora Global Databases and AWS RDS Proxy ensure 99.95% uptime and low-latency scaling for 1M MAU.
- KMS encryption, IAM authentication, and advanced auditing satisfy strict GDPR and CCPA compliance requirements.