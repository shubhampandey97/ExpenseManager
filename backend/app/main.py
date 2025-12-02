from fastapi import FastAPI
from app.api import routes, user_routes, auth_routes, analytics_routes, predict_routes
from app.db.base import Base, engine

# Create tables if not exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Manager API")

app.include_router(routes.router, prefix="/api")
app.include_router(user_routes.router, prefix="/api")
app.include_router(auth_routes.router, prefix="/api")
app.include_router(analytics_routes.router, prefix="/api")
app.include_router(predict_routes.router)


@app.get("/")
def root():
    return {"message": "Expense Manager API is running!"}
