# AI Career Roadmap — Project Context

Full plan: [ai_career_roadmap.md](ai_career_roadmap.md). This file is the working-session summary.

## Who's working here

22yo, BTech CSE, ~6mo Junior SWE (AI/ML), Hyderabad, ₹6 LPA. Knows Python, FastAPI (not pro), Docker, some React/Java, RAG/LLM/LangChain basics.

Redoing Phase 1 on purpose — not first exposure. Goal: verify fundamentals, catch gaps, actually ship the 3 projects. Don't over-explain things already known; probe first.

## Current status

**Phase 1 — Foundation (mo 1-3, wk 1-12).** Currently: Week 3 — tool/function calling schemas.

Update this line as weeks/checkpoints complete: `Currently: Week X — <topic>`.

### Completed weeks

- **Week 1** — [week01-prompting/](week01-prompting/) — CLI script hitting Groq via OpenAI-compatible SDK (`app.py`, `config.py`). Architecture diagram: [Exiladraw/week1-cli-tool.excalidraw](week01-prompting/Exiladraw/week1-cli-tool.excalidraw). Bugs hit + fixed: env-load order (`load_dotenv()` never called), SDK base_url pointing at OpenAI instead of Groq, legacy `completions.create` vs `chat.completions.create`, Windows console cp1252 vs UTF-8 output encoding — logged in "Recurring small-detail gaps" below.
- **Week 2** — [week02-structured-output/](week02-structured-output/) — `get_recipe()` in `app.py` forces JSON via Groq `response_format` (json_schema mode), validates with `Recipe.model_validate_json()` (`models.py`), retries up to 3x on `ValidationError` feeding the error back into the prompt. Tested with `pytest` + `unittest.mock.patch` on the OpenAI client (no real API calls in tests) — both happy-path and retry-exhaustion cases green. Bugs hit + fixed: retry loop had an unconditional `return None` inside the except block that fired on the *first* failure regardless of attempt count (killed the retry entirely); system prompt embedded `Recipe.model_json_schema()` as a plain string (missing `f`-prefix) so the model received literal unevaluated Python text instead of the real schema; mock test fed a raw dict into `model_validate_json` (expects a JSON string, not a dict) — all logged in "Recurring small-detail gaps" below. Key concept learned: `response_format` (constrained decoding, server-side, syntactic guarantee) and Pydantic validation (client-side, semantic guarantee) are complementary, not redundant.

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
- **Control flow inside except/loop blocks** (2026-08-07, Wk2 app.py): `return None` sat at the same indent as an `if attempt == max_attempts - 1` check inside a retry loop's except block — fired on the *first* failure instead of only the last, silently defeating the retry logic while looking correct at a glance. Watch for repeats when a loop has an early-exit statement near (but not inside) a conditional meant to gate it — check indentation maps to intent, not just that it runs without error.
- **Forgotten f-string prefix** (2026-08-07, Wk2 app.py): wrote `"...schema: {'name': 'Recipe', 'schema': Recipe.model_json_schema()}"` as a plain string — no `f` prefix, so `Recipe.model_json_schema()` was sent to the model as literal text, never evaluated. Silent — no error, just wrong data flowing downstream. Watch for repeats whenever a string literal contains `{expression}` — confirm the `f` is there before assuming interpolation happened.
