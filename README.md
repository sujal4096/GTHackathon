# Hyper-Personalized Customer Experience AI Agent
### GroundTruth Hackathon 2025 | Track: H-002 Customer Experience & Conversational AI

## Overview
This project solves the problem of "dumb" retail chatbots. Instead of generic answers, our **Hyper-Personalized AI Agent** combines real-time user context, location data, store inventory, and **RAG (Retrieval Augmented Generation)** to provide concierge-level support.

It features a **Privacy-First Architecture** that automatically masks sensitive PII (Personally Identifiable Information) before any data touches the LLM.

---

## Key Features

### 1. Contextual Awareness (Hyper-Personalization)
The agent doesn't just chat; it knows **who** you are and **where** you are.
*   **User Profile Integration:** Accesses purchase history & preferences (e.g., "Likes Hot Cocoa").
*   **Geo-Spatial Awareness:** Calculates distance to the nearest store (e.g., "Starbucks is 50m away").
*   **Dynamic Greetings:** Uses LLM to generate a unique, non-robotic welcome message based on active store promotions.

### 2. RAG with Vector Database (FAISS)
We went beyond simple keyword matching.
*   **Vector Search:** Uses **Google Generative AI Embeddings** to convert policy documents (PDFs) into vector space.
*   **FAISS Index:** Utilizes a local FAISS vector database for sub-second retrieval of non-structured data (e.g., Wifi passwords, Refund Policies).

### 3. Privacy & PII Masking
*   **Zero-Trust Layer:** A dedicated middleware scans all user input *before* it reaches the LLM.
*   **Regex Redaction:** Automatically replaces phone numbers and emails with `[PHONE_REDACTED]` and `[EMAIL_REDACTED]` to ensure compliance.

### 4. Conversational Memory
*   Maintains chat history for a natural, multi-turn conversation flow.

---

## Technical Architecture

**The Data Pipeline:**
```mermaid
graph TD;
    A[User Message] -->|Input| B(PII Guardrail);
    B -->|Masked Text| C{Context Engine};
    C -->|Fetch| D[User Profile JSON];
    C -->|Fetch| E[Store Metadata JSON];
    C -->|Vector Search| F[FAISS / RAG Retriever];
    F -->|Policy Docs| G[Prompt Builder];
    G -->|Structured Prompt| H[LLM - Google Gemini 1.5 Flash];
    H -->|Response| I[Frontend UI];
 Tech Stack
Backend: Python 3.10+, Flask
LLM: Google Gemini 1.5 Flash
Orchestration: LangChain
Vector DB: FAISS (Facebook AI Similarity Search)
Frontend: HTML5, CSS3 (Glassmorphism UI), Markdown rendering
Data: JSON (Mock User/Store Data), PDF (Unstructured Knowledge)
 Demo Scenarios (Proof of Capabilities)
Scenario 1: Hyper-Personalization
User: "I'm feeling cold."
Bot: "Hi Alex! Since you're just 50m away from Starbucks, come in for a Hot Cocoa! We have a 10% OFF coupon waiting for you."
(Logic: Matches "Cold" + User Preference "Cocoa" + Location "50m" + Store Promo)
Scenario 2: RAG (Document Retrieval)
User: "What is the guest wifi password?"
Bot: "The guest wifi password is BeanThereDoneThat2024."
(Logic: Retrieves answer dynamically from the internal Store Policy PDF)
Scenario 3: Privacy Protection
User: "Call me at 555-012-3456."
Logs:  Masked Input: Call me at [PHONE_REDACTED]
(Logic: The LLM never sees the real phone number)
 How to Run This Project
Prerequisites
Python 3.10 or higher
Google Gemini API Key
Installation Steps
Navigate to the Source Code:
code
Bash
cd "1. SourceCode"
Install Dependencies:
code
Bash
pip install -r requirements.txt
Configure Environment:
Create a .env file in the 1. SourceCode folder:
code
Env
GOOGLE_API_KEY=your_actual_api_key_here
Initialize Knowledge Base (RAG):
(Optional: The repo comes with pre-built embeddings in data/embeddings, but you can rebuild them if needed)
code
Bash
python seed.py
Run the Application:
code
Bash
python app.py
Access UI:
Open your browser to http://localhost:5000
 Project Structure
code
Text
1. SourceCode/
├── app.py                 # Main Flask Application
├── seed.py                # Script to ingest PDFs into FAISS
├── requirements.txt       # Python Dependencies
├── .env                   # API Keys (Not included in repo)
├── src/
│   ├── services/          # RAG & LLM Logic
│   ├── utils/             # PII Masking & Loaders
│   └── ...
├── data/
│   ├── users.json         # Mock User Profiles
│   ├── stores.json        # Mock Store Metadata
│   ├── knowledge_base/    # Raw PDF Documents
│   └── embeddings/        # FAISS Vector Database
└── templates/             # Frontend UI

2. Outputs/
└── terminal_logs.txt      # Execution logs proving successful run

3. Screenshots_and_Recording/
└── ...                    # Visual proof of UI and features
