## Overview
[The Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with recommendations and reviews, designed to handle 1M MAU.]
[It is built on AWS across multiple regions, ensuring GDPR and CCPA compliance, multi-currency support, and 99.95% uptime.]

## Key Elements
*   **Customers & Admins**: End users and content managers interacting with the system.
*   **Frontend**: Single-Page Application (SPA) and Back-Office Admin Portal (React, Amazon S3, Amazon CloudFront).
*   **API Gateway**: Amazon API Gateway routing traffic via VPC Links [mTLS].
*   **Core Microservices Container**: Hosted on Amazon ECS Fargate, comprising:
    *   *Catalog & Search Component* (Spring Boot)
    *   *Checkout & Order Component* (Spring Boot)
    *   *Admin & Compliance Component* (Python/FastAPI)
    *   *Async Notification Service* (Python/FastAPI)
*   **Databases & Messaging**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon EventBridge, Amazon SNS, Amazon SES.
*   **External Systems**: Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Recommendation Engine.

## Relationships
*   API Gateway -> Core Microservices: Routes traffic [mTLS over VPC Links]
*   Core Microservices -> Amazon Aurora PostgreSQL: Reads/writes relational data [JDBC/TLS]
*   Core Microservices -> Amazon DynamoDB: Reads/writes cart states [AWS SDK / TLS]
*   Core Microservices -> Amazon EventBridge: Publishes/consumes domain events [AWS SDK / TLS]
*   Core Microservices -> Payment Gateway, Shipping Provider APIs, Tax & Compliance Service, Recommendation Engine: Processes transactions, fulfillment, compliance, and recommendations [REST/TLS]
*   Async Notification Service -> Amazon SNS / Amazon SES: Dispatches notifications [AWS SDK/TLS]

## Technology Stack
*   **Frontend**: React deployed on Amazon S3 and distributed via Amazon CloudFront for fast global performance (<2s on 3G).
*   **Compute**: Amazon ECS Fargate for serverless container orchestration of microservices.
*   **Languages & Frameworks**: Spring Boot for Catalog/Checkout; Python/FastAPI for Admin and Async Notification services.
*   **Databases**: Amazon Aurora PostgreSQL for relational data with AWS KMS encryption; Amazon DynamoDB for low-latency cart states.
*   **Messaging & Integration**: Amazon EventBridge for event-driven workflows; Amazon SNS/SES for asynchronous notifications.

## Rationale
[This microservices architecture isolates critical revenue-generating workflows like checkout from non-critical paths like recommendations to guarantee 99.95% availability and high scalability.]
[Event-driven patterns and managed AWS services ensure secure, asynchronous operations that easily scale to support 1M MAU while meeting strict GDPR and CCPA compliance standards.]