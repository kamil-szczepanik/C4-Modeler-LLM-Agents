## Overview
The Configuration & Feature Store manages dynamic routing and feature flags for the Insurance Claims Modernization platform. It enables gradual claim type migration and rapid emergency rollbacks between the legacy mainframe and the new cloud platform.

## Key Elements
- Feature Flag Manager (Azure App Configuration Feature Management)
- Dynamic Routing Store (Azure App Configuration KV-sets)
- GitOps Deployment Pipeline (Bicep/Terraform with automated JSON schema validation)
- Break-Glass Workflow (Automated emergency PR mechanism for rapid rollbacks)
- API Gateway / BFF (.NET Core)

## Relationships
- API Gateway / BFF -> Feature Flag Manager: Evaluates feature flags [HTTPS / Azure SDK, polling/push via Event Grid]
- API Gateway / BFF -> Dynamic Routing Store: Retrieves endpoint routing maps [HTTPS / Azure SDK]
- Emergency Operators -> Break-Glass Workflow: Triggers instant claim-type fallback [HTTPS]

## Technology Stack
- Azure App Configuration: Centralized storage for dynamic feature flags and tenant-specific routing rules supporting instant rollbacks (R-06).
- Azure Managed Identities (Entra ID): Authenticates the API Gateway / BFF without static credentials, enforcing least privilege.
- GitOps Pipeline: Ensures all routing changes and feature toggles are version-controlled, validated via JSON schema, and automatically synced.
- Azure Monitor: Provides business impact telemetry and high-priority security alerting for emergency Break-Glass events.

## Rationale
This architecture balances the requirement for rapid, one-day claim rollbacks with strict security and operational guardrails tailored for a team with limited cloud experience. Utilizing GitOps and managed identities eliminates configuration drift and security risks while enabling seamless phased migration.