## Overview
An AWS-hosted online bookstore delivering a secure, globally distributed single-page application for physical and electronic book retail. It ensures low-latency performance and high availability across multiple international regions.

## Key Elements
- Customer (End User)
- Amazon CloudFront (Global CDN & Edge Router)
- AWS S3 Bucket (Static Asset Storage)
- CloudFront Functions (Edge Logic)
- AWS WAF (Web Application Firewall)
- AWS API Gateway (Backend API Entry Point)

## Relationships
- Customer -> Amazon CloudFront: Requests static assets and SPA routes via HTTPS
- Amazon CloudFront -> CloudFront Function: Executes URL rewrites and header injections at edge runtime
- Amazon CloudFront -> AWS S3: Fetches uncached static assets using Origin Access Control (OAC) over AWS Private Link
- Amazon CloudFront -> AWS API Gateway: Forwards API requests with JWT validation via HTTPS/REST
- AWS WAF -> Amazon CloudFront: Inspects incoming client traffic for security threats

## Technology Stack
- React & TypeScript: Frontend SPA framework for client-side catalog browsing, cart, and reviews
- AWS S3: Scalable object storage with server-side encryption via AWS KMS and Block Public Access
- AWS CloudFront: Edge distribution providing SSL/TLS termination and global caching
- CloudFront Functions: JavaScript edge runtime for sub-2ms request/response transformations
- AWS WAF: Edge security filtering for OWASP Top-10 mitigations

## Rationale
This architecture leverages Amazon CloudFront and S3 to meet global performance targets with sub-2-second page loads on 3G networks. Edge-level security controls, OAC isolation, and multi-region S3 replication guarantee 99.95% uptime and strict compliance with data protection standards.