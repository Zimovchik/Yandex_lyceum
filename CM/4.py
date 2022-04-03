import sqlite3


class BankAccount:

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.op_type = {"replenishment": 1, "withdrawal": -1, "other": 0}

    def balance(self, surname):
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT sum, op_id FROM movement as m
WHERE m.acc_id=(SELECT s.id FROM accounts as s WHERE s.surname='{surname}')""").fetchall()
        cor_res = []
        for i in res:
            i = list(i)
            a = (cur.execute(f"""SELECT type FROM operations as o WHERE o.op_id == {i[1]}""").fetchall())[0][0]
            cor_res.append([i[0], a])
        return sum([int(i[0]) * self.op_type[i[1]] for i in cor_res if i[1] != "other"])

    def operation(self, op_name):
        cur = self.con.cursor()
        res = cur.execute(f"""SELECT acc_id, date FROM movement as m
WHERE m.op_id=(SELECT s.op_id FROM operations as s WHERE s.type='{op_name}')""").fetchall()
        ans = []
        for i in res:
            a = cur.execute(f"""SELECT name, surname FROM accounts as m WHERE id={i[0]}""").fetchall()[0]
            ans.append(" ".join(a[::-1]) + " " + i[1])
        return ans


# q
