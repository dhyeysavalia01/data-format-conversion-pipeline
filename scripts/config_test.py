import os
from pathlib import Path

from dotenv import load_dotenv


BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

project_name = os.getenv("PROJECT_NAME")
environment = os.getenv("ENVIRONMENT")
source_file = os.getenv("SOURCE_FILE")
output_format = os.getenv("OUTPUT_FORMAT")

print("Project:", project_name)
print("Environment:", environment)
print("Source file:", source_file)
print("Output format:", output_format)