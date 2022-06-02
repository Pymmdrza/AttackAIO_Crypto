@Echo off
title zCash [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python zcash.py
goto loop