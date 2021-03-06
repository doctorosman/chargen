import json, random, urllib.request

# DATE CLASS

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def format(self, form = 'dd/mm/yyyy'):
        date = [self.year, self.month, self.day]
        if form == 'dd/mm/yyyy':
            return Char.putZeros(date[2]) + '/' + Char.putZeros(date[1]) + '/' + str(date[0])
        elif form == 'd/m/yyyy':
            return str(date[2]) + '/' + str(date[1]) + '/' + str(date[0])
        elif form == 'mm/dd/yyyy':
            return Char.putZeros(date[1]) + '/' + Char.putZeros(date[2]) + '/' + str(date[0])
        elif form == 'm/d/yyyy':
            return str(date[1]) + '/' + str(date[2]) + '/' + str(date[0])
        elif form == 'dd.mm.yyyy':
            return Char.putZeros(date[2]) + '.' + Char.putZeros(date[1]) + '.' + str(date[0])

# CHAR CLASS

class Char:

    # CONSTRUCTOR

    def __init__(self, minyear = 1960, maxyear = 2000):
        self.firstname = self.genFirstName()
        self.lastname = self.genLastName()
        self.fullname = self.firstname + " " + self.lastname
        self.tckn = self.genTCKN()
        self.birthdate = self.genDate(minyear, maxyear)
        self.email = self.genEmail(self.firstname, self.lastname)
        self.province = self.genProv()
        self.town = self.genTown(self.province)

    # HELPER FUNCTIONS

    @staticmethod
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

    @staticmethod
    def putZeros(field):
        if len(str(field)) == 1:
            return "0" + str(field)
        else:
            return str(field)

    @staticmethod
    def getTowns(province):
        with open('src/ilceler.json', encoding='utf8') as f:
            array = json.loads(f.read())
        
        for prov in array:
            if prov['name'] == province:
                return prov['towns']

    # GENERATE FUNCTIONS

    @staticmethod
    def genTCKN():
        # FIRST 9 DIGITS
        first9 = ""
        for i in range(9):
          if i == 0:
            first9 += str(random.randint(1, 9))
          else:
            first9 += str(random.randint(0, 9))

        # CONTROL DIGITS
        c1 = ((int(first9[0]) + int(first9[2]) + int(first9[4]) + int(first9[6]) + int(first9[8])) * 7 - (int(first9[1]) + int(first9[3]) + int(first9[5]) + int(first9[7]))) % 10
        c2 = (int(first9[0]) + int(first9[1]) + int(first9[2]) + int(first9[3]) + int(first9[4]) + int(first9[5]) + int(first9[6]) + int(first9[7]) + int(first9[8]) + c1) % 10

        # COMBINING
        return int(first9 + str(c1) + str(c2))

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def genFullName():
        return Char.genFirstName() + " " + Char.genLastName()

    @staticmethod
    def genDate(minYear, maxYear):
        year = random.randint(minYear, maxYear)
        month = random.randint(1, 12)

        ms31 = [1, 3, 5, 7, 8, 10, 12]

        if month == 2:
            if Char.isLeap(year):
                day = random.randint(1, 29)
            else:
                day = random.randint(1, 28)
        elif month in ms31:
            day = random.randint(1, 31)
        else:
            day = random.randint(1, 30)

        return Date(year, month, day)

    @staticmethod
    def genEmail(fname, lname):
        for i, j in {'İ' : 'I', 'Ö' : 'O', 'Ş' : 'S', 'Ü' : 'U', 'Ç' : 'C', 'Ğ' : 'G'}.items():
            fname = fname.replace(i, j)
            lname = lname.replace(i, j)

        fname = fname.replace(' ', '_')
        lname = lname.replace(' ', '_')

        fname = fname.lower()
        lname = lname.lower()
        
        hosts = ['@gmail.com', '@hotmail.com', '@yandex.com', '@outlook.com']
        pick = random.randint(0, 4)

        if pick == 0:
            email = fname + '_' + lname + random.choice(hosts)
        elif pick == 1:
            email = fname + lname + str(random.randint(0, 99)) + random.choice(hosts)
        elif pick == 2:
            email = fname + '.' + lname + str(random.randint(0, 9)) + random.choice(hosts)
        elif pick == 3:
            email = fname[0] + lname + str(random.randint(0, 9)) + random.choice(hosts)
        else:
            email = fname[0] + lname + random.choice(hosts)

        return email

    @staticmethod
    def genProv():
        # forked from turzifer.com
        provs = ['Adana', 'Adıyaman', 'Afyon', 'Ağrı', 'Amasya', 'Ankara', 'Antalya', 'Artvin', 'Aydın', 'Balıkesir', 'Bilecik', 'Bingöl', 'Bitlis', 'Bolu', 'Burdur', 'Bursa', 'Çanakkale', 'Çankırı', 'Çorum', 'Denizli', 'Diyarbakır', 'Edirne', 'Elazığ', 'Erzincan', 'Erzurum', 'Eskişehir', 'Gaziantep', 'Giresun', 'Gümüşhane', 'Hakkari', 'Hatay', 'Isparta', 'İçel (Mersin)', 'İstanbul', 'İzmir', 'Kars', 'Kastamonu', 'Kayseri', 'Kırklareli', 'Kırşehir', 'Kocaeli', 'Konya', 'Kütahya', 'Malatya', 'Manisa', 'K.maraş', 'Mardin', 'Muğla', 'Muş', 'Nevşehir', 'Niğde', 'Ordu', 'Rize', 'Sakarya', 'Samsun', 'Siirt', 'Sinop', 'Sivas', 'Tekirdağ', 'Tokat', 'Trabzon', 'Tunceli', 'Şanlıurfa', 'Uşak', 'Van', 'Yozgat', 'Zonguldak', 'Aksaray', 'Bayburt', 'Karaman', 'Kırıkkale', 'Batman', 'Şırnak', 'Bartın', 'Ardahan', 'Iğdır', 'Yalova', 'Karabük', 'Kilis', 'Osmaniye', 'Düzce']
        return random.choice(provs)

    @staticmethod
    def genTown(province):
        # forked from github.com/armaganbayraktar01/il-ilce
        return random.choice(Char.getTowns(province))

    @staticmethod
    def genLoc():
        prov = Char.genProv()
        town = Char.genTown(prov)
        
        return [prov, town]
