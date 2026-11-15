## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce site for purchasing physical and electronic books with integrated reviews and recommendations. The architecture leverages AWS across multiple regions to ensure high availability, scalability for 1 million monthly active users, and global compliance.

## Key Elements
- **Customers**: End-users browsing the catalogue, managing shopping carts, and executing checkouts.
- **Single Page Application (SPA)**: React and TypeScript application hosted on Amazon S3 and distributed via Amazon CloudFront.
- **API Gateway**: AWS API Gateway managing entry points and routing traffic.
- **Notification Service (Go)**: Container housing internal components for dispatching alerts.
- **Notification Router Component**: Handles incoming gRPC requests and domain events.
- **Template Engine Component**: Compiles localized templates using Amazon DynamoDB.
- **Dispatcher Worker Pool Component**: Concurrent Go workers executing third-party API dispatches.
- **Delivery Status Tracker Component**: Records audit logs to Amazon Aurora PostgreSQL.
- **Event Consumer Component**: Subscribes to the async event bus.
- **External Systems**: Third-Party Payment Gateway, Third-Party Shipping Provider, Identity Provider, Currency Exchange Rate Service, and External ESP/SMS APIs.
- **Data & Messaging Stores**: Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon EventBridge, and Amazon MSK.

## Relationships
- SPA -> API Gateway: Communicates via HTTPS.
- API Gateway -> Notification Service: Routes requests using gRPC over TLS.
- Async Event Bus -> Event Consumer Component: Consumes events via Kafka protocol over TLS.
- Notification Router -> Template Engine: Invokes rendering via in-memory function calls.
- Template Engine -> Dispatcher Worker Pool: Passes payloads via Go channels.
- Dispatcher Worker Pool -> External ESP/SMS APIs: Sends messages via HTTPS.
- Delivery Status Tracker -> Amazon Aurora PostgreSQL: Records receipts via SQL over TLS.

## Technology Stack
- **Frontend**: React and TypeScript for responsive browser rendering.
- **Cloud Delivery**: Amazon S3 and Amazon CloudFront for static asset hosting and global CDN edge caching.
- **Backend Services**: Spring Boot, Node.js/Express, Python/FastAPI, and Go for scalable microservices.
- **Notification Service**: Go language chosen for high performance, concurrency, and low memory footprint.
- **Databases & Messaging**: Amazon Aurora PostgreSQL for relational transactional data; Amazon DynamoDB for fast key-value storage; Amazon EventBridge and Amazon MSK for event-driven messaging.
- **Infrastructure**: Multi-region AWS deployment (us-east-1, eu-west-1, ap-southeast-1) to guarantee 99.95% uptime and global performance.

## Rationale
This decoupled, multi-region AWS architecture ensures 99.95% availability, sub-second performance on constrained networks, and linear scalability for 1 million MAUs. Containerized Go microservices and asynchronous event processing isolate third-party latency while strictly enforcing GDPR and CCPA data compliance.