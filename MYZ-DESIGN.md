# Design : MCP Server — Mutant: Année Zéro → Obsidian

**Date:** 2026-06-02  
**Projet:** Extraction automatique des livres de règles MAZ vers un vault Obsidian de MJ  
**Statut:** Conception

---

## Vue d'ensemble

Un **serveur MCP Python** qui orchestre l'analyse de plusieurs **PDFs de règles** de Mutant: Année Zéro via un LLM (AnyLLM ou Claude). Le serveur expose des outils pour :

- Extraire et découper le contenu des PDFs en chunks
- Analyser chaque chunk selon le prompt d'extraction MJ
- Parser les résultats et créer des fichiers Markdown individuels par entité
- Construire un vault Obsidian structuré et navigable

**Principe clé :** L'IA est l'orchestrateur. L'utilisateur demande "analyse tous les livres MAZ" et l'IA appelle les outils MCP séquentiellement.

**Différence avec le projet DCC :** PDFs au lieu d'EPUBs, structure de vault spécifique JDR/MJ, gestion multi-livres avec déduplication des règles répétées.

---

## Structure du vault Obsidian généré

```
vault-myz/
├── INDEX.md                          # Point d'entrée principal
├── 00-Sources/                       # PDFs originaux (ne pas modifier)
│   ├── myz-core.pdf
│   ├── zone-compendium-1.pdf
│   └── ...
│
├── 01-Regles/                        # Règles du jeu
│   ├── INDEX.md
│   ├── Personnage/
│   │   ├── INDEX.md
│   │   ├── Roles/                    # Un fichier par rôle
│   │   │   ├── INDEX.md
│   │   │   ├── Bossman.md
│   │   │   ├── Chroniqueur.md
│   │   │   └── ...
│   │   ├── Talents/                  # Un fichier par talent
│   │   │   ├── INDEX.md
│   │   │   └── ...
│   │   ├── Competences/              # Un fichier par compétence
│   │   │   ├── INDEX.md
│   │   │   └── ...
│   │   └── Mutations/                # Un fichier par mutation
│   │       ├── INDEX.md
│   │       └── ...
│   └── Mecanique/                    # Systèmes de jeu
│       ├── INDEX.md
│       ├── Gangrene.md
│       ├── Combat.md
│       ├── Poussee-de-jet.md
│       ├── Navigation-zone.md
│       ├── Recuperation.md
│       └── ...
│
├── 02-Lieux/                         # Géographie et lieux
│   ├── INDEX.md
│   ├── Arche/                        # Le refuge des mutants
│   │   ├── INDEX.md
│   │   ├── Description-generale.md
│   │   ├── Pieces/                   # Un fichier par pièce
│   │   │   ├── INDEX.md
│   │   │   └── ...
│   │   ├── Personnages/              # PNJ de l'Arche
│   │   │   ├── INDEX.md
│   │   │   └── ...
│   │   └── Groupes/                  # Factions de l'Arche
│   │       ├── INDEX.md
│   │       └── ...
│   └── Zones/                        # Secteurs explorables
│       ├── INDEX.md
│       └── Zone-{NomSecteur}/        # Un dossier par secteur
│           ├── Description.md
│           ├── Personnages/
│           └── Artefacts/
│
├── 03-Factions/                      # Groupes et organisations
│   ├── INDEX.md
│   └── ...
│
├── 04-PNJ/                           # Tous les PNJ (index global)
│   ├── INDEX.md
│   └── ...                           # Symlinks ou copies selon besoin
│
├── 05-Artefacts/                     # Tous les artefacts
│   ├── INDEX.md
│   └── ...
│
├── 06-Menaces/                       # Monstres et dangers de la Zone
│   ├── INDEX.md
│   └── ...
│
├── 07-Avant/                         # Le Temps d'Avant (lore)
│   ├── INDEX.md
│   └── ...
│
└── 08-Tables/                        # Tables aléatoires
    ├── INDEX.md
    ├── Rencontres-Zone.md
    ├── Meteo.md
    └── ...
```

---

## Améliorations proposées vs structure minimale

