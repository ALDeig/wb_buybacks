from datetime import date, timedelta

import sqlalchemy as sa
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError, DBAPIError

from tgbot.models.tables import User


async def add_user(session: AsyncSession, user_id: int, subscribe: int) -> bool:
    """
    Добавляет нового пользователя
    :param session:
    :param user_id:
    :param subscribe: Количество дней, на сколько активируется подписка у человека
    :return:
    """
    user = User(id=user_id, subscribe=date.today() + timedelta(days=subscribe))
    session.add(user)
    try:
        await session.commit()
        return True
    except (IntegrityError, DBAPIError):
        await session.rollback()
        return False
