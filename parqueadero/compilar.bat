@echo off
echo ===================================================
echo   AUTOPARKING - Compilador de C++ (Windows g++)
echo ===================================================
echo.

cd cpp
echo [1/3] Compilando autoparking.exe...
g++ main.cpp generador.cpp parqueadero.cpp socket_cliente.cpp -o autoparking.exe -lws2_32
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Error al compilar autoparking.exe
    pause
    exit /b %errorlevel%
)
echo [OK] autoparking.exe compilado con exito.
echo.
:: compilador de la libreria ddl
echo [2/3] Compilando libreria.dll...
g++ -shared -o libreria.dll libreria.cpp parqueadero.cpp -lws2_32
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Error al compilar libreria.dll
    pause
    exit /b %errorlevel%
)
echo [OK] libreria.dll compilada con exito.
echo.