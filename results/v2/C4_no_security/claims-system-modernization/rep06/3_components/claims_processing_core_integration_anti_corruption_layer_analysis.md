## Overview
The Insurance Claims Modernization system gradually replaces a 30-year-old COBOL/DB2 mainframe claims system with a modern hybrid platform on Azure. It enables online claims submission and adjuster workflows while ensuring continuous legacy coexistence and zero data loss.

## Key Elements
* Claim Routing Component: Spring Cloud Gateway/Router evaluating claim types against a dynamic configuration store for routing and 1-day rollbacks.
* Legacy Mainframe Adapter: Spring Integration service translating JSON domain models into COBOL copybook structures via IBM MQ or CICS sockets.
* New Domain Core: Spring Boot domain service processing migrated claim types natively.
* Event Publisher Component: Spring Cloud Stream service emitting domain events.
* Azure SQL Database: Transactional data store implementing the transactional outbox pattern.
* Azure Service Bus: Asynchronous message broker using AMQP.

## Relationships
* Claim Routing Component -> Legacy Mainframe Adapter: Routes unmigrated claims [In-process / Java Method Call]
* Claim Routing Component -> New Domain Core: Routes migrated claims [In-process / Java Method Call]
* Legacy Mainframe Adapter -> COBOL/DB2 Mainframe: Connects via synchronous TCP/IP [IBM MQ / CICS over Site-to-Site VPN / Azure ExpressRoute]
* New Domain Core -> Azure SQL Database: Reads and writes transactional state [JDBC / TLS]
* New Domain Core -> Event Publisher Component: Triggers events [In-process / Spring Application Events]
* Event Publisher Component -> Azure Service Bus: Publishes messages [AMQP]

## Technology Stack
* Java / Spring Boot: Core framework chosen for team expertise and robust enterprise ecosystem.
* Spring Cloud Gateway & Spring Integration: Used for dynamic claim routing and legacy protocol translation.
* Azure Container Apps & Azure SQL Database: Cloud runtime and data persistence providing native resilience for a team with low cloud experience.
* Azure Service Bus & OpenTelemetry: Messaging and distributed tracing ensuring R-04 consistency and hybrid observability.

## Rationale
This hybrid architecture isolates the fragile mainframe behind an Anti-Corruption Layer, enabling gradual claim migration and rapid rollbacks. It balances strict consistency and performance constraints while mitigating the team's low cloud experience with familiar Java technologies.