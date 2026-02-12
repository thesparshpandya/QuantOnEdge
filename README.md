# QuantOnEdge: Privacy-First Financial AI

A local, multi-agent financial analysis system designed to run on edge devices.

## Features
- **Privacy-First:** Runs entirely offline using local LLMs (Llama 3).
- **RAG Architecture:** Ingests and analyzes Annual Reports (PDFs).
- **Edge Optimized:** Benchmarking 4-bit quantization for performance on consumer hardware.

## Setup
1. Clone the repo.
2. Create a virtual env: `python3 -m venv venv`
3. Install dependencies: `pip install -r requirements.txt`
4. Run ingestion: `python src/ingestion.py`