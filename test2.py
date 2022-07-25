"""sleep2"""
from signal import SIGUSR1


def main():
    """T_T"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    val = num1-num2
    ps1 = val%3
    if ps1 == 0:
        snack = 10
        val1 = int(snack*num3)
        val2 = val-val1
        ps2 = val2%3
        if ps2 == 0:
            snack = 12
            val3 = int(num4*snack)
            val4 = val2-val3
    elif ps1 == 1:
        snack = 15
        val1 = int(snack*num3)
    else:
        snack = 20
        val1 = int(snack*num3)
main()
