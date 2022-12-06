import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton
from vk_api.utils import get_random_id
import random

class User:
    __text_information_boss_MajorTrojanVirus = 'Троянские вирусы — Trojan\n' \
                                              'Троянская программа маскируется в других безвредных программах. ' \
                                              'И до того момента как пользователь не запустит эту самую безвредную программу, ' \
                                              'троян не несет никакой опасности и обнаружить его нелегко. Троянская программа может ' \
                                              'нанести различный ущерб для компьютера. В основном трояны используются для кражи, изменения или ' \
                                              'удаления личных данных пользователя. Отличительной особенностью вируса-трояна является то, что он не ' \
                                              'может самостоятельно размножаться.\n\n'

    __text_information_boss_Adware = 'Рекламные вирусы — Adware\n' \
                                   'Программы-рекламы, без ведома пользователей встраиваются в различное программное ' \
                                   'обеспечение с целью демонстрации рекламных объявлений. Как правило, программы-рекламы встроены ' \
                                   'в программное обеспечение, распространяющееся бесплатно. Реклама располагается в рабочем интерфейсе. ' \
                                   'Данные программы также собирают и переправляют своему разработчику персональную информацию о пользователе.\n\n'

    __text_information_boss_Zombie = 'Зомби — Zombie\n' \
                                     'Зомби позволяют злоумышленнику управлять компьютером пользователя. ' \
                                     'Компьютеры – зомби могут быть объединены в сеть  и использоваться для массовой атаки на сайты или рассылки спама. ' \
                                     'Пользователь может даже не догадываться, что его компьютер зомбирован и используется злоумышленником.\n\n'

    __text_information_boss_Rootkit = 'Вирус-маскировщик — Rootkit\n' \
                                      'Маскировщики используются для сокрытия вредоносной активности. Они маскируют вредоносные программы, ' \
                                      'чтобы избежать их обнаружения антивирусными программами. Rootkit’ы также могут модифицировать операционную систему на ' \
                                      'компьютере и заменять основные ее функции, чтобы скрыть свое собственное присутствие и действия, которые предпринимает злоумышленник' \
                                      ' на зараженном компьютере.\n\n'

    def __init__(self, vk_bot):
        self.vk_bot = vk_bot

        self.isBattle_DestructiveTrojanHorse = False
        self.isWin_DestructiveTrojanHorse = False  # Деструктивный троянский конь
        self.isBattle_AdWare = False  # рекламная программа
        self.isWin_AdWare = False
        self.isBattle_Clicker = False
        self.isWin_Clicker = False  # Кликер

        self.isBattle_KeyLogger = False
        self.isWin_KeyLogger = False # Клавиатурный шпион

        self.isBattle_RAT = False
        self.isWin_RAT = False # Программа удаленного администрирования
        self.isBattle_Dropper = False
        self.isWin_Dropper = False # Клей
        self.isBattle_Rootkit = False
        self.isWin_Rootkit = False # Руткит
        self.isBattle_Hijacker = False
        self.isWin_Hijacker = False # Хиджакер
        self.isBattle_Joke = False
        self.isWin_Joke = False # Шутка
        # боссы
        self.isBattle_boss_MajorTrojanVirus = False
        self.isWin_boss_MajorTrojanVirus = False  # Главный троянский вирус
        self.isBattle_boss_Adware = False
        self.isWin_boss_Adware = False  # Рекламные вирусы

        self.isBattle_boss_lossing = False
        self.isWin_boss_lossing = False # Проигрышный босс

        self.isBattle_boss_Zombie = False
        self.isWin_boss_Zombie = False # Зомби
        self.isBattle_boss_Rootkit = False # Вирус-маскировщик
        self.isWin_boss_Rootkit = False  # Маскировщик
        #обучение
        self.is_meeting_with_a_person = False

        self.text_total_information = ''
        self.target = 'start'

    def get_name(self, user_id):
        id = user_id
        user_get = self.vk_bot.users.get(user_ids=(id))
        user_get = user_get[0]
        return user_get['first_name']  # Имя пользователя

    def send_photo(self, photo_1, user_id):
        global attachment
        upload = vk_api.VkUpload(self.vk_bot)
        photo = upload.photo_messages(photo_1)
        owner_id = photo[0]['owner_id']
        photo_id = photo[0]['id']
        access_key = photo[0]['access_key']
        attachment = f'photo{owner_id}_{photo_id}_{access_key}'
        self.vk_bot.messages.send(user_id=user_id, random_id=get_random_id(), attachment=attachment)

    def send_message_with_target(self, target, user_id, keyboard, message):
        if self.isWin_boss_MajorTrojanVirus or self.isWin_boss_Adware:  # дальше тут дописываем боссов
            keyboard.add_line()
            keyboard.add_button('Общая информация')
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=message,
            keyboard=keyboard.get_keyboard()
        )
        return target

    def send_message(self, user_id, keyboard, message):
        if self.isWin_boss_MajorTrojanVirus or self.isWin_boss_Adware:  # дальше тут дописываем боссов
            keyboard.add_line()
            keyboard.add_button('Общая информация')
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id = get_random_id(),
            message = message,
            keyboard = keyboard.get_keyboard()
        )

    def send_message_not_buttons(self, user_id, message):
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            message=message
        )

    def add_button_start(self, user_id, keyboard):
        self.vk_bot.messages.send(
            user_id=user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard()
        )

    # мини-боссы
    def choice_boss_or_mini_boss(self, user_id):
        if self.isWin_DestructiveTrojanHorse and not self.isWin_boss_MajorTrojanVirus:
            self.isBattle_boss_MajorTrojanVirus = True
            keyboard = VkKeyboard()
            keyboard.add_button('Бой')
            self.target = self.send_message_with_target(
                'is_battle_boss_MajorTrojanVirus', user_id, keyboard,
                'Программа кажется абсолютно обычной, но стоит вам подойти ближе как перед вами возникает БОСС-Главный троянский вирус.')
        elif self.isWin_AdWare and self.isWin_Clicker and not self.isWin_boss_Adware:
            self.isBattle_boss_Adware = True
            self.target = 'is_battle_boss_Adware'
        else:
            while True:
                mini_boss = random.randint(0, 2)
                if mini_boss == 0 and not self.isWin_DestructiveTrojanHorse:
                    break
                elif mini_boss == 1 and not self.isWin_AdWare:
                    break
                elif mini_boss == 2 and not self.isWin_Clicker:
                    break
            if mini_boss == 0:
                self.isBattle_DestructiveTrojanHorse = True
                keyboard = VkKeyboard()
                keyboard.add_button('Напасть')
                keyboard.add_line()
                keyboard.add_button('Попытаться незаметно ускользнуть')
                self.target = self.send_message_with_target(
                    'is_battle_mini-boss_DestructiveTrojanHorse', user_id, keyboard,
                    'Вы явно не самый везучий, ведь путь вам преградил не кто иной, как деструктивный троянский конь. В школе на занятиях по информатике вам рассказывали о самых распространённых компьютерных вирусах, поэтому ты легко опознал в существе врага')
            elif mini_boss == 1:
                self.isBattle_AdWare = True
                keyboard = VkKeyboard()
                keyboard.add_button('Бой')
                self.target = self.send_message_with_target(
                    'is_battle_mini-boss_AdWare', user_id, keyboard,
                    'Наткнувшись на иконку браузера вы заметили возле него Рекламную программу считывающую полную информацию о вас')
            elif mini_boss == 2:
                self.isBattle_Clicker = True
                keyboard = VkKeyboard()
                keyboard.add_button('Бой')
                self.target = self.send_message_with_target('is_battle_mini-boss_Clicker', user_id, keyboard, 'Перед вами появляется программа Кликер который занимается рассылкой спама, содержащий потенциально опасные приложения')

    def battle_DestructiveTrojanHorse(self, text, user_id):
        if self.target == 'is_battle_mini-boss_DestructiveTrojanHorse':
            if text == 'Напасть' or text == 'Попытаться незаметно ускользнуть' or text == 'Начать бой сначала':
                if text == 'Попытаться незаметно ускользнуть':
                    self.send_message_not_buttons(user_id, 'Упс, Но кажется, вам не удалось остаться незамеченным, так что убежать уже не представляется возможным ')

                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')

                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'На вид кажущаяся безобидной программой, Деструктивный троянский конь несет в себе немало вреда. '
                                                               'Чтобы попасть в ваше устройство он использовал маскировку, но с недавнего времени он начал свою '
                                                               'беспощадную атаку.')
                self.send_message_not_buttons(user_id, '1. Выполнить полную проверку системы и удалить вредоносное ПО')
                self.send_message_not_buttons(user_id, '2. Удалить корневую папку где находился вирус, подождать некоторое время, вдруг вирус сам испариться')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse_choice', user_id, keyboard, '3. Остановить программу через диспетчер задач')
        elif self.target == 'is_battle_mini-boss_DestructiveTrojanHorse_choice':
            if text == '1':
                self.isWin_DestructiveTrojanHorse = True
                self.isBattle_DestructiveTrojanHorse = False  # победили мини-босса, открыли путь к боссу
                self.isBattle_boss_MajorTrojanVirus = True
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить путь')
                self.target = self.send_message_with_target('boss_1', user_id, keyboard, 'Поздравляем вы уничтожили своего первого противника, но впереди еще долгое путешествие, наберитесь сил и отправляйтесь дальше')
            elif text == '2':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id, keyboard, 'Похоже, что удаление папки только разозлило деструктивного троянского коня. Разъярённый, он бросился на вас. Вы проиграли, но не отчаивайтесь и попробуйте ещё раз.')
            elif text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id, keyboard, 'Вы остановили программу, но не самого вируса. Попробуйте ещё раз.')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, 'Подсказка: Если троянская программа проникла на Ваше устройство, то самый универсальный способ избавиться от нее и восстановить прежнюю функциональность системы это выполнить полную проверку системы с помощью эффективной программы, способной автоматически удалять вредоносное ПО.')

    def battle_boss_MajorTrojanVirus(self, text, user_id):
        if self.target == 'boss_1':
            if text == 'Продолжить путь':
                keyboard = VkKeyboard()
                keyboard.add_button('Опознать врага')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard, 'Вы не успели отдышаться, как на вашем пути появилась новая неизвестная программа.')
        elif self.target == 'is_battle_boss_MajorTrojanVirus':
            if text == 'Опознать врага' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'Программа кажется идентичной предыдущей, но стоит вам приглядеться, как вы понимаете, '
                                                         'что этот соперник гораздо больше, из это неудивительно, ведь перед вами Главный троянский вирус. '
                                                         'Он наносит первый удар настолько неожиданно, что вы не успели среагировать. К счастью нанести вам большой '
                                                         'урон у врага не получилось, и уже вы предпринимаете попытку атаковать. Так как вы уже встречались с трояном '
                                                         'вы решили попробовать сделать то же самое, "выполнить полную проверку системы и удалить вредоносное ПО", '
                                                         'но босс не так прост, чтобы убрать его с устройства нужно больше усилий.')
                self.send_message_not_buttons(user_id, '1. Попытаться проникнуть внутрь коня изнутри его уничтожить')
                self.send_message_not_buttons(user_id, '2. Отключить питание устройства и запустить его снова')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus_choice', user_id, keyboard, '3. Установить утилиту для удаления троянских коней')
        elif self.target == 'is_battle_boss_MajorTrojanVirus_choice':
            if text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Запуск антивируса')
                self.target = self.send_message_with_target('Запуск антивируса для удаления остатков коней', user_id, keyboard, 'Ого! Ваши действия нанесли сильный вред противнику, троян почти уничтожен, но остался последний удар, чтобы его добить.')
                self.send_message_not_buttons(user_id, 'Запуск антивируса для удаления остатков коней')
            elif text == '1':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard, 'Вы оказались очень ловким и смогли проникнуть внутрь, '
                                                     'но там вам не удалось нанести врагу значительный урон, несмотря на все ваши удары')
            elif text == '2':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_boss_MajorTrojanVirus', user_id, keyboard,
                                  'Похоже это было бесполезным действием, так как после того как вы перезапустили компьютер, монстр остался на том же месте')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, '(Подсказка: Если троянская программа проникла на Ваше устройство, '
                                                       'то самый универсальный способ избавиться от нее и восстановить прежнюю функциональность системы '
                                                       'это выполнить полную проверку системы с помощью эффективной программы, способной автоматически удалять '
                                                       'вредоносное ПО.)')
        elif self.target == 'Запуск антивируса для удаления остатков коней' and text == 'Запуск антивируса':
            self.isWin_boss_MajorTrojanVirus = True
            self.isBattle_boss_MajorTrojanVirus = False
            self.is_meeting_with_a_person = True
            keyboard = VkKeyboard()
            self.text_total_information += self.__text_information_boss_MajorTrojanVirus
            keyboard.add_button('Отправиться дальше')
            self.target = self.send_message_with_target('meeting_with_a_person', user_id, keyboard, 'Поздравляем вы полностью избавились от троянских вирусов, '
                                                   'теперь вам доступна полная информация о них(теперь вы можете увидеть '
                                                   'всю информацию о вирусе, нажавав кнопку "Общая информация")')

    def meeting_with_a_person(self, user_id, text):
        if self.target == 'meeting_with_a_person' and text == 'Отправиться дальше':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')
            self.target = self.send_message_with_target('Выбрать_от_1_до_3', user_id, keyboard, 'Немного передохнув, вы двинулись дальше, но '
                                                                                                'пройдя совсем немного заметили, как на встречу вам бежит ещё '
                                                                                                'один совершенно незнакомый вам человечек')
            self.send_message_not_buttons(user_id, '(1) Остановиться и подождать ')
            self.send_message_not_buttons(user_id, '(2) Зачем нам ещё один бой? Попробовать убежать ')
            self.send_message_not_buttons(user_id, '(3) Этот мир не очень дружелюбный, не помешает подготовиться к битве')

        elif self.target == 'Выбрать_от_1_до_3' and (text == '1' or text == '2' or text == '3'):
            if text == '1':
                self.send_message_not_buttons(user_id, 'Через пару секунд существо нагнало вас, запыхавшись он начал говорить:')
            elif text == '2':
                self.send_message_not_buttons(user_id, 'Вы развернулись и даже успели сделать несколько шагов, после чего услышали как '
                                                       'вас окликнули по имени и остановились. Вам стало любопытно, откуда этому лицу известно ваше имя. '
                                                       'Решив разобраться в этой ситуации, вы развернулись и настороженно стали ждать, когда человечек подойдёт ближе.\n'
                                                       'Долго ждать не пришлось, и уже через несколько секунд он был около вас. Остановившись, он оглядел вас и начал говорить:')
            elif text == '3':
                self.send_message_not_buttons(user_id, 'Морально настроившись на ещё один бой, вы встали в оборонительную позицию. Приблизившись к вам на расстояние нескольких шагов, '
                                                       'человечек остановился, оглядел вас и, примирительно подняв руки, сказал: ')
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')
            self.send_message(user_id, keyboard, '«{user}, я очень рад, что ты принял моё приглашение и пришёл помочь освободить '
                                                 'наш мир от непрошенных гостей. Судя по твоему виду, ты уже встретил кого-то из наших недоброжелателей. '
                                                 'Хорошо, что ты не пострадал! Ой, я совсем забыл представиться, меня зовут Cmd, надеюсь, мы быстро подружимся '
                                                 'и вместе одолеем всех вирусов.»'.format(user=self.get_name(user_id)))
            self.send_message_not_buttons(user_id, '(1) «А что здесь произошло, почему в моём компьютере одновременно оказалось столько вредоносных программ?» ')
            self.send_message_not_buttons(user_id, '(2) «И как нам справиться со всеми врагами?»')
            self.send_message_not_buttons(user_id, '(3) «Рад знакомству, какие будут предложения, что делать дальше?»')
            self.target = 'Дальнейшее развитие'
        elif self.target == 'Дальнейшее развитие' and (text == '1' or text == '2' or text == '3'):
            keyboard = VkKeyboard()
            keyboard.add_button('Что для этого нужно?')
            self.target = self.send_message_with_target('Что для этого нужно?', user_id, keyboard, '«Ты сидишь но многих незащищённых сайтах, скачиваешь с них различные файлы, а вместе с ними и вирусы разных видов. С каждым днём они становятся всё хитрее и изворотливее, иногда могут долгое время оставаться незаметными, усыпляя бдительность систем ПО и поджидая удобного случая напасть. Даже современные антивирусы не всегда успевают за их эволюцией. Таким образом на твоём компьютере появлялось всё больше и больше вредоносных программ, что привело к тому, что сейчас необходимо провести экстренную зачистку.»')
        elif self.target == 'Что для этого нужно?' and text == 'Что для этого нужно?':
            keyboard = VkKeyboard()
            keyboard.add_button('И где находится эта папка?')
            self.target = self.send_message_with_target('И где находится эта папка?', user_id, keyboard, '«В первую очередь тебе надо пробраться в корневую папку и найти там архив с фалами паролей. Их нужно изменить, чтобы вирусы больше не могли иметь доступ к любым файлам и операциям. Сейчас корневая папка находится под контролем зомби, поэтому будь готов к сражению. Также тебе стоит знать, что в нашем мире вирусы разделились на боссов и их помощников. Так что для того, чтобы разобраться со всеми вредителями, надо уничтожить их главаря.»')
        elif self.target == 'И где находится эта папка?' and text == 'И где находится эта папка?':
            self.send_message_not_buttons(user_id, '«Чтобы добраться до неё тебе следует идти по этой дороге через несколько других папок, если будешь быстро идти, то потребуется совсем немного времени, но будь осторожен, нельзя предсказать, что тебя ждёт на этом пути. У меня самого ещё есть дела, поэтому не могу пойти с тобой, но я верю, что ты со всем справишься! Встретимся позже.»')
            self.send_message_not_buttons(user_id, 'После этих слов ваш новый приятель сделал молниеносный рывок и скрылся за ближайшим поворотом.')
            self.send_message_not_buttons(user_id, 'Вы же постояли некоторое время на месте, обдумывая всё только что услышанное, и только после пары минут активной мозговой деятельности пришли к выводу, что нужно попытаться освободить свой компьютер от этих нежелательных гостей, и двинулись в указанном направлении.')
            keyboard = VkKeyboard()
            keyboard.add_button('Опознать программу')
            self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Поначалу всё было спокойно, неподвижную тишину нарушал только звук ваших шагов. Направление вашего движения подсказывали указатели, расставленные на какой развилке. Вы уже даже успели подумать, что всё не так страшно, как показалось изначально, как вдруг прямо перед вами материализовалась какая-то программа.')
            self.is_meeting_with_a_person = False
            self.isBattle_Rootkit = True

    #Руткит
    def battle_Rootkit(self, text, user_id):
        if self.target == 'mini-boss_Rootkit':
            if text == 'Опознать программу' or text == 'Начать бой сначала' or text == 'Продолжить':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_line()
                keyboard.add_button('3')
                keyboard.add_button('4')
                keyboard.add_button('5')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id,
                                                  'Небольшой анализ позволил вам определить, что вы столкнулись с Руткитом. Используя эффект неожиданности, противник нанёс удар, но, благодаря молниеносной реакции, вам удалось увернуться, и удар прошёл мимо. ')
                    self.send_message_not_buttons(user_id,
                                                  'Похоже, что руткит серьёзно настроен устранить вас, поэтому избежать сражения не представляется возможным. Стоит попробовать ответить обидчику.')

                self.send_message_not_buttons(user_id, '1. Удалить все файлы руткита которые сразу заметны')
                self.send_message_not_buttons(user_id, '2. Позволить антивирусу разобраться')
                self.send_message_not_buttons(user_id, '3. Провести полный анализ системы и очистить все глубокие источники руткита')
                self.send_message_not_buttons(user_id, '4. Переустановить операционную систему')
                self.target = self.send_message_with_target('mini-boss_Rootkit_choice', user_id, keyboard, '5. Сбросить настройки системы')
        elif self.target == 'mini-boss_Rootkit_choice':
            if text == '1':
                #переходим к проигрышному боссу
                if not self.isWin_boss_lossing:
                    self.isBattle_Rootkit = False
                    self.isBattle_boss_lossing = True
                    keyboard = VkKeyboard()
                    keyboard.add_button('Продолжить')
                    self.target = self.send_message_with_target('boss_lossing', user_id, keyboard, 'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита ')
                else:
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать бой сначала')
                    self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита')
            elif text == '2':
                if not self.isWin_boss_lossing:
                    # переходим к проигрышному боссу
                    self.isBattle_Rootkit = False
                    self.isBattle_boss_lossing = True
                    keyboard = VkKeyboard()
                    keyboard.add_button('Продолжить')
                    self.target = self.send_message_with_target('boss_lossing', user_id, keyboard, 'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
                else:
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать бой сначала')
                    self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
            elif text == '4':
                if not self.isWin_boss_lossing:
                    # переходим к проигрышному боссу
                    self.isBattle_Rootkit = False
                    self.isBattle_boss_lossing = True
                    keyboard = VkKeyboard()
                    keyboard.add_button('Продолжить')
                    self.target = self.send_message_with_target('boss_lossing', user_id, keyboard, 'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
                else:
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать бой сначала')
                    self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
            elif text == '5':
                if not self.isWin_boss_lossing:
                    # переходим к проигрышному боссу
                    self.isBattle_Rootkit = False
                    self.isBattle_boss_lossing = True
                    keyboard = VkKeyboard()
                    keyboard.add_button('Продолжить')
                    self.target = self.send_message_with_target('boss_lossing', user_id, keyboard, 'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
                else:
                    keyboard = VkKeyboard()
                    keyboard.add_button('Начать бой сначала')
                    self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
            elif text == '3':
                # Победа!!
                self.isWin_Rootkit = True
                self.isBattle_Rootkit = False
                self.isBattle_KeyLogger = True
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('mini_boss_KeyLogger', user_id, keyboard, 'Только руткит собрался ударить ещё раз, как начал распадаться на мелкие частички и через пару секунд совсем исчез')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, '(Подсказка): Руткит обычно прячется глубоко в недрах операционной системы и специально написаны таким образом, чтобы избегать обнаружения антивирусом')

    #проигрышный босс
    def battle_lossing_boss(self, text, user_id):
        if self.target == 'boss_lossing':
            if text == 'Продолжить':
                keyboard = VkKeyboard()
                keyboard.add_button('Снова включить компьютер')
                keyboard.add_line()
                keyboard.add_button('Закончить игру')
                self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard, 'Вы оказались снова у себя в комнате, а компьютер перед вами выключен.')
        elif self.target == 'boss_lossing_choice':
            if text == 'Снова включить компьютер' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_line()
                keyboard.add_button('3')
                keyboard.add_button('4')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'Как только вы нажали кнопку включения, компьютер сразу затянул вас внутрь. Но ввести пароль для входа вам мешает ещё один вирус, спулер. Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?')
                self.send_message_not_buttons(user_id, '1. Проведу полный анализ системы и очистить все глубокие источники руткита')
                self.send_message_not_buttons(user_id, '2. Удалю все заметные файлы руткита ')
                self.send_message_not_buttons(user_id, '3. Переустановлю операционную систему')
                self.target = self.send_message_with_target('boss_lossing_choice_2', user_id, keyboard, '4. Сброшу настройки системы')
            elif text == 'Закончить игру':
                # заканчиваем игру
                # доработать !!!!!!!!
                self.target = 'the_end'
                self.isBattle_boss_lossing = False
        elif self.target == 'boss_lossing_choice_2':
            if text == '1':
                # Победа!!
                self.isBattle_boss_lossing = False
                self.isWin_boss_lossing = True
                self.isBattle_Rootkit = True
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard, 'Прекрасно! Вы справились с шпионом на вашем компьютере и можете продолжить свой путь.')
            elif text == '2' or text == '3' or text == '4':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard, 'Похоже, что ваши действия не возымели действия, стоит попробовать сделать что-то другое')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, '(Подсказка): Руткит обычно прячется глубоко в недрах операционной системы и специально написаны таким образом, чтобы избегать обнаружения антивирусом')

    def battle_KeyLogger(self, text, user_id):
        if self.target == 'mini_boss_KeyLogger':
            if text == 'Продолжить':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                self.send_message_not_buttons(user_id, 'Дальнейший ваш путь прошёл без происшествий. Вы уже видите указатель на корневую папку, но тут ваш взгляд привлек к себе небольшой странный комок, состоящий из проводов.')
                self.send_message_not_buttons(user_id, 'Подойдя чуть ближе, вы смогли разглядеть, что узел проводов подключён к самому компьютеру и перекачивает ваши данные. Скорее всего, это клавиатурный шпион. Как поступите?')
                self.send_message_not_buttons(user_id, '1. Пройду мимо, незачем отвлекаться от намеченной цели, сейчас есть дела поважнее')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard, '2. Нельзя позволять вирусам так безнаказанно воровать информацию у меня под носом!')
        elif self.target == 'mini_boss_KeyLogger_choice':
            if text == '1':
                # убежали
                self.isBattle_KeyLogger = False
                self.target = 'the_end'
            elif text == '2' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_line()
                keyboard.add_button('3')
                keyboard.add_button('4')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'Что предпримите?')
                self.send_message_not_buttons(user_id, '1. Установлю антишпионский продукт')
                self.send_message_not_buttons(user_id, '2. Буду всегда вводить пароли вручную')
                self.send_message_not_buttons(user_id, '3. Буду сохранять пароли и вводить их на любых сайтах, даже не очень защищённых')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice_2', user_id, keyboard, '4. Обновлю систему и программные продукты и в будущем буду делать так регулярно')
        elif self.target == 'mini_boss_KeyLogger_choice_2':
            if text == '1' or text == '4':
                # ждём продолжения сюжета
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.isBattle_KeyLogger = False
                self.target = self.send_message_with_target('the_end', user_id, keyboard, 'К огромному сожалению вируса, вам удалось перекрыть ему доступ к данным, так что делать ему здесь больше нечего и он просто быстро уполз ')
            elif text == '2':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard, 'Данные действия только упростили вирусу задачу, стоит попробовать что-то другое')
            elif text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard, 'Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, '(Клавиатурный шпион(KeyLogger)- это отслеживание нажатий каждой клавиши клавиатуры, поэтому ввод паролей на незащищенных сайтах и ввод его в ручную является грубой ошибкой при пользовании устройством)')

    #с сюжетом доработать включая задержку
    def battle_AdWare(self, text, user_id):
        if self.target == 'mini_boss_2':
            keyboard = VkKeyboard()
            keyboard.add_button('Бой')
            self.target = self.send_message_with_target('is_battle_mini-boss_AdWare', user_id, keyboard, 'Наткнувшись на иконку браузера вы заметили возле него '
                                                                                                         'Рекламную программу считывающую полную информацию о вас')
        elif self.target == 'is_battle_mini-boss_AdWare':
            if text == 'Бой' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'Недолго думая вы решили настоятельно уничтожить программу')
                self.send_message_not_buttons(user_id, '1. Удалить браузер')
                self.send_message_not_buttons(user_id, '2. Использовать панель управления для удаления вредоносного ПО')
                self.send_message(user_id, keyboard, '3. Сбросить все настройки браузера, обнулить операционную систему')
            elif text == '2':
                self.isBattle_AdWare = False
                self.isWin_AdWare = True
                self.isBattle_Clicker = True
                keyboard = VkKeyboard()
                keyboard.add_button('Опознать врага')
                self.target = self.send_message_with_target('Опознать врага', user_id, keyboard, 'Рекламная программа была удалена, вы решили следовать дальше.\n'
                                                                                              'Ваши поиски прерывает новый враг')
            elif text == '1' or text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.send_message(user_id, keyboard,  'Вы проиграли но не отчаивайтесь у вас есть еще один шанс. “Никогда не сдавайся перед трудностями. Все проблемы в жизни проверяют наш характер и делают нас сильнее.”')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, 'Программа для демонстрации рекламных окон, открытия рекламируемых сайтов. Помимо этого может следить за действиями пользователя (посещенные сайты, введенные строки для поиска) и работать совместно с другими вредоносными программами.')

    #с сюжетом доработать включая задержку
    def battle_Clicker(self, text, user_id):
        if self.target == 'Опознать врага':
            keyboard = VkKeyboard()
            keyboard.add_button('Бой')
            self.target = self.send_message_with_target('is_battle_mini-boss_Clicker', user_id, keyboard, 'Перед вами появляется программа Кликер который занимается '
                                                                                                          'рассылкой спама, содержащий потенциально опасные приложения')
        elif self.target == 'is_battle_mini-boss_Clicker':
            if text == 'Бой' or text == 'Начать бой сначала':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                if text == 'Начать бой сначала':
                    keyboard.add_line()
                    keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'Кликер не особо рад вашему присутствию')
                self.send_message_not_buttons(user_id, '1. Удалить весь спам собственноручно')
                self.send_message_not_buttons(user_id, '2. Установить утилиту против кликера')
                self.send_message(user_id, keyboard, '3. Написать товарищам, что ваши сообщения спам')
            elif text == '2':
                self.isWin_Clicker = True
                self.isBattle_Clicker = False
                self.isBattle_boss_Adware = True
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('is_battle_boss_Adware', user_id, keyboard, 'Кликер был уничтожен')
            elif text == '1' or text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.send_message(user_id, keyboard, 'Вы проиграли но не отчаивайтесь у вас есть еще один шанс. '
                                                   '“Никогда не сдавайся перед трудностями. Все проблемы в жизни проверяют наш характер и делают нас сильнее.”')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, 'Программа, для накручивания счетчиков (посещения страниц, показа баннеров), увеличения популярности сайта в '
                                                       'поисковиках, несанкционированно использует ресурсы компьютера, увеличивает трафик, тем самым приводят '
                                                       'к нарушению работы ЭВМ или их сети.')

    # не доделан босс снизу boss_Adware
    #с сюжетом доработать включая задержку
    def battle_boss_Adware(self, text, user_id):
        if self.target == 'is_battle_boss_Adware':
            if text == 'Продолжить' or text == 'Начать бой сначала' or text == 'Продолжить':
                keyboard = VkKeyboard()
                keyboard.add_button('1')
                keyboard.add_button('2')
                keyboard.add_button('3')
                if text == 'Начать бой сначала':
                        keyboard.add_line()
                        keyboard.add_button('Подсказка')
                else:
                    self.send_message_not_buttons(user_id, 'После сражений перед вами появляются все рекламные вирусы. '
                                                           'Вы решили использовать полученные знания, но ваши попытки были тщетны, '
                                                           'этот босс оказался не так прост.')
                self.send_message_not_buttons(user_id, '1. Сброс настроек и удаление вредоностного ПО')
                self.send_message_not_buttons(user_id, '2. Удалить вирусы по одному')
                self.send_message(user_id, keyboard, '3. Установить новый браузер')
            if text == '1':
                self.isBattle_boss_Adware = False
                self.isWin_boss_Adware = True
                #дополнить, когда появятся новые боссы и мини-боссы
                self.text_total_information += self.__text_information_boss_Adware
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('the_end', user_id, keyboard, 'Поздравляем! Все рекламные вирусы были удалены с устройства.\n'
                                                                                                  'Теперь вы можете увидеть всю информацию о вирусе, нажавав кнопку "Общая информация"')
            elif text == '2' and text == '3':
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.send_message(user_id, keyboard, 'Вы проиграли но не отчаивайтесь у вас есть еще один шанс. '
                                                       '“Никогда не сдавайся перед трудностями. Все проблемы в жизни проверяют наш характер и делают нас сильнее.”')
            elif text == 'Подсказка':
                self.send_message_not_buttons(user_id, 'Программы-рекламы, без ведома пользователей встраиваются в различное программное обеспечение с целью демонстрации рекламных объявлений. Как правило, программы-рекламы встроены в программное обеспечение, распространяющееся бесплатно. Реклама располагается в рабочем интерфейсе. Данные программы также собирают и переправляют своему разработчику персональную информацию о пользователе.')
