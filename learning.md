# Applied AI Engineer — Practical Learning Path

## How We Will Learn

This roadmap is **build-first, production-oriented, and sequential**.

The goal is not to finish courses. The goal is to become capable of designing, building, debugging, evaluating, deploying, and explaining real AI systems.

### Learning rules

1. Follow the roadmap in order. Later abstractions should be learned only after understanding the underlying mechanics.
2. Build while learning. Every major concept gets implemented in code.
3. Prefer fundamentals over framework magic. For example, implement tool calling, RAG, and an agent loop manually before using LangChain/LangGraph.
4. For every concept, learn:
   - what it is
   - why it exists
   - how it works internally
   - when to use it
   - when not to use it
   - tradeoffs and failure modes
   - production best practices
5. Debug rather than blindly replacing code. Understand errors and API responses.
6. Keep notes on durable concepts, mental models, tradeoffs, and architecture—not every syntax detail.
7. Each project should become progressively more production-like: configuration, error handling, validation, testing, logging, evaluation, security, cost, latency, deployment, and documentation.

---

# Phase 1 — LLM Application Foundations

## 1. LLM API + Python Foundation

### Learn
- Python needed for AI engineering
- APIs, HTTP, JSON, SDKs
- API keys and environment variables
- requests/responses
- model selection
- basic error handling
- conversation state
- token usage

### Build — Project 0: CLI AI Assistant
Start with a terminal LLM application.

Progressively implement:
- basic LLM call
- `.env` configuration
- conversation history
- response inspection
- token usage tracking
- sliding-window history
- conversation summarization
- basic retries/error handling
- clean project structure
- tests

### Goal
Understand exactly what happens between your Python application and an LLM API.

---

## 2. LLM Fundamentals

### Learn
- tokens and tokenization
- context windows
- input vs output tokens
- temperature and sampling
- model capabilities
- reasoning models
- latency
- cost
- hallucinations
- prompt/context design
- system/developer/user instructions
- model limitations

### Build
Improve Project 0 and run controlled experiments.

### Goal
Be able to explain why an LLM behaves differently when model, prompt, context, or generation settings change.

---

## 3. Structured Outputs + Streaming

### Learn
- structured output
- JSON/schema-constrained generation
- validation
- parsing failures
- streaming
- partial responses
- UX implications
- structured data vs free-form text

### Build
Turn the CLI assistant into an application that can reliably return structured objects and stream responses.

### Goal
Move from “LLM gives me text” to “my application can reliably consume model output.”

---

# Phase 2 — Retrieval-Augmented Generation

## 4. Embeddings + Vector Search

### Learn
- embeddings
- semantic similarity
- cosine similarity
- vector databases
- indexing
- nearest-neighbor search
- metadata filtering
- chunking basics

### Build — Project 1: Document Search
Create a document ingestion and semantic-search system.

### Goal
Understand retrieval independently before adding generation.

---

## 5. RAG

### Learn
- ingestion pipeline
- document parsing
- chunking
- embedding
- indexing
- retrieval
- prompt construction
- answer generation
- citations/source attribution

### Build — Project 2: RAG Assistant
Build a question-answering application over a document collection.

Pipeline:

`Documents → Parse → Chunk → Embed → Index → Retrieve → Generate`

### Goal
Understand RAG as a system, not as a framework feature.

---

## 6. RAG Engineering + Evaluation

### Learn
- chunk-size tradeoffs
- overlap
- metadata
- top-k
- similarity thresholds
- reranking
- hybrid search
- retrieval failure modes
- groundedness
- answer quality
- retrieval metrics
- evaluation datasets
- regression testing

### Build
Turn Project 2 into a measurable RAG system.

Add:
- evaluation dataset
- retrieval evaluation
- answer evaluation
- failure analysis
- experiments
- regression tests

### Goal
Be able to answer: “How do you know your RAG system works?”

---

# Phase 3 — Tools and Agents

## 7. Tool / Function Calling

