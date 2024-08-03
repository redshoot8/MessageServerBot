from typing import List
import datetime
import json

from fastapi import APIRouter, HTTPException

from database import database
from models import Message

router = APIRouter()


@router.get('/api/v1/messages/')
async def get_messages():
    try:
        cached_messages = await database.redis.get('messages')
        if cached_messages:
            return {
                'status': 'success',
                'data': json.loads(cached_messages),
                'details': 'cached'
            }

        messages = await database.db.messages.find().to_list(1000)

        for i in range(len(messages)):
            messages[i]['created_at'] = str(messages[i]['created_at'])

            if '_id' in messages[i]:
                messages[i].pop('_id', None)

        await database.redis.set('messages', json.dumps(messages, default=str))
        return {
            'status': 'success',
            'data': messages,
            'details': 'just uploaded'
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail={
            'status': 'error',
            'data': None,
            'details': exc
        })


@router.post('/api/v1/messages/')
async def create_message(message: Message):
    try:
        message_dict = message.dict()
        message_dict['created_at'] = str(datetime.datetime.now(datetime.UTC))
        result = await database.db.messages.insert_one(message_dict)
        message_dict['id'] = str(result.inserted_id)

        if '_id' in message_dict:
            message_dict.pop('_id', None)

        await database.redis.delete('messages')

        return {
            'status': 'success',
            'data': message_dict,
            'details': 'message uploaded to the server'
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail={
            'status': 'error',
            'data': None,
            'details': exc
        })
