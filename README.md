# FastAPI 메모 게시판

Python 3.10 이상과 FastAPI, SQLAlchemy, SQLite를 사용한 서버 렌더링 메모 게시판입니다. 메모 등록, 목록, 상세 조회, 수정, 삭제 기능을 제공합니다.

## 실행 방법

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Windows에서는 가상환경 활성화 명령을 `.venv\Scripts\activate`로 실행하세요. 서버를 실행한 뒤 [http://127.0.0.1:8000](http://127.0.0.1:8000)에 접속할 수 있습니다.

## 사용 방법

- 홈 화면에서 메모 목록을 열거나 새 메모를 등록할 수 있습니다.
- 목록에서 제목을 누르면 상세 화면으로 이동하며, 상세 화면에서 수정하거나 삭제할 수 있습니다.
- 등록·수정·삭제는 POST 후 303 리다이렉트로 처리합니다.
- SQLite 데이터베이스 파일 `memos.db`는 프로젝트 루트에 자동 생성됩니다.

## 프로젝트 구조

```text
.
├── database.py
├── main.py
├── models/
├── repositories/
├── routers/
├── services/
└── templates/
```
