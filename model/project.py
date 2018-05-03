


class Project:

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def __repr__(self):
        return "Project %s:%s" % (self.id, self.name)

    def __eq__(self, other):
        return (self.id == other.id or self.id is None or other.id is None) and self.name == other.name
