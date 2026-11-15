## Overview
A scaled-down Amazon-style e-commerce Single Page Application providing book browsing, secure checkout, reviews, and recommendations. It delivers a fast, secure user experience globally while maintaining GDPR and CCPA compliance.

## Key Elements
* Shopper / Reviewer (User)
* Store Administrator (User)
* Single Page Application (Container: React, TypeScript, Amazon CloudFront, Amazon S3)
* Routing & Shell Component (Component)
* Catalogue & Search View (Component)
* Cart & Checkout Flow (Component)
* Review & Rating Widget (Component)
* State Management Store (Component)
* API Client (Component)
* API Gateway & Security (External Container)

## Relationships
* Shopper / Reviewer -> Single Page Application: Accesses static assets and interacts with UI [HTTPS]
* Store Administrator -> Single Page Application: Accesses admin features via UI [HTTPS]
* Routing & Shell -> Catalogue, Cart & Checkout, and Review components: Dynamically loads feature bundles [In-Memory]
* Catalogue, Cart, and Review components -> State Management Store: Reads and writes local UI state [In-Memory]
* All functional components -> API Client: Synchronizes data and communicates [In-Memory]
* API Client -> API Gateway & Security: Sends REST API requests [HTTPS/REST]

## Technology Stack
* React & TypeScript: Core UI framework for component-driven architecture and type safety
* Amazon CloudFront & S3: Global static asset hosting for ultra-low latency delivery (<2s on 3G)
* Zustand / React Context: Ephemeral client state management for currency and cart counts without prop-drilling
* Axios / Fetch wrapper: Centralized HTTP client managing CSRF headers, PII redaction, and circuit breakers
* CloudWatch RUM & AWS X-Ray: Real-user telemetry for Core Web Vitals and conversion funnel tracking

## Rationale
This architecture uses a static-only CloudFront CDN combined with client-side rendering to meet strict sub-2-second performance goals across global AWS regions. Enforcing a strict security boundary—using short-lived httpOnly cookies, API Gateway authorization, and client-side PII scrubbing—ensures robust OWASP mitigation and GDPR/CCPA compliance.