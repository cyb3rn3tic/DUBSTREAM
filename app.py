import uvicorn
import os
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from urllib.parse import unquote

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MANIFEST = {
    "id": "org.dubstream.ultra",
    "version": "11.0.0",
    "name": "DUBSTREAM ⚡",
    "description": "Filmes e Séries Dublados com Player Pro",
    "resources": ["stream"],
    "types": ["movie", "series"],
    "idPrefixes": ["tt"]
}

@app.get("/manifest.json")
async def get_manifest():
    return MANIFEST

# Rota opcional para evitar o erro 404 do ícone no terminal
@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    from fastapi.responses import Response
    return Response(status_code=204)

@app.get("/player", response_class=HTMLResponse)
async def player_page(request: Request, url: str, tmdbId: str | None = None):
    return templates.TemplateResponse(
        request=request, 
        name="player.html", 
        context={"url": url, "tmdbId": tmdbId}
    )

@app.get("/stream/{type}/{id}.json")
async def get_stream(type: str, id: str, request: Request):
    id_limpo = unquote(id).replace(".json", "")
    imdb_id = id_limpo.split(':')[0]
    
    parts = id_limpo.split(':')
    s = parts[1] if len(parts) > 1 else "1"
    e = parts[2] if len(parts) > 2 else "1"

    # URL base do MegaEmbed
    if type == "movie":
        url_origem = f"https://megaembed.com/embed/{imdb_id}"
    else:
        url_origem = f"https://megaembed.com/embed/{imdb_id}/{s}/{e}"

    # Captura a URL do servidor (seja localhost ou Render/Koyeb)
    host_url = str(request.base_url).rstrip('/')
    url_final_player = f"{host_url}/player?url={url_origem}&tmdbId={imdb_id}"

    return {
        "streams": [
            {
                "name": "DUBSTREAM ⚡",
                "description": "Assistir Dublado / Legendado",
                "externalUrl": url_final_player
            }
        ]
    }

if __name__ == "__main__":
    # Configuração de porta para deploy online
    port = int(os.environ.get("PORT", 80))
    uvicorn.run(app, host="0.0.0.0", port=port)