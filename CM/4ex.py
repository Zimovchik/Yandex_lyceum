import sqlite3


class AccountingPassengers:
    def __init__(self, namedb):
        self.con = sqlite3.connect(namedb)

    def trip(self, date, nameShip):
        cur = self.con.cursor()
        result = cur.execute(f"""SELECT surname, name, class_id, tickets 
        FROM accounting as acc WHERE acc.date == '{date}' and 
        acc.ship_id=(SELECT s.id FROM ships as s WHERE s.name='{nameShip}')""").fetchall()
        # print(result)
        rs = []
        for row in result:
            tmp = cur.execute(f"""SELECT cost FROM tickets WHERE id=={row[2]}""").fetchall()
            rs.append([row[0], row[1], tmp[0][0] * row[3]])
        cur.close()
        rs = sorted(rs, key=lambda x: (x[0], x[1]))
        result = []
        for row in rs:
            result.append(row[0] + ' ' + row[1] + ', ' + str(row[2]))
        return result

    def date_list(self, date):
        cur = self.con.cursor()
        result = cur.execute(f"""SELECT ship_id, tickets FROM accounting 
        as acc WHERE acc.date == '{date}'""").fetchall()
        ships = {}
        for row in result:
            ships[row[0]] = ships.get(row[0], 0) + row[1]
        shipsW = {}
        for id_ship in ships:
            result = cur.execute(f"""SELECT name FROM ships WHERE id == '{id_ship}'""").fetchall()
            shipsW[result[0][0]] = ships[id_ship]
        cur.close()
        shipsW = sorted(list(shipsW.items()))[::-1]
        # print(ships)
        return shipsW

# ap = AccountingPassengers("steamers.db")
# print(*ap.trip("27/08", "Magnolia"), sep="\n")


# ap = AccountingPassengers("steamers.db")
# print(*ap.date_list("27/08"), sep="\n")
