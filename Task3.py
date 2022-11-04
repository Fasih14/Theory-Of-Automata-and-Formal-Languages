class Task3:
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
            if alphabet == 'c':
                state = 1
            elif alphabet == 'a':
                state = 2
            elif alphabet == 'b':
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 1:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 2
            elif alphabet == 'c':
                state = 2
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 2:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)

        elif state == 3:
            if alphabet == 'a':
                state = 3
            elif alphabet == 'b':
                state = 3
            elif alphabet == 'c':
                state = 3
            else:
                print("INVALID CHARACTER: ", alphabet)
        return state


    def Work_flow(self, newWord):
        self.word = newWord
        for i in self.word:
            self.final_state = self.transition(str(i), self.final_state)
        if self.final_state == 2:
            print("VALID STRING")
        else:
            print("INVALID STRING")

if __name__ == "__main__":
    inputString = str(input("Enter the String to check: "))
    t3 = Task3()
    t3.Work_flow(inputString)