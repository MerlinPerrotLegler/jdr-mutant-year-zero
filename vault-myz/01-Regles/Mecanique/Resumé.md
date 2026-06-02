---
tags: [règle, mécanique, combat, résumé, référence-rapide]
source: "Core book, p. 79-95"
---

# Résumé — Mécanique de Combat

> Référence rapide pour la MJ. Tous les liens pointent vers les fiches détaillées.

---

## 1. Structure d'un Tour de Conflit

```mermaid
flowchart TD
    A([Début du conflit]) --> B[Jet d'Initiative\nAgilité de chaque combattant]
    B --> C{Égalité ?}
    C -- Oui --> D[Actions simultanées]
    C -- Non --> E[Ordre décroissant d'initiative]
    D --> F
    E --> F[TON TOUR]
    F --> G[1 ACTION]
    F --> H[1 MANŒUVRE]
    G --> G1[Combat\nou Tir\nou Mutation\nou Manipulation\nou Soins\nou Forcer jet...]
    H --> H1[Déplacement d'1 rang\nou Viser\nou Recharger\nou Ramasser un objet\nou Rappeler le chien]
    G1 --> I{Fin de tous les tours ?}
    H1 --> I
    I -- Non --> F
    I -- Oui --> J([Tour suivant])
```

> **Mutation (A) :** peut être activée pendant une action ou manœuvre sans la consommer (effet d'amélioration ou de réaction).

---

## 2. Combat Rapproché

```mermaid
flowchart LR
    A([Attaquant\ndéclare Combat]) --> B{Défenseur\nse défend ?}
    B -- Oui\ndéclarer AVANT le jet --> C[Jets simultanés\nles deux font Combat]
    B -- Non --> D[Seul l'attaquant\nlance]

    C --> E{Résultat}
    D --> E

    E -- Échec de l'attaquant --> F[Aucun effet\nla MJ peut punir]
    E -- Réussite\nattaquant > défenseur --> G[DÉGÂTS de l'arme\n+ Prouesses attaque]
    E -- Réussite défenseur --> H[Prouesses défense]

    G --> G1["• +1 dégât ×N\n• +1 épuisement\n• Initiative +2\n• Désarmer -1 init.\n• Renverser\n• Immobiliser"]
    H --> H1["• Annuler 1 / adverse ×N\n• Initiative +2\n• Désarmer\n• Repousser\n• +1 épuisement\n• Contre-attaque (dégâts)"]

    H1 -. Défense coûte\nla prochaine action .-> A
```

---

## 3. Combat à Distance

```mermaid
flowchart LR
    A([Attaquant\ndéclare Tir]) --> B{A visé\navant ?}
    B -- Oui\n1 manœuvre avant --> C[+1 mod\n+2 avec abri]
    B -- Non --> D[Pas de bonus]
    C --> E[Jet de Tir]
    D --> E

    E --> F{Modificateur\nde portée}
    F -- Portée de main --> G[-3\nSauf cible sans défense]
    F -- Proche --> H[±0]
    F -- Courte --> I[-1]
    F -- Longue --> J[-2]

    E --> K{Résultat}
    K -- Échec --> L[Raté\nbruit possible\nprojectile perdu]
    K -- Réussite --> M[DÉGÂTS de l'arme\n+ Prouesses]
    M --> M1["• +1 dégât ×N\n• Épuisement\n• Initiative +2\n• Désarmer\n• Renverser"]

    E --> N[Recharger après le tir\n= 1 manœuvre\nSauf chargeur artefact]
```

---

## 4. Portées et Déplacements

| Zone | Exemples | Déplacement |
|---|---|---|
| **Portée de main** | Corps à corps | — |
| **Proche** | Quelques mètres | 1 manœuvre depuis main |
| **Courte** | Une pièce / ~30 m | 1 manœuvre depuis Proche |
| **Longue** | Visible à l'œil nu | 2 manœuvres depuis Courte |
| **Lointaine** | Hors de portée réaliste | Hors conflit |

> Se déplacer de Courte → Longue coûte **2 manœuvres dans le même tour** (donc aucune action ce tour).

---

## 5. Système de Traumatismes et Brisé

```mermaid
flowchart TD
    A[Subir des dégâts] --> B{Attribut tombe à 0 ?}
    B -- Non --> C[Traumatisme noté sur la fiche]
    B -- Oui --> D[BRISÉ]

    D --> E{Type de\ntraumatisme}
    E -- Vigueur = 0 Dégâts --> F[Blessure critique\nD66 sur table p.90\nPeut être mortel]
    E -- Agilité = 0 Épuisement --> G[KO / à terre\nPas de mort immédiate]
    E -- Intellect = 0 Confusion --> H[Inconscient\nPas de mort immédiate]
    E -- Empathie = 0 Doute --> I[Effondrement\nPas de mort immédiate]

    F --> J{Test de Soins\nréussi ?}
    J -- Oui --> K[Stabilisé\nRécupère N points\npar /]
    J -- Non --> L[En danger de mort\nD6 jours]

    C --> M[Récupération]
    K --> M
    M --> M1["Dégâts → manger + repos\nÉpuisement → boire + repos\nConfusion → dormir 4h\nDoute → compagnie mutants"]
```

### Les 4 traumatismes

| Traumatisme | Attribut réduit | Sources courantes |
|---|---|---|
| **Dégâts** | Vigueur | Armes, explosions, chutes, acide |
| **Épuisement** | Agilité | Faim, venin, déshydratation |
| **Confusion** | Intellect | Peur, drogues, mutations psy |
| **Doute** | Empathie | Manipulation, Intimidation, Tourmenteur psy |

---

## 6. Forcer un Jet et Points de Mutation

```mermaid
flowchart TD
    A[Jet de dés\n: échec ou prouesses souhaitées] --> B{Forcer ?}
    B -- Non --> C[Accepter l'échec]
    B -- Oui --> D[Relancer TOUS les dés\nqui ne montrent ni / ni = ni ⚙\nUNE SEULE FOIS]

    D --> E{Dés obtenus}
    E -- = sur dé jaune --> F[+1 traumatisme\nsur l'attribut utilisé\n+1 PM gagné]
    E -- ⚙ sur dé noir --> G[-1 bonus\nd'équipement\nde l'objet]
    E -- / --> H[Réussite\nou prouesse sup.]

    F --> I[Accumuler\nles PM]
    I --> J[Activer mutations\nen combat]
```

> **Jet forcé interdit** pour : récupérer de Soins sur soi-même, Tenir le coup.

---

## 7. Utiliser les Mutations en Combat

```mermaid
flowchart LR
    A[Décision d'activer\nune mutation] --> B{Type d'effet}

    B -- Action normale --> C[Compte comme\nvotre action du tour\nCoûte X PM]
    B -- Effet Amélioration A --> D[S'active pendant\nune action/manœuvre\nNe consomme pas l'action]
    B -- Effet Réaction R --> E[S'active à N'IMPORTE QUEL\nmoment du tour\nNe consomme pas l'action]

    C --> F{Jet de raté ?\n1 dé base par PM dépensé}
    D --> F
    E --> F

    F -- = obtenu --> G[Tirer D6 sur\ntable des Ratés\nMutation produit quand même son effet]
    F -- Pas de = --> H[Mutation\nfonctionne normalement]
```

### Table des Ratés des Mutations (rappel)

| D6 | Effet |
|---|---|
| **1** | +1 traumatisme permanent + nouvelle mutation |
| **2** | Vous subissez aussi les effets + même traumatisme que la cible |
| **3** | Coûte 2× les PM (sans effet amélioré) |
| **4** | Mutation bloquée pour le reste de la séance |
| **5** | Modification cosmétique permanente |
| **6** | PM remboursés + réactivation immédiate gratuite |

---

## 8. Fuir un Conflit

```mermaid
flowchart LR
    A([Décider de fuir]) --> B[Test de Déplacement]
    B --> C{Modificateur\nselon distance\nde l'ennemi le plus proche}
    C -- Portée de main --> D[-2]
    C -- Proche --> E[-1]
    C -- Courte --> F[±0]
    C -- Longue --> G[+1]
    C -- Lointaine --> H[Aucun test\nfuite automatique]

    D --> I{Réussite ?}
    E --> I
    F --> I
    G --> I

    I -- Oui --> J[Vous vous échappez\nFin du conflit pour vous]
    I -- Non --> K[Cloué sur place\nrestez à la même portée\nRessayez au prochain tour]
```

> Mutations **Sprinteur**, **Jambes de grenouille** et **Spores** permettent de fuir sans test.

---

## 9. Attaque Surprise et Embuscade

```mermaid
flowchart TD
    A[Attaquant veut surprendre] --> B{Type}

    B -- Attaque surprise\nmouvement discret --> C[Test opposé\nFurtivité vs Observation\nmodificateur selon distance]
    B -- Embuscade\nattente immobile --> D[Test de Déplacement\n+ modificateur de distance\n+ bonus fixe +2]

    C --> E{Réussite ?}
    D --> E

    E -- Oui --> F[Action GRATUITE\navant jet d'initiative\nPas de manœuvre]
    E -- Non --> G[Détecté à la\nposition de départ]

    F --> H{Plusieurs attaquants ?}
    H -- Oui --> I[Chacun fait\nson propre test\nSi un échoue →\ntous détectés]
    H -- Non --> J[Attaque surprise\nréussie]
```

| Distance | Mod. Furtivité | Mod. Embuscade |
|---|---|---|
| Portée de main | -2 | -2 + 2 = ±0 |
| Proche | -1 | -1 + 2 = +1 |
| Courte | ±0 | ±0 + 2 = +2 |
| Longue | +1 | +1 + 2 = +3 |
| Lointaine | +2 | +2 + 2 = +4 |

---

## 10. Conflits Sociaux (Manipulation / Intimidation)

```mermaid
flowchart LR
    A[Décision de Manipuler\nou Intimider] --> B[MJ évalue la\nPOSITION DE NÉGOCIATION]
    B --> C{Modificateurs}
    C -- Favorables +1 chacun --> D["Plus de gens de votre côté\nDemande sans coût pour la cible\nCible traumatisée\nVous avez aidé la cible\nArguments sensés"]
    C -- Défavorables -1 chacun --> E["Cible a plus de soutiens\nCible en plein combat (-2)\nCe que vous demandez est déraisonnable"]

    B --> F{Jet opposé\nManip. vs Perception émo.\nou Intimid. vs Intimid.}
    F -- Réussite --> G[Cible obéit\nmais demande\nquelque chose en retour]
    F -- Prouesse --> H[+1 doute par /\nSi Brisé en doute → obéit\nsans contrepartie]
    F -- Échec --> I[Refus\npeut attaquer\nsi provoquée]
```

---

## 11. Récapitulatif Rapide — Prouesses par Compétence

| Compétence | 1 seul / | / supplémentaires |
|---|---|---|
| **Combat** (attaque) | Dégâts de l'arme | +dégât · épuisement · init+2 · désarmer · renverser · immobiliser |
| **Combat** (défense) | Annuler 1 / adverse | +annuler · init+2 · désarmer · repousser · épuisement · contre-attaque |
| **Tir** | Dégâts de l'arme | +dégât · épuisement · init+2 · désarmer · renverser |
| **Furtivité** | Passer inaperçu | +1 à la 1re attaque par / sup. |
| **Déplacement** (fuite) | Échapper | Aider un ami à fuir sans jet |
| **Endurance** | Tenir le coup | Aider un ami à tenir sans jet |
| **Manipulation** | Obéissance avec contrepartie | +1 doute par / sup. |
| **Intimidation** | Obéir ou attaquer | +1 doute par / sup. |
| **Soins** (Brisé) | +1 attribut récupéré | +1 attribut par / sup. |
| **Inspirer** (aide) | +2 à la compétence cible | +1 supplémentaire par / sup. |
| **Inspirer** (gêne) | -2 à la compétence cible | -1 supplémentaire par / sup. |

---

## Liens vers les fiches détaillées

- [[Combat|Mécanique : Combat complet]]
- [[Traumatismes|Mécanique : Traumatismes]]
- [[Regles-des-jets|Règles des jets de dés]]
- [[Ratés-des-mutations|Ratés des mutations]]
- [[Etats|États : Affamé, Déshydraté, Exténué, Hypothermie]]
- [[Blessures-critiques|Blessures critiques]]
- [[../../Regles/Competences/Combat|Compétence : Combat (détail)]]
- [[../../Regles/Competences/Tir|Compétence : Tir (détail)]]
- [[../../Regles/Competences/Deplacement|Compétence : Déplacement (détail)]]
- [[../../Regles/Competences/Manipulation|Compétence : Manipulation (détail)]]
