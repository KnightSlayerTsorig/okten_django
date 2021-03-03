from django.shortcuts import render

from requests.exceptions import HTTPError


def home(request):
    return render(request, 'calculator/index.html')


def calculator(request, f_num, action, s_num):
    try:
        f_num, s_num = int(f_num), int(s_num)

        if action == '+':
            result = f_num + s_num
        elif action == '-':
            result = f_num - s_num
        elif action == '*':
            result = f_num * s_num
        elif action == 'divide':
            result = f_num / s_num
            action = '/'

        string_for_rend = f'{f_num} {action} {s_num} = {result}'

    except ValueError:

        string_for_rend = 'wrong'

    except UnboundLocalError:

        string_for_rend = 'wrong'

    return render(
        request, 'calculator/calculator.html',
        {'string_for_rend': string_for_rend}
    )




