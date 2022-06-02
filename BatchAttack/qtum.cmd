@Echo off
title qtum [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python qtum.py
goto loop