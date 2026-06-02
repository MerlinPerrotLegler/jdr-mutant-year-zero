---
tags: [règle, création, personnage, référence-rapide]
source: "Core book, p. 16-25"
---

# Création de Personnage — Guide Complet

> Suivre les 12 étapes dans l'ordre.

---

## Diagramme des 12 étapes

```mermaid
flowchart TD
    START([🎲 Créer votre mutant]) --> E1

    E1["① RÔLE\nChoisir parmi les 8 rôles"]
    E2["② NOM\nChoisir ou inventer"]
    E3["③ APPARENCE\nVisage · Corps · Vêtements"]
    E4["④ ATTRIBUTS\n14 points à répartir\nentre 2 et 4\n(5 pour l'attribut clé)"]
    E5["⑤ COMPÉTENCES\n10 points à répartir\nmax 3 par compétence\nmin 1 en compétence spécialiste"]
    E6["⑥ TALENT\n1 talent de départ\nparmi ceux du rôle"]
    E7["⑦ MUTATION\nTirer aléatoirement\n1 mutation de départ"]
    E8["⑧ RELATIONS\nAvec les autres PJ\nAvec des PNJ\n(aimer / haïr / protéger)"]
    E9["⑨ GRAND RÊVE\nObjectif personnel\n(moteur narratif)"]
    E10["⑩ ÉQUIPEMENT\nArme de départ\nBalles · Bouffe · Eau\nselon le rôle"]
    E11["⑪ L'ARCHE\nCréer collectivement\nvoyez le chapitre 7"]
    E12["⑫ PLANQUE\nDescription + équipement\ncaché dedans"]

    E1 --> E2 --> E3 --> E4 --> E5 --> E6 --> E7 --> E8 --> E9 --> E10 --> E11 --> E12
    E12 --> DONE([✅ Prêt à jouer])
```

---

## Les 8 Rôles

```mermaid
flowchart LR
    ROLES([Choisir un rôle])

    ROLES --> A["🗡️ FRACASSEUR\nVigueur clé\nIntimidation\n1 mutation D6"]
    ROLES --> B["📖 CHRONIQUEUR\nEmpathie clé\nInspirer\n1 mutation au choix"]
    ROLES --> C["🤝 COMBINARD\nEmpathie clé\nConclure un marché\n1 mutation au choix"]
    ROLES --> D["👑 CAÏD\nIntellect clé\nCommandement\n1 mutation au choix"]
    ROLES --> E["⛓️ LARBIN\nVigueur clé\nTenir le coup\n1 mutation au choix"]
    ROLES --> F["🐕 MAÎTRE-CHIEN\nAgilité clé\nLâcher le chien\n1 mutation au choix"]
    ROLES --> G["🔧 RAFISTOLEUR\nIntellect clé\nSystème D\n1 mutation au choix\n+ 1 artefact"]
    ROLES --> H["🗺️ ZONARD\nAgilité clé\nTrouver le chemin\n1 mutation au choix"]
```

---

## Étape ④ — Répartition des Attributs

```mermaid
flowchart TD
    A["14 points à distribuer"] --> B{Règles}
    B --> C["Minimum : 2\ndans chaque attribut"]
    B --> D["Maximum : 4\npour la plupart"]
    B --> E["Maximum : 5\npour l'attribut clé du rôle"]

    C --> F["VIGUEUR\n= Dégâts subis\n(Corps à corps · Endurance · Force)"]
    C --> G["AGILITÉ\n= Épuisement subi\n(Vitesse · Tir · Furtivité)"]
    C --> H["INTELLECT\n= Confusion subie\n(Savoir · Compréhension)"]
    C --> I["EMPATHIE\n= Doute subi\n(Social · Soins · Mutations mentales)"]
```

| Rôle | Attribut clé (max 5) |
|---|---|
| Fracasseur | Vigueur |
| Larbin | Vigueur |
| Maître-chien | Agilité |
| Zonard | Agilité |
| Chroniqueur | Empathie |
| Combinard | Empathie |
| Caïd | Intellect |
| Rafistoleur | Intellect |

---

## Étape ⑤ — Compétences

```mermaid
flowchart TD
    A["10 points à répartir"] --> B["12 compétences de base\n+ 1 spécialiste du rôle"]
    B --> C{"Règles"}
    C --> D["Maximum 3\npar compétence\nà la création"]
    C --> E["Minimum 1\nen compétence spécialiste"]
    C --> F["0 = possible\nsauf compétence spécialiste"]

    B --> G["VIGUEUR\nEndurance · Force · Combat"]
    B --> H["AGILITÉ\nFurtivité · Déplacement · Tir"]
    B --> I["INTELLECT\nObservation · Compréhension\nConnaissance de la Zone"]
    B --> J["EMPATHIE\nPerception des émotions\nManipulation · Soins"]
```

