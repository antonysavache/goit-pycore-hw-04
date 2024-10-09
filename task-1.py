from utils import garbage_cleaner


def calculate_salary(path: str, encoding: str) -> tuple[float, float]:
    total_salary = 0
    avarage_salary = 0

    try:
        with open(path, 'r', encoding=encoding) as fh:
            for worker in fh.readlines():
                name, salary = worker.split(',')
                salary = int(garbage_cleaner(salary))
                total_salary = total_salary + salary
            fh.seek(0)
            try:
                avarage_salary = total_salary / len(fh.readlines())
            except ZeroDivisionError:
                print('Something Wrong with your salary, buddy')

            return total_salary, avarage_salary
    except Exception as e:
        print(e)



print(calculate_salary('workers.txt', 'utf-8'))

