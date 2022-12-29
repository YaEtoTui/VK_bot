from vk_api.keyboard import VkKeyboard, VkKeyboardColor, VkKeyboardButton

def battle_DestructiveTrojanHorse(self, text, user_id):
    if self.target == 'is_battle_mini-boss_DestructiveTrojanHorse':
        if text == 'Напасть' or text == 'Попытаться незаметно ускользнуть' or text == 'Начать бой сначала' or text == 'Продолжить':
            if text == 'Попытаться незаметно ускользнуть':
                self.send_message_not_buttons(user_id,
                                              'Упс, Но кажется, вам не удалось остаться незамеченным, так что убежать уже не представляется возможным ')

            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            keyboard.add_button('3')

            if text == 'Начать бой сначала':
                keyboard.add_line()
                keyboard.add_button('Подсказка')
            else:
                self.send_message_not_buttons(user_id,
                                              'На вид кажущаяся безобидной программой, Деструктивный троянский конь несет в себе немало вреда. '
                                              'Чтобы попасть в ваше устройство он использовал маскировку, но с недавнего времени он начал свою '
                                              'беспощадную атаку.')
            self.send_message_not_buttons(user_id, '1. Выполнить полную проверку системы и удалить вредоносное ПО')
            self.send_message_not_buttons(user_id,
                                          '2. Удалить корневую папку где находился вирус, подождать некоторое время, вдруг вирус сам испариться')
            self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse_choice', user_id,
                                                        keyboard, '3. Остановить программу через диспетчер задач')
    elif self.target == 'is_battle_mini-boss_DestructiveTrojanHorse_choice':
        if text == '1':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить путь')
            self.target = self.send_message_with_target('boss_1', user_id, keyboard,
                                                        'Поздравляем вы уничтожили своего первого противника, но впереди еще долгое путешествие, наберитесь сил и отправляйтесь дальше')
        elif text == '2':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'is_battle_mini-boss_DestructiveTrojanHorse'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Похоже, что удаление папки только разозлило деструктивного троянского коня. Разъярённый, он бросился на вас. Вы проиграли, но не отчаивайтесь и попробуйте ещё раз.')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id,
                                                            keyboard,
                                                            'Похоже, что удаление папки только разозлило деструктивного троянского коня. Разъярённый, он бросился на вас. Вы проиграли, но не отчаивайтесь и попробуйте ещё раз.')
        elif text == '3':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'is_battle_mini-boss_DestructiveTrojanHorse'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вы остановили программу, но не самого вируса. Попробуйте ещё раз.')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('is_battle_mini-boss_DestructiveTrojanHorse', user_id,
                                                            keyboard,
                                                            'Вы остановили программу, но не самого вируса. Попробуйте ещё раз.')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          'Подсказка: Если троянская программа проникла на Ваше устройство, то самый универсальный способ избавиться от нее и восстановить прежнюю функциональность системы это выполнить полную проверку системы с помощью эффективной программы, способной автоматически удалять вредоносное ПО.')
    return self

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
            self.send_message_not_buttons(user_id,
                                          '3. Провести полный анализ системы и очистить все глубокие источники руткита')
            self.send_message_not_buttons(user_id, '4. Переустановить операционную систему')
            self.target = self.send_message_with_target('mini-boss_Rootkit_choice', user_id, keyboard,
                                                        '5. Сбросить настройки системы')
    elif self.target == 'mini-boss_Rootkit_choice':
        if text == '1':
            # переходим к проигрышному боссу
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита ')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Вирус проник намного глубже и удаление только заметных файлов не помогли окончательно избавиться от руткита')
        elif text == '2':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Антивирус оказался не самым быстрым вашим другом, а следующий удар руткита всё же достиг задуманной цели и попал в вас')
        elif text == '4':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'К сожалению, переустановка не помогла, и вторым ударом вирус спокойно добил вас')
        elif text == '5':
            if not self.isWin_boss_lossing:
                # переходим к проигрышному боссу
                self.target_return_to_mini_boss = 'mini-boss_Rootkit'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini-boss_Rootkit', user_id, keyboard,
                                                            'Попытка была неплохой, но не самой действенной, ведь после сброса настроек вирус так и остался перед вами, да ещё и с очередным ударом, увернуться от которого уже не представляется возможным ')
        elif text == '3':
            # Победа!!
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('mini_boss_KeyLogger', user_id, keyboard,
                                                        'Только руткит собрался ударить ещё раз, как начал распадаться на мелкие частички и через пару секунд совсем исчез')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка): Руткит обычно прячется глубоко в недрах операционной системы и специально написаны таким образом, чтобы избегать обнаружения антивирусом')
    return self

