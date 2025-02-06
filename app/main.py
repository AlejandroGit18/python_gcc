from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import (
    auth,
    consulta_saldo_cuenta,
    usuarios,
    roles,
    campanas,
    campanas_usuarios,
    gestiones,
    encryption,
    modulos,
    modulos_usuarios,
    drop,
    tipologias,
    consulta_saldos,
    actualiza_saldos,
    tipo_descuento,
    carga_tipologias,
    consulta_tipologias,
    registrar_pago,
    reporte_pagos,
    reporte_promesas,
    consulta_saldo_cuenta,
    ingresa_tipologias,
    ingresa_promesa,
    update_datos_contacto,
    reporte_tipologias,
    consulta_usuarios_carga_gestiones,
    consulta_historico_pagos,
)

app = FastAPI()

# Configuración de CORS
origins = [
    "http://localhost",        # Para pruebas locales
    "http://localhost:3000",   # Para un frontend local
    "http://127.0.0.1:5500",   # Otra dirección local
    "http://127.0.0.1:3000",   # Otra dirección local
    "https://GCC.com",  # Dominios específicos permitidos
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir estos orígenes
    allow_credentials=True,  # Permitir cookies/credenciales
    allow_methods=["*"],     # Permitir todos los métodos HTTP
    allow_headers=["*"],     # Permitir todos los encabezados
)

# Registrar rutas existentes
app.include_router(auth.router, prefix="/api", tags=["authentication"])
app.include_router(usuarios.router, prefix="/api", tags=["usuarios"])
app.include_router(roles.router, prefix="/api", tags=["roles"])
app.include_router(campanas.router, prefix="/api", tags=["campanas"])
app.include_router(campanas_usuarios.router, prefix="/api", tags=["campanas_usuarios"])
app.include_router(gestiones.router, prefix="/api", tags=["gestiones"])
app.include_router(encryption.router, prefix="/api", tags=["encriptar"])  # Registrar rutas de encriptación

# Registrar nuevas rutas
app.include_router(modulos.router, prefix="/api", tags=["modulos"])
app.include_router(modulos_usuarios.router, prefix="/api", tags=["modulos_usuarios"])
app.include_router(drop.router, prefix="/api", tags=["drops"])
app.include_router(tipologias.router, prefix="/api", tags=["tipologias"])
app.include_router(consulta_saldos.router, prefix="/api", tags=["consulta_saldos"])
app.include_router(actualiza_saldos.router, prefix="/api", tags=["actualiza_saldos"])
app.include_router(tipo_descuento.router, prefix="/api", tags=["tipo_descuento"])
app.include_router(carga_tipologias.router, prefix="/api", tags=["carga_tipologias"])
app.include_router(consulta_tipologias.router, prefix="/api", tags=["consulta_tipologias"])
app.include_router(registrar_pago.router, prefix="/api", tags=["registrar_pago"])

app.include_router(reporte_pagos.router, prefix="/api", tags=["reporte_pagos"])
app.include_router(reporte_promesas.router, prefix="/api", tags=["reporte_promesas"])
app.include_router(consulta_saldo_cuenta.router, prefix="/api", tags=["consulta_saldo_cuenta"])
app.include_router(ingresa_tipologias.router, prefix="/api", tags=["ingresa_tipologias"])
app.include_router(ingresa_promesa.router, prefix="/api", tags=["ingresa_promesa"])
app.include_router(update_datos_contacto.router, prefix="/api", tags=["update_datos_contacto"])
app.include_router(reporte_tipologias.router, prefix="/api", tags=["reporte_tipologias"])
app.include_router(consulta_usuarios_carga_gestiones.router, prefix="/api", tags=["consulta_usuarios_carga_gestiones"])
app.include_router(consulta_historico_pagos.router, prefix="/api", tags=["consulta_historico_pagos"])


@app.get("/")
def root():
    return {"message": "Welcome to FastAPI"}
