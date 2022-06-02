@Echo off
title Bitcoin P2WPKH [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoin-p2wpkh.py
goto loop