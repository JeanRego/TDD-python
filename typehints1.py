#PARA EXECUTAR O TEST NESSE MODULO: mypy .\typehints1.py
from typing import List, Union,Tuple,Dict,NewType, Callable, Sequence, Iterable
#Primitivos
numero: int = 10
flutuante: float = 10.0
boleano: bool = True
strings: str = 'je'

#Sequencias
lista: List[int] = [1,2,3,4]
lista_mista1: List[Union[int,float,str,list]] = [1,'123','ewrf',10,14.7,[1212,'qwe']]
lista_mista2: list = [1,'123','ewrf',10,14.7,['123',123]]
tupla1: tuple = (1,2,3,4)
tupla2: Tuple[int,int,int] = (1,2,3)
tupla3: Tuple[int,int,int,str,str] = (1,2,3,'qwer','tr')

#Dicionarios e conjuntos
pessoa1: dict = {'nome':'Jean','sobrenome':'Rego'}
pessoa2: Dict[str,str] = {'nome':'Jean','sobrenome':'Rego','id':'10','nome':'isa'}
pessoa3: Dict[str,Union[str,int]] = {'nome':'Jean','sobrenome':'Rego','id':'10','nome':'isa','id':11}

#Meu outro tipo
UserId = NewType('UserId', int)
UserId2 = NewType('UserId2', str)

pessoa10 = UserId(10)
pessoa12 = UserId2('10')


def retorna_funcao(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return x + y
    
print(retorna_funcao(soma)(10,20))

class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome: str = nome
        self.sobrenome: str = sobrenome
        self.idade: int = idade
    
    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} está falando...')
    

def interar(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]

def interar2(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]



print(interar((1,2,3)))
print(interar2((1,2,3)))

 