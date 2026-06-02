# MYZ MCP Analyzer — Mutant: Année Zéro → Obsidian

Serveur MCP Python qui extrait les livres de règles **Mutant: Année Zéro** (PDF) et les structure en vault Obsidian pour Maître du Jeu.

## Prérequis

```bash
pip install -r requirements.txt
# Pour l'OCR (PDFs scannés seulement) :
# apt install tesseract-ocr tesseract-ocr-fra
```

## Configuration

Variables d'environnement :

| Variable | Défaut | Description |
|----------|--------|-------------|
| `SOURCES_PATH` | `./00-Sources` | Dossier contenant les PDFs |
| `VAULT_PATH` | `./vault-myz` | Dossier du vault Obsidian à créer |
| `PROMPT_PATH` | `./prompt-extraction-myz.md` | Prompt d'extraction IA |
| `CHUNK_SIZE` | `12000` | Taille des chunks en caractères |
| `CHUNK_OVERLAP` | `1500` | Overlap entre chunks |

## Enregistrement dans AnyLLM

```json
{
  "mcpServers": {
    "myz-analyzer": {
      "command": "python /chemin/vers/myz-mcp-analyzer/mcp_server.py",
      "env": {
        "SOURCES_PATH": "/chemin/vers/00-Sources",
        "VAULT_PATH": "/chemin/vers/vault-myz",
        "PROMPT_PATH": "/chemin/vers/prompt-extraction-myz.md"
      }
    }
  }
}
```

## Utilisation

1. Dépose tes PDFs MAZ dans `00-Sources/`
2. Configure le serveur dans AnyLLM
3. Envoie ce message à l'IA :

```
Analyse tous les livres Mutant: Année Zéro disponibles et crée le vault 
Obsidian de MJ. Pour chaque livre :
1. Appelle extract_and_chunk_pdf
2. Pour chaque chunk, appelle get_chunk_for_analysis, analyse le texte 
   selon le prompt, puis appelle parse_and_write_entities avec le résultat
3. Une fois tous les livres traités, appelle create_obsidian_structure
4. Utilise get_progress pour suivre l'avancement
```

## Outils exposés

| Outil | Description |
|-------|-------------|
| `list_pdf_books` | Liste les PDFs disponibles |
| `extract_and_chunk_pdf` | Extrait et découpe un PDF |
| `get_chunk_for_analysis` | Prépare prompt + texte pour le LLM |
| `parse_and_write_entities` | Écrit les entités dans le vault |
| `create_obsidian_structure` | Crée dossiers et INDEX |
| `get_progress` | Rapport d'avancement |

## Structure du vault généré

```
vault-myz/
├── INDEX.md
├── 01-Regles/
│   ├── Personnage/{Roles,Talents,Competences,Mutations}/
│   └── Mecanique/
├── 02-Lieux/
│   ├── Arche/{Pieces,Personnages,Groupes}/
│   └── Zones/Zone-{nom}/
├── 03-Factions/
├── 04-PNJ/
├── 05-Artefacts/
├── 06-Menaces/
├── 07-Avant/
└── 08-Tables/
```
