# Design: MCP Server Dungeon Crawler Carl Analyzer

**Date:** 2026-05-29  
**Project:** Automated analysis of Dungeon Crawler Carl novels with AnyLLM  
**Status:** Design Approved ✓

---

## Overview

A **Model Context Protocol (MCP) server** that orchestrates the analysis of 4 Dungeon Crawler Carl EPUB novels using AnyLLM. The server exposes tools that AnyLLM uses to:
- Extract and chunk EPUB content
- Analyze each chunk according to the reverse-engineering prompt
- Parse results and create individual markdown files
- Populate an Obsidian vault with structured game-system documentation

**Key principle:** AnyLLM is the orchestrator. The user asks AnyLLM to "analyze all tomes," and AnyLLM uses the MCP tools to coordinate the entire workflow.

---

## Architecture

### Components

**1. MCP Server (Python)**
- Runs locally, registered with AnyLLM via JSON config
- Exposes 5 tools that AnyLLM calls
- Manages file I/O, EPUB extraction, markdown parsing, Obsidian vault structure
- No internal LLM calls; all analysis delegated to AnyLLM

**2. AnyLLM Integration**
- Detects the MCP server via `anythingllm_mcp_servers.json`
- Calls MCP tools sequentially
- Receives markdown with embedded entity markers
- Continues iterating through chunks until complete

**3. Obsidian Vault**
- Target: `/Users/merlinperrot/Documents/JDR/Dungeon Crawler/obsidian/JDR - Cousin/`
- Structure created automatically with 5 main folders:
  - `00-Sources/` (original tomes)
  - `01-Observations/` (raw analysis notes per entity)
  - `02-Systeme/` (organized game mechanics)
  - `03-Reverse-Engineering/` (derived formulas and patterns)
  - `04-Patterns/` (cross-cutting themes)

---

## Data Flow

```
┌─────────────────────────────────────────┐
│ User → AnyLLM                           │
│ "Analyze all Dungeon Crawler Carl tomes"│
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ MCP Tool: extract_and_chunk_tomes()     │
│ - Read 4 EPUBs                          │
│ - Extract raw text                      │
│ - Chunk into ~10-15k char blocks        │
│ - Overlap = 2k chars (context bridge)   │
│ - Return: [{chunk, tome, position},...] │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ For each chunk:                         │
│                                         │
│ ┌───────────────────────────────────┐   │
│ │ MCP Tool: analyze_chunk()         │   │
│ │ Input: chunk + reverse-eng prompt │   │
│ │ → AnyLLM sends to configured LLM  │   │
│ │ ← Returns markdown with entities  │   │
│ │   <!-- ENTITY: Type/Name -->      │   │
│ └───────────────────────────────────┘   │
│                 │                       │
│                 ▼                       │
│ ┌───────────────────────────────────┐   │
│ │ MCP Tool: parse_and_write_entities()  │
│ │ - Parse markdown sections         │   │
│ │ - Extract each entity             │   │
│ │ - Create individual .md files     │   │
│ │ - Auto-tag with Obsidian tags    │   │
│ │ - Handle cross-references         │   │
│ └───────────────────────────────────┘   │
│                 │                       │
│ (loop to next chunk)                    │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ MCP Tool: create_obsidian_structure()    │
│ - Ensure all 5 main folders exist      │
│ - Create index/README files             │
│ - Generate summary of findings          │
└──────────────────┬──────────────────────┘
                   │
                   ▼
┌─────────────────────────────────────────┐
│ ✓ Obsidian Vault Populated               │
│ - 1 file per entity (Character, Monster,│
│   Item, Skill, Spell, Effect, etc.)    │
│ - Organized in 01-Observations/,        │
│   02-Systeme/, etc.                     │
│ - Tags applied: #character, #monster... │
│ - Cross-references: [[Carl]], etc.      │
└─────────────────────────────────────────┘
```

---

## Tools Specification

### Tool 1: `extract_and_chunk_tomes`

