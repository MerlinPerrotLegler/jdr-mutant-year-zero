# Prompt d'extraction — Mutant: Année Zéro (MJ Obsidian Vault)

## Contexte

Tu analyses des livres de règles du jeu de rôle **Mutant: Année Zéro** (MAZ). Ton rôle est d'extraire toutes les informations pertinentes et de les structurer en fichiers Markdown individuels prêts pour un vault Obsidian de Maître du Jeu (MJ).

Le jeu se déroule dans un futur post-apocalyptique. Les personnages sont des **mutants** vivant dans **l'Arche**, leur refuge dans une Zone contaminée. Ils explorent des secteurs dangereux, récoltent des artefacts du **Temps d'Avant**, et luttent pour leur survie contre des menaces de la Zone, d'autres factions et leur propre Gangrène.

---

## Instructions générales

- Extrais **chaque entité distincte** (personnage, talent, compétence, lieu, artefact...) dans un bloc séparé.
- Utilise le marqueur `<!-- ENTITY: Catégorie/Sous-catégorie/Nom -->` avant chaque entité.
- Rédige en **français** (le jeu est en français).
- Inclus toujours le **frontmatter YAML** Obsidian avec les métadonnées.
- Utilise les **liens Obsidian** `[[Nom]]` pour référencer d'autres entités.
- Préfixe les tags avec `#` : `#pnj`, `#artefact`, `#zone`, `#talent`, `#règle`, etc.
- Si une information est **incertaine** ou **implicite**, marque-la avec `> *Déduction:*` ou `> *Incertain:*`.
- Ne fabrique pas d'information absente du texte.

---

## Catégories à extraire et format attendu

---

### 1. PERSONNAGES JOUEURS — Rôles (`Regles/Personnage/Roles/`)

Extrait chaque **Rôle** (archétype de personnage joueur).

**Marqueur:** `<!-- ENTITY: Regles/Personnage/Roles/NomDuRole -->`

**Format:**
```markdown
---
tags: [#role, #personnage-joueur, #règle]
source: "Nom du livre, p. XX"
---

# Rôle : [Nom]

## Description
[Description narrative du rôle dans la société de l'Arche]

## Attribut clé
[L'attribut principal associé à ce rôle]

## Compétence de rôle
[[CompétenceDeRôle]] — [brève description]

## Talent de rôle
[[TalentDeRôle]] — [description du talent unique]

## Équipement de départ
- [Item 1]
- [Item 2]

## Mutation de départ (si applicable)
[[MutationDeRôle]]

## Relations dans l'Arche
[Avec qui ce rôle interagit, quelle est sa place sociale]

## Notes MJ
[Conseils pour jouer contre ou avec ce type de personnage]
```

---

### 2. TALENTS (`Regles/Personnage/Talents/`)

Extrait chaque **Talent** (capacité spéciale, passive ou active).

**Marqueur:** `<!-- ENTITY: Regles/Personnage/Talents/NomDuTalent -->`

**Format:**
```markdown
---
tags: [#talent, #règle]
role: "[Rôle associé ou 'Général']"
rang: [1/2/3 ou "Unique"]
source: "Nom du livre, p. XX"
---

# Talent : [Nom]

## Rang [1/2/3]
[Effet du rang]

## Rang [2/3] *(si applicable)*
[Effet supplémentaire]

## Conditions d'activation
[Ce qui déclenche ou permet l'utilisation]

## Interactions
- Synergies avec : [[AutreTalent]], [[Compétence]]
- Incompatible avec : (si applicable)

## Exemple d'utilisation
[Situation concrète de jeu]
```

---

### 3. COMPÉTENCES (`Regles/Personnage/Competences/`)

Extrait chaque **Compétence** (skill utilisé avec des dés).

**Marqueur:** `<!-- ENTITY: Regles/Personnage/Competences/NomDeLaCompetence -->`

