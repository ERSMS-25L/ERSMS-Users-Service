from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database import get_session
from src import models, schemas
from src.database import engine

app = FastAPI()
bearer_scheme = HTTPBearer()

@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)


def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    email = f"{token}@example.com"
    role = "admin" if token.endswith("admin") else "user"
    return {"email": email, "role": role}

@app.get("/me", response_model=schemas.UserResponse)
async def get_user(user=Depends(verify_token), session: AsyncSession = Depends(get_session)):
    stmt = select(models.User).where(models.User.email == user["email"])
    result = await session.execute(stmt)
    db_user = result.scalar_one_or_none()

    if not db_user:
        new_user = models.User(email=user["email"], role=user["role"])
        session.add(new_user)
        await session.commit()
        await session.refresh(new_user)
        db_user = new_user

    return {"email": db_user.email, "role": db_user.role}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/ready")
async def ready():
    return {"status": "ready"}

@app.get("/user/{user_id}")
async def get_user_by_id(user_id: int, session: AsyncSession = Depends(get_session)):
    stmt = select(models.User).where(models.User.id == user_id)
    result = await session.execute(stmt)
    user = result.scalar_one_or_none()
    if user:
        return {"id": user.id, "email": user.email, "role": user.role}
    return {"error": "User not found"}



