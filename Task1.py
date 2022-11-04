class Task1:
    word = ''
    initial_state = 0
    final_state = 0
    valid = False

    def __int__(self):
        self.word = ''
        self.initial_state = 0

    def constructor(self, w, i):
        self.word = w
        self.initial_state = i

    def transition(self, alphabet, state):
        if state == 0:
            if alphabet == 0:
                state = 1
            elif alphabet == 1:
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 1:
            if alphabet == 0:
                state = 0
            elif alphabet == 1:
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 2:
            if alphabet == 0:
                state = 3
            elif alphabet == 1:
                state = 1
            else:
                print("INVALID CHARACTER: ", alphabet)
        elif state == 3:
            if alphabet == 0:
                state = 2
            elif alphabet == 1:
                state = 0
            else:
                print("INVALID CHARACTER: ", alphabet)
        return state

    def Work_flow(self, newWord):
        self.word = newWord
        for i in self.word:
            self.final_state = self.transition(int(i), self.final_state)
        if self.final_state == 0:
            print("VALID STRING")
        else:
            print("INVALID STRING")


if __name__ == "__main__":
    inputString = str(input("Enter the String to check: "))
    t1 = Task1()
    t1.Work_flow(inputString)