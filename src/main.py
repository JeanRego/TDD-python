from src.calculator import soma

try:
    print(soma(50,0.5))
except AssertionError as e:
    print(f'Conta invalida: {e}')