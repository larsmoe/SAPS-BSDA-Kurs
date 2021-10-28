class Teacher:
    def __init__(self, solutions):
        self.solutions = solutions

    def hint(self, task, hint_number):
        if hint_number == 1:
            print(self.solutions.hint_1.iloc[task-1])

    def check(self, task, answer):
        if (answer==self.solutions.Solution.iloc[task-1]).all():
            print('Your answer is correct :)')
        else:
            print('Your answer is incorrect :(')

