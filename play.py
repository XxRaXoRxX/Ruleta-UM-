from random import seed, randint, randrange
import constants as cs

class Play():

    # Edit if you need change values of roulette.
    __initialRoulette = 0
    __finalRoulette = 36

    def __init__(self, students):
        self.__players = students
        self.bets = []

    def RandomValue(self, start, end):
        """Random int number generator between two range [start, end]
            - ags:
                - start: initial range (int)
                - end: final range (int)
            - return: random value between start and end values"""
        seedValue = randrange(0, 999999)
        seed(seedValue)
        value = randint(start, end)
        return value

    def __ShowStudentsNumbers(self, studentList, betList):
        """Show all students bets in a list.
            -return: students and bets in a list
        """
        list = []

        for i in range(0, len(studentList)):
            # Remove missing student
            if(betList[i] == -1):
                continue

            list.append(f"{studentList[i]} - {betList[i]}")

        return list

    def __StudentsDecision(self):
        """Ask all students in list to select a number and update bets list."""
        for student in self.__players:
            message = f"{cs.PLAYER1} {student} {cs.PLAYER2}"

            while True:
                    num = input(message)
                    if (num == "-1"):
                        num = int(num)
                        break
                    elif(not num.isdigit()):
                        print(cs.INVALID, num)
                    else:
                        num = int(num)
                        if (num > 36 or num < 0):
                            print(cs.INVALID, num)
                        else:
                            break
            self.bets.append(num)

    def __StartGame(self):
        """Game Logic"""
        print(cs.SPACE)
        roulette = self.RandomValue(start = self.__initialRoulette, end = self.__finalRoulette)
        print(cs.ROULETTE, roulette)
        print(cs.SPACE)

        winners = []

        for i in range(0, len(self.__players)):
            if(self.bets[i] == roulette):
                winners.append(self.__players[i])

        print(cs.WINNERS)
        for w in winners:
            print(w)

        print(cs.SPACE)
        input(cs.PASS)
        return winners

    def Start(self):
        """Logic before starting game"""
        print(cs.SPACE)
        print(cs.PLAYER0)

        self.__StudentsDecision()

        print(cs.SPACE)
        print(cs.BEFOREPLAY)
        list = self.__ShowStudentsNumbers(studentList = self.__players, betList = self.bets)
        for l in list:
            print(l)

        while True:
            print(cs.SPACE)
            opc = input(cs.PLAY)

            if (opc == "s"):
                return self.__StartGame()
            elif (opc == "n"):
                print(cs.CANCEL)
                input(cs.PASS)
                return False
            else:
                print(cs.INVALID, opc)