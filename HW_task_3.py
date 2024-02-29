"""
Создайте функцию генератор чисел Фибоначчи"""


def gen_fibonachi() -> list:
    nums = [1, 1]
    while True:
        count = int(input('Введите кол-во чисел посл-ти (не меньше 3): '))
        if count < 3:
            continue
        else:
            break
    for i in range(count - 2):
        nums.append(nums[i] + nums[i + 1])
    return nums


if __name__ == "__main__":
    print(gen_fibonachi())
