@echo off
echo ===================================================
echo   AUTOPARKING - Compilador de C++ (Windows g++)
echo ===================================================
echo.

cd cpp
echo [1/3] Compilando autoparking.exe...
g++ main.cpp generador.cpp parqueadero.cpp socket_cliente.cpp -o autoparking.exe -lws2_32