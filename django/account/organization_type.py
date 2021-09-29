from enum import IntFlag, auto


class OrganizationType(IntFlag):
    M = auto()
    E = auto()
    I = auto()
    C = auto()
    A = auto()
    CLUB = auto()
    DEPARTMENTS = M | E | I | C | A

    @classmethod
    def choices(cls):
        return [
            (cls.M.value, "機械科"),
            (cls.E.value, "電機科"),
            (cls.I.value, "情報科"),
            (cls.C.value, "環境科"),
            (cls.A.value, "建築科"),
            (cls.CLUB.value, "部活動"),
        ]

    @classmethod
    def name_of_value(cls, target_value):
        for e in cls:
            if e.value == target_value:
                return e.name
        return None
