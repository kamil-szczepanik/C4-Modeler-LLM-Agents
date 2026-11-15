## Overview
An Amazon-style online bookstore designed to provide scalable catalogue browsing, secure checkout, and recommendations for 1M MAU. The system operates across multiple AWS regions while maintaining strict GDPR, CCPA, and multi-currency compliance.

## Key Elements
- **Actors:** Guest Shopper, Registered Customer, Store Administrator, Customer Support Agent.
- **Core System:** Online Bookstore (AWS cloud-native application).
- **External Systems:** Payment Gateway, Shipping Provider API, Tax/Compliance Service.
- **Infrastructure Containers:** AWS Route 53, AWS SQS/EventBridge, Amazon DynamoDB.

## Relationships
- Shopper / Customer -> Online Bookstore: HTTPS (Web/Mobile) for catalogue browsing, cart, and checkout.
- Store Administrator -> Online Bookstore: HTTPS (Admin Portal) for inventory and moderation.
- Online Bookstore -> Payment Gateway: HTTPS / REST (Synchronous with Circuit Breaker and TLS 1.3).
- Online Bookstore -> Shipping Provider & Tax APIs: Asynchronous event-driven messaging via AWS SQS/EventBridge.

## Technology Stack
- **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) to guarantee 99.95% uptime and global scale.
- **Traffic Routing:** Amazon Route 53 for global DNS health-checking and latency-based routing.
- **Messaging & Decoupling:** AWS SQS/EventBridge to prevent cascading failures from external third-party APIs.
- **Resilience & State:** Amazon DynamoDB for idempotency storage and safe transaction retries.

## Rationale
This multi-region, event-driven architecture isolates third-party dependencies to prevent checkout failures and protect conversion rates. It ensures regulatory compliance, low latency, and high availability for a global user base.