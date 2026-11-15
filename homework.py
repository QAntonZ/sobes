import sys
from dbm.sqlite3 import error


class stack:
    def __init__(self):
        self.body = []

    def is_empty(self) -> bool:
        if len(self.body) == 0:
            return True
        else:
            return False

    def push(self, item):
        self.body = [item] + self.body
        return

    def pop(self):
        return self.body.pop(0)

    def peek(self):
        return self.body[0]

    def size(self):
        return len(self.body)

def zadacha(spis):
    st = stack()
    skobki = {")" : "(", "]" : "[", '}' : "{"}
    for item in spis:
        if item in skobki.values():
            st.push(item)
        else:
            if len(st.body) == 0 or skobki[item] != st.peek():
                return  ("Не верно")
            else:
                st.pop()
    if st.is_empty() == True:
        return ("Верно")
    else:
        return  ("Не верно")

