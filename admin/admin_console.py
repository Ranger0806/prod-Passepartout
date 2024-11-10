import smtplib
import sqlite3
from datetime import datetime

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from admin_settings import notifications_password
from admin_settings import notifications_login


class Database:
    def __init__(self):
        self.conn = sqlite3.connect('../db.sqlite3')
        self.cursor = self.conn.cursor()

    def replace_date(self, new_time, id):
        self.cursor.execute("UPDATE 'mainapp_tickets' SET date_start = ? WHERE id = ?",
                            (datetime.strptime(new_time, "%Y-%m-%d").date(), id))
        self.conn.commit()

    def get_user_id(self, id):
        return self.cursor.execute("SELECT user_id FROM 'mainapp_tickets' WHERE id = ?", (id,)).fetchone()[0]

    def get_user_email(self, user_id):
        return self.cursor.execute("SELECT email FROM 'firstapp_projectuser' WHERE id = ?", (user_id,)).fetchone()[0]


def send_notification(notif_login, notif_pwd, user_email, text, theme):
    message = MIMEMultipart()
    message['From'] = notif_login
    message['To'] = user_email
    message['Subject'] = theme
    message.attach(MIMEText(text, 'plain'))

    try:
        smtp_server = smtplib.SMTP('smtp.yandex.ru', 587)
        smtp_server.starttls()
        smtp_server.ehlo()
        smtp_server.login(notif_login, notif_pwd)
        smtp_server.sendmail(notif_login, user_email, message.as_string())
        print("Сообщение успешно отправлено!")
        smtp_server.quit()
    except Exception as err:
        print('Произошла какая-то ошибка!')
        print(err)


def make_new_notification():
    try:
        db = Database()
        id = int(input("Введите id поездки: "))
        new_time = input("Введите новое время (в формате %Y-%m-%d): ")
        db.replace_date(new_time, id)
        user_id = db.get_user_id(id)
        user_email = db.get_user_email(user_id)
        theme = input("Введите тему уведомления: ")
        text = input("Введите текст уведомления: ")
        notif_login = notifications_login
        notif_pwd = notifications_password
        send_notification(notif_login, notif_pwd, user_email, text, theme)
        print("Операция завершена успешно!")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    make_new_notification()
