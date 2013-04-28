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

    def is_female(self):
        return self.gender == 'F'

    def is_male(self):
        return self.gender == 'M'

    def siblings(self):
        all_kids = set(self.mother.children() + self.father.children())
        all_kids = all_kids - {self}
        return all_kids

    def get_brothers(self):
        return list(kid for kid in self.siblings() if kid.is_male())

    def get_sisters(self):
        return list(kid for kid in self.siblings() if kid.is_female())

    def is_direct_successor(self, successor):

        if successor in self.ListOfChildren:
            return True

        else:
            return False