### Learn
- tool schemas
- model-generated tool calls
- argument validation
- application-side execution
- tool results
- multi-step tool calls
- authorization
- deterministic business logic

### Build — Project 3: Tool-Using Developer Assistant
Build a developer assistant that can use safe application tools.

First implement the tool-calling loop **manually**.

### Goal
Understand that the model requests a tool; your application executes it.

---

## 8. Agents

### Learn
- agent loop
- planning vs execution
- state
- observation
- tool selection
- stopping conditions
- retries
- failure handling
- agent boundaries
- autonomous behavior risks

### Build — Project 4: Agent / Developer Support Agent

Build an agent that can:
- reason about a task
- select tools
- execute them
- inspect results
- continue
- stop when the goal is complete

### Goal
Understand agents as an application architecture, not as a magical model capability.

---

## 9. LangChain + LangGraph

### Learn
Only now learn the frameworks.

Understand:
- what abstractions they provide
- how they map to the manual implementations
- chains
- retrievers
- tools
- agents
- state
- graphs
- middleware/integrations

### Build
Rebuild selected parts of Projects 2–4 using LangChain/LangGraph.

### Goal
Use frameworks because they reduce engineering work—not because they hide concepts you don't understand.

---

# Phase 4 — Production AI Backend

## 10. FastAPI + PostgreSQL + Redis + Queues

### Learn
- REST APIs
- request validation
- async processing
- PostgreSQL
- transactions
- indexes
- Redis
- caching
- background jobs
- queues
- workers
- rate limiting
- authentication basics

### Build — Project 5: Production AI Backend

Turn an AI application into a real backend with:
- FastAPI
- PostgreSQL
- Redis
- background workers/queues
- persistent conversations
- user/application state
- API authentication
- rate limiting

### Goal
Be able to build AI features as real backend services.

---

# Phase 5 — Production AI Engineering

## 11. Production AI

### Learn
- latency optimization
- cost optimization
- caching
- batching
- concurrency
- retries
- timeouts
- fallbacks
- model routing
- configuration management
- secrets management
- reliability
- scaling

### Build
Improve Project 5 under realistic constraints.

Measure:
- latency
- token usage
- cost
- throughput
- failure rate

### Goal
Build systems that work reliably outside a local demo.

---

## 12. Evaluation + Observability + Security

### Learn
### Evaluation
- offline evaluation
- online evaluation
- test sets
- LLM-as-judge
- human evaluation
- regression testing

### Observability
- logs
- traces
- metrics
- request IDs
- model/tool traces
- latency breakdowns
- token/cost tracking

### Security
- prompt injection
- data leakage
- tool abuse
- authorization
- secret management
- untrusted documents
- output validation

### Build — Project 6: Evaluated + Observable AI System

Add:
- evaluation pipeline
- dashboards/metrics
- tracing
- security tests
- failure monitoring

### Goal
Know not only how to build an AI system, but how to know when it is failing.

---

# Phase 6 — Deployment and Infrastructure

## 13. Docker + AWS

### Learn
- Docker
- images/containers
- networking
- environment configuration
- containerized services
- AWS fundamentals
- compute
- storage
- databases
- networking
- IAM
- deployment
- monitoring
- scaling

### Build
Deploy a production-style AI application.

### Goal
Be capable of taking an AI service from local development to cloud deployment.

---

# Phase 7 — Deep Learning Foundations

## 14. PyTorch + Deep Learning

### Learn
- tensors
- autograd
- datasets/dataloaders
- training loops
- loss functions
- optimizers
- neural networks
- backpropagation
- overfitting
- regularization
- GPU basics

### Build
Implement and train small neural networks yourself.

### Goal
Understand what happens underneath modern AI models.

---

## 15. Transformers

### Learn
- embeddings
- positional information
- attention
- self-attention
- queries/keys/values
- multi-head attention
- feed-forward layers
- residual connections
- normalization
- transformer blocks
- autoregressive generation

### Build
Implement a small Transformer/GPT-style model from scratch or from minimal components.

### Goal
Understand the architecture behind modern LLMs.

