## Overview
The Adjuster Workspace is a Backend-for-Frontend container within a hybrid Azure and on-premises platform that modernizes regional insurance claims processing. It provides a high-performance web interface for claims adjusters while decoupling UI workflows from slow legacy systems.

## Key Elements
* Routing Controller (Express.js)
* Workflow Orchestrator (Node.js)
* Engine Client (gRPC/Protobuf)
* Event Publisher (Azure Event Hubs SDK)
* Integration Adapter (Apache Camel / Node SDK)

## Relationships
* Routing Controller -> Workflow Orchestrator: In-process function calls [HTTPS / OpenID Connect]
* Workflow Orchestrator -> Engine Client: Remote procedure calls [gRPC]
* Engine Client -> Claims Core Engine: Secure remote procedure calls [gRPC over TLS]
* Workflow Orchestrator -> Integration Adapter: Asynchronous in-process dispatch [Internal]
* Integration Adapter -> Integration Layer: Publish/subscribe messaging [AMQP / Azure Event Hubs]

## Technology Stack
* Node.js / Express.js: Chosen for lightweight routing and fast I/O handling
* Azure App Service: Provides managed hosting with integrated Azure Active Directory SSO
* gRPC / Protobuf: Enables high-performance, low-latency synchronous communication with the Claims Core Engine
* Azure Event Hubs: Facilitates scalable, asynchronous event streaming and decoupled messaging

## Rationale
This component architecture uses local caching and asynchronous integration adapters within the Workflow Orchestrator to guarantee sub-2-second UI load times despite slow backend dependencies. It securely isolates UI state management and meets hybrid deployment constraints without impacting legacy mainframe batch windows.