| Élément minimal demandé | Amélioration proposée | Raison |
|------------------------|----------------------|--------|
| `regles/personnage/{role,talent,compétences,mutation}` | Identique + frontmatter YAML | Navigation Obsidian améliorée |
| `regles/Mechanics/{Gangrène,...}` | `01-Regles/Mecanique/` + index | Accès rapide pendant les sessions |
| `Lieux/Arche/{pièces,personnages,groupes}` | Identique | ✓ |
| `Lieux/Zone-{nom}/{description,personnages,artefact}` | `Lieux/Zones/Zone-{nom}/` | Consistance de nommage |
| `Le temps d'avant/` | `07-Avant/` numéroté | Tri naturel dans Obsidian |
| — | `03-Factions/` | Factions qui traversent plusieurs lieux |
| — | `04-PNJ/` index global | Vue d'ensemble de tous les PNJs |
| — | `06-Menaces/` | Stats de combat rapides en session |
| — | `08-Tables/` | Tables aléatoires pour improvisation |
| — | Tags Obsidian systématiques | Filtrage par type |
| — | Déduplication inter-livres | Évite les doublons quand les règles sont répétées |
| — | Section "Notes MJ" dans chaque fichier | Utilisation directe en session |
| — | Niveau de Gangrène par secteur | Info critique pendant exploration |

---

## Architecture technique

### Composants

**1. MCP Server (Python)**
- Expose 6 outils appelés par l'IA
- Gère l'extraction PDF, le chunking, l'écriture Markdown
- Pas d'appels LLM internes — délégué à l'IA orchestratrice
- Gère la déduplication et la fusion des entités

**2. Extraction PDF**
- Bibliothèque : `PyMuPDF` (fitz) — plus robuste que pdfplumber pour les PDFs scannés/mis en page
- Extraction page par page avec numéros de page
- Gestion des colonnes multiples (fréquentes dans les livres de règles)
- Fallback OCR si le PDF est une image : `pytesseract` (optionnel)

**3. Chunking intelligent**
- Chunks de ~12k caractères (fenêtre plus petite car les PDFs JDR sont denses)
- Overlap de 1500 caractères
- **Découpage aux limites de section** (détecte les titres) quand possible
- Métadonnées : numéro de livre, numéro de page, position dans le chunk

**4. Déduplication inter-livres**
- Hash du nom normalisé de l'entité
- Si fichier existe : fusion intelligente (ajoute section `## Sources supplémentaires`)
- Détection et signalement des contradictions entre livres

---

## Spécification des outils MCP

### Outil 1 : `list_pdf_books`

**Input:** chemin du dossier sources

**Output:**
```json
{
  "books": [
    {"id": "myz-core", "path": "/sources/myz-core.pdf", "pages": 272, "size_mb": 45.2},
    {"id": "zone-comp-1", "path": "/sources/zone-compendium-1.pdf", "pages": 128}
  ],
  "total_books": 2
}
```

---

### Outil 2 : `extract_and_chunk_pdf`

**Input:**
```json
{
  "book_id": "myz-core",
  "chunk_size": 12000,
  "chunk_overlap": 1500
}
```

**Output:**
```json
{
  "chunks": [
    {
      "id": "myz-core_p001_c001",
      "book_id": "myz-core",
      "page_start": 1,
      "page_end": 5,
      "text": "...",
      "section_hint": "Chapitre 2 : Création de personnage"
    }
  ],
  "total_chunks": 312
}
```

**Logique :**
- Extraction texte via PyMuPDF
- Détection des titres de section (H1/H2 par taille de police ou style)
- Préférence de découpe aux limites de section
- Gestion des colonnes multiples

---

### Outil 3 : `analyze_chunk`

**Input:**
```json
{
  "chunk_id": "myz-core_p001_c001",
  "text": "...",
  "prompt_path": "/path/to/prompt-extraction-myz.md",
  "already_known_entities": ["Combat", "Gangrene", "Bossman"]
}
```

**Output:** Markdown brut avec marqueurs `<!-- ENTITY: ... -->`

**Logique :**
- Charge le prompt depuis le fichier
- Passe la liste des entités déjà extraites pour éviter les doublons redondants
- Combine prompt + contexte + chunk → appel LLM
- Retourne le markdown structuré

---

### Outil 4 : `parse_and_write_entities`

**Input:**
```json
{
  "markdown": "<!-- ENTITY: ... --> ...",
  "chunk_id": "myz-core_p001_c001",
  "vault_path": "/path/to/vault"
}
```

**Output:**
```json
{
  "files_created": ["01-Regles/Personnage/Roles/Bossman.md"],
  "files_updated": ["01-Regles/Mecanique/Combat.md"],
  "conflicts_detected": [],
  "entities_processed": 4
}
```

