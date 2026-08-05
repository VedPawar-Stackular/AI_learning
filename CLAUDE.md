# AI Career Roadmap — Project Context

Full plan: [ai_career_roadmap.md](ai_career_roadmap.md). This file is the working-session summary.

## Who's working here

22yo, BTech CSE, ~6mo Junior SWE (AI/ML), Hyderabad, ₹6 LPA. Knows Python, FastAPI (not pro), Docker, some React/Java, RAG/LLM/LangChain basics.

Redoing Phase 1 on purpose — not first exposure. Goal: verify fundamentals, catch gaps, actually ship the 3 projects. Don't over-explain things already known; probe first.

## Current status

**Phase 1 — Foundation (mo 1-3, wk 1-12).** Starting at Week 1.

Update this line as weeks/checkpoints complete: `Currently: Week X — <topic>`.

## Phase 1 target (12 weeks)

3 public, deployed, evaluated projects:
1. LLM tool, structured output + tool calling (wk 1-3)
2. RAG system w/ citations, deployed (wk 4-6)
3. Tool-using agent w/ eval harness (wk 7-9)

Wk 10-12: cost/latency optimization + polish + writeups across all three.

Learning:building ratio ~40:60 this phase — lean toward building.

## Week-by-week (Phase 1)

| Wk | Learn | Build |
|---|---|---|
| 1 | System/user prompts, few-shot, hosted model API | CLI script: prompt → raw text |
| 2 | Forced JSON output, Pydantic validation, retry-on-invalid | Typed/validated JSON output |
| 3 | Tool/function calling schemas | Finish tool, README, public repo |
| 4 | Embeddings, chunking strategies | Chunk a real corpus |
| 5 | Vector DB, similarity + hybrid search | Index corpus, basic retrieval |
| 6 | Context assembly, citations | Full RAG + deploy (Render/Railway/Fly.io) — **Checkpoint 1** |
| 7 | Agent loops, ReAct, LangGraph | Minimal agent, 1 real tool |
| 8 | Multi-tool orchestration, memory/state | Agent w/ 2-3 tools, multi-step task |
| 9 | Evals for non-deterministic systems, RAGAS/LangSmith | Eval harness + guardrails |
| 10 | Token cost math, latency sources, caching | Instrument cost/latency tracking |
| 11 | Model routing, prompt caching, batching | Implement 1-2 optimizations, measure |
| 12 | — | Polish all 3, public writeups — **Checkpoint 1 major** |

### Checkpoint 1 (major, end of month 3) — pass criteria
- [ ] 3 projects public + deployed (not just repos)
- [ ] Each has an eval or measured before/after
- [ ] Can explain every architectural choice under questioning
- [ ] One honest written failure case per project

Short on 1-2 → spend an extra week here before Phase 2. This gate matters more than the calendar.

## After Phase 1

- **Phase 2** (mo 4-6): DSA (NeetCode150/Blind75) + system design basics + pick specialization (leaning Context Engineering / Agentic AI Engineering; LLMOps backup)
- **Phase 3** (mo 7-12): specialization depth, project #2, visibility, resume v1
- **Phase 4** (mo 13-18): market readiness, mock interviews
- **Phase 5** (mo 19-24+): apply in batches, track outcomes

Full detail for these phases lives in [ai_career_roadmap.md](ai_career_roadmap.md) — only Phase 1/2 are planned week-by-week on purpose.

## Resources (Phase 1)

- Anthropic Messages API docs, OpenAI API docs
- DeepLearning.AI short courses (free) — prompt engineering, RAG, agentic RAG
- Pydantic docs
- LangChain / LangGraph docs
- pgvector / Chroma / Qdrant
- RAGAS, LangSmith
- Render / Railway / Fly.io (deploy)

## Working rules for this repo

- Don't skip checkpoints — they're the anti-rabbit-hole mechanism.
- Every deliverable ships public (repo/demo/writeup), not left private.
- When user drifts off current week's scope, redirect back to it.
- User's global CLAUDE.md still applies (junior-dev teaching mode, explain WHY, flag "💡 Learn this" concepts, tests alongside code, no debug prints, direct communication).

## Architecture diagrams (Excalidraw)

Maintain a living system-design/architecture diagram per project via the Excalidraw MCP server (already configured — `mcp__excalidraw__*` tools). Update it incrementally, don't regenerate from scratch, every time new code or a structural change lands during that week's session.

- One diagram per project: wk1-3 tool, wk4-6 RAG system, wk7-9 agent (3 total across Phase 1)
- Update after each build session, not just at project end — diagram tracks current code, not the final design
- Use `create_element` / `batch_create_elements` for new components, `update_element` for changed ones, `delete_element` for removed ones. Never `clear_canvas` + redraw — that loses history
- Show real system boundaries: scripts/modules, API calls (incl. which provider/endpoint), data stores, external services, request/response flow — not abstract concepts
- When a snapshot is needed for a project writeup, use `export_scene` or `get_canvas_screenshot`

## Recurring small-detail gaps (watch + reinforce)

Track patterns here when Ved hits the same *kind* of bug more than once, so foundations actually solidify instead of getting patched over each time.

- **Env var loading order** (2026-08-05, Wk1 app.py): wrote `os.getenv()` in a file that never called `load_dotenv()` — had it in a separate `config.py` that was never imported. `.env` is inert until something loads it *before* the read happens; import order matters. Watch for repeats when adding new scripts/modules that need secrets.
- **SDK client vs. provider endpoint mismatch** (2026-08-05, Wk1 app.py): set `openai.api_key` to a Groq key, but never overrode `base_url` — SDK still points at OpenAI's servers by default. Setting a key ≠ pointing at the right server. Watch for repeats when swapping providers behind an OpenAI-compatible SDK (Groq, Together, OpenRouter, etc.).
- **Legacy vs. current API shape** (2026-08-05, Wk1 app.py): called `completions.create(prompt=...)` (legacy text-completion endpoint) against a chat model — needed `chat.completions.create(messages=[...])`. Watch for repeats confusing older tutorial code with current chat-based APIs.
