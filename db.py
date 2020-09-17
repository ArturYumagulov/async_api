from gino import Gino
import asyncio

db = Gino()


class Ticket(db.Model):
    __tablename__ = 'tickets'

    number = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.String())
    time = db.Column(db.String())
    #
    # def __init__(self, number, date, time):
    #     self.number = number
    #     self.date = date
    #     self.time = time


async def main():
    await db.set_bind('postgresql://postgres:1@localhost:5432/')
    # await db.gino.create_all()
    ticket = Ticket(number='123', date='2020-09-17', time="19:07")
    await db.pop_bind().close()


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())