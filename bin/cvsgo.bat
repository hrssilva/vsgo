
@echo off
for /f "delims=" %%a in ('%~dp0/dist/vsgo %1') do set COMMAND=%%a
%COMMAND%