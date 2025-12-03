<<<<<<< HEAD
# 🌟 Hyper-Personalized Customer Experience AI Agent  
### GroundTruth Tech Hackathon 2025 — Customer Experience & Conversational AI

---
=======
# H-002 Hyper-Personalized Customer Experience AI Agent  
**GroundTruth Tech Hackathon 2025 – Track: Customer Experience & Conversational AI**
>>>>>>> d78877f5365ddb01ecf42cfaf9ab233932558ff3

## Overview

This project implements a **Hyper-Personalized AI Customer Support Agent** capable of understanding:

- **User context** (location, needs, triggers)  
- **Customer history** (visits, purchases, loyalty tier)  
- **Store intelligence** (inventory, hours, nearby branches)  
- **Policy & offer documents** via RAG  
- **Implicit user intent** (“I’m cold” → recommend nearest warm beverage store)  

Unlike traditional chatbots that provide generic, template-like responses, this agent is designed to behave like a **real customer support executive**, but with instant, intelligent automation.

**Example Scenario:**  
User: *“I’m cold.”*  
AI: *“There’s a Starbucks 50m away from you. You also have a 10% off coupon for Hot Cocoa. Want me to guide you there?”*

This demonstrates personalization, contextual reasoning, and intelligent recommendation.

---

## Problem Statement

Retail customers expect instant, accurate answers to queries like:

- **“Is this store open?”**  
- **“Do you have this item in size 10?”**  
- **“Where is my order?”**  
- **“I’m cold…” (implicit need requiring reasoning)**  

Traditional chatbots fail because:

- They rely on static rule-based flows  
- They ignore context and user history  
- They cannot retrieve live metadata or policy docs  
- They give generic, repetitive responses  

This results in **poor customer experience and lost opportunities**.

---

## Solution — Our Hyper-Personalized CX AI Agent

The system combines four major intelligence layers:

###  **PII-Safe Input Processing**
Before any message reaches the AI model, we mask:

- Phone numbers  
- Email addresses  
- Customer IDs  
- Transaction numbers  

This ensures strict privacy compliance.  
Example:  
`"My number is 9876543210"` → `"My number is PHONE_[1]"`

---

### **Context Retrieval Engine**
The agent fetches dynamic, user-specific context:

- Purchase history, last visited stores  
- Customer loyalty tier  
- Active coupons & rewards  
- Nearest store within geofence  
- Inventory & store working hours  

This transforms the response from *generic* to *deeply personalized*.

---

###  **RAG (Retrieval-Augmented Generation)**
We retrieve relevant snippets from:

- Store policies  
- Offer documents  
- Operating procedures  
- Product metadata  
- FAQ PDFs  

Ensuring that the AI’s response is **fact-based** and aligned with company policies.

---

### **LLM Reasoning (Google Gemini)**
Gemini processes:

- Cleaned user input  
- Context data  
- RAG snippets  
- Interaction history  

to produce a **highly contextual, actionable** customer response.

---

## System Architecture

Below is the architecture diagram used in this project  
(Replace `architecture.png` with your actual image name):

![Architecture Diagram]("C:\Users\DELL\Downloads\Gemini_Generated_Image_pff4prpff4prpff4.png")

---

## Architecture Breakdown (Pipeline Flow)

```
User Message
      ↓
PII Masking Layer (removes phone, email, IDs)
      ↓
Context Fetching Layer
      ├─ User Profile (history, loyalty)
      ├─ Store Intelligence (hours, inventory)
      ├─ Location & Geofencing
      └─ Active Coupons
      ↓
RAG Retriever Layer
      ├─ Policy Documents
      ├─ Offer PDFs
      └─ Store Metadata
      ↓
Prompt Builder (constructs structured input)
      ↓
LLM Engine (Google Gemini)
      ↓
Post-processing (reinsert masked placeholders)
      ↓
Final Personalized Response → Sent to User
```

--- 

## Tech Stack

### **Backend**
- Python  
- Flask (REST API)  
- LangChain (pipeline orchestration)  
- Google Gemini (LLM engine)  

### **Data & Retrieval**
- Local document store for policies/offers  
- Keyword or embedding-based RAG retrieval  

### **Utilities**
- dotenv (config)  
- pydantic (request/response validation)  
- Custom PII masking functions  

---

## Features (MVP)

- Hyper-personalized context-aware responses  
- Location & geofence-based recommendations  
- Store-level inventory & hours lookup  
- Coupon + loyalty-based suggestions  
- PII privacy masking layer  
- RAG-based policy & document retrieval  
- Gemini-powered reasoning  
- Modular API routes for scalability  

---

## Project Structure (Final)

```
app.py
src/
  config/
    settings.py
  utils/
    pii.py
    loader.py
    geolocation.py
  rag/
    retriever.py
    document_store.py
  llm/
    client.py
    prompt_builder.py
  pipeline/
    orchestrator.py
  api/
    routes.py
    schemas.py
  ui/
    templates/
    static/
data/
  policies/
  offers/
tests/
README.md
requirements.txt
```

---

## How to Run the Project (Local)

```
pip install -r requirements.txt
python app.py
```
<<<<<<< HEAD



---

## Privacy Compliance Checklist

- ✔ No raw PII sent to LLM  
- ✔ Masking layer applied before processing  
- ✔ Logs anonymized  
- ✔ Temporary data auto-deleted  
- ✔ Local-only RAG (no external data leakage)  

---

## Current Status

This README is submitted as part of the GroundTruth Hackathon submission requirements.  
The full implementation is in progress and will be completed within the dedicated build window.

---

## Final Notes

Our approach ensures:

- Strong personalization  
- Accurate, context-rich responses  
- Privacy-first data handling  
- Expandable architecture  
- Real-world applicability  

This system demonstrates the future of **AI-driven customer experience**.

=======
>>>>>>> d78877f5365ddb01ecf42cfaf9ab233932558ff3
