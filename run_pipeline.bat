@echo off
setlocal

set "PROJECT_DIR=%~dp0"
cd /d "%PROJECT_DIR%"

if not exist "logs" mkdir "logs"

echo ================================================== >> logs\batch_output.log
echo [%date% %time%] Starting scheduled pipeline run >> logs\batch_output.log

call ".venv\Scripts\activate"
python main.py --headless >> logs\batch_output.log 2>&1

if errorlevel 1 (
    echo [%date% %time%] Pipeline run failed >> logs\batch_output.log
    exit /b 1
)

echo [%date% %time%] Pipeline run completed successfully >> logs\batch_output.log
exit /b 0
