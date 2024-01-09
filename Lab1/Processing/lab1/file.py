def find_nth_happy_number(N, max_attempts=1000000):
    n = 1
    attempts = 0

    while N > 0 and attempts < max_attempts:
        if is_happy_number(n):
            N -= 1
        n += 1
        attempts += 1

    if N == 0:
        return n - 1  # Останнє перевірене число є N-м щасливим числом
    else:
        return None  # Якщо не вдається знайти N щасливих чисел

def is_happy_number(num):
    num_str = str(num)
    return all(char in '47' for char in num_str)

N = 5  # Знайти 5-те щасливе число
result = find_nth_happy_number(N)
if result is not None:
    print(f'{N}-те щасливе число: {result}')
else:
    print(f'Не вдалося знайти {N} щасливих чисел')
