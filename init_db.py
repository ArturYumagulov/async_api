from gino import Gino
import asyncio

from db import db


async def main():
    await db.set_bind('postgresql://postgres:1@localhost:5432/')
    await db.gino.create_all()
    await db.pop_bind().close()

asyncio.get_event_loop().run_until_complete(main())
