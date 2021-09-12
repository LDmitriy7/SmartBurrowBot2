from __future__ import annotations

import json
from typing import TypeVar, Generic

import mongoengine as me
from aiogram import Dispatcher
from aiogram.dispatcher import FSMContext

T = TypeVar('T')


class StorageProxy(Generic[T]):

    def __init__(self, model: type[T]):
        self.model = model
        self.field_name = model.__name__
        self._object = None

    @staticmethod
    def get_state() -> FSMContext:
        return Dispatcher.get_current().current_state()

    async def get_storage_data(self) -> dict:
        return await self.get_state().get_data()

    async def get_object(self) -> T:
        if self._object is None:
            storage_data = await self.get_storage_data()
            self._object = self.model(**storage_data.get(self.field_name, {}))
        return self._object

    async def update_storage_data(self):
        _object: me.Document = await self.get_object()
        object_data: dict = json.loads(_object.to_json())
        await self.get_state().update_data({self.field_name: object_data})

    async def __aenter__(self) -> T:
        return await self.get_object()

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            await self.update_storage_data()
