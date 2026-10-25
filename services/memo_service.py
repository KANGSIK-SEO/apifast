from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import Memo
from repositories import memo_repository


def list_memos(db: Session) -> list[Memo]:
    return memo_repository.get_all(db)


def get_memo(db: Session, memo_id: int) -> Memo:
    memo = memo_repository.get_by_id(db, memo_id)
    if memo is None:
        raise HTTPException(status_code=404, detail="요청한 메모를 찾을 수 없습니다.")
    return memo


def create_memo(db: Session, title: str, content: str) -> Memo:
    return memo_repository.create(db, title.strip(), content.strip())


def update_memo(db: Session, memo_id: int, title: str, content: str) -> Memo:
    memo = get_memo(db, memo_id)
    return memo_repository.update(db, memo, title.strip(), content.strip())


def delete_memo(db: Session, memo_id: int) -> None:
    memo = get_memo(db, memo_id)
    memo_repository.delete(db, memo)
