## Overview
The Online Bookstore is a globally distributed e-commerce platform designed to sell physical and electronic books with integrated recommendations, reviews, and multi-currency support. Its core purpose is to deliver secure, scalable, and compliant retail services to 1 million monthly active users worldwide.

## Key Elements
- **Actors:** Customer (browser/mobile), Store Administrator
- **System Boundary:** Online Bookstore Platform
- **External Systems:** Payment Gateway, Shipping Providers, Tax Calculation Service, Notification Service, SIEM Provider, Compliance/Archival Store
- **Edge Infrastructure:** Global Content Delivery Network (CDN), Web Application Firewall (WAF)
- **Deployment Regions:** AWS Regions `us-east-1`, `eu-west-1`, `ap-southeast-1`

## Relationships
- **Customer to CDN/WAF:** HTTPS via TLS 1.3
- **Platform to Payment Gateway:** REST/JSON over HTTPS for secure checkout and multi-currency transactions
- **Platform to Shipping Providers:** REST/JSON APIs for fulfillment
- **Platform to Tax Calculation Service:** gRPC/HTTPS for regional tax compliance
- **Platform to Notification Service:** Asynchronous event messaging (AMQP/HTTPS) for transactional emails

## Technology Stack
- **Cloud Provider:** AWS (multi-region deployment across `us-east-1`, `eu-west-1`, `ap-southeast-1`) for global scalability and low latency
- **Edge Security & Delivery:** Global CDN and WAF for OWASP Top-10 mitigation and DDoS protection
- **Data & Compliance:** Regional data isolation boundaries and immutable audit logs to enforce GDPR and CCPA requirements

## Rationale
This architecture guarantees 99.95% availability and sub-2-second page loads globally by leveraging edge distribution and multi-region AWS infrastructure. Strict boundary separation and data residency controls ensure full compliance with GDPR, CCPA, and OWASP security standards.