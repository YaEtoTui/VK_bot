import datetime
import sqlite3
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.longpoll import VkLongPoll, VkEventType
import os
from User import User

def check_if_exists(user_id):
    c.execute('SELECT * FROM users_game_bot_VK WHERE user_id = %d' % user_id)
    result = c.fetchone()
    if result is None:
        return False
    return True

def register_new_user(user_id):
    c.execute(
        'INSERT INTO users_game_bot_VK(user_id, target, isWin_boss_lossing, isWin_boss_MajorTrojanVirus, target_return_to_mini_boss) VALUES (%d, "start", %d, %d, "")' % (user_id, 0, 0))
    conn.commit()
    print('User зарегистрирован')

def saved_in_bd(user_id, target, isWin_boss_lossing, isWin_boss_MajorTrojanVirus, target_return_to_mini_boss):
    c.execute('UPDATE users_game_bot_VK SET target="%s", isWin_boss_lossing=%d, isWin_boss_MajorTrojanVirus=%d, target_return_to_mini_boss="%s" WHERE user_id=%d' % (target, isWin_boss_lossing, isWin_boss_MajorTrojanVirus, target_return_to_mini_boss, user_id))
    conn.commit()
    print('Сохранено')

def set_target(user_id):
    c.execute('SELECT target FROM users_game_bot_VK WHERE user_id = %d' % user_id)
    result = c.fetchone()
    return result[0]

def set_isWin_boss_MajorTrojanVirus(user_id):
    c.execute('SELECT isWin_boss_MajorTrojanVirus FROM users_game_bot_VK WHERE user_id = %d' % user_id)
    result = c.fetchone()
    if result[0] != 0:
        return True
    else:
        return False

def set_isWin_boss_lossing(user_id):
    c.execute('SELECT isWin_boss_lossing FROM users_game_bot_VK WHERE user_id = %d' % user_id)
    result = c.fetchone()
    if result[0] != 0:
        return True
    else:
        return False

def set_target_return_to_mini_boss(user_id):
    c.execute('SELECT target_return_to_mini_boss FROM users_game_bot_VK WHERE user_id = %d' % user_id)
    result = c.fetchone()
    return result[0]

def delete_saved_data(user_id):
    c.execute('DELETE FROM users_game_bot_VK WHERE user_id=%d' % user_id)
    conn.commit()
    print('Удалены сохранения')

conn = sqlite3.connect('database.db')
c = conn.cursor()

