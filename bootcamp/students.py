
class SiriusEducationStudents:

    def __init__(self) -> None:
        names = ['João', 'José', 'Fernando', 'Rafaela', 'Kleber', 'Laercio', 
                 'Carlos','Paula','Adriana','Walkyria','Guilherme','Gustavo',
                 'Gabriel', 'Mayara', 'Ana', 'Daniela', 'Rafael', 'Daiane', 
                 'Maria', 'Mateus', 'Monique', 'Brian', 'Henrique', 'Alberto', 
                 'Mônica', 'Bruce', 'Simone']
        results = [8,7,6,9,3,8,7,
                   5,9,1,4,5,8,4,9,
                   7,5,6,2,7,4,5,8,
                   7,9,10,5]
        ages = [25,17,56,32,27,31,48,
                24,41,50,29,22,30,31,
                28,52,27,33,35,36,38,
                26,29,35,38,41,46]
        provinces = ['PR','SP','SP','MG','RJ','MG','PB','AM','SC','MS',
                     'SP','MG','AM','RO','MG','BA','MG','ES','CE','MG',
                     'PA','PI','PE','MG','RR','MG','SE']
        self.data = {name: {'result': results[i], 'age': ages[i], 'province': provinces[i]} for i, name in enumerate(names)}

    def _alunos_por_estado(self, state: str) -> str:
        for student in self.data.keys():
            if self.data[student]['province'] == state:
                yield student 
    
    def single_alunos_por_estado(self, state: str) -> list:
        return list(self._alunos_por_estado(state))

    def media_por_estado(self, state: str):
        nota = 0
        qtd = 0
        alunos = self.single_alunos_por_estado(state)
        for aluno in alunos:
            nota += self.data[aluno]['result']
            qtd += 1
        print("A média das notas do está {state} é {avr}".format(state=state, avr=(nota/qtd))) 


    def quant_aprov_estado(self, state: str) -> None:
        num = 0
        alunos = self.single_alunos_por_estado(state)
        for aluno in alunos:
            num += 1 if self.data[aluno]['result'] >= 6 else 0
        print("O número de alunos aprovado para o estado {state} é {num}".format(state=state, num=num))

    def alunos_por_estado(self) -> None:
        print_data = {}
        for aluno in self.data.keys():
            if print_data.get(self.data[aluno]['province']):
                print_data[self.data[aluno]['province']] += 1
            else:
                print_data[self.data[aluno]['province']] = 1
        [print(f"No estado {key} há {item} alunos") for (key, item) in print_data.items()]

    def media_idade_aprov_por_estado(self, state: str) -> None:
        idade = 0
        qtd = 0
        alunos = self.single_alunos_por_estado(state)
        for aluno in alunos:
            idade += self.data[aluno]['age'] if self.data[aluno]['result'] >= 6 else 0
            qtd += 1 if self.data[aluno]['result'] >= 6 else 0
        print("A média das notas do está {state} é {avr}".format(state=state, avr=(idade/qtd))) 

students = SiriusEducationStudents()

#Resposta questão 1 
print(students.single_alunos_por_estado('SP'))

#Resposta questão 2
students.quant_aprov_estado('SP')

#Resposta questão 3
students.alunos_por_estado()

#Resposta questão 4
students.media_por_estado('SP')

#Resposta questão 5
students.media_idade_aprov_por_estado('SP')
