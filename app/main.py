from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .products.router import products_router
from .providers.router import providers_router

app = FastAPI(
        title="Gestión de Inventario",
        description="Un servicio web para gestionar una tienda online",
        version="0.0.01",
        contact={
            "name": "Gustavo de los Santos",
            "email": "gusleo94@gmail.com",
            },
        license_info={
            "name": "MIT",
            }
        )


origins = [
    "http://localhost",
    "http://localhost:8000",
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(products_router.router)
app.include_router(providers_router.router)
