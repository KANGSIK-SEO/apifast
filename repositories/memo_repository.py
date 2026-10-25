from sqlalchemy import select
from sqlalchemy.orm import Session

from models import Memo


def get_all(db: Session) -> list[Memo]:
    statement = select(Memo).order_by(Memo.created_at.desc(), Memo.id.desc())
    return list(db.scalars(statement))


def get_by_id(db: Session, memo_id: int) -> Memo | None:
    return db.get(Memo, memo_id)


def create(db: Session, title: str, content: str) -> Memo:
    memo = Memo(title=title, content=content)
    db.add(memo)
    db.commit()
    db.refresh(memo)
    return memo


def update(db: Session, memo: Memo, title: str, content: str) -> Memo:
    memo.title = title
    memo.content = content
    db.commit()
    db.refresh(memo)
    return memo


def delete(db: Session, memo: Memo) -> None:
    db.delete(memo)
    db.commit()
