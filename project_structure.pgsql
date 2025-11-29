rag-cp-agent/
│
├── backend/                     # FastAPI service (Gemini + Qdrant)
│   ├── app/
│   │   ├── main.py              # FastAPI entry
│   │   ├── rag.py               # RAG pipeline: embed->search->LLM
│   │   ├── gemini_client.py     # Gemini API wrapper
│   │   ├── qdrant_client.py     # Qdrant API wrapper
│   │   ├── schemas.py           # Pydantic models
│   │   ├── config.py            # env variables
│   │   └── utils.py
│   ├── requirements.txt
│   ├── start.sh                 # uvicorn start script (Render)
│   └── README.md
│
├── ingest/                      # Offline ingestion pipeline
│   ├── scrape.py                # scrape blog sites
│   ├── clean.py                 # html -> markdown
│   ├── chunk.py                 # chunking text
│   ├── embed.py                 # call gemini embeddings
│   ├── upsert.py                # push vectors to Qdrant
│   ├── config.py                # local .env loader
│   └── README.md
│
├── frontend/                    # Next.js UI (Vercel deploy)
│   ├── app/
│   ├── components/
│   ├── lib/
│   ├── public/
│   ├── package.json
│   ├── next.config.js
│   └── README.md
│
├── shared/                      # (Optional) shared logic for both sides
│   ├── prompts/
│   │   └── cp_prompt.txt        # RAG prompt template
│   ├── constants.py
│   ├── helpers.py
│   └── README.md
│
├── .gitignore
├── .env.example                 # env vars template (no secrets)
├── LICENSE
└── README.md                    # explain whole project
