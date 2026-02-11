AI Memory Management for a Domain-Specific Conversational Assistant
Overview
This project implements a simplified domain-specific conversational AI assistant designed for a student-facing SaaS platform. The focus is on memory design and orchestration, demonstrating how different memory types influence response quality across turns and sessions.
The system is implemented using LangGraph to explicitly model memory read/write flows and to surface memory state transparently.

Memory Types Implemented
1.Ephemeral (Turn-Level) Memory
Scope: Single turn
Contents: Current user input
Lifetime: Discarded after response generation
Purpose: Ensures stateless processing within a turn

2.Short-Term (Session) Memory
Scope: One conversation session
a. Contents:
Current topic
Detected confusion or difficulty signals
b. Lifecycle:
Written after each turn
Summarized when exceeding a threshold
Cleared at session end
c. Purpose: Maintain conversational coherence without over-retention

3.Long-Term (User) Memory
Scope: Persistent per user
a. Contents:
Explicit learning goals (e.g., “prepare for biology exam”)
Stable preferences or recurring difficulties
b.Lifecycle:
Written only when relevance criteria are met
Updated or overwritten, not appended indefinitely
c.Purpose: Personalization across sessions without memory leakage

Memory Lifecycle
Stage	Description
Write	Memory is written conditionally based on relevance
Retrieve	Relevant memory is injected into prompt construction
Update	Existing memory may be summarized or overwritten
Forget	Low-signal or outdated data is pruned

Memory Scoping Strategy
Turn-scoped: Ephemeral memory
Session-scoped: Short-term memory
User-scoped: Long-term memory
This prevents unintended cross-session leakage while preserving useful personalization.

Memory Influence on Responses

Memory is used to:
Contextualize explanations using stored goals
Adapt explanation depth based on prior confusion
Avoid repeating ineffective explanations

Memory Tuning Techniques
Summarization: Compress session memory into high-level insights
Relevance Filtering: Persist only stable, high-signal information
Overwrite Strategy: Prevent unbounded growth in long-term memory

Trade-offs & Limitations
Simplified persistence layer (file-based JSON)
Single-user simulation
Mock LLM used for deterministic behavior
These choices favor clarity of memory reasoning over production scale.

Qualitative Evaluation
A qualitative evaluation is provided in evaluation/examples.md, demonstrating how memory changes response relevance, coherence, and adaptability across turns and sessions.

Memory Visibility
Memory state is surfaced via:
Console logs during memory read/write nodes
Printed session and long-term memory after each turn
This allows developers to inspect what the assistant “remembers” at any point in time.
