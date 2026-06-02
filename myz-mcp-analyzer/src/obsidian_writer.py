"""Write and merge entity files into the Obsidian vault."""

import re
from pathlib import Path

from .entity_parser import Entity

# Vault folder structure to create on init
VAULT_FOLDERS = [
    "00-Sources",
    "01-Regles/Personnage/Roles",
    "01-Regles/Personnage/Talents",
    "01-Regles/Personnage/Competences",
    "01-Regles/Personnage/Mutations",
    "01-Regles/Mecanique",
    "02-Lieux/Arche/Pieces",
    "02-Lieux/Arche/Personnages",
    "02-Lieux/Arche/Groupes",
    "02-Lieux/Zones",
    "03-Factions",
    "04-PNJ",
    "05-Artefacts",
    "06-Menaces",
    "07-Avant",
    "08-Tables",
]

# Minimal Obsidian workspace config
_OBSIDIAN_APP_JSON = """{
  "legacyEditor": false,
  "livePreview": true
}
"""

_INDEX_TEMPLATE = """---
tags: [index]
---

# Index : {folder_name}

> Généré automatiquement. Mettre à jour après chaque analyse.

## Contenu

<!-- Les fichiers de ce dossier apparaîtront ici après analyse -->

## Sous-dossiers

<!-- Les sous-dossiers apparaîtront ici -->
"""

_ROOT_INDEX = """---
tags: [index, vault-root]
---

# Vault MJ — Mutant: Année Zéro

Vault Obsidian pour Maître du Jeu, généré depuis les livres de règles officiels.

## Navigation rapide

| Section | Contenu |
|---------|---------|
| [[01-Regles/INDEX\\|01 — Règles]] | Rôles, Talents, Compétences, Mutations, Mécanique |
| [[02-Lieux/INDEX\\|02 — Lieux]] | Arche, Zones, Secteurs |
| [[03-Factions/INDEX\\|03 — Factions]] | Groupes et organisations |
| [[04-PNJ/INDEX\\|04 — PNJ]] | Tous les personnages non-joueurs |
| [[05-Artefacts/INDEX\\|05 — Artefacts]] | Objets du Temps d'Avant |
| [[06-Menaces/INDEX\\|06 — Menaces]] | Monstres et dangers de la Zone |
| [[07-Avant/INDEX\\|07 — Avant]] | Lore du Temps d'Avant |
| [[08-Tables/INDEX\\|08 — Tables]] | Tables aléatoires |

## Sources analysées

<!-- Liste des PDFs analysés -->
"""


def create_vault_structure(vault_path: str) -> dict:
    """Create all vault folders and initial INDEX files."""
    vault = Path(vault_path)
    folders_created = []

    for folder in VAULT_FOLDERS:
        target = vault / folder
        target.mkdir(parents=True, exist_ok=True)
        folders_created.append(str(folder))

        index_file = target / "INDEX.md"
        if not index_file.exists():
            folder_name = target.name
            index_file.write_text(_INDEX_TEMPLATE.format(folder_name=folder_name), encoding="utf-8")

    # Root INDEX
    root_index = vault / "INDEX.md"
    if not root_index.exists():
        root_index.write_text(_ROOT_INDEX, encoding="utf-8")

    # Obsidian config
    obsidian_dir = vault / ".obsidian"
    obsidian_dir.mkdir(exist_ok=True)
    app_json = obsidian_dir / "app.json"
    if not app_json.exists():
        app_json.write_text(_OBSIDIAN_APP_JSON, encoding="utf-8")

    return {
        "folders_created": len(folders_created),
        "index_files_created": len(folders_created) + 1,
        "vault_path": str(vault),
    }


def write_entities(entities: list[Entity], vault_path: str) -> dict:
    """Write or merge entity files into the vault. Returns a summary."""
    vault = Path(vault_path)
    created = []
    updated = []
    conflicts = []

    for entity in entities:
        safe_name = _safe_filename(entity.name)
        target_dir = vault / entity.vault_path
        target_dir.mkdir(parents=True, exist_ok=True)
        target_file = target_dir / f"{safe_name}.md"

        if not target_file.exists():
            target_file.write_text(entity.content, encoding="utf-8")
            created.append(str(target_file.relative_to(vault)))
        else:
            conflict = _merge_entity(target_file, entity)
            updated.append(str(target_file.relative_to(vault)))
            if conflict:
                conflicts.append(conflict)

    return {
        "files_created": created,
        "files_updated": updated,
        "conflicts_detected": conflicts,
        "entities_processed": len(entities),
    }


def _safe_filename(name: str) -> str:
    """Convert entity name to a safe filename."""
    name = name.strip()
    name = re.sub(r'[\\/*?:"<>|]', "-", name)
    name = re.sub(r"\s+", "-", name)
    return name[:120]


def _merge_entity(target_file: Path, new_entity: Entity) -> str | None:
    """Merge new entity info into an existing file. Returns conflict description if found."""
    existing = target_file.read_text(encoding="utf-8")
    source_note = f"\n\n---\n## Source supplémentaire\n- Livre: `{new_entity.source_book}` (chunk `{new_entity.chunk_id}`)\n"

    # Detect potential contradictions in key sections
    conflict = _detect_contradiction(existing, new_entity.content, new_entity.name)

    # Append new source block to avoid data loss
    if source_note.strip() not in existing:
        merged = existing.rstrip() + source_note
        target_file.write_text(merged, encoding="utf-8")

    return conflict


def _detect_contradiction(existing: str, new_content: str, name: str) -> str | None:
    """Simple heuristic: flag if key stat lines differ between versions."""
    key_patterns = [
        re.compile(r"\|\s*Force\s*\|\s*(\d+)", re.IGNORECASE),
        re.compile(r"\|\s*PV\s*\|\s*(\d+)", re.IGNORECASE),
        re.compile(r"coût:\s*(\d+)", re.IGNORECASE),
    ]
    for pattern in key_patterns:
        old = pattern.search(existing)
        new = pattern.search(new_content)
        if old and new and old.group(1) != new.group(1):
            return f"{name}: valeur '{pattern.pattern}' differ — ancien={old.group(1)}, nouveau={new.group(1)}"
    return None