---

## Étape ⑥ — Talents de départ par rôle

| Rôle | Talents disponibles (choisir 1) |
|---|---|
| **Fracasseur** | Coup vicieux · Cruel · Passage en force |
| **Chroniqueur** | Agitateur · Toubib · Troubadour |
| **Combinard** | Info croustillante · Magouilleur · Vicelard |
| **Caïd** | Commandant · Détrousseur · Flingueurs |
| **Larbin** | Blasé · Dur à cuire · Rebelle |
| **Maître-chien** | Chien de combat · Le meilleur ami du mutant · Limier |
| **Rafistoleur** | Fou du volant · Inventeur · Rétameur |
| **Zonard** | Chasseur de monstres · Dénicheur de Gangrène · Récupérateur |

---

## Étape ⑦ — Mutation de départ

```mermaid
flowchart LR
    A["Tirer 1 mutation\nau hasard\nD66 sur la table"] --> B{Résultat}
    B --> C["Ailes d'insecte\nAimant humain\nAmphibie\nBouffeur de Gangrène\nCracheur de feu\nHomme-bête\nHomme-plante\nInsectoïde\n..."]
    A --> D["PM de départ\n= nombre de mutations\nau début de chaque séance"]
    D --> E["Maximum 4 mutations\ntout au long du jeu"]
    E --> F["Nouvelles mutations\npar ratés ou PX"]
```

> Le Fracasseur (livret d'intro) tire sur une table D6 restreinte. En campagne complète, utiliser la table D66 du [[Mutations/Table-mutations-D66|chapitre 5]].

---

## Étape ⑩ — Équipement de départ par rôle

| Rôle | Balles | Bouffe | Eau | Arme(s) | Spécial |
|---|---|---|---|---|---|
| **Fracasseur** | D6 | 2D6 | D6 | Batte cloutée · Poing américain · Hache | — |
| **Chroniqueur** | D6 | D6 | D6 | Aucune | — |
| **Combinard** | 2D6 | 2D6 | D6 | Couteau · Poing américain · Derringer | — |
| **Caïd** | 2D6 | 2D6 | D6 | Batte cloutée · Couteau · Pistolet | — |
| **Larbin** | 0 | D6 | D6 | Batte cloutée · Chaîne de vélo · Fronde | — |
| **Maître-chien** | D6 | D6 | D6 | Chaîne · Couteau · Fronde · Fusil | **Le chien** |
| **Rafistoleur** | 2D6 | D6 | D6 | Poing américain · Chaîne · Pistolet | **1 artefact** |
| **Zonard** | D6 | D6 | 2D6 | Fusil de fortune · Arc (5 flèches) | — |

---

## Encombrement

```mermaid
flowchart LR
    A["Capacité de transport\n= Vigueur × 2\nobjets ordinaires"] --> B{Taille des objets}
    B --> C["Lourd = 2 emplacements"]
    B --> D["Normal = 1 emplacement"]
    B --> E["Léger = ½ emplacement\n2 légers = 1 emplacement"]
    B --> F["Minuscule = 0 emplacement"]
    B --> G["4 rations bouffe ou eau\n= 1 emplacement"]
    B --> H["Balles = 0 emplacement"]
```

---

## Progression (après création)

```mermaid
flowchart LR
    A([Fin de séance]) --> B["Obtenir des PX\nselon les événements"]
    B --> C{Dépenser 5 PX}
    C --> D["Augmenter\nune compétence\nde 1 niveau"]
    C --> E["Apprendre\nun nouveau talent\n(rôle ou général)"]
    D --> F["Niveau max : 5"]
    E --> G["Talents illimités\nau fil du jeu"]
```

---

## Liens utiles

- [[Roles/Fracasseur|Fracasseur]] · [[Roles/Chroniqueur|Chroniqueur]] · [[Roles/Combinard|Combinard]] · [[Roles/Caid|Caïd]]
- [[Roles/Larbin|Larbin]] · [[Roles/Maitre-chien|Maître-chien]] · [[Roles/Rafistoleur|Rafistoleur]] · [[Roles/Zonard|Zonard]]
- [[Mutations/Table-mutations-D66|Table des Mutations (D66)]]
- [[../Mecanique/Regles-des-jets|Règles des jets de dés]]
- [[../Mecanique/Traumatismes|Traumatismes]]
- [[../Mecanique/Arche-developpement|L'Arche — Développement (étape ⑪)]]
- [[../../Regles/Competences/Commandement|Compétences de spécialiste]]
