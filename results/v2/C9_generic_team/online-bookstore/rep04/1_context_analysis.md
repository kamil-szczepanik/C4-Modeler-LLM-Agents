## Overview
The Online Bookstore is a multi-region e-commerce platform built on AWS to sell physical and electronic books with integrated reviews and recommendations. Its core purpose is to provide a scalable, secure, and globally available shopping experience supporting high concurrency and multi-currency transactions.

## Key Elements
* Customers (End-users browsing catalogues, purchasing books, and leaving reviews)
* Administrators/Content Moderators (Internal operators managing catalogue data and moderating reviews)
* Online Bookstore System (Primary software system)
* Payment Gateway Provider (Stripe/PayPal for secure checkout and PCI-DSS compliance)
* Third-Party Shipping APIs (External fulfillment services)
* Identity/Consent Management Provider (GDPR & CCPA compliance tracking)
* Notification Services (Email/SMS for alerts and password resets)
* Currency Exchange Rate Provider (Dynamic rates for USD, EUR, and GBP)
* Monitoring and Observability Provider (APM and log aggregation SaaS)

## Relationships
* Customers interact with the Online Bookstore via HTTPS using REST/GraphQL APIs
* Administrators manage the platform via secure administrative interfaces over HTTPS
* Online Bookstore integrates with Payment Gateway Provider via HTTPS/TLS 1.3 for secure checkout
* Online Bookstore connects to Third-Party Shipping APIs via HTTPS for fulfillment tracking
* Online Bookstore synchronizes multi-currency rates with the Currency Exchange Rate Provider via REST over HTTPS

## Technology Stack
* AWS (Multi-region cloud infrastructure in us-east-1, eu-west-1, ap-southeast-1 for 99.95% availability)
* REST/GraphQL over HTTPS (Standardized protocols for all internal and external communication)
* TLS 1.3 (Enforced transport security for all data in transit)
* JSON (Uniform payload serialization format across all service boundaries)

## Rationale
The multi-region AWS architecture ensures low-latency performance (<2s on 3G) and high availability to meet global scalability demands. Offloading critical boundaries like payments, compliance, and telemetry to specialized external providers minimizes risk and maintains regulatory compliance.