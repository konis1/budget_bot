
from unittest.mock import AsyncMock, MagicMock

import pytest
from telegram import Chat, Update

from budget_bot.bot import start


@pytest.mark.asyncio
async def test_start():
    # Create a mock update
    mock_update = MagicMock(spec=Update)
    mock_update.effective_chat = MagicMock(spec=Chat)
    mock_update.effective_chat.id = 12345  # Example chat ID

    # Create a mock context
    mock_context = MagicMock()
    mock_context.bot.send_message = AsyncMock()

    # Call the function
    await start(mock_update, mock_context)

    # Assert the message was sent
    mock_context.bot.send_message.assert_awaited_once_with(
        chat_id=12345, text="i'm a bot please talk to me"
    )
