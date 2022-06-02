@Echo off
title DigiByte [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python digibyte.py
goto loop