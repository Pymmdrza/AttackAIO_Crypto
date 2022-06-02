@Echo off
title Dash [MMDRZA.CoM]
Pushd "%~dp0"
:loop
python dash.py
goto loop