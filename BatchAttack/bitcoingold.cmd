@Echo off
title Bitcoin gold [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python bitcoingold.py
goto loop