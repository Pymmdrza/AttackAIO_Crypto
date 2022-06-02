@Echo off
title Bitcoin P2SH [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoin-p2sh.py
goto loop