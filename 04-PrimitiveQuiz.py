dict1 ={"What is the capital of Austria:":'Vienna',
        "What is the capital of Germany:":'Berlin',
        "What is the capital of Italy:": 'Rome',
        "What is the capital of Norway:": 'Oslo',
        "What is the capital of Belgium:": 'Brasilia',
        "What is the capital of U.K:": 'London',
        "What is the capital of Croatia:": 'Zagreb',
        "What is the capital of Denmark:": 'Copenhagen',
        "What is the capital of Finland:": 'Helsinki',
        "What is the capital of Czechia:": 'Prague'}
def questions_answers(question,answer):
        answers = input(question)
        if answers.lstrip().lower() == answer.lstrip().lower():
                print("Wow you got that correct!")
        else:
         exit("The supreme leader has scheduled your execution in 10 minutes.")
for k,s in dict1.items():
        questions_answers(k,s)
