## Overview
[An Amazon-style online bookstore offering physical and electronic books, search, cart, secure checkout, reviews, and recommendations.]
[Engineered for global scalability, OWASP security compliance, and multi-currency transactions across three AWS regions.]

## Key Elements
• Book Buyers, Registered Reviewers, Store Administrators
• Frontend SPA (Next.js, React, AWS S3, CloudFront CDN)
• API Gateway (AWS API Gateway)
• Catalog & Search Service (ECS Fargate, Node.js/Go)
• Order & Checkout Service (ECS Fargate, Java/Spring Boot)
• Recommendation Service (ECS Fargate, Python/FastAPI)
• Pricing & Localization Service (ECS Fargate, Polyglot backend)
• Relational Database (AWS RDS PostgreSQL)
• Search Index (AWS OpenSearch)
• Cache & Session Store (AWS ElastiCache, Redis)
• Event Bus (AWS EventBridge, SNS, SQS)
• Catalog & Search UI Component, Cart & Checkout UI Component, Social Proof & Recommendation UI Component, Auth & Session Handler Component, Localization & Consent Manager Component

## Relationships
• Book Buyers, Registered Reviewers, Store Administrators -> Frontend SPA: Interacts with store interface [HTTPS, REST, GraphQL]
• Frontend SPA -> API Gateway: Sends API requests for catalogue, cart, and user actions [HTTPS, REST, GraphQL]
• API Gateway -> Backend Microservices (Catalog, Order, Recommendation, Pricing): Routes validated API traffic [gRPC, HTTPS]
• Backend Microservices -> Relational Database & Search Index: Persists data and queries search indexes [SQL, TLS]
• Frontend SPA -> AWS S3 / CloudFront CDN: Serves static assets and edge-cached pages [HTTPS]

## Technology Stack
• Frontend Framework: Next.js and React for high-performance server-side rendering and client-side routing.
• Cloud Infrastructure: AWS S3 and CloudFront CDN with Lambda@Edge for low-latency global delivery (< 2s on 3G).
• Compute & Containers: AWS ECS Fargate for running microservices securely and scalably.
• Databases & Caching: AWS RDS PostgreSQL for transactional data, AWS OpenSearch for catalogue search, and AWS ElastiCache (Redis) for session management.
• Security & Integration: NextAuth.js / OAuth2, HttpOnly Secure cookies, and strict Content Security Policy (CSP) headers for OWASP compliance.

## Rationale
[The Next.js and CloudFront edge architecture directly guarantees high performance under 3G constraints and 99.95% global availability across target AWS regions.]
[Containerized microservices on ECS Fargate paired with secure session handling ensure elastic scalability to 1M MAU while strictly enforcing GDPR, CCPA, and OWASP Top-10 security controls.]