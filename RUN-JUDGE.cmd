@echo off
setlocal
cd /d "%~dp0"
echo Wildline RC1 - offline synthetic continuity demonstration.
echo Historical and genuine Bee evidence are not included.
python -X utf8 -I -B "%~dp0demo\h5_sidecar.py" %*
exit /b %errorlevel%
