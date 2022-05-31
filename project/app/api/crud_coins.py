from app.models.tortoise import Coin
from app.models.pydantic import CoinBaseResponseSchema, CoinBaseSchema


async def get_all() -> list | None:
    coins = await Coin.all().values()
    return coins

async def post(payload: CoinBaseSchema) -> CoinBaseResponseSchema:
    coin = Coin(name_id=payload.name_id)
    await coin.save()
    return coin