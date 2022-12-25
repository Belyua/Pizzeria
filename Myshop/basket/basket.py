from home.models import Product
from decimal import Decimal
import requests


TELEGRAM_TOKEN = '5900059723:AAE6xTyuzZNrNPxY83oY0TiPwJy5VKYs8Vc'
TELEGRAM_CHAT_ID = '-1001812590972'
msg = 'hui'
URL = (f'https://api.telegram.org/'
       f'bot{TELEGRAM_TOKEN}/'
       f'sendMessage?'
       f'chat_id={TELEGRAM_CHAT_ID}'
       f'&text=')


class Basket:

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product, qty):
        product_id = str(product.id)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        else:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}
        self.save()

    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item

    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())

    def update(self, product, qty):
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty
        self.save()

    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())

    def delete(self, product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            print(product_id)
            self.save()

    def save(self):
        self.session.modified = True

    def send_telegram_message(self):
        product = Product()

        result_url = (URL + str(self.get_total_price()) + '$ new order!:\n '
                            + str(self.__len__()) + ' items\n'
                            + str(self.basket))
        requests.get(url=result_url)

