from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from database import Base, engine
from main_templates import templates
from routers.memos import router as memos_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Memo Board")
app.include_router(memos_router)


@app.get("/", response_class=HTMLResponse, name="home")
def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={},
    )


@app.exception_handler(404)
async def not_found(request: Request, _exception):
    return templates.TemplateResponse(
        request=request,
        name="404.html",
        context={},
        status_code=404,
    )
