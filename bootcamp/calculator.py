from pydantic import BaseModel
from typing import Any, Dict

class Calculator(BaseModel):
    """
    Eu tentei fazer o exercicio com algumas validações, normalmente lido com dados via api,
    logo estou pouco acostumado com o input do usuário, mas acredito que o código esteja
    funcional.
    """
    num1: int = 0
    num2: int = 0
    operation: int = None
    methods: Dict[int, Any] = {
        1: lambda x, y: x + y,
        2: lambda x, y: x - y,
        3: lambda x, y: x * y,
        4: lambda x, y: x / y,
    }

    def cli(self):
        while self.operation != 5:
            print('Escolha o número da operação a ser realizada: ')
            print('1) Soma')
            print('2) Subtração')
            print('3) Multiplicação')
            print('4) Divisão')
            print('5) Sair da calculadora')
            self.operation = self._operation(input())
            if self.operation == 5:
                print('Obrigado pelo seu tempo')
                break
            print('Insira o primeiro número')
            self.num1 = self._num(input())
            print('Insira o segundo número')
            self.num2 = self._num(input())
            print('O resultado da sua operação é:{result}'.
                  format(result=self.methods[self.operation](self.num1, self.num2)))
    

    def _operation(self, v= None):
        try:
            v = int(v)
        except:
            v = None
            while not v:
                print('Opção invalida digite novamente: ')
                try:
                    v = int(input())
                except:
                    pass
        if v not in [1, 2, 3, 4, 5]:
            while v not in [1, 2, 3, 4, 5]:
                try:
                    print('Opção invalida digite novamente: ')
                    v = int(input())
                except:
                    pass
            return v
        else:
            return int(v)

        
    def _num(self, v):
        try:
            float(v)
            return float(v)
        except:
            while not isinstance(v, int):
                try:
                    print('Este valor não é um número! Insira novamente: ')
                    v = float(self._num(input()))
                    return v
                except:
                    pass
Calculator().cli()