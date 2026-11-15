## Overview
- An Amazon-style e-commerce web platform enabling global users to purchase physical and electronic books with integrated reviews and recommendations.
- Built for high availability (99.95% uptime) across three AWS regions to support 1 million monthly active users under strict compliance standards.

## Key Elements
- **Actors:** Customer, Administrator / Content Manager
- **Core System:** Online Bookstore System (AWS VPC, multi-region)
- **External Systems:** Payment Gateway (Stripe/PayPal), Shipping Provider APIs, Identity Provider (AWS Cognito/Auth0), Recommendation ML Service, Notification Service (Amazon SES/SendGrid)
- **Containers:** Edge API Gateway/CDN, Frontend Web/Mobile App, Catalogue Service, Shopping Cart & Secure Checkout Service, Review & Rating Service, Recommendation Service

## Relationships
- **Customer -> Edge API Gateway/CDN:** HTTPS (Web/Mobile) for browsing, purchasing, and reviews
- **Online Bookstore System -> Payment Gateway:** REST/HTTPS for secure transactions and tokenization
- **Online Bookstore System -> Shipping Provider APIs:** REST/HTTPS for rate calculation and label generation (asynchronously queued)
- **Online Bookstore System -> Identity Provider:** OAuth2/OIDC via HTTPS for authentication and MFA
- **Online Bookstore System -> Recommendation ML Service:** REST/gRPC via HTTPS for item affinity scoring
- **Online Bookstore System -> Notification Service:** REST/SMTP for asynchronous transactional alerts

## Technology Stack
- **Cloud Infrastructure:** AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`) for multi-region global distribution and low latency
- **Edge & Routing:** Anycast DNS / Global Load Balancer, managed API Gateway / CDN for static caching and rate-limiting
- **Security & Auth:** AWS Cognito/Auth0 (OAuth2/OIDC), TLS 1.3 for transport encryption, mTLS for internal VPC communication
- **Integration:** Asynchronous message queues for decoupled shipping fulfillment and notification dispatch

## Rationale
- Multi-region AWS deployment with edge caching ensures sub-2-second page loads globally and satisfies the 99.95% uptime SLA.
- Decoupling checkout containers and offloading payments, shipping, and ML recommendations minimizes blast radius and maintains compliance with GDPR, CCPA, and PCI-DSS.