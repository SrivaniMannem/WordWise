@echo off
title WordWise Launcher
cd /d "%~dp0"
echo =====================================
echo           WORDWISE STARTER
echo =====================================
where py >nul 2>nul
if %errorlevel%==0 goto USE_PY
where python >nul 2>nul
if %errorlevel%==0 goto USE_PYTHON
echo.
echo Python is installed perhaps, but Windows cannot find it.
echo Please install Python from https://www.python.org/downloads/
echo During installation, tick "Add python.exe to PATH".
echo Then close and reopen VS Code and double-click this file again.
echo.
pause
exit /b 1

:USE_PY
echo Checking and installing the required package...
py -m pip install -r requirements.txt
if errorlevel 1 goto INSTALL_ERROR
py app.py
goto END

:USE_PYTHON
echo Checking and installing the required package...
python -m pip install -r requirements.txt
if errorlevel 1 goto INSTALL_ERROR
python app.py
goto END

:INSTALL_ERROR
echo.
echo Could not install Flask. Check your internet connection and try again.
pause
exit /b 1

:END
pause
