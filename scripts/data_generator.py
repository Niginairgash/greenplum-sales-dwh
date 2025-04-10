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