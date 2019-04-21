#!/usr/bin/env python
# encoding: utf-8

# le chemin complet d'accès au fichier csv
CSV_FILE_FULL_NAME = "/home/hamza/Repository/Python/Public service/Ressources/fr.openfoodfacts.org.products.csv"

# une variable indiquant le nombre total des lignes dans le fichier csv (sans compter l'entête)
ITEMS_COUNT = 0

# l'index de la ligne suivante à traiter
CURRENT_INDEX = 0

# indique si les paramètres d'indexation ont été initialisés
INITIALIZED = False