**Format:**
```markdown
---
tags: [#compétence, #règle]
attribut: "[Attribut associé]"
source: "Nom du livre, p. XX"
---

# Compétence : [Nom]

## Attribut associé
[[NomAttribut]]

## Description
[Ce que fait cette compétence]

## Utilisation de base
[Procédure standard de lancer de dés]

## Réussites supplémentaires
| Succès | Effet |
|--------|-------|
| +1     | ...   |
| +2     | ...   |
| +3     | ...   |

## Pousser le jet
[Conséquences spécifiques si on pousse ce jet]

## Situations typiques
- [Exemple 1]
- [Exemple 2]
```

---

### 4. MUTATIONS (`Regles/Personnage/Mutations/`)

Extrait chaque **Mutation** (pouvoir mutant).

**Marqueur:** `<!-- ENTITY: Regles/Personnage/Mutations/NomDeLaMutation -->`

**Format:**
```markdown
---
tags: [#mutation, #règle]
type: "[Physique/Mentale/Animale]"
coût: [Coût en points de mutation]
source: "Nom du livre, p. XX"
---

# Mutation : [Nom]

## Type
[Physique / Mentale / Animale]

## Coût
[Points de mutation requis]

## Effet
[Description de l'effet]

## Réussites supplémentaires
| Succès | Effet |
|--------|-------|
| +1     | ...   |

## Effet de surcharge *(poussé à l'extrême)*
[Ce qui se passe si la mutation est sur-utilisée]

## Notes MJ
[Comment exploiter cette mutation en tant que MJ]
```

---

### 5. MÉCANIQUE DU JEU (`Regles/Mecanique/`)

Extrait chaque **règle ou système** de jeu distinct.

**Marqueur:** `<!-- ENTITY: Regles/Mecanique/NomDeLaRegle -->`

Sujets typiques à extraire :
- Gangrène (Rot)
- Combat (initiative, attaque, défense)
- Poussées de jet
- Soins et récupération
- Chasse et ravitaillement
- Repos et récupération
- Navigation dans la Zone
- Commerce et troc

**Format:**
```markdown
---
tags: [#règle, #mécanique]
source: "Nom du livre, p. XX"
---

# [Nom de la règle]

## Résumé
[Une phrase : à quoi sert cette règle]

## Procédure
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

## Tableau de référence *(si applicable)*
| Situation | Modificateur |
|-----------|-------------|
| ...       | ...         |

## Exceptions et cas particuliers
- [Cas 1]
- [Cas 2]

## Interactions avec d'autres règles
- Lié à : [[AutreRegle]]

## Aide-mémoire MJ
[Ce que le MJ doit retenir en priorité]
```

---

### 6. GANGRÈNE — Règle spéciale (`Regles/Mecanique/Gangrene.md`)

La Gangrène mérite une page dédiée et détaillée.

**Marqueur:** `<!-- ENTITY: Regles/Mecanique/Gangrene -->`

Inclure :
- Niveaux de Gangrène et effets
- Sources d'exposition (secteurs, eau, nourriture...)
- Effets sur les jets de dés
- Mutations provoquées par la Gangrène
- Guérison et traitement (si possible)
- Tableau de référence rapide

---

### 7. L'ARCHE — Lieux (`Lieux/Arche/`)

Extrait chaque **pièce ou zone de l'Arche** séparément.

**Marqueur:** `<!-- ENTITY: Lieux/Arche/Pieces/NomDeLaPiece -->`

**Format:**
```markdown
---
tags: [#arche, #lieu, #pièce]
statut: "[Contrôlé/Contesté/Neutre/Ruiné]"
contrôlé_par: "[[NomFaction]]"
source: "Nom du livre, p. XX"
---

# [Nom de la pièce]

## Description
[Ambiance, état physique, odeurs, sons]

## Contenu notable
- [Item ou détail important]

## Personnages présents
- [[PNJ1]] — [rôle dans ce lieu]
- [[PNJ2]]

## Groupe/Faction en contrôle
[[NomFaction]]

## Rumeurs et secrets
> *Secret MJ:* [Information cachée]

## Scènes possibles
- [Scène ou événement qui peut se produire ici]
```

---

### 8. PERSONNAGES DE L'ARCHE (`Lieux/Arche/Personnages/`)

Extrait chaque **PNJ de l'Arche** séparément.

**Marqueur:** `<!-- ENTITY: Lieux/Arche/Personnages/NomDuPNJ -->`