**Logique :**
- Split sur `<!-- ENTITY: Catégorie/Sous-catégorie/Nom -->`
- Mapping catégorie → dossier vault
- Création ou mise à jour du fichier (fusion si existant)
- Détection de contradictions (même section, contenu différent)
- Mise à jour du fichier de progression

---

### Outil 5 : `create_obsidian_structure`

**Input:** `vault_path`

**Output:** Structure créée avec fichiers INDEX

**Logique :**
- Crée tous les dossiers selon la structure définie
- Génère les `INDEX.md` initiaux
- Ajoute `.obsidian/` config de base (si absent)
- Crée le `INDEX.md` global avec carte du vault

---

### Outil 6 : `get_progress`

**Input:** rien (lit le fichier `.progress.json`)

**Output:**
```json
{
  "books_processed": 1,
  "total_books": 3,
  "current_book": "zone-comp-1",
  "chunks_processed": 156,
  "total_chunks": 487,
  "percent": 32,
  "entities_found": {
    "roles": 7,
    "talents": 43,
    "competences": 12,
    "mutations": 28,
    "pnj": 19,
    "lieux": 8,
    "artefacts": 34,
    "menaces": 11
  },
  "files_written": 162
}
```

---

## Configuration

### Variables d'environnement
```bash
SOURCES_PATH=/chemin/vers/00-Sources
VAULT_PATH=/chemin/vers/vault-obsidian
PROMPT_PATH=/chemin/vers/prompt-extraction-myz.md
CHUNK_SIZE=12000
CHUNK_OVERLAP=1500
```

### Enregistrement MCP (AnyLLM)
```json
{
  "mcpServers": {
    "myz-analyzer": {
      "command": "python /chemin/vers/mcp_server.py",
      "env": {
        "SOURCES_PATH": "/chemin/vers/00-Sources",
        "VAULT_PATH": "/chemin/vers/vault-myz",
        "PROMPT_PATH": "/chemin/vers/prompt-extraction-myz.md"
      }
    }
  }
}
```

---

## Flux d'exécution pour l'utilisateur

```
1. Dépose les PDFs dans 00-Sources/
2. Lance AnyLLM avec le serveur MCP configuré
3. Envoie :
   "Analyse tous les livres MAZ et crée le vault Obsidian 
    de MJ selon le prompt d'extraction."
4. L'IA orchestre :
   → list_pdf_books()
   → Pour chaque livre :
      → extract_and_chunk_pdf()
      → Pour chaque chunk :
         → analyze_chunk()
         → parse_and_write_entities()
      → Optionnel : get_progress()
   → create_obsidian_structure()
5. Ouvre le vault dans Obsidian
```

---

## Structure des fichiers techniques

```
myz-mcp-analyzer/
├── README.md
├── requirements.txt
├── mcp_server.py                 # Point d'entrée MCP
├── prompt-extraction-myz.md     # Prompt d'extraction IA
├── src/
│   ├── __init__.py
│   ├── pdf_handler.py           # Extraction PDF + chunking (PyMuPDF)
│   ├── entity_parser.py         # Parse markdown → entités
│   ├── obsidian_writer.py       # Écrit/fusionne fichiers .md
│   ├── deduplicator.py          # Gestion doublons inter-livres
│   └── progress_tracker.py     # Suivi d'avancement
├── tests/
│   └── ...
└── .progress.json               # Généré à l'exécution
```

---

## Gestion des cas particuliers PDF

| Problème | Solution |
|---------|---------|
| PDF scanné (image) | Détection automatique, fallback pytesseract |
| Colonnes multiples | PyMuPDF lit en ordre logique de flux |
| Tableaux de stats | Extraction spéciale avec formatage Markdown |
| Images de règles | Ignorer (noter "voir image p.XX" dans le fichier) |
| Caractères spéciaux (FR) | UTF-8 forcé, normalisation unicode |
| PDF protégé | Erreur claire avec instruction déprotection |

---

## Critères de succès

- [ ] Tous les PDFs extraits et chunckés sans perte
- [ ] 1 fichier Markdown par entité unique (talent, PNJ, lieu, etc.)
- [ ] Déduplication : pas de doublons entre livres différents
- [ ] INDEX.md fonctionnel dans chaque dossier
- [ ] Tags Obsidian appliqués partout
- [ ] Liens `[[croisés]]` dans les fichiers
- [ ] Frontmatter YAML valide
- [ ] Gangrène et mécaniques clés extraites avec tableaux de référence
- [ ] Sections "Notes MJ" utilisables directement en session
