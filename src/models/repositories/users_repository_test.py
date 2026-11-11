import pytest

from .users_repository import UsersRepository


@pytest.mark.asyncio
@pytest.mark.skip(reason="Insert in DB")
async def test_insert_user():
    new_user = {"user_name": "Teste", "age": 33, "uf": "PE"}
    repo = UsersRepository()
    await repo.insert_users(new_user)
