## Overview
The AI Symptom Checker Service provides traceable, region-compliant symptom analysis and care urgency recommendations for patients in the EU and US. It decomposes into internal Python components deployed on GCP to meet strict healthcare regulations.

## Key Elements
* API Router & Validator (Python/FastAPI)
* Region-Aware Orchestrator (Python)
* Audit & Traceability Logger (Python / SQLAlchemy)
* LLM Integration Client (Python/HTTPX)
* AI Model Provider / LLM API (External System)
* Cloud SQL PostgreSQL (Database)

## Relationships
* API Router & Validator to Region-Aware Orchestrator: In-memory function call with Pydantic models
* Region-Aware Orchestrator to LLM Integration Client: Asynchronous method call
* LLM Integration Client to AI Model Provider / LLM API: HTTPS / REST with TLS 1.3
* Region-Aware Orchestrator to Audit & Traceability Logger: Local asynchronous event emission
* Audit & Traceability Logger to Cloud SQL PostgreSQL: SQLAlchemy / SQL over secure TCP

## Technology Stack
* Python / FastAPI: High-performance framework for rapid API routing and payload validation
* Pydantic: Strict data schema validation ensuring compliance with healthcare data formats
* HTTPX: Asynchronous HTTP client providing robust LLM API communication with circuit breakers
* SQLAlchemy: ORM for secure, structured writes to regional relational databases
* Structured Logging: Captures immutable audit trails for MDR and HIPAA compliance

## Rationale
This component architecture ensures EU MDR, GDPR, and HIPAA compliance by isolating regional data routing, enforcing strict payload minimization, and maintaining immutable audit logs for every symptom-checker interaction. Asynchronous processing and circuit breakers ensure high availability and resilience across distributed GCP regions.