## Overview
The Online Bookstore is a multi-region e-commerce platform built on AWS to sell physical and electronic books with recommendations and reviews. Its core purpose is to provide a scalable, secure, and globally performant shopping experience meeting strict compliance and availability standards.

## Key Elements
* **Users:** Customers (browsing, purchasing, reviewing)
* **Core System:** Online Bookstore (AWS-hosted e-commerce platform)
* **External Systems:** Third-party Payment Gateway, Shipping Providers, Identity/Compliance Services, Notification Services, Foreign Exchange (FX) Rate Provider, Tax Calculation Service, Anti-Fraud / Risk Assessment Service, Book Distributors / Inventory Suppliers, Observability/Audit Logging Provider, CI/CD Deployment and Configuration Management

## Relationships
* **Customers to Online Bookstore:** HTTPS / WebSockets via AWS CloudFront CDN
* **Online Bookstore to Payment Gateway:** HTTPS / REST API for secure checkout transactions
* **Online Bookstore to Shipping Providers:** HTTPS / REST API for logistics and fulfillment
* **Online Bookstore to Tax & FX Providers:** HTTPS / REST API for real-time tax calculation and multi-currency conversion (USD, EUR, GBP)
* **Online Bookstore to Inventory Suppliers:** HTTPS / REST API for real-time stock synchronization

## Technology Stack
* **Cloud Infrastructure:** AWS (Regions: us-east-1, eu-west-1, ap-southeast-1) for global multi-region scalability and 99.95% uptime
* **Delivery & Performance:** AWS CloudFront CDN for edge caching to achieve <2s page load times on 3G
* **Security & Compliance:** Centralized SIEM/Audit Logging and Secret Management pipelines for GDPR/CCPA compliance and OWASP Top-10 mitigations

## Rationale
This architecture leverages managed global cloud services and specialized third-party APIs to handle complex regulatory, financial, and logistical constraints. Regional data residency and edge caching ensure high performance and strict data privacy compliance for 1M MAU.