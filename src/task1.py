import queue
import time
import random

# Створення черги заявок
requests_queue = queue.Queue()

# Генерація нової заявки з унікальним ідентифікатором
def generate_request():
    request_id = random.randint(1, 9999)  # Генерація ID
    request_data = f"Request-{request_id}"
    requests_queue.put(request_data)
    print(f"Заявка {request_data} додана до черги.")

# Обробка заявки
def process_request():   
    if not requests_queue.empty():
        data = requests_queue.get()
        print(f"Обробляється заявка {data}...")
        time.sleep(random.uniform(0.5, 2.0))  # Імітація часу обробки
        print(f"Заявка {data} оброблена.")
    else:
        print("Черга пуста. Очікування нових заявок...")
        time.sleep(1)  # Очікування перед перевіркою черги

while True:
    time.sleep(random.uniform(1, 3))  # Інтервал між заявками
    generate_request()
    process_request()