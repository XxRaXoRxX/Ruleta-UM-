#------------------------------------------------------------------------------------#
#---------------------Proyecto Ruleta para pasar al frente en------------------------#
#-------------------------------Diseño de Sistemas-----------------------------------#
#-----------------------------Author: Marcos Miglierina------------------------------#
#------------------------------------------------------------------------------------#

from list import listConfig
from play import Play
import constants as cs

class Main():

    def __init__ (self):
        self.__list = listConfig()
        self.__students = []
        self.__tokens = []

    def __UpdateTokens(self, winners, bets):
        """Update all tokens when finishing a game"""
        i = 0
        for i in range(0, len(self.__students)):
            if (self.__students[i] in winners or bets[i] == -1):
                continue
            else:
                self.__tokens[i] -= 1

    def __ShowStudents(self):
        """Print Students and Tokens in a list."""
        print(cs.SPACE)
        for i in range(0, len(self.__students)):
            print(self.__students[i], self.__tokens[i])
        print(cs.SPACE)

    def __SelectRandomLoser(self):
        """Select one of loser students (token = 0) to come to the front
        - return: Loser student name"""
        loserStudents = []

        for i in range(0, len(self.__students)):
            if (self.__tokens[i] <= 0):
                loserStudents.append(self.__students[i])

        if (len(loserStudents) != 1):
            print(cs.SPACE)
            print(cs.STUDENTS_WITHOUT_TOKENS)
            for loser in loserStudents:
                print(loser)
            print(cs.SPACE)
            input(cs.STUDENTS_LOSER_SELECTION)
        elif (len(loserStudents) == 1):
            print(cs.SPACE)
            print(cs.STUDENT_WITHOUT_TOKENS)

        play = Play(students = self.__students)
        randomValue = play.RandomValue(start = 0, end = (len(loserStudents) - 1))
        loser = loserStudents[randomValue]
        loserStudents.remove(loser)

        self.__UpdateLosersTokens(loser = loser, loserStudents = loserStudents)
        
        return loser

    def __UpdateLosersTokens(self, loser, loserStudents):
        """Update all tokens for loser students"""
        for i in range(0, len(self.__students)):
            # Add 1 token for all students with 0 tokens
            if (self.__students[i] in loserStudents):
                self.__tokens[i] += 1
            # Add 5 tokens for loser student.
            elif (self.__students[i] == loser):
                self.__tokens[i] += 5

    def start(self):
        """Program Start"""
        self.menu()

    def menu(self):
        """Show app menu and interact with user decisions"""

        self.__students, self.__tokens = self.__list.GetStudentsList()

        while True:
            print(cs.LOGO)
            print(cs.MENU)

            opc = input(cs.ANSWER) # User selecting option.

            if (opc == "1"):
                play = Play(students = self.__students)
                winners = play.Start()
                if (winners == False):
                    continue

                print(cs.TOKENS_UPDATE)
                tokens = self.__UpdateTokens(winners = winners, bets = play.bets)

                for token in self.__tokens:
                    if (token <= 0):
                        loser = self.__SelectRandomLoser()
                        print(cs.SPACE)
                        print(f" {cs.LOSER0}{loser} {cs.LOSER1}")
                        print(cs.SPACE)
                        input(cs.PASS)

            elif (opc == "2"):
                self.__ShowStudents()
                input(cs.PASS)

            elif (opc == "3"):
                self.__list.SaveStudentsList(studentsList = self.__students, tokensList = self.__tokens)
                print(cs.EXIT)
                return

            else:
                print(cs.INVALID, opc)


# Run program
main = Main()
main.start()