## Overview
The Online Bookstore database architecture utilizes Amazon Aurora PostgreSQL managed via AWS RDS Proxy to provide scalable, transactional persistence for catalog and order services. It ensures 99.95% availability, regional fault tolerance, and GDPR/CCPA compliance across global AWS regions.

## Key Elements
* **AWS RDS Proxy:** Connection pooling proxy managing database traffic from microservices.
* **Database Engine Instance - Writer:** PostgreSQL 15+ instance handling transactional writes.
* **Database Engine Instance - Reader:** PostgreSQL 15+ instance handling read-only queries.
* **Distributed Storage Volume:** Amazon Aurora Storage replicating 6 copies across 3 Availability Zones.
* **AWS Secrets Manager:** Secret management system for credential handling.
* **Amazon CloudWatch:** Monitoring tool for performance metrics and auto-scaling alarms.

## Relationships
* **Catalog Service -> AWS RDS Proxy:** Sends read-only catalog queries [PostgreSQL Protocol over TCP/5432]
* **Order & Checkout Service -> AWS RDS Proxy:** Sends ACID transaction queries [PostgreSQL Protocol over TCP/5432]
* **AWS RDS Proxy -> Database Engine Instance - Writer/Reader:** Multiplexes pooled connections [PostgreSQL Protocol over TCP/5432]
* **Writer -> Distributed Storage Volume:** Performs block-level log replication [AWS Proprietary Protocol]

## Technology Stack
* **Amazon Aurora PostgreSQL:** Relational database chosen for ACID compliance and high scalability.
* **AWS RDS Proxy:** Connection pooling layer to prevent connection storms from ECS Fargate tasks and support 1M MAU.
* **Terraform (`aws_rds_cluster`):** Infrastructure as Code for Multi-AZ and multi-region deployments (`us-east-1`, `eu-west-1`, `ap-southeast-1`).
* **AWS KMS:** Encryption at rest using customer-managed keys for GDPR/CCPA compliance.
* **AWS IAM Database Authentication & `pgaudit`:** Security controls for token-based authentication and compliance auditing.

## Rationale
This architecture uses Amazon Aurora PostgreSQL combined with AWS RDS Proxy to absorb traffic spikes from 1M MAU while maintaining strict ACID transactional integrity. Security controls like TLS 1.3, IAM authentication, and KMS encryption ensure OWASP and data privacy compliance without sacrificing performance.