import win32debug, sys, os


class D:
    """dict"""
    def __init__(self, d1, d2):
        self.d1 = d1
        self.d2 = d2


class S:
    """slots"""
    __slots__ = 'slot1', 'slot2'

    def __init__(self, s1, s2):
        self.slot1 = s1
        self.slot2 = s2


class DsubD(D):
    """dict, parent dict"""
    def __init__(self, d1, d2, d3):
        D.__init__(self, d1, d2)
        self.d3 = d3


class SsubS(S):
    """slots, parent slots"""
    __slots__ = 'slot3'

    def __init__(self, s1, s2, s3):
        S.__init__(self, s1, s2)
        self.slot3 = s3


class DsubS(S):
    def __init__(self, s1, s2, d3):
        S.__init__(self, s1, s2)
        self.d3 = d3


class SsubD(D):
    __slots__ = 'slot3'

    def __init__(self, d1, d2, s3):
        D.__init__(self, d1, d2)
        self.slot3 = s3


class SsubDS(D, S):
    __slots__ = 'slot3'

    def __init__(self, d1, d2, s1, s2, s3):
        D.__init__(self, d1, d2)
        S.__init__(self, s1, s2)
        self.slot3 = s3


d = D(1, 2)
s = S(1, 2)
dsubd = DsubD(1, 2, 3)
ssubs = SsubS(1, 2, 3)
dsubs = DsubS(1, 2, 3)
ssubd = SsubD(1, 2, 3)
ssubds = SsubDS(1, 2, 3, 4, 5)
win32debug.dump_process("object_details.dmp")