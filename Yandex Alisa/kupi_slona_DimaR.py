def insert_blob(photo):
    sqlite_connection = sqlite3.connect('data/for_bot.db')
    cursor = sqlite_connection.cursor()
    # print("Подключен к SQLite")
    try:
        sqlite_insert_blob_query = """INSERT INTO pictures
                                  (pics) VALUES (?)"""

        # res_photo = convert_to_binary_data(photo)
        res_photo = photo

        cursor.execute(sqlite_insert_blob_query, (res_photo,))
        sqlite_connection.commit()
        # print("Изображение успешно вставлено как BLOB в таблицу")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            # print("Соединение с SQLite закрыто")


class PostironyGenerator:
    def init(self):
        pass

    def generate_pics_url(self):
        '''Шайтан машина наполовину стыренная со стаковерфлоу, просто парсит инет по урл ссылке'''
        rw = RandomWord(5)
        rand = rw.generate()

        '''Ссылка с рандомным словом в конце'''
        r = requests.get(f"https://www.google.ru/search?tbm=isch&q={rand}")

        text = r.text

        soup = bs(text, "html.parser")

        '''Возвращаемая конечная ссылка на картинку'''
        res = soup.find_all('img')[random.randint(0, 10)].get('src')
        return res

    def get_picture(self):
        '''Сохраняет в базу данных картинку, полученную по ссылке из generate_pics_url'''
        url = self.generate_pics_url()
        try:
            img = urllib.request.urlopen(url).read()

            insert_blob(img)
        except Exception as e:
            print('We got a mistake:', e, '\n', 'retrying')
            self.get_picture()
