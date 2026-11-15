## Overview
The Online Bookstore uses a global AWS edge architecture to deliver high-performance e-commerce features with 99.95% availability. It processes physical and electronic book sales, recommendations, and reviews for 1 million monthly active users globally.

## Key Elements
- Route 53 DNS Resolver
- CloudFront CDN Distribution
- CloudFront Lambda@Edge / CloudFront Functions
- AWS WAF (Web Application Firewall)
- CloudFront Origin Groups & Failover

## Relationships
- Customer & Admin/Content Manager -> Route 53 DNS Resolver: Resolves domain [DNS]
- Route 53 DNS Resolver -> CloudFront CDN Distribution: Points traffic to edge [Anycast IP]
- CloudFront CDN Distribution -> AWS WAF: Inspects incoming requests [Internal AWS API]
- CloudFront Lambda@Edge / CloudFront Functions -> CloudFront CDN Distribution: Modifies headers/routes [In-memory execution]
- CloudFront CDN Distribution -> CloudFront Origin Groups & Failover: Evaluates failover routing [Internal]
- CloudFront Origin Groups & Failover -> BFF Container: Forwards dynamic traffic [HTTPS, Mutual TLS, HSTS]

## Technology Stack
- AWS Route 53: Global DNS management with latency-based routing for performance
- Amazon CloudFront: CDN for TLS 1.3 termination, caching, and reverse proxying
- CloudFront Lambda@Edge / Functions: Executes edge logic for security headers and geo-routing
- AWS WAF: Enforces OWASP Top-10 mitigations, rate-limiting, and geo-blocking

## Rationale
This edge architecture ensures global low-latency page loads under 2 seconds and strict GDPR/CCPA compliance. Automated origin failover and WAF integration guarantee 99.95% availability and robust security against web threats.