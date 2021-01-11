import io


class Reading:
    def __init__(self, file):
        self.file = file

    def counting(self):
        i = 1
        c = ''
        d = 0
        f = io.open(self.file, mode="r", encoding="utf-8")
        if f.mode == 'r':
            for line in f:
                for char in line:
                    if char == ";":
                        i += 1
                        print(d)
                        d = 0
                        c += ', '
                    else:
                        c += char
                        d += 1
                    print(f.read(d))
                print(c)

        print(i)
        f.close()


answers = Reading("a.txt")
answers.counting()
