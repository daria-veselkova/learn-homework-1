"""

Домашнее задание №1

Исключения: приведение типов

* Перепишите функцию discounted(price, discount, max_discount=20)
  из урока про функции так, чтобы она перехватывала исключения,
  когда переданы некорректные аргументы.
* Первые два нужно приводить к вещественному числу при помощи float(),
  а третий - к целому при помощи int() и перехватывать исключения
  ValueError и TypeError, если приведение типов не сработало.

TypeError -  не тот тип объекта
ValueError - тип тот, значение не подходит
   
"""

class MyValueError(Exception):         #чтобы обрабатывать ошибку иначе, чем ValueError (использовалась в примере из лекции)
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


def check_discount(discount):
    if discount >= 100:
            raise MyValueError


def discounted(price, discount, max_discount=20):
    
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
        
        check_discount(discount)

        if discount >= max_discount:
            return price
        else:
            return price - (price * discount / 100)

    except TypeError as e:
        return 'Incorrect type of data. Use integers, floats or strings'
    except ValueError:
        return 'Incorrect value. Use numbers, not numerics'
    except MyValueError:
        return f'Incorrect discount: {discount} >= 100'
    
    
if __name__ == "__main__":
    print(discounted(100, 2))
    print(discounted(100, "3"))
    print(discounted("100", "4.5"))
    print(discounted("five", 5))
    print(discounted("сто", "десять"))
    print(discounted(100.0, 5, "10"))
    print(discounted(100, 5, {}))
    print(discounted([100, 5], 30))
    print(discounted(100, 120, 30))
    