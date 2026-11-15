## Overview
The Customer & Review Service is a Node.js microservice managing user profiles, compliance, and 5-star reviews for the Online Bookstore. It isolates transactional user data and review logs to support 1 million MAU and regulatory standards.

## Key Elements
* Customer & Review Service (Node.js, Express/NestJS Container)
* Review Management Component
* Customer Profile Component
* Review Moderation Component
* Data Privacy / Compliance Component
* MongoDB Atlas (Database)
* Amazon SNS & SQS (Messaging)

## Relationships
* API Gateway -> Review Management & Customer Profile: Routes requests [gRPC / HTTPS]
* Review Management & Customer Profile -> MongoDB Atlas: Persists documents [TLS / MongoDB Protocol]
* Review Management -> Amazon SNS: Publishes review events [HTTPS / MQTT]
* Review Management -> Amazon SQS: Consumes moderation failure events [HTTPS]
* Customer Profile -> Data Privacy Component: Triggers compliance cascades [Internal Function Calls]

## Technology Stack
* Node.js with Express/NestJS: Provides lightweight, asynchronous execution for high-throughput API endpoints.
* MongoDB Atlas: Offers flexible, semi-structured document storage for reviews and user profiles.
* Mongoose ODM: Enforces schema validation over TLS connections.
* Amazon SNS & SQS: Manages decoupled, asynchronous event-driven messaging for scalability.

## Rationale
This component architecture separates profile management, review handling, and compliance workflows to meet strict GDPR/CCPA requirements. Decoupled asynchronous messaging and scalable document storage ensure high availability and performance under heavy traffic.