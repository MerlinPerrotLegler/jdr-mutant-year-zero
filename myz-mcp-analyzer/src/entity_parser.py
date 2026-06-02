"""Parse LLM markdown output into individual entities."""

import re
from dataclasses import dataclass, field

_ENTITY_MARKER = re.compile(r"<!--\s*ENTITY:\s*([^>]+?)\s*-->")

# Maps category prefix → vault subdirectory
CATEGORY_TO_PATH: dict[str, str] = {
    "Regles/Personnage/Roles": "01-Regles/Personnage/Roles",
    "Regles/Personnage/Talents": "01-Regles/Personnage/Talents",
    "Regles/Personnage/Competences": "01-Regles/Personnage/Competences",
    "Regles/Personnage/Mutations": "01-Regles/Personnage/Mutations",
    "Regles/Mecanique": "01-Regles/Mecanique",
    "Lieux/Arche/Pieces": "02-Lieux/Arche/Pieces",
    "Lieux/Arche/Personnages": "02-Lieux/Arche/Personnages",
    "Lieux/Arche/Groupes": "02-Lieux/Arche/Groupes",
    "Lieux/Zones": "02-Lieux/Zones",
    "Factions": "03-Factions",
    "PNJ": "04-PNJ",
    "Artefacts": "05-Artefacts",
    "Menaces": "06-Menaces",
    "Avant": "07-Avant",
    "Tables": "08-Tables",
    "INDEX": "INDEX",
}


@dataclass
class Entity:
    category: str       # e.g. "Regles/Personnage/Roles"
    name: str           # e.g. "Bossman"
    content: str        # Full markdown content
    vault_path: str     # Resolved subfolder in vault
    chunk_id: str = ""
    source_book: str = ""


def parse_entities(markdown: str, chunk_id: str = "") -> list[Entity]:
    """Split markdown on ENTITY markers and return Entity objects."""
    parts = _ENTITY_MARKER.split(markdown)

    # parts alternates: [pre_text, category/name, content, category/name, content, ...]
    entities: list[Entity] = []
    i = 1
    while i < len(parts) - 1:
        raw_path = parts[i].strip()
        content = parts[i + 1].strip()
        i += 2

        if not content:
            continue

        category, name = _split_path(raw_path)
        vault_path = _resolve_vault_path(category)
        book_id = chunk_id.split("_")[0] if chunk_id else ""

        entities.append(Entity(
            category=category,
            name=name,
            content=content,
            vault_path=vault_path,
            chunk_id=chunk_id,
            source_book=book_id,
        ))

    return entities


def _split_path(raw: str) -> tuple[str, str]:
    """Split 'Category/Sub/Name' into (category, name)."""
    parts = raw.rsplit("/", 1)
    if len(parts) == 2:
        return parts[0], parts[1]
    return raw, raw


def _resolve_vault_path(category: str) -> str:
    """Map an entity category to a vault subdirectory."""
    # Exact match first
    if category in CATEGORY_TO_PATH:
        return CATEGORY_TO_PATH[category]

    # Prefix match (handles dynamic zone paths like Lieux/Zones/NomSecteur/...)
    for prefix, vault_dir in CATEGORY_TO_PATH.items():
        if category.startswith(prefix):
            suffix = category[len(prefix):]
            return vault_dir + suffix.replace("/", "/")

    # Fallback: use the category path directly under vault root
    return category
