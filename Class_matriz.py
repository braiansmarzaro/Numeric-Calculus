
class Matriz:
    def __init__(self, m: int, n: int, default=0):
        self.default = default
        self.m = m if m > 1 else 1
        self.n = n if n > 1 else 1

        self.matriz = [[self.default] * self.n for _ in range(self.m)]

    def __getitem__(self, index):
        return self.matriz[index]

    def __setitem__(self, index, item: list):
        self.matriz[index] = list(item)

    def copia(self):
        nova_matriz = Matriz(self.m, self.n)
        nova_matriz.matriz = [[self[i][j] for j in range(self.n)] for i in range(self.m)]
        return nova_matriz

    def add_coluna(self, values: list = None):
        for i in range(self.m):
            try:
                self.matriz[i].append(values[i])
            except:
                self.matriz[i].append(self.default)
        self.n += 1

    def add_linha(self, values: list = None):
        new_line = []
        for j in range(self.n):
            try:
                new_line.append(values[j])
            except:
                new_line.append(self.default)
        self.matriz.append(new_line)
        self.m += 1

    def __str__(self):
        string = ""

        for i in range(-1, len(self.matriz)):  # Percorre as linhas da Matriz
            string += " \t" if i == -1 else f"{i}\t"  # Printa o número da linha

            for j in range(len(self.matriz[i])):
                string += f"{j}" if i == -1 else f"{self.matriz[i][j]}"  # Printa os elementos de cada linha

                if j < len(self.matriz[i]) - 1:  # Enquanto j não for o ultimo termo da linha
                    string += "\t"  # Printa o espaçamento entre os itens
            string += "\n"

        return string

    def __repr__(self):
        return str(self.matriz)

    def __add__(self, other):
        if isinstance(other, Matriz) and self.m == other.m and self.n == other.n:
            soma = Matriz(self.m, self.n)
            soma.matriz = [[self[i][j] + other[i][j] for j in range(self.n)] for i in range(self.m)]
            return soma
        print('Impossível somar')
        return None

    def __mul__(self, other):
        if isinstance(other, (int, float, complex)):
            produto = Matriz(self.m, self.n)
            produto.matriz = [[other * self[i][j] for j in range(self.n)] for i in range(self.m)]

            return produto
        elif isinstance(other, Matriz) and self.n == other.m:
            produto = Matriz(self.m, other.n, 0)

            for i in range(self.m):
                for j in range(other.n):
                    for k in range(self.n):
                        produto[i][j] += self[i][k] * other[k][i]

            return produto
        print('Multiplicação impossível')
        return None

    def __pos__(self):
        return self.copia()

    def __neg__(self):
        return (-1) * self

    def __sub__(self, other):
        return self + (- other)

    def __eq__(self, other):
        if isinstance(other, Matriz):
            if self.m != other.m or self.n != other.n:
                return False

            for i in range(self.m):
                for j in range(self.n):
                    if self[i][j] != other[i][j]:
                        return False

            return True
        return False

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Matriz):
            if self.m * self.n < other.m * other.n:
                return True
            if self.m * self.n > other.m * other.n:
                return False

            for i in range(self.m):
                for j in range(self.n):
                    if self[i][j] != other[i][j]:
                        return self[i][j] < other[i][j]

            return False
        return None

    def __gt__(self, other):
        return other < self

    def __le__(self, other):
        return self < other or self == other

    def __ge__(self, other):
        return self > other or self == other

