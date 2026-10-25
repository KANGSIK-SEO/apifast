from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session

from database import get_db
from main_templates import templates
from services import memo_service


router = APIRouter(prefix="/memos", tags=["memos"])


@router.get("/", response_class=HTMLResponse, name="memo_list")
def memo_list(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse(
        request=request,
        name="memos/list.html",
        context={"memos": memo_service.list_memos(db)},
    )


@router.get("/new", response_class=HTMLResponse, name="memo_create_form")
def create_form(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={"memo": None, "action": request.url_for("memo_create")},
    )


@router.post("/", name="memo_create")
def create_memo(
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    memo_service.create_memo(db, title, content)
    return RedirectResponse(url="/memos/", status_code=303)


@router.get("/{memo_id}", response_class=HTMLResponse, name="memo_detail")
def memo_detail(request: Request, memo_id: int, db: Session = Depends(get_db)):
    memo = memo_service.get_memo(db, memo_id)
    return templates.TemplateResponse(
        request=request,
        name="memos/detail.html",
        context={"memo": memo},
    )


@router.get("/{memo_id}/edit", response_class=HTMLResponse, name="memo_edit_form")
def edit_form(request: Request, memo_id: int, db: Session = Depends(get_db)):
    memo = memo_service.get_memo(db, memo_id)
    return templates.TemplateResponse(
        request=request,
        name="memos/form.html",
        context={"memo": memo, "action": request.url_for("memo_update", memo_id=memo.id)},
    )


@router.post("/{memo_id}/edit", name="memo_update")
def update_memo(
    memo_id: int,
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
):
    memo_service.update_memo(db, memo_id, title, content)
    return RedirectResponse(url=f"/memos/{memo_id}", status_code=303)


@router.post("/{memo_id}/delete", name="memo_delete")
def delete_memo(memo_id: int, db: Session = Depends(get_db)):
    memo_service.delete_memo(db, memo_id)
    return RedirectResponse(url="/memos/", status_code=303)
