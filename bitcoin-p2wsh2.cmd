@Echo off
title Bitcoin P2WSH in P2SH [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoin-p2wsh2.py
goto loop