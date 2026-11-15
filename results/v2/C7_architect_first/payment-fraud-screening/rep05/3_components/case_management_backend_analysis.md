## Overview
The Case Management Backend is a Node.js and TypeScript microservice running on AWS ECS Fargate that manages analyst reviews, state transitions, and audit trails for flagged payment transactions. It ensures strict compliance, secure data handling, and scalable workflow execution within a fixed budget.

## Key Elements
* **Case API Controller**: Node.js, Express, and TypeScript component handling incoming HTTPS requests from Fraud Analysts.
* **Case Workflow Engine**: TypeScript component managing case state transitions and SLA timers.
* **Audit & Evidence Assembler**: TypeScript component sanitizing payloads and gathering decision metadata.
* **Read Model Projection Component**: TypeScript component maintaining denormalized read views from asynchronous events.
* **Data Access Layer**: TypeORM/Prisma component interfacing with PostgreSQL via AWS RDS Proxy.
* **Audit and Case Data Store**: Amazon Aurora PostgreSQL database storing transactional case data.
* **Messaging & Event Bus**: Amazon SQS and SNS for asynchronous event distribution.

## Relationships
* **Case API Controller** -> **Case Workflow Engine**: Invokes workflow operations [In-process]
* **Case API Controller** -> **Audit & Evidence Assembler**: Gathers decision metadata and sanitized evidence [In-process]
* **Case API Controller** -> **Read Model Projection Component**: Queries paginated audit trails [In-process]
* **Case Workflow Engine** & **Audit & Evidence Assembler** -> **Data Access Layer**: Executes queries [In-process]
* **Case Workflow Engine** -> **Messaging & Event Bus**: Publishes state change events [Amazon SQS/SNS]
* **Data Access Layer** -> **Audit and Case Data Store**: Performs transactional queries [AWS RDS Proxy over VPC endpoints]

## Technology Stack
* **Node.js / TypeScript**: Provides rapid development and strong typing for the 3-engineer team.
* **AWS ECS Fargate**: Minimizes operational overhead with serverless container orchestration.
* **Amazon Aurora PostgreSQL**: Provides robust relational storage for case data and audit trails.
* **AWS RDS Proxy**: Manages connection pooling to prevent database exhaustion from Fargate tasks.
* **TypeORM / Prisma**: Simplifies data modeling and database access within the TypeScript backend.
* **Amazon SQS / SNS**: Enables reliable asynchronous event-driven messaging and audit logging.

## Rationale
This architecture balances low-latency analyst workflows with strict 7-year auditability and PCI-DSS compliance requirements. Decoupling asynchronous read projections from transactional writes protects database performance while staying within the 25,000 EUR monthly infrastructure budget.