from bot_token import *

def send_tutors(msg_id):
  bot.send_photo(msg_id, open('images/tutors/img1.jpg', 'rb'), 'Тьютор ведёт занятия на Василия Гольцова 10')
  bot.send_photo(msg_id, open('images/tutors/img2.jpg', 'rb'), 'Тьютор ведёт занятия на Василия Гольцова 10, Республики 160')
  bot.send_photo(msg_id, open('images/tutors/img3.jpg', 'rb'), 'Тьютор ведёт занятия на Василия Гольцова 10')