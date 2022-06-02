@Echo off
title trx [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python trx.py
goto loop