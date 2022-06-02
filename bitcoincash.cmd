@Echo off
title Bitcoincash [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoincash.py
goto loop