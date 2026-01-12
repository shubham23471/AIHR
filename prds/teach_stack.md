## 1. Technical Stack (The "Vibe-Code" Foundation)

* **Frontend:** Next.js 15 (App Router), TypeScript, Tailwind CSS, Shadcn/UI.
* **Backend:** FastAPI (Python 3.12), Pydantic V2 for data validation.
* **Asynchronous Processing:** Celery + Redis (for handling long-running Agent research).
* **Database:** PostgreSQL with `pgvector` (for semantic candidate search).
* **Agent Intelligence:** * **Local (Dev):** DeepSeek-R1-Distill-Qwen-14B-GGUF Q4_K_M via lm-studio.
* **Production:** DeepSeek V3.2 or Llama 4 Maverick (hosted on RunPod/vLLM).
* **Memory:** Mem0 (to store recruiter preferences and historical feedback).

---