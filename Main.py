from abc import ABCMeta, abstractmethod
from datetime import datetime, timedelta
import random


class Field(metaclass=ABCMeta):
    @property
    @abstractmethod
    def val(self): pass

    @abstractmethod
    def generate_val(self): pass

    def get_val(self):
        return self.val


class StrField(Field):

    val = ""

    def __init__(self):
        self.generate_val()

    def generate_val(self):
        import names
        self.val = names.get_first_name()

    def __repr__(self):
        return "StrField() with value: {0}".format(self.val)

    def __str__(self):
        return 'Value: ' + self.val   


class NumField(Field):

    val = 0

    _min_val = 0
    _max_val = 10
    _type = int

    def __init__(self, min_val, max_val, f_type=int):
        self._min_val = min_val
        self._max_val = max_val
        self._type = f_type
        self.generate_val()

    def generate_val(self):
        if self._type == int:
            self.val = random.randint(self._min_val, self._max_val)
        else:
            self.val = random.uniform(self._min_val, self._max_val)

    def __repr__(self):
        return "{1} NumField() with value: {0}".format(self.val, self._type)

    def __str__(self):
        return 'Value: ' + self.val


class DateField(Field):

    val = ''

    _year = 0
    _month = 0
    _day = 0

    def __init__(self):
        self.generate_val()

    def generate_val(self):
        self.val = ''

        self._year = random.randint(1900, datetime.now().date().year)
        self._month = random.randint(1, 12)
        self._day = random.randint(1, 30)

        self.val += str(self._year) + '-'

        if(self._month < 10):
            self.val +=  '0' + str(self._month) + '-'
        else:
            self.val +=  str(self._month) + '-'

        if(self._day < 10):
            self.val +=  '0' + str(self._day)
        else:
            self.val +=  str(self._day)

    def __repr__(self):
        return "DateField() with value: {0}".format(self.val)

    def __str__(self):
        return 'Value: ' + self.val


class TimeField(Field):

    val = ""

    _hour = 0
    _min = 0
    _sec = 0

    def __init__(self):
        self.generate_val()

    def generate_val(self):
        self.val = ""

        self._hour = random.randint(0, 23)
        self._min = random.randint(0, 59)
        self._sec = random.randint(0, 59)

        if(self._hour < 10):
            self.val +=  '0' + str(self._hour) + '-'
        else:
            self.val +=  str(self._hour) + '-'

        if(self._min < 10):
            self.val +=  '0' + str(self._min) + '-'
        else:
            self.val +=  str(self._min) + '-'

        if(self._sec < 10):
            self.val +=  '0' + str(self._sec)
        else:
            self.val +=  str(self._sec)

    def __repr__(self):
        return "TimeField() with value: {0}".format(self.val)

    def __str__(self):
        return 'Value: ' + self.val


class TextField(Field):

    val = ""

    def __init__(self, text):
        self.val = text
        self.generate_val()

    def generate_val(self):
        pass

    def __repr__(self):
        return "TextField() with value: {0}".format(self.val)

    def __str__(self):
        return 'Value: ' + self.val


class DataFormat:

    _commands = []
    _trails = []
    _max_data_lines = 1

    def __init__(self, max_lines):
        self._commands = []
        self._trails = []
        self._max_data_lines = max_lines

    def add_command(self, c, trail = ' '):
        self._commands.append(c)
        self._trails.append(trail)

    def output(self):
        result = ""

        for i in range(0, self._max_data_lines):
            for j in range(0, len(self._commands)):
                self._commands[j].generate_val()
                result += "{0}{1}".format(self._commands[j].get_val(), self._trails[j])

            result += "\n"

        return result

    def gen_to_files(self, dir, count, name = 'gen_file_'):
        for i in range(0, count):
            path = dir + "/" + name + str(i) + '.txt'

            text_file = open(path, "w")
            text_file.write(self.output())
            text_file.close()
        

def entry():
    fmt = DataFormat(200)

    #Date
    fmt.add_command(DateField())

    #Time
    #fmt.add_command(TimeField())

    #IP
    fmt.add_command(NumField(0, 255, int), '.')
    fmt.add_command(NumField(0, 255, int), '.')
    fmt.add_command(NumField(0, 255, int), '.')
    fmt.add_command(NumField(0, 255, int))

    fmt.add_command(StrField())
    fmt.add_command(NumField(0, 420, int))

    fmt.add_command(StrField())
    fmt.add_command(StrField())

    fmt.add_command(NumField(16, 30, int))
    fmt.add_command(NumField(0, 64, int))

    fmt.add_command(StrField())

    #Path
    #fmt.add_command(TextField("localhost:"), '/')
    #fmt.add_command(StrField(), '/')
    #fmt.add_command(StrField(), '/')
    #fmt.add_command(StrField())

    fmt.gen_to_files('GeneratedFiles', 10)


#Python main func
if __name__ == '__main__':
    entry()
