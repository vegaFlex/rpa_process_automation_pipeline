@echo off
cd /d C:\Users\vega_\Documents\Playground\rpa_process_automation_pipeline

call .venv\Scripts\activate

python main.py >> logs\batch_output.log 2>&1
