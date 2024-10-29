class Fapt:
    def __init__(self, *args):
        self.fapte = args

    def getArguments(self):
        return self.fapte

    def __str__(self):
        return f'Fapt: {self.fapte}'

    def __repr__(self):
        return self.__str__()


class Structura:
    def __init__(self, *args):
        self.domeniu = [x for xs in args for x in xs.getArguments()]

    def extend(self, fapt):
        self.domeniu.append(fapt)

    def getDomain(self):
        return self.domeniu

    def __str__(self):
        return f'Domeniu: {self.domeniu}'


class Tree:
    def __init__(self, fapt: Fapt, *others):
        self.fapt = fapt
        self.trees = others

    def getSuccessors(self):
        res = [x.getFapt() for x in self.trees]
        return res

    def check_negative(tree, x):
        if x in tree.fapt.getArguments():
            return False
        for succ in tree.getSuccessors():
            if not Tree.check_negative(succ,x):
                return False
        return True

    def search(tree, x):
        global seen
        if x in tree.fapt.getArguments():
            seen=True
            for e in tree.getSuccessors():
                if not Tree.pos_until_not(e,x):
                    return False
        else:
            for e in tree.getSuccessors():
                if seen:
                    if not Tree.check_negative(e,x):
                        return False
                else:
                    if not Tree.search(e,x):
                        return False
        return True

    def getStructure(self):
        structura = Structura()
        structura.extend(self.fapt)
        for succ in self.trees:
            structura.extend(succ.getStructure().domeniu)
        return structura

    def getFapt(self):
        return self.fapt

    def __str__(self):
        s = ""
        for it in self.trees:
            s += it.fapt.__str__()
            s += " "
        return f'Tree: {s}'

seen = False
f1 = Fapt('r(a,b,c,d,e)')
f2 = Fapt('s(a,b,c,f)')
f3 = Fapt('s(c,d,e,g)')
s = Structura(f1, f2)
tree = Tree(f1, Tree(f2), Tree(f3))
tree2 = Tree(f1, Tree(f2, Tree(f3)))
print(tree2.getStructure())