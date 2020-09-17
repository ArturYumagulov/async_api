from aiohttp import web
import aiohttp_jinja2
import jinja2
import asyncio

from db import db, Ticket

app = web.Application()

aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
ticket = await Ticket.create(number='123', date='12-09-2020')

@aiohttp_jinja2.template("index.html")
async def index(request):
    return


async def add(request):
    print(request.query)
    return web.Response(text="Запрос получен")

app.add_routes([web.get('/', index), web.get('/add', add)])

if __name__ == '__main__':
    web.run_app(app)