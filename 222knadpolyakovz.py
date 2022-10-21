# Импорт библиотек
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from zxczxc import easy_words, hard_words, parts_2
import random

# токен бота
TOKEN = '5703664330:AAFwKB8J0cZ8lgX8mJAVEsZBDVtKtO1dQSM'


# Начало работы
def start(update, context):
    keyboard = [['Слова', 'Предложения']]

    markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True
    )
    update.message.reply_text('Привет я бот - тест, если хочешь узнать что я'
                              ' могу, жми /help\nМожем приступить к'
                              ' заданиям, для начала выбери тип теста',
                              reply_markup=markup)


# помощь
def help(update, context):
    update.message.reply_text('Я умею выдавать два типа тестов, в первом я '
                              'прошу вас превести слова, а во втором вставить'
                              ' недостающее слово')


# Разветление на тест со соловами и с предложениями
def En_test(update, context):
    if update.message.text == 'Слова':
        keyboard = [['Лёгкий', 'Сложный']]

        markup = ReplyKeyboardMarkup(
            keyboard, one_time_keyboard=False, resize_keyboard=True
        )
        update.message.reply_text('Выберити уровень сложности',
                                  reply_markup=markup)
        return 1
    if update.message.text == 'Предложения':
        update.message.reply_text('Выбрано задание с предложениями.'
                                  ' Начинаем тест.')
        predloj_test(update, context)
        return 5
    else:
        update.message.reply_text('Простите я вас не понимаю')


# Начало теста на слова, с выбранным уровнем сложности
def slova(update, context):
    if update.message.text == 'Лёгкий':
        update.message.reply_text('Выбран лёгкий уровень. Начинаем тест.',
                                  reply_markup=ReplyKeyboardRemove())
        easy_test(update, context)
        return 3

    if update.message.text == 'Сложный':
        update.message.reply_text('Выбран сложный уровень. Начинаем тест.',
                                  reply_markup=ReplyKeyboardRemove())
        hard_test(update, context)
        return 4
    update.message.reply_text('Простите я вас не понимаю')
    return 1


# Первый вопрос, определение констант подсчета
# и рандомно выбранный список слов для теста
def easy_test(update, context):
    global d
    global count
    global i
    i = 0
    count = 0
    d = random.sample(easy_words.easy_word.keys(), 10)
    update.message.reply_text('Как переводится слово ' + d[0] +
                              '?\n/stop чтобы закончить тест раньше')


# Оценка предыдущего ответа, подсчёт правильных ответов, окончание
# теста после 10 вопроса
def easy_test_1(update, context):
    global i
    global count
    if update.message.text == '/stop' or update.message.text == '/start':
        zanogo(update)
        return ConversationHandler.END

    elif update.message.text.lower() in easy_words.easy_word[d[i]]:
        update.message.reply_text('Верно!')
        count += 1
    else:
        update.message.reply_text(
            'Неверно! Правильный ответ - ' + easy_words.easy_word[d[i]][0])
    if i != 9:
        i += 1
        update.message.reply_text('Как переводится слово ' + d[i] +
                                  '?\n/stop чтобы закончить тест раньше')
    else:
        if count > 5:
            tx = 'Вы молодец!'
        else:
            tx = 'Не расстраивайтесь, скоро будет получаться лучше.'
        update.message.reply_text('Тест завершён.\nВаш результат:'
                                  ' ' + str(count) + ' из 10.\n' + tx)
        zanogo(update)
        return ConversationHandler.END


# Первый вопрос, определение констант подсчета
# и рандомно выбранный список слов для теста
def hard_test(update, context):
    global d
    global count
    global i
    i = 0
    count = 0
    d = random.sample(hard_words.hard_word.keys(), 10)
    update.message.reply_text('Как переводится слово ' + d[0] +
                              '?\n/stop чтобы закончить тест раньше')