**Input:**
- None (uses env vars for paths)

**Output:**
```json
{
  "chunks": [
    {
      "id": "T1_chunk_001",
      "tome": 1,
      "start_char": 0,
      "end_char": 15000,
      "text": "...",
      "overlap_with_next": true
    },
    ...
  ],
  "total_chunks": 847,
  "tomes_processed": [1, 2, 3, 4]
}
```

**Logic:**
- Extracts text from EPUB files (using `ebooklib` or `pypub`)
- Splits into ~15k char chunks
- 2k char overlap between consecutive chunks
- Returns chunks in order

---

### Tool 2: `analyze_chunk`

**Input:**
```json
{
  "chunk_id": "T1_chunk_001",
  "text": "...",
  "prompt_path": "/path/to/prompt.md"
}
```

**Output:**
```markdown
# Analysis Results

<!-- ENTITY: Personnages/Carl -->
## Carl
### Type
Character
### Description
...
### Informations certaines
...
### Tags
#character #dcc

<!-- ENTITY: Objets/Glorious Shit Ton -->
## Glorious Shit Ton
...
```

**Logic:**
- Loads the reverse-engineering prompt from file
- Combines prompt + chunk text
- **Calls AnyLLM's configured LLM** (user's active model)
- Parses markdown response
- Returns raw markdown with entity markers

---

### Tool 3: `parse_and_write_entities`

**Input:**
```json
{
  "markdown": "<!-- ENTITY: ... --> ... ",
  "chunk_id": "T1_chunk_001"
}
```

**Output:**
```json
{
  "files_created": [
    "01-Observations/Personnages/Carl.md",
    "01-Observations/Objets/Glorious_Shit_Ton.md"
  ],
  "entities_extracted": 5,
  "duplicates_merged": 2
}
```

**Logic:**
- Splits markdown on `<!-- ENTITY: Type/Name -->`
- For each entity:
  - Determines folder (01-Observations, 02-Systeme, etc.) based on type
  - Creates/updates markdown file: `<folder>/<type>/<name>.md`
  - Appends chunk metadata (source tome, position)
  - Adds Obsidian tags from content
  - Creates `[[links]]` for cross-references
- Handles duplicates: merges info if entity seen before

---

### Tool 4: `create_obsidian_structure`

**Input:**
- None (uses env vars)

**Output:**
```json
{
  "folders_created": 5,
  "index_files_created": 5,
  "structure": {
    "00-Sources": "original EPUBs (already present)",
    "01-Observations": "raw observations per entity type",
    "02-Systeme": "organized game mechanics",
    "03-Reverse-Engineering": "derived formulas",
    "04-Patterns": "cross-cutting themes"
  }
}
```

**Logic:**
- Creates directory structure if missing
- Generates `README.md` in each main folder explaining its purpose
- Creates `INDEX.md` with summary of analysis
- Ensures `.obsidian/` config is present

---

### Tool 5: `get_progress`

**Input:**
- None

**Output:**
```json
{
  "chunks_processed": 342,
  "total_chunks": 847,
  "percent_complete": 40,
  "entities_found": 156,
  "files_written": 156,
  "tomes": [
    {"tome": 1, "chunks": 200, "processed": 150},
    {"tome": 2, "chunks": 180, "processed": 150},
    {"tome": 3, "chunks": 267, "processed": 42},
    {"tome": 4, "chunks": 200, "processed": 0}
  ]
}
```

**Logic:**
- Reads from a progress file (updated by `parse_and_write_entities`)
- Returns percentage complete, entities found, etc.
- AnyLLM can call this periodically to show progress

---

## Configuration

### File Location
```
~/Library/Application Support/anythingllm-desktop/storage/plugins/anythingllm_mcp_servers.json
```

