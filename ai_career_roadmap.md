# AI-first career roadmap: junior engineer → high-paying product / FAANG-tier role

**Starting point:** 22, BTech CSE, ~6 months into a Junior SWE (AI/ML) role in Hyderabad, ₹6 LPA. Know Python, FastAPI (not at pro level), Docker, a little React and Java, and the basics of RAG/LLMs/LangChain.

**Weekly time budget used in this plan:** ~17-18 hrs/week (2 hrs on weekdays, 3-4 hrs on weekends).

**Horizon:** ~24 months, in 5 phases. Weeks 1-26 (months 1-6) are planned week by week, because that's the part worth planning precisely. Beyond month 6, the plan moves to monthly blocks on purpose — pretending to know exactly what week 43 looks like today would be false precision. You'll re-plan the far phases as you get there, using the checkpoints in this doc.

---

## How to read this document

- **Learning : building ratio** changes by phase — heavy on learning early, heavy on building later. It's called out per phase.
- **Self-eval checkpoints** are placed at natural phase boundaries. Don't skip them — they're the mechanism that stops "preparing" from becoming an identity instead of a phase.
- **Resources** are consolidated in one master list near the end so you're not hunting through the whole doc.
- Every project deliverable should end up **public** (a repo, a deployed demo, a short writeup) — private, unfinished work doesn't compound the way shipped work does.

---

## Phase overview

| Phase | Duration | Focus | Learning : building |
|---|---|---|---|
| 1. Foundation | Months 1-3 (wk 1-12) | LLM apps, RAG, agents, evals — 3 shipped projects | ~40:60 |
| 2. Consolidation | Months 4-6 (wk 13-26) | DSA patterns + system design basics + pick a specialization | ~50:50 |
| 3. Specialization | Months 7-12 | Go deep in one AI-engineering lane, second major project | ~20:80 |
| 4. Market readiness | Months 13-18 | Resume, networking, mock interviews, visibility | ~10:90 |
| 5. Application | Months 19-24+ | Apply, interview, negotiate | ~5:95 |

---

## Phase 1 — Foundation (months 1-3, weeks 1-12)

Goal by end of phase: **3 public, deployed, evaluated projects** — an LLM tool with structured output, a RAG system, and a tool-using agent with an eval harness.

### Week 1 — Prompting and API basics
- **Learn:** system/user prompts, few-shot prompting, calling a hosted model API from Python.
- **Build:** a CLI script that sends a prompt and returns raw text.
- **Resources:** Anthropic's Messages API docs, OpenAI API docs, DeepLearning.AI's short course on prompt engineering for developers (free).
- Split this week: ~60% learning / 40% building — new territory.

### Week 2 — Structured output and validation
- **Learn:** forcing a model to return JSON, validating it with Pydantic, retry-on-invalid-output patterns.
- **Build:** extend last week's tool to return typed, validated JSON instead of raw text.
- **Resources:** Pydantic docs, Anthropic/OpenAI structured-output docs.

### Week 3 — Tool/function calling, ship it
- **Learn:** function/tool-calling schemas, basic multi-tool patterns.
- **Build:** finish the tool — add tool calling, clean it up, write a README, push to a public GitHub repo.
- **Checkpoint (mini):** can you explain every design decision in this tool if someone questions it? If not, that's this week's real task, not more building.

