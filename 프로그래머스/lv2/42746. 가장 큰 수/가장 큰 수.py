def solution(numbers):
    number_str = [str(num) for num in numbers]
    number_str.sort(key=lambda num: num*3, reverse = True )
    return str(int(''.join(number_str)))