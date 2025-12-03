# H-002 Hyper-Personalized Customer Experience AI Agent  
**GroundTruth Tech Hackathon 2025 – Track: Customer Experience & Conversational AI**

## Overview
Hyper-Personalized Customer Support AI Agent that fuses contextual intelligence, user personalization, store metadata, and RAG-powered document retrieval to deliver concierge-grade assistance.  
> User: “I’m cold.” → Bot: “Starbucks 50m away, 10% Hot Cocoa coupon.”

## Problem Statement
Customers constantly ask contextual questions:
- “Is this store open?”
- “Do you have size 10?”
- “Where is my order?”

Traditional chatbots fall back to generic FAQ answers, eroding trust and losing conversion opportunities.

## Solution — Hyper-Personalized AI Agent
The agent synthesizes live and historical signals to craft relevant responses:
- User profile, purchase history
- Location awareness
- Store inventory and hours
- Coupons and loyalty tier
- RAG (policy docs)
- LLM reasoning (Gemini)

Each reply is context-rich, specific, and framed for the individual customer.

## Privacy First Design
We enforce zero-tolerance PII exposure:
- Mask phone numbers
- Mask emails
- Mask customer IDs
- Mask transaction numbers  
No raw user data ever reaches public LLM endpoints.

## System Architecture
```
User Message
↓
PII Masking Layer
↓
Context Fetcher (user, stores, coupons)
↓
RAG Retriever (policies, docs)
↓
Prompt Builder
↓
LLM (Gemini)
↓
Hyper-Personalized Response
↓
Frontend/UI
```

## Tech Stack
- Python, Flask
- LangChain for pipeline orchestration
- Google Gemini for LLM
- dotenv, pydantic
- Simple keyword-based RAG (expandable to FAISS)

## Features (MVP)
- Hyper-personalized responses
- Location awareness
- Store intelligence
- Active coupons lookup
- PII Masking
- RAG document retrieval
- Clean API endpoints
- Lightweight frontend UI

## Project Structure (Planned)
```
app.py
src/
config/
utils/
rag/
llm/
pipeline/
api/
ui/
data/
tests/
requirements.txt
README.md
```

## How to Run
```bash
pip install -r requirements.txt
python app.py
```