# Оценка предыдущего ответа, подсчёт правильных ответов, окончание
# теста после 10 вопроса
def hard_test_1(update, context):
    global i
    global count
    if update.message.text == '/stop' or update.message.text == '/start':
        zanogo(update)
        return ConversationHandler.END
    elif update.message.text.lower() in hard_words.hard_word[d[i]]:
        update.message.reply_text('Верно!')
        count += 1
    else:
        update.message.reply_text(
            'Неверно! Правильный ответ - ' + hard_words.hard_word[d[i]][0])
    if i != 9:
        i += 1
        update.message.reply_text('Как переводится слово ' + d[i] +
                                  '?\n/stop чтобы закончить тест раньше')
    else:
        if count > 5:
            tx = 'Вы молодец!'
        else:
            tx = 'Не расстраивайтесь, скоро будет получаться лучше.'
        update.message.reply_text('Тест завершён.\nВаш результат:'
                                  ' ' + str(count) + ' из 10.\n' + tx)
        zanogo(update)
        return ConversationHandler.END


# Первый вопрос, определение констант подсчета
# и рандомно выбранный список слов для теста
def predloj_test(update, context):
    global d
    global count
    global i
    i = 0
    count = 0
    d = random.sample(parts_2.part_2.keys(), 6)
    markup = kb(d[i])
    update.message.reply_text(
        'Какое слово надо вставить в предлоение:\n' + d[i] +
        '\n/stop чтобы закончить тест раньше',
        reply_markup=markup)


# создание клавиатуры с вариантам ответов, под конкретное предложение
def kb(d):
    d = parts_2.part_2[d]
    keyboard = [[d[0][0]], [d[0][1]], [d[0][2]]]
    markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True
    )
    return markup


# Оценка предыдущего ответа, подсчёт правильных ответов, окончание
# теста после 10 вопроса
def predloj_test_1(update, context):
    global i
    global count
    if update.message.text == '/stop' or update.message.text == '/start':
        zanogo(update)
        return ConversationHandler.END
    elif update.message.text.lower() == parts_2.part_2[d[i]][1][0]:
        update.message.reply_text('Верно!')
        count += 1
    else:
        update.message.reply_text(
            'Неверно! Правильный ответ - ' + parts_2.part_2[d[i]][1][0])
    if i != 5:
        i += 1
        markup = kb(d[i])
        update.message.reply_text(
            'Какое слово надо вставить в предлоение:\n' + d[i] +
            '\n/stop чтобы закончить тест раньше',
            reply_markup=markup)
    else:
        if count > 3:
            tx = 'Вы молодец!'
        else:
            tx = 'Не расстраивайтесь, скоро будет получаться лучше.'
        update.message.reply_text('Тест завершён.\nВаш результат:'
                                  ' ' + str(count) + ' из 6.\n' + tx)
        zanogo(update)
        return ConversationHandler.END


# завершение теста, возвращение в начало диалога
def zanogo(update):
    keyboard = [['Слова', 'Предложения']]
    markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True
    )
    update.message.reply_text('Продолжим занятие?', reply_markup=markup)


# Функция остановки диалога
def stop(update, context):
    keyboard = [['Слова', 'Предложения']]
    markup = ReplyKeyboardMarkup(
        keyboard, one_time_keyboard=False, resize_keyboard=True
    )
    update.message.reply_text('Продолжим занятие?', reply_markup=markup)
    return ConversationHandler.END


# добавить обработчики событий
# dispatcher - диспетчер событий
def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    word_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text, En_test)],
        states={
            1: [MessageHandler(Filters.text, slova)],
            3: [MessageHandler(Filters.text, easy_test_1)],
            4: [MessageHandler(Filters.text, hard_test_1)],
            5: [MessageHandler(Filters.text, predloj_test_1)]
        },
        fallbacks=[CommandHandler("stop", stop)],
    )

    dispatcher.add_handler(word_handler)


# запуск бота
def main():
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    add_handlers(dispatcher)

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
