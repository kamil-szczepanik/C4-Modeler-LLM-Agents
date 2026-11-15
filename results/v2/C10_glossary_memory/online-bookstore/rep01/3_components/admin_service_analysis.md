## Overview
The Admin Service is a backend Node.js container that manages administrative operations, catalogue curation, and store configurations for the Online Bookstore. It secures platform operations for Store Administrators across multi-region AWS deployments.

## Key Elements
- Store Administrator [person, container]
- Amazon API Gateway [container]
- Admin Service [container, Node.js / Express]
- Catalogue Management Controller [component, Express Router / Joi]
- Audit Logging Middleware [component, Winston / Amazon CloudWatch]
- Admin Data Repository [component, Sequelize ORM]
- Amazon Aurora PostgreSQL [container]
- Amazon CloudWatch / S3 [externalSystem]
- AWS Secrets Manager [externalSystem]

## Relationships
- Store Administrator -> Admin Portal (HTTPS via AWS CloudFront)
- Admin Portal -> Amazon API Gateway (HTTPS/REST with JWT validation)
- Amazon API Gateway -> Admin Service (HTTPS/REST with JWT validation)
- Catalogue Management Controller -> Admin Data Repository (TCP/Sequelize)
- Audit Logging Middleware -> Amazon CloudWatch / S3 (HTTPS/REST)
- Admin Data Repository -> Amazon Aurora PostgreSQL (TLS/TCP)
- Admin Service -> AWS Secrets Manager (HTTPS/REST)

## Technology Stack
- Node.js / Express: Chosen for rapid backend API development and asynchronous I/O performance.
- Sequelize ORM: Used for structured database interactions with Amazon Aurora PostgreSQL.
- Joi: Implemented for strict input validation and payload sanitization during batch imports.
- Winston & Amazon CloudWatch: Utilized for asynchronous structured compliance and audit logging.
- TLS/TCP & AWS IAM: Enforces secure database transport and least-privilege access.

## Rationale
This architecture ensures secure, highly available administrative control while optimizing transactional database performance through asynchronous audit offloading. It fulfills strict security, compliance, and multi-region scalability requirements for the e-commerce platform.