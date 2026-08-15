"""
create_zip.py - Packages the entire PlantaSanitus codebase into a downloadable ZIP archive.
"""

import os
import zipfile
import shutil

PROJECT_DIR = os.path.dirname(__file__)
ZIP_FILENAME = "PlantaSanitus_Plant_Disease_Detection.zip"
ZIP_OUTPUT_PATH = os.path.join(PROJECT_DIR, ZIP_FILENAME)

# Artifacts output path
ARTIFACTS_DIR = r"C:\Users\rifan\.gemini\antigravity\brain\eeede41f-d881-4a6d-9cfe-c14eeeb99950"
ARTIFACT_ZIP_PATH = os.path.join(ARTIFACTS_DIR, ZIP_FILENAME)

EXCLUDE_DIRS = {'__pycache__', '.git', '.idea', '.vscode', 'venv'}
EXCLUDE_EXTENSIONS = {'.pyc', '.pyo', '.db'}

def build_zip():
    print(f"[INFO] Creating zip archive: {ZIP_OUTPUT_PATH}")
    with zipfile.ZipFile(ZIP_OUTPUT_PATH, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(PROJECT_DIR):
            # Exclude unwanted directories
            dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
            
            for file in files:
                if file == ZIP_FILENAME or file.endswith('.db') or file.endswith('.pyc'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, PROJECT_DIR)
                zipf.write(file_path, arcname)
                print(f"   Added: {arcname}")

    if os.path.exists(ARTIFACTS_DIR):
        shutil.copy(ZIP_OUTPUT_PATH, ARTIFACT_ZIP_PATH)
        print(f"[SUCCESS] Copied zip to artifacts: {ARTIFACT_ZIP_PATH}")

if __name__ == "__main__":
    build_zip()
