import io


class RaW:
    def __init__(self, file, score):
        self.file = file
        self.score = score
        self.i = self.i

    def reading(self):
        self.i = 0
        with io.open(self.file, mode="r", encoding="utf-8") as f:
            if f.mode == 'r':
                for line in f:
                    self.i += 1
                    print(line)

            print(self.i)

    def writing(self):
        if self.file:
            f = open(self.file, "r")
            s = f.readline()
            f.close()
        else:
            f = open(self.file, "w")
            f.write("0")
            s = 0
            f.close()

        if self.score > int(s):
            f = open(self.file, "w")
            f.write(str(self.score))
            f.close()
