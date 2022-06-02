@Echo off
title LTC [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python litecoin.py
goto loop