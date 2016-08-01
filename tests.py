import silicon

class Tester:
    test = 1
    tests = {
        '55+': [10],
        '_11_8+': [19],
        '57>': [0],
        '52>': [1],
        '"5"n': [5],
        '"test"y': [4],
        '9D': [8],
        '8H': [4],
        '"3,5,2,1"ÈTQ': [1,2,3,5],
        '"Hi!"R': ["!iH"],
        '"1,2,3,4"ÈTM': [10],
        'Ù': [[]],
    }
        

    def test(self, i):
        i = i()
        for t in self.tests:
            i.run(t)
            if i.stack == self.tests[t]:
                print("Test " + str(self.test) + ": OK")

            else:
                print("Test " + str(self.test) + ": Failed")

            i.clr()
            self.test += 1
