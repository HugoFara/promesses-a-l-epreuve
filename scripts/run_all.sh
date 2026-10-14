#!/usr/bin/env bash
# Valide data/raw/, régénère les CSV publiés et dérivés, puis lance les contrôles.
set -euo pipefail
cd "$(dirname "$0")/../data"
python3 ../scripts/build.py
python3 ../scripts/calc.py > /dev/null
python3 ../scripts/moteur.py > /dev/null
python3 ../scripts/sensibilite.py > /dev/null
python3 ../scripts/validation.py > /dev/null
[ -f projection_parametres.csv ] && python3 ../scripts/projection.py > /dev/null
bash ../scripts/distributif.sh > /dev/null
python3 ../scripts/build_web.py > /dev/null
python3 ../scripts/check_regression.py
STRICT_REFERENCE="${STRICT_REFERENCE:-1}" python3 ../scripts/garde_fous.py