### Configuration Entry
```json
{
  "mcpServers": {
    "dcc-analyzer": {
      "command": "python /path/to/mcp_server.py",
      "env": {
        "TOMES_PATH": "/Users/merlinperrot/Documents/JDR/Dungeon Crawler/obsidian/JDR - Cousin/00-Sources",
        "VAULT_PATH": "/Users/merlinperrot/Documents/JDR/Dungeon Crawler/obsidian/JDR - Cousin",
        "PROMPT_PATH": "/Users/merlinperrot/Documents/JDR/Dungeon Crawler/obsidian/prompt.md",
        "CHUNK_SIZE": "15000",
        "CHUNK_OVERLAP": "2000"
      }
    }
  }
}
```

---

## Execution Flow (How to Use)

1. **Start AnyLLM** — App runs normally
2. **MCP auto-detects** — AnyLLM detects the server from config
3. **User message to AnyLLM:**
   ```
   "Analyze all four Dungeon Crawler Carl tomes according to the 
   reverse-engineering prompt. Create individual markdown files 
   for each entity (character, monster, item, etc.) in the 
   Obsidian vault."
   ```
4. **AnyLLM orchestrates:**
   - Calls `extract_and_chunk_tomes` → gets all chunks
   - Loops through each chunk:
     - Calls `analyze_chunk` → gets analysis
     - Calls `parse_and_write_entities` → writes files
     - Optionally calls `get_progress` → shows status
   - Calls `create_obsidian_structure` → finalizes vault
5. **User reviews results** in Obsidian

---

## Error Handling & Edge Cases

### Large Tomes
- **Problem:** Tomes may be very large (5-10MB text)
- **Solution:** Chunking with overlap ensures no context is lost between chunks

### Duplicate Entities
- **Problem:** Same character/monster may be mentioned in multiple chunks
- **Solution:** `parse_and_write_entities` checks if file exists, appends new info with `## Sources` section

### Missing Files/Permissions
- **Problem:** Vault path doesn't exist or is read-only
- **Solution:** Tool creates parent directories and catches permission errors gracefully

### LLM Failures
- **Problem:** `analyze_chunk` fails if AnyLLM's LLM times out
- **Solution:** AnyLLM handles retries; MCP just returns error, user can resume

---

## Testing Strategy

1. **Unit tests** for chunk extraction (verify EPUB parsing)
2. **Integration test** with a single chunk (verify analyze → parse → write flow)
3. **End-to-end** with all 4 tomes (verify full workflow and Obsidian structure)
4. **Spot-check** Obsidian vault for:
   - Files created in correct folders
   - Tags applied correctly
   - Cross-references (backlinks) work
   - Duplicate handling works

---

## Deployment

1. Create MCP project directory
2. Implement tools in Python
3. Register in `anythingllm_mcp_servers.json`
4. Test with AnyLLM
5. User runs analysis via chat

---

## Success Criteria

- ✓ All 4 tomes successfully chunked and analyzed
- ✓ 1 markdown file per unique entity (character, monster, item, etc.)
- ✓ Files organized in Obsidian vault structure (01-Observations, 02-Systeme, etc.)
- ✓ Obsidian tags applied (`#character`, `#monster`, `#dcc`, etc.)
- ✓ Cross-references (internal links) work in Obsidian
- ✓ Analysis preserves the 3-tier structure (Informations certaines / Déductions / Hypothèses)
- ✓ Progress trackable via `get_progress` tool

---

## Risks & Mitigations

| Risk | Mitigation |
|------|-----------|
| EPUB parsing fails | Use robust library, test with sample EPUB |
| LLM context overflow | Careful chunking with overlap; monitor token count |
| Obsidian vault gets too large | Implement archival strategy in future (move old tomes to subfolder) |
| Duplicate handling loses data | Test merge logic thoroughly; keep version history in comments |
| MCP server crashes mid-analysis | Implement progress file; allow resume from last chunk |

---

## Future Enhancements

- Support for Tome 5+ (just add to TOMES_PATH)
- Bulk export of specific entities (all characters, all bosses)
- Automated conflict detection when entities overlap
- Integration with other DCC fan resources
- Citation system (link to specific chapter/page)

