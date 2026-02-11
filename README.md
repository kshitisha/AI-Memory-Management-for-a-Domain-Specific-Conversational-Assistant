# AI Memory Management for a Domain-Specific Conversational Assistant

## Overview
This project implements a simplified domain-specific conversational AI assistant designed for a student-facing SaaS platform. The focus is on **memory design and orchestration**, demonstrating how different memory types influence response quality across conversation turns and user sessions.

The system is implemented using **LangGraph** to explicitly model memory read and write flows, while surfacing memory state transparently for inspection and evaluation.

---

## Memory Types Implemented

### 1. Ephemeral (Turn-Level) Memory
- **Scope:** Single turn  
- **Contents:** Current user input  
- **Lifetime:** Discarded after response generation  
- **Purpose:** Ensures stateless processing within a turn  

---

### 2. Short-Term (Session) Memory
- **Scope:** One conversation session  

**Contents:**
- Current topic
- Detected confusion or difficulty signals  

**Lifecycle:**
- Written after each turn  
- Summarized when exceeding a threshold  
- Cleared at session end  

**Purpose:**  
Maintains conversational coherence while avoiding over-retention of transient signals.

---

### 3. Long-Term (User) Memory
- **Scope:** Persistent per user  

**Contents:**
- Explicit learning goals (e.g., *“prepare for biology exam”*)
- Stable preferences or recurring difficulties  

**Lifecycle:**
- Written only when relevance criteria are met  
- Updated or overwritten instead of being appended indefinitely  

**Purpose:**  
Enables personalization across sessions without memory leakage or over-personalization.

---

## Memory Lifecycle

| Stage     | Description |
|----------|-------------|
| Write    | Memory is written conditionally based on relevance |
| Retrieve | Relevant memory is injected into prompt construction |
| Update   | Existing memory may be summarized or overwritten |
| Forget   | Low-signal or outdated data is pruned |

---

## Memory Scoping Strategy
- **Turn-scoped:** Ephemeral memory  
- **Session-scoped:** Short-term memory  
- **User-scoped:** Long-term memory  

This scoping strategy prevents unintended cross-session leakage while preserving useful personalization.

---

## Memory Influence on Responses

Memory is used to:
- Contextualize explanations using stored learning goals  
- Adapt explanation depth based on prior confusion  
- Avoid repeating ineffective explanations  

---

## Memory Tuning Techniques
- **Summarization:** Compress session memory into high-level insights  
- **Relevance Filtering:** Persist only stable, high-signal information  
- **Overwrite Strategy:** Prevent unbounded growth in long-term memory  

---

## Trade-offs & Limitations
- Simplified persistence layer using file-based JSON  
- Single-user simulation  
- Mock LLM used for deterministic behavior  

These design choices favor **clarity of memory reasoning** over production-scale complexity.

---

## Qualitative Evaluation
A qualitative evaluation is provided in `evaluation/examples.md`, demonstrating how memory changes response relevance, coherence, and adaptability across turns and sessions.

---

## Memory Visibility
Memory state is surfaced through:
- Console logs during memory read and write nodes  
- Printed session and long-term memory after each turn  

This allows developers to clearly inspect what the assistant “remembers” at any point in time.
