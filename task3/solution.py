class Person:
    def __init__(self, name, birth_year, gender, mother=None, father=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.mother = mother
        self.father = father
        self.ListOfChildren = []

        if self.mother is not None:
            self.mother.ListOfChildren.append(self)

        if self.father is not None:
            self.father.ListOfChildren.append(self)

    def children(self, **kwargs):
        if kwargs:
            kids = []
            for x in self.ListOfChildren:
                if x.gender == kwargs['gender']:
                    kids.append(x)
            return kids

        else:
            return self.ListOfChildren

    def get_brothers(self):
        FatherKids = set()
        MotherKids = set()

        if self.father is not None:
            FatherKids = {kid for kid in self.father.children()
                          if (kid is not self) and (kid.gender == 'M')}
        if self.mother is not None:
            MotherKids = {kid for kid in self.mother.children()
                          if (kid is not self) and (kid.gender == 'M')}

        allChildren = list(MotherKids.union(FatherKids))
        return allChildren

    def get_sisters(self):
        FatherKids = set()
        MotherKids = set()

        if self.father is not None:
            FatherKids = {kid for kid in self.father.children()
                          if (kid is not self) and (kid.gender == 'F')}

        if self.mother is not None:
            MotherKids = {kid for kid in self.mother.children()
                          if (kid is not self) and (kid.gender == 'F')}

        allChildren = list(MotherKids.union(FatherKids))

        return list(allChildren)

    def is_direct_successor(self, successor):

        if successor in self.ListOfChildren:
            return True

        else:
            return False
