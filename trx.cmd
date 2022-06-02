@Echo off
title trx [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python tron.py
goto loop
