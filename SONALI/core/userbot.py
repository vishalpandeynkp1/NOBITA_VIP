from typing import Callable, Optional
import pyrogram
from pyrogram import Client
import config
from ..logging import LOGGER

assistants = []
assistantids = []
clients = []


class Userbot(Client):
    def __init__(self):
        self.one = Client(
            "RAUSHANAss1",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING1),
        )

        self.two = Client(
            "RAUSHANAss2",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING2),
        )

        self.three = Client(
            "RAUSHANAss3",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING3),
        )

        self.four = Client(
            "RAUSHANAss4",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING4),
        )

        self.five = Client(
            "RAUSHANAss5",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            session_string=str(config.STRING5),
        )

    async def start(self):
        LOGGER(__name__).info(f"Starting Assistant Clients")

        # Function to join a list of channels safely
        async def join_channels(client, channels):
            for channel in channels:
                try:
                    await client.join_chat(channel)
                    LOGGER(__name__).info(f"Joined {channel} successfully.")
                except Exception as e:
                    LOGGER(__name__).warning(f"Failed to join {channel}: {e}")

        if config.STRING1:
            await self.one.start()
            await join_channels(self.one, [
                "ll_NOBITA_BOT_DEVLOPER_ll",
                "NOBITA_BOT_MAKER_STATUS",
                "NOBITA_SUPPORT",
                "NOBITA_ALL_BOT"
            ])
            assistants.append(1)
            clients.append(self.one)
            try:
                await self.one.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as e:
                LOGGER(__name__).info(
                    f"Assistant Account 1 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! Error: {e}"
                )
            get_me = await self.one.get_me()
            self.one.username = get_me.username
            self.one.id = get_me.id
            self.one.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.one.name = get_me.first_name + " " + get_me.last_name
            else:
                self.one.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Started as {self.one.name}")

        if config.STRING2:
            await self.two.start()
            await join_channels(self.two, [
                "ll_NOBITA_BOT_DEVLOPER_ll",
                "NOBITA_SUPPORT",
                "NOBITA_ALL_BOT",
                "NOBITA_BOT_MAKER_STATUS"
            ])
            assistants.append(2)
            clients.append(self.two)
            try:
                await self.two.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account 2 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! Error: {e}"
                )

            get_me = await self.two.get_me()
            self.two.username = get_me.username
            self.two.id = get_me.id
            self.two.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.two.name = get_me.first_name + " " + get_me.last_name
            else:
                self.two.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Two Started as {self.two.name}")

        if config.STRING3:
            await self.three.start()
            await join_channels(self.three, [
                "ll_NOBITA_BOT_DEVLOPER_ll",
                "NOBITA_BOT_MAKER_STATUS",
                "NOBITA_SUPPORT",
                "NOBITA_ALL_BOT"
            ])
            assistants.append(3)
            clients.append(self.three)
            try:
                await self.three.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account 3 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! Error: {e}"
                )

            get_me = await self.three.get_me()
            self.three.username = get_me.username
            self.three.id = get_me.id
            self.three.mention = get_me.mention
            assistantids.append(get_me.id)
            if get_me.last_name:
                self.three.name = get_me.first_name + " " + get_me.last_name
            else:
                self.three.name = get_me.first_name
            LOGGER(__name__).info(f"Assistant Three Started as {self.three.name}")

        if config.STRING4:
            await self.four.start()
            await join_channels(self.four, [
                "NOBITA_ALL_BOT",
                "ll_NOBITA_BOT_DEVLOPER_ll",
                "NOBITA_SUPPORT",
                "NOBITA_BOT_MAKER_STATUS"
            ])
            assistants.append(4)
            clients.append(self.four)
            try:
                await self.four.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account 4 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! Error: {e}"
                )

            get_me = await self.four.get_me()
            self.four.username = get_me.username
            self.four.id = get_me.id
            self.four.mention = get_me.mention
            assistantids.append(get_me.id)

        if config.STRING5:
            await self.five.start()
            await join_channels(self.five, [
                "NOBITA_BOT_MAKER_STATUS",
                "NOBITA_SUPPORT",
                "NOBITA_ALL_BOT",
                "ll_NOBITA_BOT_DEVLOPER_ll"
            ])
            assistants.append(5)
            clients.append(self.five)
            try:
                await self.five.send_message(config.LOG_GROUP_ID, "Assistant Started")
            except Exception as e:
                LOGGER(__name__).error(
                    f"Assistant Account 5 has failed to access the log Group. Make sure that you have added your assistant to your log group and promoted as admin! Error: {e}"
                )

            get_me = await self.five.get_me()
            self.five.username = get_me.username
            self.five.id = get_me.id
            self.five.mention = get_me.mention
            assistantids.append(get_me.id)


def on_cmd(
    filters: Optional[pyrogram.filters.Filter] = None, group: int = 0
) -> Callable:
    def decorator(func: Callable) -> Callable:
        for client in clients:
            client.add_handler(pyrogram.handlers.MessageHandler(func, filters), group)
        return func

    return decorator
