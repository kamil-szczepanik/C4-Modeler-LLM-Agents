## Overview
An AWS-hosted Global Edge Layer provides secure, low-latency entry for 1 million monthly active users of the Online Bookstore. It leverages Amazon Route 53, AWS WAF, and Amazon CloudFront to satisfy stringent security, GDPR, and performance requirements.

## Key Elements
*   **DNS Router**: Amazon Route 53 (Anycast geo-DNS)
*   **Web Application Firewall**: AWS WAF (OWASP Top-10 mitigation and rate-limiting)
*   **Edge Request Transformer**: CloudFront Functions / Lambda@Edge (Header sanitization and JWT validation)
*   **Edge Content Delivery Network**: Amazon CloudFront and Amazon S3 (Static asset caching and dynamic routing)
*   **Regional Backend**: Amazon API Gateway

## Relationships
*   **DNS Router** -> **Web Application Firewall**: Directs global user traffic [DNS]
*   **Web Application Firewall** -> **Edge Request Transformer**: Forwards filtered HTTP/S requests [HTTPS]
*   **Edge Request Transformer** -> **Edge Content Delivery Network**: Passes enriched requests for cache evaluation [Internal]
*   **Edge Content Delivery Network** -> **Amazon API Gateway**: Routes dynamic API traffic and bypasses cache for authenticated routes [HTTPS/REST]

## Technology Stack
*   **Amazon Route 53**: Selected for geo-DNS routing and automated health-check failovers across regions.
*   **AWS WAF**: Chosen for real-time OWASP Top-10 mitigation, rate-limiting, and geo-restriction compliance.
*   **Amazon CloudFront & S3**: Implemented for global static asset delivery and dynamic origin shielding.
*   **CloudFront Functions / Lambda@Edge**: Utilized for sub-millisecond request transformation and edge JWT validation.

## Rationale
This architecture ensures global page loads under 2 seconds on 3G networks through edge caching and Anycast routing. Furthermore, it meets 99.95% availability targets and robust GDPR/CCPA security constraints via automated failovers and edge-level threat mitigation.