**Format:**
```markdown
---
tags: [#pnj, #arche]
faction: "[[NomFaction]]"
rôle: "[Rôle social]"
statut: "[Vivant/Mort/Inconnu]"
source: "Nom du livre, p. XX"
---

# PNJ : [Nom]

## Description physique
[Apparence, signes distinctifs, mutations visibles]

## Personnalité
[En 2-3 adjectifs et une phrase]

## Motivation / Angle
[Ce que ce PNJ veut avant tout]

## Liens
- Allié de : [[AutrePNJ]]
- Ennemi de : [[AutrePNJ]]
- Membre de : [[Faction]]

## Attributs (si précisés)
| Attribut | Valeur |
|----------|--------|
| Force    | X      |
| Agilité  | X      |
| Esprit   | X      |
| Empathie | X      |

## Compétences notables
- [[Compétence]] X

## Talents
- [[Talent]]

## Secrets
> *Secret MJ:* [Ce que les joueurs ne savent pas]

## Scènes et interactions
- [Comment ce PNJ peut intervenir en jeu]
```

---

### 9. FACTIONS/GROUPES DE L'ARCHE (`Lieux/Arche/Groupes/`)

**Marqueur:** `<!-- ENTITY: Lieux/Arche/Groupes/NomDuGroupe -->`

**Format:**
```markdown
---
tags: [#faction, #arche, #groupe]
taille: "[Petite/Moyenne/Grande]"
puissance: [1-5]
source: "Nom du livre, p. XX"
---

# Faction : [Nom]

## Idéologie
[Ce en quoi ils croient, leur vision du monde]

## Objectif
[Ce qu'ils veulent accomplir]

## Chef
[[NomDuChef]]

## Membres notables
- [[PNJ1]] — [rôle]
- [[PNJ2]] — [rôle]

## Ressources contrôlées
- [[Pièce ou ressource]]

## Alliés et ennemis
- Alliés : [[AutreFaction]]
- Ennemis : [[AutreFaction]]

## Tensions et conflits
[Problèmes internes ou externes en cours]

## Comment les recruter / les éviter
[Conseils MJ]
```

---

### 10. ZONES (`Lieux/Zones/`)

Chaque **secteur de la Zone** explorable est un dossier séparé.

**Marqueur:** `<!-- ENTITY: Lieux/Zones/NomDuSecteur/Description -->`

**Format pour la description :**
```markdown
---
tags: [#zone, #secteur, #lieu]
gangrène: [Niveau 1-4]
distance_arche: "[Proche/Moyenne/Lointaine]"
source: "Nom du livre, p. XX"
---

# Secteur : [Nom]

## Ambiance
[Description en 3-4 phrases — atmosph  ère, danger, couleurs, sons]

## Niveau de Gangrène
[Niveau et effets spécifiques à ce secteur]

## Points d'intérêt
- [Lieu 1]
- [Lieu 2]

## Menaces
- [[Monstre ou danger]]

## Artefacts potentiels
- [[Artefact]] (Table X)

## PNJ et factions présents
- [[PNJ]]

## Rumeurs pour atteindre ce secteur
[Ce que les joueurs peuvent entendre à l'Arche]

## Secrets
> *Secret MJ:* [Histoire cachée du secteur]
```

**Pour les PNJ et artefacts de zone :**
- `<!-- ENTITY: Lieux/Zones/NomDuSecteur/Personnages/NomDuPNJ -->`
- `<!-- ENTITY: Lieux/Zones/NomDuSecteur/Artefacts/NomDeLArtefact -->`

---

### 11. ARTEFACTS (`Artefacts/`)

**Marqueur:** `<!-- ENTITY: Artefacts/NomDeLArtefact -->`

**Format:**
```markdown
---
tags: [#artefact, #temps-davant]
type: "[Arme/Outil/Véhicule/Objet/Mystérieux]"
encombrement: [Valeur]
valeur: "[Troc estimé]"
source: "Nom du livre, p. XX"
---

# Artefact : [Nom]

## Description physique
[À quoi ça ressemble, état de conservation]

## Fonction probable
[Ce que les mutants en font, utilité supposée]

## Fonction réelle *(Temps d'Avant)*
[Ce que c'était vraiment — couteau suisse, radio, etc.]

## Effets de jeu
[Bonus/malus mécaniques, règles spéciales]

## Condition / Fiabilité
[Risque de panne, utilisation limitée]

## Valeur au troc
[Estimation en rations/eau/autre]

## Où le trouver
- Secteurs : [[NomSecteur]]
- Tables de fouille : Table X
```

