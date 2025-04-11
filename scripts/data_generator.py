import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta


fake = Faker()
Faker.seed(42)
random.seed(42)

# 1. Клиенты
def generate_clients(n=100):
    clients = []
    for i in range (1, n+1):
        clients.append({
            'client_id':f'C{i:04}',
            'client_name': fake.company(),
            'contact_name':fake.name(),
            'region':fake.country()
        })
    return pd.DataFrame(clients)

# 2. Товары
categories = ['Серверы', 'Маршрутизаторы', 'Ноутбуки', 'Мониторы', 'Сетевое оборудование']
def generate_products(n=50):
    products = []
    for i in range(1, n+1):
        category = random.choice(categories)
        price = round(random.uniform(100, 5000), 2)
        products.append({
            'product_id': f'P{i:03}',
            'product_name': f'{category} - {fake.word().capitalize()}',
            'category' : category,
            'price' : price
        })
    return pd.DataFrame(products)

# 3. Заказы
def generate_orders(clients, products, n=1000):
    orders = []
    order_lines = []
    for i in range(1, n+1):
        order_id = f'O{i:05}'
        client_id = random.choice(clients['client_id'].values)
        order_date =  fake.date_between(start_date='-1y', end_date='today')
        num_items = random.randint(1, 5)
        selected_products = random.choices(products.to_dict('records'), k=num_items)
        for product in selected_products:
            quantity = random.randint(1, 10)
            orders.append({
                'order_id' : order_id,
                'client_id' : client_id,
                'product_id' : product['product_id'],
                'order_date' : order_date,
                'quantity' : quantity,
                'unit_price' : product['price']
            })
    return pd.DataFrame(orders)

# 4. Оплаты
def generate_payments(orders):
    payments = []
    grouped = orders.groupby('order_id').first().reset_index()
    for _, row in grouped.iterrows():
        pay_date = row['order_date'] + timedelta(days=random.randint(0, 10))
        payments.append({
            'payment_id' : f'PAY{row.order_id[1:]}',
            'order_id' : row.order_id,
            'payment_date': pay_date,
            'amount': (orders[orders.order_id == row.order_id]['quantity'] * orders[orders.order_id == row.order_id]['unit_price']).round(2)
            #'amount': float(orders[orders.order_id == row.order_id]['quantity'] * orders[orders.order_id == row.order_id]['unit_price']).round(2)
        })
    return pd.DataFrame(payments)

# 5. Поставки
def generate_shipments(orders):
    shipments = []
    grouped = orders.groupby('order_id').first().reset_index()
    for _, row in grouped.iterrows():
        ship_date = row['order_date'] + timedelta(days=random.randint(1, 7))
        shipments.append({
            'shipment_id' : f'SH{row.order_id[1:]}',
            'order_id' : row.order_id,
            'shipment_date' : ship_date,
            'shipment_status' : random.choice(['Отгружено', 'В пути', 'Доставлено', 'Отменено'])
        })
    return pd.DataFrame(shipments)


# Generate datas
clients = generate_clients(100)
products = generate_products(50)
orders = generate_orders(clients, products, 1000)
payments = generate_payments(orders)
shipments = generate_shipments(orders)

# saving to CSV
clients.to_csv('clients.csv', index=False)
products.to_csv('products.csv', index=False)
orders.to_csv('orders.csv', index=False)
payments.to_csv('payments.csv', index=False)
shipments.to_csv('shipments.csv', index=False)

print("All data have generated and saved to CSV!")