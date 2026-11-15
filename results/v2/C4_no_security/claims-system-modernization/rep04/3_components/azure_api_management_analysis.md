## Overview
[Gradually replaces the 30-year-old mainframe claims system of a regional insurer with a modern platform while the legacy system keeps processing claims.]

## Key Elements
* Azure API Management (Standard v2 tier)
* Token Validator Component
* Dynamic Routing Policy Engine
* Transformation & Header Injection Component
* Active Directory / Identity Provider
* Claims Core Engine (Java Spring Boot)
* Integration Mediator (Azure Logic Apps / Function App)
* Legacy Mainframe (COBOL/DB2)
* Azure App Configuration
* Application Insights & Azure Monitor

## Relationships
* End Customers & Brokers -> Azure API Management: Submit claims and interact via HTTPS (REST/JSON)
* Claims Adjusters -> Azure API Management: Manage claims via HTTPS (REST/JSON)
* Azure API Management -> Active Directory / Identity Provider: Validates OAuth2/OIDC tokens via HTTPS
* Azure API Management -> Claims Core Engine: Routes API requests via HTTPS (gRPC)
* Azure API Management -> Integration Mediator: Routes legacy traffic via HTTPS
* Azure API Management -> Azure App Configuration: Fetches Named Values for routing rules via HTTPS

## Technology Stack
* Azure API Management (Standard v2 tier): Balances predictable performance with managed infrastructure for a cloud-novice team
* APIM Policy Fragments & Named Values: Enables dynamic path-based routing and rapid 1-day rollbacks (R-06) without code deployments
* Azure App Configuration: Decouples routing switches from code for secure configuration management
* Azure Bicep: Provides Infrastructure-as-Code to prevent manual configuration drift
* Application Insights & Azure Monitor: Tracks end-to-end latency, error rates, and isolates routing overhead from mainframe responses

## Rationale
[This architecture uses Azure API Management as a unified entry point to securely route traffic, enforce Active Directory SSO, and execute dynamic path-based routing for gradual claim type migration. It ensures business continuity and sub-2-second adjuster screen loads while minimizing operational complexity for a cloud-novice team.]