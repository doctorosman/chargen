import random, urllib.request

# HELPER CLASSES

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self, form = 'dd/mm/yyyy'):
        date = [self.year, self.month, self.day]
        if form == 'dd/mm/yyyy':
            return putZeros(date[2]) + '/' + putZeros(date[1]) + '/' + str(date[0])
        elif form == 'd/m/yyyy':
            return str(date[2]) + '/' + str(date[1]) + '/' + str(date[0])
        elif form == 'mm/dd/yyyy':
            return putZeros(date[1]) + '/' + putZeros(date[2]) + '/' + str(date[0])
        elif form == 'm/d/yyyy':
            return str(date[1]) + '/' + str(date[2]) + '/' + str(date[0])
        elif form == 'dd.mm.yyyy':
            return putZeros(date[2]) + '.' + putZeros(date[1]) + '.' + str(date[0])

# HELPER FUNCTIONS

def isLeap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def putZeros(field):
    if len(str(field)) == 1:
        return "0" + str(field)
    else:
        return str(field)

# GENERATE FUNCTIONS

def genTCKN():
    # FIRST 9 DIGITS
    first9 = ""
    for _ in range(9):
        first9 += str(random.randint(0, 9))

    # CONTROL DIGITS
    c1 = ((int(first9[0]) + int(first9[2]) + int(first9[4]) + int(first9[6]) + int(first9[8])) * 7 - (int(first9[1]) + int(first9[3]) + int(first9[5]) + int(first9[7]))) % 10
    c2 = (int(first9[0]) + int(first9[1]) + int(first9[2]) + int(first9[3]) + int(first9[4]) + int(first9[5]) + int(first9[6]) + int(first9[7]) + int(first9[8]) + c1) % 10

    # COMBINING
    return int(first9 + str(c1) + str(c2))

def genFirstName():
    # forked from gist.github.com/emrekgn/b4049851c88e328c065a
    names = []

    with open('src/isimler.txt', encoding='utf8') as f:
        line = f.readline()
        while line:
            pline = line.replace('\n', '')
            if pline not in names:
                names.append(pline)
            line = f.readline()
    
    return random.choice(names)

def genLastName():
    # forked from gist.github.com/emrekgn/493304c6445de15657b2
    names = []

    with open('src/soyisimler.txt', encoding='utf8') as f:
        line = f.readline()
        while line:
            pline = line.replace('\n', '')
            if pline not in names:
                names.append(pline)
            line = f.readline()
    
    return random.choice(names)

def genFullName():
    return genFirstName() + " " + genLastName()

def genDate(minYear, maxYear):
    year = random.randint(minYear, maxYear)
    month = random.randint(1, 12)

    ms31 = [1, 3, 5, 7, 8, 10, 12]

    if month == 2:
        if isLeap(year):
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    elif month in ms31:
        day = random.randint(1, 31)
    else:
        day = random.randint(1, 30)

    return Date(year, month, day)

def genEmail():
    # TODO
    pass