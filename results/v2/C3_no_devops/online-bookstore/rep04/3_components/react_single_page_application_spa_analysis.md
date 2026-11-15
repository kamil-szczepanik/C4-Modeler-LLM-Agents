## Overview
An Amazon-style online bookstore providing catalog browsing, secure checkout, reviews, and personalized recommendations. Built to handle 1 million monthly active users globally while complying with GDPR, CCPA, and OWASP Top-10 security standards.

## Key Elements
* **Users:** Customer, Store Administrator
* **External Systems:** Payment Gateway, Third-Party Shipping/Carrier APIs, Tax Calculation Service, Recommendation Provider, Identity Provider
* **Containers:** React Single Page Application (SPA), AWS API Gateway, Catalog & Search, Checkout & Order, Review & Rating, Notification Service, Recommendation, AWS App Mesh & Security
* **SPA Components:** Routing & Layout Component, Catalog & Search Component, Checkout & Cart Component, Admin Dashboard Component, API Client

## Relationships
* **Customer -> React SPA:** Browses catalog, manages cart, places orders, and leaves reviews via HTTPS/JSON, TLS 1.3
* **Store Administrator -> React SPA:** Accesses admin features for catalog and store management via HTTPS, OAuth2/OIDC
* **React SPA -> AWS API Gateway:** Sends API requests for catalog, checkout, reviews, and recommendations via HTTPS/JSON, TLS 1.3

## Technology Stack
* **Frontend:** React, React Router, Zustand/Redux Toolkit, Axios/Fetch
* **Hosting & Delivery:** AWS S3, AWS CloudFront (with CSP and SRI headers)
* **Backend & APIs:** Spring Boot, Node.js/Express, Python/FastAPI, AWS API Gateway
* **Databases & Search:** Amazon OpenSearch, Amazon DynamoDB, Amazon Aurora PostgreSQL
* **Security & Auth:** OAuth2/OIDC, JWT via httpOnly Secure SameSite=Strict cookies, AWS Secrets Manager, AWS KMS

## Rationale
This decoupled SPA architecture ensures sub-2-second page loads on 3G networks via route-based code-splitting and global CloudFront caching. Strict adherence to token security and backend authorization mitigates OWASP Top-10 vulnerabilities while scaling effortlessly across multiple AWS regions.