## Overview
The Analyst & Rules Portal provides a secure React-based interface for analysts and risk managers to review suspicious payment cases and configure fraud rules. It operates on AWS CloudFront and S3 while adhering to PCI-DSS Level 1 compliance and budget constraints.

## Key Elements
- SPA Frontend Core (React/TypeScript, Recharts, AWS S3, CloudFront)
- Case Review UI Module
- Rule Authoring & Simulation Module
- Simulation Results Visualizer
- AWS WAF & Amazon SQS
- Identity Provider (AWS Cognito/Okta)

## Relationships
- Manual Analyst -> SPA Frontend Core via HTTPS [OIDC/OAuth2]
- Merchant Risk Manager -> SPA Frontend Core via HTTPS [OIDC/OAuth2]
- Rule Authoring & Simulation Module -> Amazon SQS via JSON [AWS SDK]
- SPA Frontend Core -> Case Management Backend via REST/HTTPS
- SPA Frontend Core -> Identity Provider via OIDC/OAuth2 [PKCE flow]

## Technology Stack
- React/TypeScript: Lightweight SPA framework for fast frontend delivery by a three-engineer team.
- AWS S3 & CloudFront: Cost-effective static hosting with global CDN delivery.
- Recharts/Chart.js: Minimal bundle-size charting library for rendering simulation impact metrics.
- Amazon SQS: Asynchronous queue to safely decouple heavy rule-backtesting jobs from frontend requests.
- AWS WAF: Edge security to protect authentication endpoints from brute-force attacks.

## Rationale
This architecture balances strict security, PCI compliance, and user requirements while operating within a fixed 25,000 EUR monthly budget and three-engineer team limit. Asynchronous simulation queuing and memory-only token storage prevent resource starvation and data-exfiltration risks.