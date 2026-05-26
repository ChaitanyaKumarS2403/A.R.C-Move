@echo off
SETLOCAL Enabledelayedexpansion

:: Switch to the folder where this batch file lives
cd /d "%~dp0"

echo ===================================================
echo             Initializing A.R.C
echo ===================================================

:: Ensure Python is available globally to create the venv
where python >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR] Python is not installed or not in your system PATH.
    pause
    exit /b
)

:: 1. Handle Virtual Environment Creation & Activation
if not exist "venv\" (
    echo [INFO] Creating virtual environment...
    python -m venv venv
    if !ERRORLEVEL! neq 0 (
        echo [ERROR] Failed to create virtual environment.
        pause
        exit /b
    )
)

echo [INFO] Activating virtual environment...
call .\venv\Scripts\activate.bat

:: 2. Check and Install Dependencies Inside the venv
echo [INFO] Checking dependencies...
set "MISSING_DEP=0"

for /f "tokens=1 delims==<>" %%A in (requirements.txt) do (
    set "pkg=%%A"
    set "pkg=!pkg: =!"
    
    if not "!pkg!"=="" if not "!pkg:~0,1!"=="#" (
        pip show !pkg! >nul 2>nul
        if !ERRORLEVEL! neq 0 (
            echo [WARN] Missing dependency detected: !pkg!
            set "MISSING_DEP=1"
            goto :install_deps
        )
    )
)

:install_deps
if "%MISSING_DEP%"=="1" (
    echo [INFO] Installing dependencies from requirements.txt...
    pip install -r requirements.txt
    
    if !ERRORLEVEL! neq 0 (
        echo [ERROR] Failed to install requirements.
        pause
        exit /b
    )
) else (
    echo [INFO] All dependencies are already met. Preparing to launch...
)

echo ===================================================
echo            A.R.C Initialized...
echo ===================================================

cls

:: 3. Run the application using the venv's Python interpreter
:: Note: Using 'pythonw' inside the venv directly avoids needing the 'start' command 
:: if you want to keep it fully contained, but 'start' works fine too.
start venv\Scripts\pythonw.exe ARC.py

echo ---------------------------------------------------
echo [INFO] Script finished execution.