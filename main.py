from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# 🟨 Lista de licencias activas (AQUÍ AGREGAS MÁS)
LICENCIAS = [
    {
        "correo": "fullskipper8@gmail.com",  # ✅ Tu correo
        "id_usuario": 173888022              # ✅ Tu ID de IQ Option
    },
    # 🟡 Para agregar más licencias, copia este bloque:
    # {
    #     "correo": "cliente2@email.com",
    #     "id_usuario": 112233445
    # },
]

class SolicitudLicencia(BaseModel):
    correo: str
    id_usuario: int

@app.post("/validar")
def validar_licencia(solicitud: SolicitudLicencia):
    for licencia in LICENCIAS:
        if (
            licencia["correo"].strip().lower() == solicitud.correo.strip().lower()
            and licencia["id_usuario"] == solicitud.id_usuario
        ):
            return {"estado": "valido ✅"}

    raise HTTPException(status_code=403, detail="❌ Licencia no válida. Contacte a soporte.")
