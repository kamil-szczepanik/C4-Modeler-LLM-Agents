## Overview
The Localization Service is an edge-based router built on AWS Lambda@Edge that handles multi-currency conversion, regional routing, and language localization for the Online Bookstore. Its core purpose is to drive global conversion rates and ensure low-latency performance for international shoppers.

## Key Elements
* Shoppers, Vendors, and Admins (Users)
* AWS CloudFront & AWS WAF (CDN and Edge Security)
* Localization Service - AWS Lambda@Edge (Container/Service)
* Geo-Router Component (Component)
* Currency & Translation Resolver Component (Component)
* Cookie & Preference Manager Component (Component)
* Origin Request Transformer Component (Component)
* Amazon S3 (Localization dictionaries and static currency rates)
* Amazon API Gateway (Upstream entry point)

## Relationships
* Shoppers to AWS CloudFront: HTTPS (TLS 1.3) viewer request/response events
* Localization Service to Amazon S3: HTTPS (TLS 1.3) via internal AWS backbone for fetching dictionaries
* Localization Service to Amazon API Gateway: HTTPS with injected custom headers (`X-User-Currency`, `X-User-Locale`)
* AWS CloudWatch Canary to Localization Service: Automated global synthetic monitoring

## Technology Stack
* AWS Lambda@Edge (Node.js/JavaScript): Chosen for execution limits and low-latency global edge compute
* Amazon S3 & CloudFront: Used for bundling and syncing static dictionaries to eliminate cross-region database calls
* TLS 1.3 & AWS WAF: Mandated for secure client communication and injection attack prevention
* CloudWatch Lambda Insights & Synthetics: Deployed for distributed observability and 99.95% uptime validation

## Rationale
This architecture eliminates cross-region database lookups by caching dictionaries in S3 at edge locations, guaranteeing sub-second page loads on 3G. Furthermore, edge-based execution and strict request sanitization meet stringent security, GDPR compliance, and global scalability requirements.