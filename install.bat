@echo off
:: Zuping Installation
pip install -r requirements.txt
if %errorlevel% neq 0 (
    echo Error installing dependencies. Please check if pip is properly configured.
    exit /b %errorlevel%
)
echo Dependencies installed successfully.
python setup.py install
if %errorlevel% neq 0 (
    echo Error installing Zuping. Please check if Python is properly configured.
    exit /b %errorlevel%
)
echo Zuping installed successfully!
