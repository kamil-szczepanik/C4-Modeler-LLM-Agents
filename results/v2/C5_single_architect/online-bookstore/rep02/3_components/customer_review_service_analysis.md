## Overview
The Online Bookstore is a scaled-down e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. This architecture summary defines the internal component structure and protocols for the Customer Review Service.

## Key Elements
- **Review API Controller**: Node.js and Express interface handling incoming HTTP/REST/gRPC endpoints.
- **Review Domain Service**: TypeScript core containing business logic, rating aggregation, and validation.
- **Moderation Client**: Content safety and text filtering module for GDPR compliance.
- **Review Data Access Repository**: Node.js `pg` driver managing relational persistence.
- **Event Publisher Component**: AWS SDK v3 JavaScript module for event dispatch.
- **Amazon Aurora**: Relational database for review records and indices.
- **Amazon SNS / SQS**: Message broker for asynchronous event fan-out.

## Relationships
- **API Gateway** -> **Review API Controller**: Routes incoming review requests [HTTPS / REST / JSON].
- **Review API Controller** -> **Review Domain Service**: Delegates requests [Direct TypeScript Function Calls].
- **Review Domain Service** -> **Moderation Client**: Validates text content [Internal Module Call].
- **Review Domain Service** -> **Review Data Access Repository**: Queries and persists review data [SQL / TCP].
- **Review Data Access Repository** -> **Amazon Aurora**: Stores and retrieves relational records [PostgreSQL Wire Protocol / TCP].
- **Review Domain Service** -> **Event Publisher Component**: Triggers event publishing [Internal Module Call].
- **Event Publisher Component** -> **Amazon SNS / SQS**: Publishes `ReviewCreated` and `ReviewDeleted` events [HTTPS / AWS SDK v3].

## Technology Stack
- **Node.js & Express**: Powers the API layer for fast I/O handling.
- **TypeScript**: Ensures type safety across domain logic and controllers.
- **Amazon Aurora**: Provides ACID guarantees for relational review storage and rating calculations.
- **Amazon SNS/SQS**: Enables reliable, decoupled asynchronous messaging.
- **AWS SDK v3**: Facilitates secure AWS service integration using IAM roles.

## Rationale
This component-based architecture isolates review management logic to scale independently while meeting strict performance and security constraints. Node.js and TypeScript provide rapid development velocity combined with strong typing for core domain rules.