---

# Phase 8 — Model Adaptation and Inference

## 16. Fine-Tuning + LoRA / QLoRA

### Learn
- pretraining vs fine-tuning
- supervised fine-tuning
- datasets
- instruction tuning
- LoRA
- QLoRA
- adapters
- quantization basics
- when fine-tuning is appropriate
- fine-tuning vs RAG

### Build
Fine-tune a small open model for a specific task and evaluate it against the base model.

### Goal
Know when to use prompting, RAG, or fine-tuning.

---

## 17. Model Inference + vLLM + Quantization

### Learn
- model serving
- inference
- batching
- KV cache
- throughput
- latency
- GPU memory
- quantization
- model formats
- vLLM
- serving APIs

### Build — Project 7: Self-Hosted Model Service

Serve an open model locally or on cloud infrastructure.

Measure:
- tokens/sec
- latency
- concurrency
- memory usage
- cost

### Goal
Understand model inference as an engineering problem.

---

# Phase 9 — AI System Design

## 18. AI System Design

Learn to design systems such as:

- production RAG
- AI customer support
- agentic workflows
- document intelligence
- developer assistants
- recommendation/search systems
- multi-model systems
- high-scale inference systems

For every design, cover:

`Requirements → Architecture → Data Flow → Models → Retrieval → Tools → Storage → APIs → Scaling → Reliability → Security → Evaluation → Observability → Cost`

### Goal

Be able to defend architectural decisions in an interview and design real systems.

---

# Phase 10 — Portfolio + Interviews + Applications

## 19. Portfolio + Interviews + Applications

### Portfolio

Prioritize a small number of serious projects over many toy projects.

Each major project should include:

- README
- architecture diagram
- setup instructions
- API documentation
- tests
- evaluation results
- performance measurements
- security considerations
- tradeoffs
- failure cases
- deployment instructions

### Interviews

Prepare:

#### Coding
- data structures and algorithms
- Python
- backend fundamentals

#### AI
- LLM fundamentals
- RAG
- embeddings
- tool calling
- agents
- evaluation
- fine-tuning
- inference

#### System Design
- distributed systems
- databases
- caching
- queues
- scaling
- AI-specific architecture

#### Behavioral
Be able to explain:
- what you built
- why you chose the architecture
- what failed
- how you measured it
- what you changed
- what you would do differently

### Applications

Apply continuously once the portfolio has credible production-style projects. Do not wait until every topic in the roadmap is mastered.

---

# Project Progression

The practical progression is:

`Project 0 → CLI LLM Assistant`

`Project 1 → Document Semantic Search`

`Project 2 → Production RAG + Evaluation`

`Project 3 → Tool-Using Developer Assistant`

`Project 4 → Agent / Developer Support Agent`

`Project 5 → Production AI Backend`

`Project 6 → Evaluated + Observable + Secure AI System`

`Project 7 → Self-Hosted Model / Inference Service`

The projects should evolve rather than remain isolated demos.

---

# The Core Engineering Mindset

For every new AI feature, ask:

1. What problem am I solving?
2. Why does this component exist?
3. What happens underneath the abstraction?
4. What can go wrong?
5. What are the alternatives?
6. What are the latency implications?
7. What are the cost implications?
8. How do I test it?
9. How do I evaluate it?
10. How do I observe it in production?
11. How do I secure it?
12. How does it scale?

The objective is not:

> “I know LangChain.”

The objective is:

> “I can design, build, debug, evaluate, deploy, and explain an AI system—and I understand the abstractions I'm using.”

---

# Current Position

We are currently in:

**Phase 1 → Step 1: LLM API + Python Foundation**

Already covered:

- LLM API calls
- SDK vs API vs JSON
- response objects
- traversing API response structures
- conversation history
- message roles
- tokens
- token usage
- context windows
- sliding-window history
- conversation summarization
- summary + recent history
- basic Git/secrets hygiene while building the project

Next planned topic:

**Structured Outputs → then Streaming**

Do not skip ahead. Build the concepts in order.
