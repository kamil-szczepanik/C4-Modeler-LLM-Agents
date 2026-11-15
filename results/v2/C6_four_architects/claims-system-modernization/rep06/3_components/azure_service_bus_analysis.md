## Overview
[System: Insurance Claims Modernization platform, purpose: Gradually replaces a 30-year-old mainframe claims system with a modern cloud platform while maintaining dual-running and hybrid operations.]

## Key Elements
- Claim Event Topic (`claims-events`): Azure Service Bus Topic for domain events using AMQP.
- Mainframe Sync Queue (`mainframe-sync`): Azure Service Bus Queue utilizing AMQP and Sessions (FIFO) for mainframe order enforcement.
- Duplicate Detection Filter: Native Azure Service Bus property (`RequiresDuplicateDetection`) enforcing exactly-once semantics.
- Subscription Filter Rules (SQL Filters): Broker-level routing rules on topics to segment traffic by claim type.
- DLQ Processor / Forwarder: Auto-forwarding mechanism routing poisoned messages to a triage queue.
- Session State Management: Broker-native session state persistence on the sync queue.

## Relationships
- Claims Core Service -> Claim Event Topic: Publish domain events (`ClaimSubmitted`, `ClaimUpdated`) [AMQP]
- Claim Event Topic -> Subscription Filter Rules: Route events based on claim type [AMQP]
- Mainframe Integration Adapter -> Mainframe Sync Queue: Consume ordered messages and manage session state [AMQP]
- Mainframe Sync Queue -> DLQ Processor: Forward poisoned sync messages [AMQP]

## Technology Stack
- Azure Service Bus: Chosen for managed AMQP messaging, native duplicate detection, and robust partitioning.
- Azure Service Bus Sessions: Utilized for FIFO ordering to prevent race conditions during hybrid DB2 mainframe synchronization.
- Service Bus SQL Filters: Selected for broker-side message routing to support incremental claim-type migration without custom code.

## Rationale
This architecture ensures strict consistency (R-04) and supports gradual, claim-by-claim migration (R-03) while respecting the 3-year hybrid constraint and the team's limited cloud experience. Leveraging broker-native features minimizes custom application code complexity and protects the legacy mainframe interface.