import multiprocessing
from datetime import datetime


class WarehouseManager:
    def __init__(self):
        self.data = multiprocessing.Manager().dict()  # Словарь для хранения информации о товарах

    def process_request(self, request):
        product, action, quantity = request
        timestamp = datetime.now()
        if action == "receipt":
            self.data[product] = self.data.get(product, 0) + quantity
            print(f"{timestamp}: Received {quantity} units of {product}.")
        elif action == "shipment":
            if self.data.get(product, 0) >= quantity:
                self.data[product] -= quantity
                print(f"{timestamp}: Shipped {quantity} units of {product}.")
            else:
                print(f"{timestamp}: Insufficient quantity of {product} for shipment.")

    def run(self, storage_requests):
        processes = []
        for request in storage_requests:
            p = multiprocessing.Process(target=self.process_request, args=(request,))
            processes.append(p)
            p.start()

        for p in processes:
            p.join()

        print("All workers have finished.")

        # Вывод окончательных данных после завершения всех процессов
        print("Final data:", self.data)


# Пример использования:
if __name__ == "__main__":
    warehouse = WarehouseManager()
    requests = [
        ("apple", "receipt", 100),
        ("banana", "receipt", 50),
        ("apple", "shipment", 30),
        ("banana", "shipment", 70),
        ("orange", "receipt", 80),
        ("orange", "shipment", 100)
    ]
    warehouse.run(requests)
