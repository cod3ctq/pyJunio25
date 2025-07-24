from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI(title="API Gateway")

CUENTAS_SERVICE_URL = "http://localhost:8001/cuentas"

@app.api_route("/cuentas/{path:path}", methods=["GET", "POST", "DELETE", "PUT", "PATCH"])
async def gateway_cuentas(request: Request, path: str):
    url = f"{CUENTAS_SERVICE_URL}/{path}"
    method = request.method
    headers = dict(request.headers)
    body = await request.body()

    async with httpx.AsyncClient() as client:
        try:
            response = await client.request(method, url, headers=headers, content=body)
            return response.json()
        except httpx.RequestError as e:
            raise HTTPException(status_code=500, detail=f"Error en el gateway: {str(e)}")
