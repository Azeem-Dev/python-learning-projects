def print_fibonacci_series(num_of_items: int) -> None:
    if num_of_items <= 0:
        return

    first = 0
    second = 1
    series = ''
    series += f'{first} {second}'

    for i in range(2,num_of_items):
        sum = first + second
        series += f' {sum}'
        first = second
        second = sum

    print(series)


if __name__ == "__main__":
    
    print_fibonacci_series(20)
