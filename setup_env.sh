#!/bin/bash
# Schritt 1: Erstelle eine Python Virtual Environment in einem Ordner namens '.venv'
python3.12 -m venv .venv  
# Schritt 2: Aktiviere die virtuelle Umgebung
source .venv/bin/activate  
# Schritt 3: Aktualisiere `pip` und installiere die Pakete `wheel` und `python-dotenv` mit der Option `--upgrade`
pip install --upgrade pip
pip install --upgrade wheel python-dotenv autopep8 mkdocs

# Schritt 3: Installiere die erforderlichen Python-Pakete
# Wenn eine requirements.txt-Datei vorhanden ist, installiere die darin aufgelisteten Pakete
if [ -f requirements.txt ]; then
    pip install -r requirements.txt
fi

# Schritt 4: Initialisiere `docsify` in einem Ordner namens `docs`
#docsify init ./docs

# Schritt 4: Initialisiere `mkdocs` mit dem Namen des aktuellen Verzeichnisses
mkdocs new $(basename "$(pwd)")
# Erstelle eine Konfigurationsdatei für `mkdocs`. Übergebe den Namen des aktuellen Verzeichnisses als `site_name`
echo "site_name: $(basename "$(pwd)")" > mkdocs.yml
# Füge das Theme `readthedocs` zur Konfigurationsdatei hinzu
echo "theme: readthedocs" >> mkdocs.yml

# Gib eine Nachricht aus, die darauf hinweist, dass das Skript abgeschlossen ist
echo "Entwicklungsumgebung wurde eingerichtet."
