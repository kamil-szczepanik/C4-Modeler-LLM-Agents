## Overview
An Amazon-style e-commerce platform delivering global book purchasing, recommendations, and reviews. The system ensures high availability, GDPR compliance, and sub-second performance across multi-currency operations.

## Key Elements
* Customers and Registered Reviewers (Web/Mobile Users)
* Store Administrators (Internal Management)
* Online Bookstore System (Cloud-hosted core platform)
* Stripe / PayPal (Payment Gateway Provider)
* FedEx / UPS (Third-Party Shipping APIs)
* AWS SES / SendGrid (Email/Notification Service)
* Avalara / TaxJar (Tax Calculation Service)

## Relationships
* Customer -> Online Bookstore: HTTPS (Web/Mobile) for browsing, cart, and checkout
* Online Bookstore -> Payment Gateway: HTTPS / REST API (TLS 1.3) for payment processing
* Online Bookstore -> Shipping Provider: HTTPS / REST API for label generation and tracking
* Online Bookstore -> Tax Calculation Service: HTTPS / REST API for real-time tax estimation
* Online Bookstore -> Email/Notification Service: HTTPS / SMTP for transactional alerts

## Technology Stack
* AWS (`us-east-1`, `eu-west-1`, `ap-southeast-1`): Multi-region cloud infrastructure for global availability and low latency
* Route 53: Edge-terminated failover and latency-based routing
* Terraform / CDK: Infrastructure as Code for automated blue/green and canary deployments
* REST APIs with Circuit Breakers & Idempotency Keys: Resilient integration pattern for external third-party services

## Rationale
The multi-region AWS architecture ensures 99.95% uptime and sub-2-second page loads globally. Offloading PCI-DSS and tax calculations to specialized external providers minimizes security scope while guaranteeing regulatory compliance.