@echo off
set b=%cd%
cmd /k "cd /d %b% && .\Scripts\activate /cmd && python run.py /cmd"