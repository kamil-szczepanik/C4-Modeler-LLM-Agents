## Overview
The Online Bookstore is a scaled-down Amazon-style e-commerce platform for purchasing physical and electronic books with integrated reviews and recommendations. It delivers high scalability, security, and multi-region availability on AWS.

## Key Elements
* Customer and Admin / Content Manager (Human Actors)
* Online Bookstore (Core Software System)
* Payment Gateway (Stripe/PayPal)
* Shipping Provider APIs (FedEx/UPS)
* Tax & Compliance Service (Avalara)
* Recommendation Engine (AWS Personalize)

## Relationships
* Customer to Online Bookstore via HTTPS / TLS 1.3 (Web/Mobile App)
* Admin to Online Bookstore via HTTPS / TLS 1.3 with MFA and OAuth 2.0 / OIDC
* Online Bookstore to Payment Gateway via HTTPS/REST
* Online Bookstore to Shipping Provider APIs via HTTPS/REST
* Online Bookstore to Tax & Compliance Service via HTTPS/REST
* Online Bookstore to Recommendation Engine via HTTPS/REST with pseudonymized IDs

## Technology Stack
* AWS (us-east-1, eu-west-1, ap-southeast-1): Multi-region cloud infrastructure ensuring 99.95% uptime and low latency
* AWS API Gateway: Mediates and secures all external egress points and traffic
* Web Application Firewall (WAF): Deployed at the edge for OWASP Top-10 mitigation
* TLS 1.3: Enforced for all external communications to secure data in transit
* OAuth 2.0 / OIDC: Standardized token-based session management for customer authentication

## Rationale
This architecture uses multi-region AWS deployment and edge security to guarantee 99.95% uptime and performance for 1M MAU. Decoupling third-party services via TLS 1.3 secured API gateways ensures strict GDPR/CCPA compliance and data protection.