token = 'vk1.a.2AHnn2z9Pgxy-nKeuPN6fgTyRuRHNk-w6LlQ6AwDdfV2ugW9Un6kVEm5DYdDWUa37xvCC0QZUSOJti-qFF-u6ZCqXGf62qUC9fmnxKZCk-CwRak2n2l1YiMFRZQYHEwQPevp2IZ1JpGidMJDOS7102lnTom8nS3XRJMNFvUubedPTLeR9CT2H93Hb3pJ6BiY'
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk_bot = vk_session.get_api()
dict_targets = {}
print('Скрипт запущен')
while True:
    for event in longpoll.listen():
        try:
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                text = event.text
                user_id = event.user_id

                if not check_if_exists(user_id):
                    register_new_user(user_id)
                    dict_targets[user_id] = User(vk_bot)
                    print('\nНовый игрок: {}'.format(user_id))
                else:
                    print('\nИгрок: {}'.format(user_id))
                    dict_targets[user_id] = User(vk_bot, set_target(user_id), isWin_boss_lossing=set_isWin_boss_lossing(user_id) ,isWin_boss_MajorTrojanVirus=set_isWin_boss_MajorTrojanVirus(user_id), target_return_to_mini_boss=set_target_return_to_mini_boss(user_id))

                if dict_targets[user_id].target == 'start':
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать путешествие')
                    dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Начать_путешествие',
                                                                                                      user_id, keyboard,
                                                                                                      'Приветствую вас {user}, это текстовая игра(квест), все действия выполняются '
                                                                                                      'с помощью кнопок под окном чата, а результаты приходят в виде сообщений и картинок. '
                                                                                                      'Исследуйте мир вашего компьютера, узнавайте что-то новое о вирусах и программах, способных навредить '
                                                                                                      'вашему устройству, получайте подсказки, уничтожайте врагов(вирусы) и сражайтесь с основными врагами-боссами '
                                                                                                      '(главными вирусами).'.format(user=dict_targets[user_id].get_name(user_id)))
                if dict_targets[user_id].target == 'Начать_путешествие' and text == 'Начать путешествие':
                    try:
                        # отправляем фотку(ниже 1 скрин)
                        dict_targets[user_id].send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'fon_2.jpg')), user_id=user_id)
                        dict_targets[user_id].send_message_not_buttons(user_id, 'Вернувшись домой после тяжелого дня, вы замечаете, что на вашу электронную почту '
                                                                                'пришло письмо с незнакомого адреса. Заинтересованные, вы открываете его.')
                    except Exception as exc:
                        print('Картинка не прогрузилась!')
                    finally:
                        keyboard = VkKeyboard()
                        keyboard.add_button('1')
                        keyboard.add_button('2')
                        keyboard.add_button('3')

                        dict_targets[user_id].send_message(user_id, keyboard, 'В тот же миг на ваш компьютер загружается вредоносная программа, которая находилась '
                                                                              'в письме и только и ждала того, чтобы вы его открыли. ')
                        dict_targets[user_id].send_message_not_buttons(user_id, '1. Перезапущу компьютер, и всё будет хорошо')
                        dict_targets[user_id].send_message_not_buttons(user_id, '2. Ой, а что же теперь делать?')
                        dict_targets[user_id].send_message_not_buttons(user_id, '3. Да не может такого быть, приколы какие-то')
                        dict_targets[user_id].target = 'start_1'
                elif dict_targets[user_id].target == 'start_1' and (text == '1' or text == '2' or text == '3'):
                    if text == '1':
                        dict_targets[user_id].send_message_not_buttons(user_id, 'После перезапуска ничего не изменилось, и вирусы всё так же находятся в компьютере')
                    elif text == '3':
                        dict_targets[user_id].send_message_not_buttons(user_id, 'К сожалению это не чья-то глупая шутка, и вирусы действительно заполонили ваш компьютер')
                    keyboard = VkKeyboard()
                    keyboard.add_button('Нажать «Enter»')
                    #картинка
                    try:
                        # отправляем фотку(ниже 1 скрин)
                        dict_targets[user_id].send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'fon_3.png')),
                                                         user_id=user_id)
                    except Exception as exc:
                        print('Картинка не прогрузилась!')
                    finally:
                        dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Нажать «Enter»', user_id, keyboard, 'Вы не сразу заметили сообщение в '
                                                                                                                                       'командной строке, но сейчас обратили внимание. Там следующий текст: «Привет, {user}! У нас плохие времена, '
                                                                                                                                       'компьютеру и так требовалась чистка, а сейчас его захватило большое количество вирусов. Мы очень нуждаемся в тебе, поэтому я, '
                                                                                                                                       'твой cmd, обращаюсь к тебе за помощью, и если ты готов отправиться в недры своего компьютера и разобраться со всеми проблемами, '
                                                                                                                                       'то нажми Enter»'.format(user=dict_targets[user_id].get_name(user_id)))
                elif dict_targets[user_id].target == 'Нажать «Enter»' and text == 'Нажать «Enter»':
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать исследование устройства')
                    dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Начать исследование устройства', user_id, keyboard, 'Вы сами не заметили как, но уже через пару секунд оказались внутри вашего компьютера. Оглядевшись вы поняли, что вокруг запутанный лабиринт из различных папок, плат и сети проводов. Для начала следует изучить окрестности получше')
                elif dict_targets[user_id].target == 'Начать исследование устройства' and text == 'Начать исследование устройства':
                    keyboard = VkKeyboard()
                    keyboard.add_button('Опознать незнакомца')
                    dict_targets[user_id].send_message_not_buttons(user_id, 'После 10 минут плутания вы обнаружили достаточно широкую тропинку, по которой и приняли решение идти')
                    dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('mini-boss_1', user_id, keyboard, 'Но пройдя всего пару шагов и завернув за угол, вы в первый раз в этом мире встречаете живое существо. К счастью пока оно вас не видит')
                # elif text == 'Общая информация':
                #     dict_targets[user_id].send_message_not_buttons(user_id, dict_targets[user_id].text_total_information)

                #1 мини босс - Троянский конь
                elif dict_targets[user_id].target == 'mini-boss_1' and text == 'Опознать незнакомца':
                    try:
                        # отправляем фотку(ниже 1 скрин)
                        dict_targets[user_id].send_photo(photo_1=os.path.abspath(os.path.join('Pictures', 'конь1.png')), user_id=user_id)
                    except Exception as exc:
                        print('Картинка не прогрузилась!')
                    finally:
                        keyboard = VkKeyboard()
                        keyboard.add_button('Напасть')
                        keyboard.add_line()
                        keyboard.add_button('Попытаться незаметно ускользнуть')
                        dict_targets[user_id].target = dict_targets[user_id].send_message_with_target(
                        'is_battle_mini-boss_DestructiveTrojanHorse', user_id, keyboard,
                        'Вы явно не самый везучий, ведь путь вам преградил не кто иной, как деструктивный троянский конь. '
                        'В школе на занятиях по информатике вам рассказывали о самых распространённых компьютерных вирусах, поэтому ты легко опознал в существе врага')
                elif dict_targets[user_id].target == 'is_battle_mini-boss_DestructiveTrojanHorse' or dict_targets[user_id].target == 'is_battle_mini-boss_DestructiveTrojanHorse_choice': # здесь происходит битва с Деструктивный троянский конь
                    dict_targets[user_id].battle_DestructiveTrojanHorse(text, user_id)

                #1 босс - Главный троянский вирус
                elif dict_targets[user_id].target == 'boss_1' or dict_targets[user_id].target == 'is_battle_boss_MajorTrojanVirus' or dict_targets[user_id].target == 'is_battle_boss_MajorTrojanVirus_choice' or dict_targets[user_id].target == 'Запуск антивируса для удаления остатков коней': #здесь происходит битва с БОСС - Главный троянский вирус
                    dict_targets[user_id].battle_boss_MajorTrojanVirus(text, user_id)

                # встреча с человеком(обучение)
                elif dict_targets[user_id].target == 'meeting_with_a_person' or dict_targets[user_id].target == 'Выбрать_от_1_до_3' or dict_targets[user_id].target == 'Дальнейшее развитие' or dict_targets[user_id].target == 'Что для этого нужно?' or dict_targets[user_id].target == 'И где находится эта папка?':
                    dict_targets[user_id].meeting_with_a_person(user_id, text)

                #2 босс - Руткит
                elif dict_targets[user_id].target == 'mini-boss_Rootkit' or dict_targets[user_id].target == 'mini-boss_Rootkit_choice':
                    dict_targets[user_id].battle_Rootkit(user_id=user_id, text=text)

                # проигрышный босс Спуфер
                elif dict_targets[user_id].target == 'boss_lossing' or dict_targets[user_id].target == 'boss_lossing_choice' or dict_targets[user_id].target == 'boss_lossing_choice_2':
                    dict_targets[user_id].battle_lossing_boss(user_id=user_id, text=text)

                #3 мини-босс - Клавиатурный шпион
                elif dict_targets[user_id].target == 'mini_boss_KeyLogger' or dict_targets[user_id].target == 'mini_boss_KeyLogger_choice' or dict_targets[user_id].target == 'mini_boss_KeyLogger_choice_2':
                    dict_targets[user_id].battle_KeyLogger(user_id=user_id, text=text)

                # 4 мини-босс - Хиджакер
                elif dict_targets[user_id].target == 'mini_boss_Hijacker' or dict_targets[user_id].target == 'mini_boss_Hijacker_choice':
                    dict_targets[user_id].battle_Hijacker(user_id=user_id, text=text)

                # 5 мини-босс - Рекламная программа
                elif dict_targets[user_id].target == 'mini_boss_AdWare' or dict_targets[user_id].target == 'mini_boss_AdWare_choice' or dict_targets[user_id].target == 'mini_boss_AdWare_choice_2':
                    dict_targets[user_id].battle_AdWare(user_id=user_id, text=text)

                # 6 мини-босс - Кликер
                elif dict_targets[user_id].target == 'mini_boss_Clicker' or dict_targets[user_id].target == 'mini_boss_Clicker_recognize' or dict_targets[user_id].target == 'mini_boss_Clicker_choice' or dict_targets[user_id].target == 'mini_boss_Clicker_choice_2':
                    dict_targets[user_id].battle_Clicker(user_id=user_id, text=text)

                # 7 мини-босс - Шутка
                elif dict_targets[user_id].target == 'unknown_file' or dict_targets[user_id].target == 'unknown_file_choice':
                    dict_targets[user_id].unknown_file(user_id=user_id, text=text)

                # 8 мини-босс - Программы Удалённого Администрирования
                elif dict_targets[user_id].target == 'mini_boss_RAT' or dict_targets[user_id].target == 'mini_boss_RAT_choice':
                    dict_targets[user_id].battle_RAT(user_id=user_id, text=text)

                # 3 босс - Зомби
                elif dict_targets[user_id].target == 'mini_boss_Zombie' or dict_targets[user_id].target == 'mini_boss_Zombie_choice':
                    dict_targets[user_id].battle_Zombie(user_id=user_id, text=text)

                elif dict_targets[user_id].target == 'the_good_end':
                    if text == 'Продолжить':
                        keyboard = VkKeyboard()
                        keyboard.add_button('Выбраться из устройства')
                        dict_targets[user_id].send_message_not_buttons(user_id, 'После вашей победы открывается командная строка:')
                        dict_targets[user_id].send_message_not_buttons(user_id, '«Ты большой молодец! Тебе удалось уничтожить главного врага. Доступ к твоим данным снова восстановлен, вирусы и их помощники исчезли. Ты можешь вернуться в свой мир, чтобы и дальше жить своей жизнью, но помни про ошибки, которые ты сделал. Думай, прежде чем устанавливать и скачивать неизвестные файлы на своё устройство. Полагаю нам пора прощаться.»')
                        dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('Выбраться из устройства', user_id, keyboard, 'После такой трогательной речи от вашего друга можно было проронить слезу, но вы сдерживаетесь и решаетесь на последний шаг в своем путешествии.')
                elif dict_targets[user_id].target == 'Выбраться из устройства':
                    if text == 'Выбраться из устройства':
                        keyboard = VkKeyboard()
                        keyboard.add_button('Ура!!')
                        dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('final_end', user_id, keyboard, 'Очнувшись в своей комнате, вы понимаете, что ваше приключение окончено и пора возвращаться к повседневной жизни, снова...')
                elif dict_targets[user_id].target == 'final_end':
                    if text == 'Ура!!':
                        try:
                            # отправляем фотку(ниже 1 скрин)
                            dict_targets[user_id].send_photo(
                                photo_1=os.path.abspath(os.path.join('Pictures', 'финал.jpg')), user_id=user_id)
                        except Exception as exc:
                            print('Картинка не прогрузилась!')
                        finally:
                            keyboard = VkKeyboard()
                            keyboard.add_button('Завершить игру')
                            dict_targets[user_id].send_message_not_buttons(user_id, 'Поздравляем, вы смогли справиться со всеми трудностями, уничтожили все вирусы, теперь на вашем устройстве воцарятся мир и процветание, а уровень ваших знаний значительно вырос!')
                            dict_targets[user_id].send_message_not_buttons(user_id, 'Вы способны избавиться от вирусов самостоятельно. Главное, не стоит забывать, что самый простой выбор не всегда самый правильный. Также не бойтесь прибегать к уже  существующим устройствам для удаления вредоносных программ и защиты вашего компьютера, ведь не всегда у вас будет возможность самим залезть в устройство и победить всех врагов.')
                            dict_targets[user_id].send_message_not_buttons(user_id, 'Все истории подходят к концу, и, к сожалению, эта не исключение, но, если у вас будут вопросы, вы всегда можете обратиться к другим источникам для получения новых знаний.')
                            dict_targets[user_id].send_message_not_buttons(user_id, 'На этом моменте пора прощаться.')
                            dict_targets[user_id].target = dict_targets[user_id].send_message_with_target('the_end', user_id, keyboard, 'Над квестом работала команда codEater.')
                #заканчивает игру
                elif dict_targets[user_id].target == 'the_end':
                    if text != 'Общая информация':
                        # заканчиваем игру и начинаем заново
                        delete_saved_data(user_id)
                        keyboard = VkKeyboard()
                        keyboard.add_button('Начать заново')
                        dict_targets[user_id].send_message(user_id, keyboard, 'Нажмите кнопку, чтобы начать игру заново!')


                print('Текущий checkpoint: {}'.format(dict_targets[user_id].target))
                print('Время: {}'.format(datetime.datetime.now()))

                saved_in_bd(user_id, dict_targets[user_id].target, dict_targets[user_id].isWin_boss_lossing, dict_targets[user_id].isWin_boss_MajorTrojanVirus, dict_targets[user_id].target_return_to_mini_boss)

        except Exception as exc:
            print('Возникла ошибка {}'.format(exc))
