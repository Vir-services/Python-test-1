@echo off&chcp 936 >nul 2>nul&setlocal EnableDelayedExpansion
:home
cls
echo=
echo     python程序转EXE  
echo=
set /p sourceprogram="请拖入源程序："
set /p despath="请输入目标文件夹："
md %despath% >nul 2>nul

choice /c 1234q /m "请输入[ 1:64normal | 2:64gui | 3:32normal | 4:32gui | Q:退出 ]:"

if %errorlevel%==1 goto :64normal
if %errorlevel%==2 goto :64gui
if %errorlevel%==3 goto :32normal
if %errorlevel%==4 goto :32gui
if %errorlevel%==5 goto :EOF


:32gui
"C:\python3.62x86\python.exe" "C:\python3.62x86\Scripts\cxfreeze" %sourceprogram%  --target-dir %despath%  --base-name=win32gui
pause
goto :home

:32normal
"C:\python3.62x86\python.exe" "C:\python3.62x86\Scripts\cxfreeze" %sourceprogram%  --target-dir %despath%
pause
goto :home

:64gui
"C:\Program Files\Python36\python.exe" "C:\Program Files\Python36\Scripts\cxfreeze" %sourceprogram%  --target-dir %despath%  --base-name=win32gui
pause
goto :home

:64normal
"C:\Program Files\Python36\python.exe" "C:\Program Files\Python36\Scripts\cxfreeze" %sourceprogram%  --target-dir %despath%
pause
goto :home
