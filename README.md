# OncoLens 🔬
### AI-Powered Cancer Research Intelligence

OncoLens is an AI-powered research assistant designed to help researchers explore cancer-related scientific literature more efficiently. By combining Retrieval-Augmented Generation (RAG), semantic search, and evidence-grounded summarization, OncoLens helps users discover relevant research papers, extract key findings, and understand complex scientific studies without manually reading every paper in full.

The platform is designed to leverage a curated knowledge base of **300+ scientific research papers, studies, and articles** covering various aspects of cancer research, including molecular biology, cancer mechanisms, treatment approaches, and clinical studies.

## Key Features

- **Semantic Research Search:** Discover relevant cancer research papers based on research questions and scientific context.
- **AI-Powered Paper Summarization:** Extract key findings, methodologies, conclusions, and study limitations.
- **Evidence-Grounded Q&A:** Ask questions about research papers and receive answers supported by source references.
- **Scientific Literature Analysis:** Explore findings across multiple studies and identify areas of agreement or disagreement.
- **Research Metadata Filtering:** Narrow results by publication year, cancer type, and other available metadata.

## Project Goals

- Reduce the time required to discover and understand relevant scientific literature.
- Improve access to evidence within lengthy research papers.
- Build a specialized knowledge base containing 300+ scientific papers, studies, and articles on cancer research.
- Support more transparent, source-grounded exploration of scientific evidence.
- Help researchers navigate scientific findings while preserving the context and limitations of each study.

## Technology Stack

Python · RAG · Large Language Models (LLMs) · Embeddings · Vector Search · FastAPI

*The technology stack and features will evolve as development progresses.*

## Disclaimer

OncoLens is a research-support tool, not a medical decision-making system. Its outputs require verification against the original scientific literature and should not replace expert scientific or clinical judgment.


# Setup project to work

1. **install uv**
```bash
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **environment setup**
```bash
uv sync
```

3. **activate environment**
```bash
.venv\Scripts\activate
```

3. **Run main.py**
```bash
uvicorn src.main:app --reload --post 5000 --host 0.0.0.0
```

# Endpoint :

**Base Endpoint**
> *swagger interface:* [http://127.0.0.1:5000/docs](http://127.0.0.1:5000/docs)

> *Base Information Endpoint* [http://127.0.0.1:5000/api/v0.1.0/app-info](http://127.0.0.1:5000/api/v0.1.0/app-info)
