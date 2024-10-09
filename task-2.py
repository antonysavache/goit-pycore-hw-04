from utils import garbage_cleaner

def get_cats_info(path: str, encoding: str):
    cats = []
    try:
        with open(path, 'r', encoding=encoding) as fh:
            for cat in fh.readlines():
                id, name, age = cat.split(',')
                age = garbage_cleaner(age)
                cats.append({'id': id, 'name': name, 'age': age})
            fh.seek(0)

            return cats
    except Exception as e:
        print(e)


print(get_cats_info('cats.txt', 'utf-8'))