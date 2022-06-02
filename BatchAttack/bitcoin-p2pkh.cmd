@Echo off
title Bitcoin P2PKH [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoin-p2pkh.py
goto loop