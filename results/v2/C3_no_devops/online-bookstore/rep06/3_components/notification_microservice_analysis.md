## Overview
[The Notification Microservice handles asynchronous user messaging, preference management, and promotional broadcasts for the Online Bookstore. It ensures GDPR/CCPA compliance and 99.95% uptime while dispatching transactional and marketing communications.]

## Key Elements
- End Customer
- Marketing/Admin User
- Notification Microservice (Node.js, TypeScript, AWS ECS Fargate)
- Event Consumer / Message Broker Listener (Node.js, AWS SQS SDK)
- Notification Router & Template Engine (Node.js, Handlebars)
- Channel Adapters (Node.js, AWS SES, AWS SNS, FCM SDKs)
- Preference Controller (Express.js, TypeScript)
- Notification DB (AWS DynamoDB, AWS KMS)
- Campaign Manager Component (Express.js, TypeScript)
- Webhook Receiver Component (Express.js, TypeScript)

## Relationships
- API Gateway -> Preference Controller: Routes preference requests [gRPC over mTLS via AWS App Mesh]
- API Gateway -> Campaign Manager: Routes admin broadcast requests [REST over HTTPS]
- Event Consumer -> Notification Router: Dispatches messages [Internal function call]
- Campaign Manager -> Notification Router: Dispatches bulk payload batches [Internal function call]
- Preference Controller -> Notification DB: Reads and writes user consent [TCP]
- AWS SES/SNS -> Webhook Receiver: Delivers engagement callbacks [HTTPS]
- Channel Adapters -> AWS SES / SNS / FCM: Dispatches notifications [HTTPS REST / AWS SQS]

## Technology Stack
- Node.js & TypeScript: Core runtime and language for the microservice ensuring type safety and scalability.
- AWS ECS Fargate: Serverless container orchestration for reliable microservice deployment.
- AWS DynamoDB & AWS KMS: NoSQL storage with customer-managed keys for secure, compliant data persistence.
- Handlebars: Templating engine for localized message rendering.
- Express.js: Web framework for REST endpoints and webhook handling.

## Rationale
[The component decomposition cleanly separates transactional messaging, campaign management, and user consent into distinct modules within a secure Node.js container. Leveraging AWS serverless and managed security services guarantees strict GDPR/CCPA compliance, robust RBAC, and high availability.]