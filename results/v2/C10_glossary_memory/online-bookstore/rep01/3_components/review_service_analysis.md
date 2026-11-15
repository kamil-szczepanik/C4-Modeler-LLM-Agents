## Overview
The Online Bookstore is a multi-region e-commerce platform providing catalogue browsing, secure checkout, reviews, and personalized recommendations for 1 million monthly active users. Its core purpose is delivering a reliable, secure, and compliant online retail experience across global markets.

## Key Elements
- Book Shopper (person)
- Reviewer (person)
- Store Administrator (person)
- Web Frontend & Admin Portal (React SPA containers)
- Amazon API Gateway (Amazon API Gateway container)
- Catalogue Service, Order and Checkout Service, Review Service, Admin Service, Recommendation Integration Service (Backend Node.js/Go/Python containers)
- Amazon Aurora PostgreSQL, Amazon DynamoDB, Amazon OpenSearch (Data store containers)

## Relationships
- Book Shopper -> Web Frontend (HTTPS via AWS CloudFront)
- Web Frontend -> Amazon API Gateway (HTTPS/REST with JWT validation)
- Amazon API Gateway -> Review Service (HTTPS/REST with JWT validation)
- Review Service -> Amazon Aurora PostgreSQL (TCP with mTLS)
- Order and Checkout Service -> Payment Gateway (HTTPS/REST)
- Recommendation Integration Service -> ML Recommendation Engine (HTTPS/REST and Asynchronous SQS/SNS)

## Technology Stack
- React SPA: Chosen for responsive, client-side rendering supporting sub-2s page loads on 3G.
- Python / FastAPI (Review Service): Chosen for rapid API development and asynchronous request handling.
- Amazon Aurora PostgreSQL: Selected for multi-region relational data persistence with encryption and GDPR purging support.
- Amazon SQS/SNS: Used for asynchronous, decoupled event-driven communication to ensure 99.95% availability.

## Rationale
This architecture uses decoupled microservices deployed across multiple AWS regions to guarantee 99.95% availability and sub-second performance under high load. Strict security controls, including mTLS, JWT validation, and RBAC, ensure adherence to OWASP Top-10 mitigations and GDPR/CCPA compliance.