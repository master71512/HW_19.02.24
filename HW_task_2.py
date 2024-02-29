"""
Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
имена str, ставка int, премия str с указанием процентов вида “10.25%”. 
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения. 
Сумма рассчитывается как ставка умноженная на процент премии"""


def calc_perc(names: list, salary: list, bonus: list) -> dict:
    return {name: sal * float(bon.strip("%")) / 100 for name, sal, bon in zip(names, salary, bonus)}


if __name__ == "__main__":
    list_1 = ["Abb", "Jim", "Pit"]
    list_2 = [125, 151, 180]
    list_3 = ["2.5%", "5%", "2.6%"]
    print(calc_perc(list_1, list_2, list_3))
