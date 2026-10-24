set -e
pip install openpyxl
python3 tools/build_xlsx.py
python3 tools/build_ml_xlsx.py
python3 tools/build_alq_xlsx.py
python3 tools/build_cp_xlsx.py
python3 tools/build_site.py
