@Echo off
title Bitcoin P2WSH [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoin-p2wsh.py
goto loop