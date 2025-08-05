import os
import asyncpg
import asyncio
import logging

from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql://postgres:postgres@database:5432/database"
)

async def connect_to_database(max_retries=5, delay=5):
    for attempt in range(max_retries):
        try:
            pool = await asyncpg.create_pool(DATABASE_URL)
            logging.info("Connected to the database.")
            return pool
        except (ConnectionError, OSError, asyncpg.PostgresError) as exception:
            logging.error("Database connection failed, retrying...")
            logging.error(exception)
            await asyncio.sleep(delay)
    raise Exception("Could not connect to the database.")

@app.on_event("startup")
async def startup():
    app.state.db_pool = await connect_to_database()

@app.on_event("shutdown")
async def shutdown():
    await app.state.db_pool.close()

@app.get("/")
async def root():
    return "Server is up and running."