### Week 4 — Embeddings and chunking
- **Learn:** what embeddings are, chunking strategies (fixed-size, recursive, semantic).
- **Build:** pick a real corpus you care about (your own notes, a public dataset, docs from a product you use) and chunk it.
- **Resources:** a free vector-database/RAG short course (DeepLearning.AI or Google Cloud's free options), pgvector docs.

### Week 5 — Vector store and retrieval
- **Learn:** vector DB basics, similarity search, hybrid search (keyword + dense).
- **Build:** index your chunked corpus, get basic retrieval working end to end.
- **Resources:** pgvector (fits your Postgres/backend world directly) or Chroma/Qdrant for faster prototyping.

### Week 6 — Full RAG, citations, deploy
- **Learn:** assembling retrieved context into a prompt, citing sources in the answer.
- **Build:** complete the RAG system with citations, deploy a demo (Render/Railway/Fly.io free tiers all work), publish it.
- **Checkpoint 1 (end of month 1.5):** does retrieval actually improve answers on your corpus? Find and write down 2-3 cases where it fails. Being able to say *why* it fails is more valuable than pretending it's perfect.

### Week 7 — Agent fundamentals
- **Learn:** agent loops (plan → act → observe), the ReAct pattern, LangGraph or a hand-rolled loop.
- **Build:** a minimal agent with one real tool (e.g., a calculator, a web search call, a database query).
- **Resources:** LangGraph docs, Anthropic's docs on building agents.

### Week 8 — Multi-tool agents and memory
- **Learn:** orchestrating multiple tools, designing short-term memory/state.
- **Build:** extend your agent to 2-3 real tools completing a small multi-step task.

### Week 9 — Evals and guardrails
- **Learn:** what makes evaluating a non-deterministic system different from a unit test; RAGAS/LangSmith concepts.
- **Build:** an eval harness that scores your agent against a fixed set of tasks, plus basic guardrails against bad actions.
- **Resources:** RAGAS docs, LangSmith docs.
- **Checkpoint (mini):** run the eval before and after one deliberate change to the agent. Can you point to a number that moved?

### Week 10 — Cost and latency profiling
- **Learn:** token cost math, where latency actually comes from, caching strategies.
- **Build:** instrument your RAG/agent projects with cost and latency tracking.

### Week 11 — Optimization
- **Learn:** model routing (cheap model for easy cases, expensive for hard ones), prompt caching, batching.
- **Build:** implement 1-2 optimizations on an existing project, measure before/after.

### Week 12 — Polish, document, self-eval
- **Build:** clean up all three projects, write a short public post for each explaining what you tried, what failed, and what the numbers showed.
- **✅ Checkpoint 1 — major (end of month 3):**
  - [ ] 3 projects, all public, all deployed (not just repos)
  - [ ] Each has an eval or a measured before/after
  - [ ] You can explain every architectural choice under questioning
  - [ ] You've written up at least one honest failure case per project

If you're short on 1-2 of these, spend an extra week here before moving on. This checkpoint matters more than staying on schedule.

---

## Phase 2 — Consolidation (months 4-6, weeks 13-26)

Goal: build the DSA + system-design spine that FAANG-tier interviews still test regardless of role, and pick your AI specialization based on real signal from Phase 1 (which project did you enjoy most?).

| Weeks | DSA focus | Other focus |
|---|---|---|
| 13-14 | Arrays, hashing, two pointers | — |
| 15-16 | Sliding window, stacks/queues | Intro to system design (scalability basics) |
| 17-18 | Trees, BFS/DFS | **Pick your specialization** (see below) |
| 19-20 | Graphs, backtracking | Start specialization project #2 |
| 21-22 | DP fundamentals | Continue specialization project #2 |
| 23-24 | Mixed review | System design deep dive: caching, sharding, queues, consistency |
| 25-26 | Buffer / catch-up | Finish specialization project #2 |

**Picking a specialization:** based on the futurense/2026 market breakdown, your natural first choice is **Context Engineering** (RAG, retrieval, memory design) or **Agentic AI Engineering** (tool-using agents) — both build directly on Phase 1 and your existing LangChain exposure. **LLMOps/AI Infrastructure** is a strong second option given your Docker background. Don't overthink this — you can pivot later; the point is to go deep in *something* rather than staying shallow in everything.

**Resources for this phase:** NeetCode 150 or Blind 75 (work pattern by pattern, not randomly), "Designing Data-Intensive Applications" by Martin Kleppmann (the standard system-design reference, still evergreen), a pattern-based system design course if you want structure (look for a current, well-reviewed one — these get updated often).

**✅ Checkpoint 2 — major (end of month 6):**
- [ ] 120-150 DSA problems solved with real pattern recognition (not memorized)
- [ ] Can explain time/space complexity of your own solutions without prompting
- [ ] Comfortable sketching basic system-design concepts (caching, load balancing, a simple RAG-at-scale design)
- [ ] Specialization chosen, project #2 underway or done
- [ ] ~2 years total runway used so far: 6 months down, on pace

---

## Phase 3 — Specialization (months 7-12)

This is monthly, not weekly — the work gets less script-able and more like real engineering judgment from here.

- **Month 7:** Go deep in your chosen lane. Context/Agentic → graph RAG, multimodal retrieval, MCP integration. LLMOps → prompt versioning tooling, monitoring/observability stacks.
- **Month 8:** Second major specialization project — aim for something with real usage, not just a demo. If your company will let you own a small AI feature at work, that's worth more than any side project.
- **Month 9:** DSA maintenance (3-4 hrs/week is enough now, don't let it fully lapse), first light mock-interview practice.
- **Month 10:** Build visibility — 2-3 technical write-ups, tidy GitHub/LinkedIn into something that tells a coherent story of what you build.
- **Month 11:** Advanced system design (real case studies: design a rate limiter, design a RAG system at scale, design a notification system).
- **Month 12:** Draft resume v1, run your first real mock interview.

**✅ Checkpoint 3 — major (end of month 12):**
- [ ] 2 specialization projects with real depth, one with real/production usage if at all possible
- [ ] DSA still sharp (medium problems in 25-30 min)
- [ ] Resume draft exists and has been reviewed by at least one other engineer
- [ ] You've done one full mock interview and gotten specific feedback
- [ ] Gap analysis: what's the weakest of the four (DSA / system design / AI depth / communication)? That's month 13's priority.

---

## Phase 4 — Market readiness (months 13-18)

- **Months 13-14:** Iterate the resume against real job descriptions. Start networking deliberately on LinkedIn — comment, post about your projects, connect with engineers at target companies.
- **Months 15-16:** Regular mock interviews (DSA + system design + behavioral). Consider one opportunistic off-campus application as a real-world data point, even if it feels early.
- **Months 17-18:** Final polish pass on projects and resume.

**✅ Checkpoint 4 — the big readiness gate (end of month 18):** Go through the full readiness checklist below. This is the one that decides whether phase 5 starts on schedule or gets another 2-3 months.

---

## Phase 5 — Application and interview (months 19-24+)

- Apply in batches, referrals first. Track every application, interview stage, and outcome in a spreadsheet — you need this to spot patterns (weak resume screen vs weak interview performance are different problems with different fixes).
- Expect a 6-14 week loop per company, and a typical 6-12 month cool-off after a rejection before reapplying — plan your target list accordingly instead of burning all your shots at once.
- Know the quirks going in: Amazon's loop is leadership-principle-heavy (prep behavioral stories properly), Google runs team-matching after the hiring committee stage. Every company has similar idiosyncrasies — look them up before the loop, not during.
- Cast a genuinely wide net across the tier you're targeting: Google/Meta/Amazon alongside Microsoft, Adobe, Salesforce, Walmart Global Tech, Uber, and top Indian product companies. Don't over-index on 3-4 dream names.

---

## The readiness checklist (use this instead of a feeling)

"Am I ready" is not a feeling to wait for — it's this list. You don't need 100% to start applying; ~70% is enough, because real interviews are themselves part of the training loop.

**Technical**
- [ ] Solve a fresh LeetCode medium in under 25-30 minutes without help
- [ ] Explain time/space complexity of your own code unprompted
- [ ] Whiteboard a basic system design (URL shortener, RAG-at-scale, rate limiter) in 30-45 minutes
- [ ] 2-3 deployed, evaluated AI projects you can defend in detail
- [ ] Comfortable saying "here's where this breaks and why," not just "it works"

**Process**
- [ ] Resume gets shortlisted at a reasonable rate (rough benchmark: 15-20%+ callback on well-targeted applications — if you're well below this, the resume is the bug, not your skills)
- [ ] Survived at least 2-3 real mock interviews without major stumbles
- [ ] Have a specific, named target list, not just "FAANG"

**When to actually start applying (vs. keep prepping forever):**
1. You've hit roughly 70% of the checklist above.
2. You've got enough tenure at your current job that switching doesn't read as job-hopping — in the Indian market, 18-24 months at your first job is generally a safe minimum before your first move.
3. Your current role has stopped teaching you anything new month-over-month — that's a much better trigger than a calendar date.
4. You notice you're adding "just one more" project or course before applying — that's usually avoidance, not genuine unreadiness. Apply anyway; you'll learn more from three real interviews than from another month of solo prep.

---

## Master resource list

**DSA**
- NeetCode 150 / Blind 75 — pattern-based practice, not random problems
- LeetCode — for volume once patterns are solid

**System design**
- *Designing Data-Intensive Applications* (Kleppmann) — the standard reference, still evergreen
- A current pattern-based system design course (check reviews — this category updates often)

**AI / LLM engineering**
- DeepLearning.AI short courses (free) — prompting, RAG, agentic RAG
- LangChain / LangGraph official docs
- Anthropic's docs on tool use, building agents, and MCP (Model Context Protocol)
- Pydantic docs (structured output validation)

**Vector stores & evals**
- pgvector (fits a Postgres/backend stack directly), Chroma, Qdrant
- RAGAS and LangSmith for evaluation frameworks

**Deployment**
- Render, Railway, or Fly.io free tiers for demo hosting
- GitHub Actions basics for a simple CI pipeline on your projects

---

## The one-paragraph version

Ship three real AI projects in the first 90 days using what you already know from backend work. Spend months 4-6 building the DSA and system-design spine that FAANG-tier interviews still require. Go deep in one AI specialization for the next six months while keeping the fundamentals warm. Spend six months making that work visible and interview-ready. Then apply — in batches, through referrals where possible, tracking everything — and treat early rejections as data, not verdicts. Total runway: about 18-24 months of consistent, unspectacular effort at roughly 17 hours a week. That's the whole plan.