---

### 12. MENACES DE LA ZONE (`Menaces/`)

**Marqueur:** `<!-- ENTITY: Menaces/NomDeLaMenace -->`

**Format:**
```markdown
---
tags: [#menace, #monstre, #zone]
type: "[Animal mutant/Humanoïde/Machine/Autre]"
dangerosité: [1-5]
source: "Nom du livre, p. XX"
---

# Menace : [Nom]

## Description
[Apparence, comportement, habitat]

## Attributs
| Attribut | Valeur |
|----------|--------|
| Force    | X      |
| Agilité  | X      |
| Esprit   | X      |
| Empathie | X      |
| PV       | X      |

## Capacités spéciales
- [Capacité 1] : [description]

## Tactiques
[Comment cette créature/menace se comporte en combat]

## Loot / Récolte
[Ce qu'on peut obtenir en la vainquant]

## Secteurs associés
- [[NomSecteur]]

## Rumeurs et légendes
[Ce que les mutants en disent]
```

---

### 13. LE TEMPS D'AVANT (`Avant/`)

Informations sur la civilisation humaine pré-apocalyptique.

**Marqueur:** `<!-- ENTITY: Avant/NomDuSujet -->`

**Format:**
```markdown
---
tags: [#avant, #lore, #histoire]
certitude: "[Confirmé/Déduit/Légende]"
source: "Nom du livre, p. XX"
---

# Temps d'Avant : [Sujet]

## Ce qu'on sait *(informations certaines)*
[Faits confirmés par les textes]

## Ce qu'on déduit *(indices dans les artefacts/lieux)*
> *Déduction:* [Raisonnement basé sur les indices]

## Ce que les mutants en disent *(légendes)*
[Mythes et croyances des mutants à ce sujet]

## Impact sur le présent
[Comment ça affecte le jeu aujourd'hui]

## Liens
- Artefacts liés : [[Artefact]]
- Lieux liés : [[Secteur]]
```

---

## Règles de déduplication

Si une entité apparaît dans plusieurs livres :
1. **Crée un seul fichier** par entité unique
2. Ajoute une section `## Sources` listant tous les livres
3. Signale les **contradictions** entre livres avec `> ⚠️ Contradiction:`
4. Garde la version la plus complète / récente comme référence

---

## Format des INDEX par dossier

Pour chaque dossier, génère un `INDEX.md` :

**Marqueur:** `<!-- ENTITY: INDEX/CheminDuDossier -->`

```markdown
---
tags: [#index]
---

# Index : [Nom du dossier]

## Contenu
| Nom | Description courte | Tags |
|-----|-------------------|------|
| [[Fichier1]] | ... | #tag |
| [[Fichier2]] | ... | #tag |

## Sous-dossiers
- [[SousDossier/INDEX]]

## Liens rapides MJ
- [Lien vers entité souvent utilisée]
```

---

## Ce qu'il faut NE PAS extraire

- Le texte narratif de fiction (nouvelles, exemples de jeu immersifs)
- Les crédits et mentions légales
- La table des matières (elle sera reconstruite via les INDEX)
- Les répétitions exactes d'une règle déjà extraite

---

## Priorité d'extraction (du plus au moins important)

1. **Règles de base** — compétences, talents, rôles, mutations
2. **PNJ avec nom propre** — toujours un fichier dédié
3. **Lieux nommés** — Arche + Secteurs
4. **Artefacts spécifiques** — avec effets mécaniques
5. **Factions et groupes** — avec motivations
6. **Menaces de zone** — avec stats
7. **Lore Temps d'Avant** — contextuel
8. **Tables aléatoires** — synthétisées en tableaux Markdown

---

*Ce prompt est conçu pour être utilisé avec un MCP server qui découpe les PDFs en chunks de 10-15k caractères et les soumet un par un à l'IA pour extraction.*
