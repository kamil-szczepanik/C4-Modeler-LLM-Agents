## Overview
The Adjuster Web Application modernizes claim handling for internal users within a hybrid cloud architecture. It provides a sub-2-second responsive interface while integrating with a legacy mainframe system.

## Key Elements
- Claims Adjusters (Person)
- Adjuster UI (SPA/React Component)
- Claim Handling API (ASP.NET Core Component)
- Claim Context & Routing Component (.NET Component)
- Mainframe Abstraction Layer (.NET Component)
- Corporate Active Directory / Entra ID (External System)
- Claims Core API Service (Container)

## Relationships
- Claims Adjusters -> Adjuster UI: Manage claims [HTTPS/REST]
- Adjuster UI -> Claim Handling API: Invoke workflows [HTTPS/REST]
- Claim Handling API -> Claim Context & Routing Component: Evaluate routing [In-Memory]
- Claim Context & Routing Component -> Mainframe Abstraction Layer: Fetch fallback data [In-Memory]
- Claim Handling API -> Corporate Active Directory / Entra ID: Authenticate users [OIDC/OAuth 2.0]

## Technology Stack
- SPA/React: Provides responsive adjuster screens with optimistic updates
- ASP.NET Core: Powers the modular monolith backend API
- Azure Container Apps: Simplifies cloud deployment for a team with low cloud experience
- Azure App Configuration: Implements feature flags for rapid 1-day claim type rollbacks

## Rationale
The CQRS and caching patterns insulate user screens from slow legacy mainframe responses to meet the sub-2-second load requirement. Feature flags and decoupled routing allow individual claim types to be safely rolled back to the mainframe within one day.