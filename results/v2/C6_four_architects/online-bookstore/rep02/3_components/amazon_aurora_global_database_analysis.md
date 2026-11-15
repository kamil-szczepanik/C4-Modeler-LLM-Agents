## Overview
The Online Bookstore system is a scalable, multi-region e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It delivers high availability, low-latency performance, and strict regulatory compliance across three global AWS regions.

## Key Elements
- **Users**: Customer, Admin/Content Manager
- **External Systems**: Payment Gateway, Third-Party Shipping API, Email/Notification Service, External Identity Provider, Tax Calculation Service
- **Containers**: Frontend SPA (React, TypeScript), BFF Container (Next.js, Node.js), Core E-Commerce Service (Spring Boot, Java), Recommendation Engine (FastAPI, Python), Search & Discovery (Amazon OpenSearch), Notification Worker, Amazon Aurora Global Database (PostgreSQL), Amazon DynamoDB, Amazon ElastiCache (Redis), Amazon MSK (Apache Kafka), AWS Glue & Athena
- **Aurora Components**: Primary DB Instance, Secondary DB Instances, Aurora Distributed Storage Volume, Global Database Manager (GDM), Aurora Connection Manager (AWS RDS Proxy), Global Routing & Failover Monitor, Audit & Compliance Logging Subsystem, Read/Write Endpoint Resolver

## Relationships
- **Frontend SPA -> BFF Container**: Serves web application and API requests [HTTPS/REST]
- **BFF Container -> Core E-Commerce Service**: Routes business logic and transactional requests [gRPC/TLS]
- **Core E-Commerce Service -> Aurora Connection Manager**: Routes SQL queries [TLS/JDBC]
- **Aurora Connection Manager -> Primary/Secondary DB Instances**: Forwards pooled connections [TLS/PostgreSQL wire protocol]
- **Primary DB Instance -> Storage Subsystem**: Persists transaction logs via block-level replication [Internal AWS Protocol]
- **Storage Subsystem -> Secondary DB Instances**: Cross-region storage replication < 1 second lag [AWS Backbone Network]
- **Primary DB Instance -> Compliance/Audit Lambda**: Streams security and audit events [AWS Database Activity Streams / Kinesis]

## Technology Stack
- **Frontend**: React, TypeScript hosted on AWS S3 with Amazon CloudFront CDN for global low-latency content delivery.
- **Backend Services**: Next.js, Spring Boot (Java), FastAPI (Python) running on Amazon ECS/Fargate for scalable microservices.
- **Database & Caching**: Amazon Aurora Global Database (PostgreSQL) with AWS RDS Proxy for connection pooling and ACID transactions; Amazon ElastiCache (Redis) for fast caching.
- **Search & Streaming**: Amazon OpenSearch for keyword catalogue search; Amazon MSK (Apache Kafka) for event streaming.
- **Cloud Infrastructure**: AWS multi-region deployment across `us-east-1`, `eu-west-1`, and `ap-southeast-1` orchestrated via AWS Route 53.

## Rationale
This architecture uses decoupled storage and compute with Amazon Aurora Global Database to achieve low-latency reads and secure ACID writes globally. Containerized microservices on ECS/Fargate combined with AWS RDS Proxy ensure scalability for 1 million MAU and 99.95% uptime.