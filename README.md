# 🧠 When Should AI Speak?
### A Controlled Agentic AI Decision System

## Overview

This project implements a **controlled agentic AI system** that decides **whether an AI should act at all**, before generating any response.

Instead of assuming the AI must always answer, this system introduces an **agentic decision layer** that evaluates:
- user intent clarity
- retrieval-based confidence
- attention / interruption cost

Based on these signals, the agent chooses one of four actions:
- RESPOND
- ASK_CLARIFY
- DEFER
- SILENT

Text generation is allowed **only after** the agent decides that responding is appropriate.

---
## Why This Project

Most AI systems today generate responses by default and attempt to fix mistakes after generation.

This project flips that approach:

> **Decision first. Generation last.**

The AI behaves as an agent that reasons about *whether it should act*, not just *what it should say*.

---
## Agentic Design

This system follows a single-agent control loop:
Observe → Evaluate → Decide → Act

### Observe
- User query
- Lightweight context (e.g., user busy state)
- Available knowledge base

### Evaluate
The agent computes:
- **Clarity** – how clear the user’s intent is
- **Confidence** – semantic similarity against trusted knowledge
- **Attention Cost** – whether interrupting the user is worthwhile

### Decide
The agent selects one action:
- respond
- ask for clarification
- defer to a human
- stay silent

Each decision includes an explicit reason.

### Act
- RESPOND → invoke LLM
- ASK_CLARIFY → request clarification
- DEFER → escalate to human
- SILENT → no output

---
## Key Behaviors

- Silence is a valid action
- Human-in-the-loop by design
- Retrieval-grounded confidence
- Explainable decisions

---
## Technologies & Concepts

- Python
- Sentence Transformers (embeddings)
- Retrieval-Augmented Decision Making (RAG)
- Rule-based decision engine
- Controlled LLM invocation
- Agentic control loop
- Human-in-the-loop escalation

---
## What This Project Is Not

- Not a generic chatbot
- Not an agent framework demo
- Not autonomous or self-directed

This project focuses on **AI behavior control**, not model performance.

---
## Core Insight

> An AI system should not be judged by how well it answers,  
> but by when it chooses not to answer.

## How to Run

1. Clone the repository
   ```bash
   git clone https://github.com/divyamshah-aiqa/when-should-ai-speak.git
   cd when-should-ai-speak

Install dependencies
pip install -r requirements.txt

Run the agent
python run_agent.py

