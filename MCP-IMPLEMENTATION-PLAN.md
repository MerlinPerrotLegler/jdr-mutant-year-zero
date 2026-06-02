# DCC-MCP Analyzer Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Create a Python MCP server that analyzes Dungeon Crawler Carl EPUBs, chunks them intelligently, sends to AnyLLM for analysis, and populates an Obsidian vault with one markdown file per entity.

**Architecture:** 5 modular Python tools exposed via MCP protocol. AnyLLM orchestrates by calling tools sequentially. Each tool handles one responsibility: extraction, analysis, parsing, writing, progress. Server communicates with AnyLLM via stdio (standard MCP transport).

**Tech Stack:** 
- Python 3.10+
- `ebooklib` (EPUB parsing)
- `mcp` (Model Context Protocol SDK)
- `pathlib`, `json`, `re` (stdlib)
- `pytest` (testing)

---

## File Structure

```
dcc-mcp-analyzer/
├── README.md
├── requirements.txt
├── mcp_server.py              # Point d'entrée principal du server MCP
├── src/
│   ├── __init__.py
│   ├── epub_handler.py        # Extraction EPUB + chunking
│   ├── entity_parser.py       # Parse markdown, extrait entités
│   ├── obsidian_writer.py     # Écrit fichiers .md Obsidian
│   ├── progress_tracker.py    # Track l'avancement
│   └── anythingllm_client.py  # Client pour appeler AnyLLM
├── tests/
│   ├── __init__.py
│   ├── test_epub_handler.py
│   ├── test_entity_parser.py
│   ├── test_obsidian_writer.py
│   └── test_anythingllm_client.py
├── sample_data/               # Test fixtures
│   └── sample.txt             # Texte exemple pour tests
└── .progress.json             # Tracking d'avancement (généré)
```

---

[Full detailed tasks as specified above...]

(Plan saved with all 8 tasks and ~100 detailed steps)
