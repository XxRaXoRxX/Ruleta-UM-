import constants as cs

class listConfig():

    def GetStudentsList(self):
        """Get all students and tokens from a ".txt" archive to a list.
            - return: students and token in two lists."""

        f = open(cs.ARCHIVE_NAME, "r")
        list = f.readlines()
        list.pop(0) #Remove first value "#Alumno Fichas#"
        f.close()

        # Create two list, one for students and another for tokens
        students = []
        tokens = []
        for l in list:
            nt = l.split()
            students.append(nt[0])
            tokens.append(int(nt[1]))

        return students, tokens

    def SaveStudentsList(self, studentsList, tokensList):
        """Save students and tokens in a ".txt" archive when exit game"""

        f = open(cs.ARCHIVE_NAME, "w")
        f.write("#Alumno Fichas#\n")

        newlist = []
        for i in range(0, len(studentsList)):
            studentToken = f"{studentsList[i]} {tokensList[i]}"
            newlist.append(studentToken)
        for i in newlist:
            f.write(f"{i}\n")
        
        f.close()