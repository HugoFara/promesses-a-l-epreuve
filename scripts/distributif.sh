#!/usr/bin/env bash
# Lance distributif.py avec l'OpenFisca-France du clone local (../openfisca-france, à côté du projet).
# Autres emplacements : OPENFISCA_PY=/chemin/python OPENFISCA_FRANCE_DIR=/chemin/clone bash distributif.sh
set -euo pipefail
ICI="$(cd "$(dirname "$0")" && pwd)"
CLONE="${OPENFISCA_FRANCE_DIR:-$ICI/../../openfisca-france}"
PY="${OPENFISCA_PY:-$CLONE/.venv/bin/python}"
if [ ! -x "$PY" ]; then echo "OpenFisca introuvable ($PY) : étape distributive sautée" >&2; exit 0; fi
# PYTHONPATH : filet de sécurité si l'installation éditable du venv pointe ailleurs que le clone
cd "$ICI/../data" && PYTHONPATH="$CLONE${PYTHONPATH:+:$PYTHONPATH}" "$PY" "$ICI/distributif.py"
