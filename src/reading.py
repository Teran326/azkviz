import io


class RaW:
    def __init__(self, file):
        self.file = file

    def reading(self, j):
        i = 0
        with io.open(self.file, mode="r", encoding="utf-8") as f:
            if f.mode == 'r':
                for line in f:
                    i += 1
                    if i == 1:
                        result = [line]
                    else:
                        result.append(line)
        return result[j]

    def writing(self, score):
        if self.file:
            f = open(self.file, "r")
            s = f.readline()
            f.close()
        else:
            f = open(self.file, "w")
            f.write("0")
            s = 0
            f.close()

        if score > int(s):
            f = open(self.file, "w")
            f.write(str(score))
            f.close()
