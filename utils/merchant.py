import asyncio

from cloudipsp import Api, Checkout, Order
from cloudipsp.configuration import __protocol__
from cloudipsp.helpers import is_approved


class Merchant:

    def __init__(self, merchant_id: str, secret_key: str):
        self.api = Api(merchant_id=merchant_id, secret_key=secret_key)
        self.checkout = Checkout(api=self.api)
        self.order = Order(api=self.api)
        self.loop = asyncio.get_event_loop()

    async def run(self, func, *args):
        return await self.loop.run_in_executor(None, func, *args)

    async def get_invoice_url(self, order_id: str, price: int, bot_url: str = ''):
        resp = await self.run(
            self.checkout.url,
            {
                'currency': 'UAH',
                'order_desc': 'Пополнение баланса',
                'amount': price * 100,
                'order_id': order_id,
                'response_url': bot_url,
            }
        )
        return resp['checkout_url']

    async def _check_payment(self, order_id: str):
        resp = await self.run(
            self.order.status,
            {
                'order_id': order_id,
            }
        )

        return is_approved(resp, self.api.secret_key, __protocol__)

    async def check_payment(self, order_id: str):
        try:
            return await self._check_payment(order_id)
        except:
            return False
