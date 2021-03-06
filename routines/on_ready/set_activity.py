"""Set bot activity after server login."""
import discord
from routines.on_ready import OnReadyEvent
from bot import LOGGER
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from ..tables import Base
from .. import engine


class SetActivity(OnReadyEvent):
    """Set bot activity on server login."""

    def actions(self):
        @self.bot.event
        async def on_ready():
            LOGGER.info(f'{self.bot.user.name} has connected to Discord!')
            return await self.bot.change_presence(activity=discord.Activity(type=1, name="RS Queueing"))

    
            