def battle_lossing_boss(self, text, user_id):
    if self.target == 'boss_lossing':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('Снова включить компьютер')
            keyboard.add_line()
            keyboard.add_button('Закончить игру')
            self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard,
                                                        'Вы оказались снова у себя в комнате, а компьютер перед вами выключен.')
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
                self.send_message_not_buttons(user_id,
                                              'Как только вы нажали кнопку включения, компьютер сразу затянул вас внутрь. Но ввести пароль для входа вам мешает ещё один вирус, Спуфер. Чтобы обратно вернуться в цифровой мир вам следует избавиться от него. Что предпримите?')
            self.send_message_not_buttons(user_id, '1. Буду использую двухфакторную аутентификацию')
            self.send_message_not_buttons(user_id, '2. Дам доступ к личной информации другим')
            self.send_message_not_buttons(user_id, '3. Буду использовать спам-фильтр ')
            self.target = self.send_message_with_target('boss_lossing_choice_2', user_id, keyboard,
                                                        '4. Везде буду использовать один и тот же пароль')
        elif text == 'Закончить игру':
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('the_end', user_id, keyboard,
                                                        'Вы закончили игру! Нажмите, чтобы продолжить')
    elif self.target == 'boss_lossing_choice_2':
        if text == '1' or text == '3':
            self.isWin_boss_lossing = True
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target(self.target_return_to_mini_boss, user_id, keyboard,
                                                        'Прекрасно! Вы справились с шпионом на вашем компьютере и можете продолжить свой путь.')
        elif text == '2' or text == '4':
            keyboard = VkKeyboard()
            keyboard.add_button('Начать бой сначала')
            self.target = self.send_message_with_target('boss_lossing_choice', user_id, keyboard,
                                                        'Похоже, что ваши действия не возымели действия, стоит попробовать сделать что-то другое')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Подсказка): Никогда не следует давать свою личную информацию, использовать один пароль, отвечать на звонки незнакомым людям')
    return self

def battle_KeyLogger(self, text, user_id):
    if self.target == 'mini_boss_KeyLogger':
        if text == 'Продолжить':
            keyboard = VkKeyboard()
            keyboard.add_button('1')
            keyboard.add_button('2')
            self.send_message_not_buttons(user_id,
                                          'Дальнейший ваш путь прошёл без происшествий. Вы уже видите указатель на корневую папку, но тут ваш взгляд привлек к себе небольшой странный комок, состоящий из проводов.')
            self.send_message_not_buttons(user_id,
                                          'Подойдя чуть ближе, вы смогли разглядеть, что узел проводов подключён к самому компьютеру и перекачивает ваши данные. Скорее всего, это клавиатурный шпион. Как поступите?')
            self.send_message_not_buttons(user_id,
                                          '1. Пройду мимо, незачем отвлекаться от намеченной цели, сейчас есть дела поважнее')
            self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                        '2. Нельзя позволять вирусам так безнаказанно воровать информацию у меня под носом!')
    elif self.target == 'mini_boss_KeyLogger_choice':
        if text == '1':
            # убежали
            # Продолжение сюжета, пока ничего не произойдёт
            pass
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
            self.send_message_not_buttons(user_id,
                                          '3. Буду сохранять пароли и вводить их на любых сайтах, даже не очень защищённых')
            self.target = self.send_message_with_target('mini_boss_KeyLogger_choice_2', user_id, keyboard,
                                                        '4. Обновлю систему и программные продукты и в будущем буду делать так регулярно')
    elif self.target == 'mini_boss_KeyLogger_choice_2':
        if text == '1' or text == '4':
            # ждём продолжения сюжета, пока вернет обратно к началу
            keyboard = VkKeyboard()
            keyboard.add_button('Продолжить')
            self.target = self.send_message_with_target('the_end', user_id, keyboard,
                                                        'К огромному сожалению вируса, вам удалось перекрыть ему доступ к данным, так что делать ему здесь больше нечего и он просто быстро уполз ')
        elif text == '2':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_KeyLogger'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Данные действия только упростили вирусу задачу, стоит попробовать что-то другое')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Данные действия только упростили вирусу задачу, стоит попробовать что-то другое')
        elif text == '3':
            if not self.isWin_boss_lossing:
                self.target_return_to_mini_boss = 'mini_boss_KeyLogger'
                keyboard = VkKeyboard()
                keyboard.add_button('Продолжить')
                self.target = self.send_message_with_target('boss_lossing', user_id, keyboard,
                                                            'Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз')
            else:
                keyboard = VkKeyboard()
                keyboard.add_button('Начать бой сначала')
                self.target = self.send_message_with_target('mini_boss_KeyLogger_choice', user_id, keyboard,
                                                            'Кажется, что перекачка пошла ещё быстрее, давайте попытаемся ещё раз')
        elif text == 'Подсказка':
            self.send_message_not_buttons(user_id,
                                          '(Клавиатурный шпион(KeyLogger)- это отслеживание нажатий каждой клавиши клавиатуры, поэтому ввод паролей на незащищенных сайтах и ввод его в ручную является грубой ошибкой при пользовании устройством)')
    return self