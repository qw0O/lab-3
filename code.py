class Task:
    """Класс для объекта задачи"""
    def __init__(self, task_id, description, priority):
        self.task_id = task_id
        self.description = description
        self.priority = priority

    def __str__(self):
        return f"[ID: {self.task_id} | Приоритет: {self.priority} | Описание: {self.description}]"


class TaskQueue:
    """Класс очереди задач"""
    def __init__(self):
        self._queue = deque()

    def isEmpty(self):
        """Проверка: пуста ли очередь"""
        return len(self._queue) == 0

    def enqueue(self, task):
        """Добавляет задачу в конец очереди"""
        if not isinstance(task, Task):
            raise TypeError("В очередь можно добавлять только объекты класса Task")
        self._queue.append(task)
        print(f"Добавлено: {task}")

    def dequeue(self):
        """Удаляет и возвращает первую задачу из очереди"""
        if self.isEmpty():
            print("Ошибка: Очередь пуста, нечего удалять.")
            return None
        
        removed_task = self._queue.popleft()
        return removed_task

    def front(self):
        """Возвращает первую задачу без её удаления"""
        if self.isEmpty():
            print("Очередь пуста.")
            return None
        return self._queue[0]

    #   ВАРИАТИВНАЯ ЧАСТЬ
    def has_task_by_id(self, search_id):
        """Проверка: есть ли задача с заданным id в очереди"""
        for task in self._queue:
            if task.task_id == search_id:
                return True
        return False


if __name__ == "__main__":
    
    queue = TaskQueue()

    #   Пример задач
    t1 = Task(task_id=1, description="Проконсультировать клиента", priority="Высокий")
    t2 = Task(task_id=2, description="Внести в учет новые книги", priority="Средний")
    t3 = Task(task_id=3, description="Расставить книги на полках", priority="Низкий")

    print("--- Добавление ---")
    queue.enqueue(t1)
    queue.enqueue(t2)
    queue.enqueue(t3)

    print("\n--- Вывод первого элемента ---")
    print(f"Первый в очереди: {queue.front()}")

    print("\n--- Вариативная часть ---")
    search_id = 1
    print(f"Есть ли задача с ID {search_id}?: {queue.has_task_by_id(search_id)}")
    
    missing_id = 9
    print(f"Есть ли задача с ID {missing_id}?: {queue.has_task_by_id(missing_id)}")

    print("\n--- Выполнение задач ---")
    while not queue.isEmpty():
        current_task = queue.dequeue()
        print(f"Выполняется: {current_task}")

    print("\n--- Проверка на пустоту ---")
    print(f"Очередь пуста?: {queue.isEmpty()}")


