﻿define sanya = Character('Саня', color="#f5fcc4")
define sanya_with_surname = Character("[player_name]", color="#f5fcc4")
define pasha = Character('Пашка Запивон', color="#ffcccc")

label start:
    jump first_day

label first_day:
    scene black scen

    play sound "audio/alarm-sound.mp3"
    "*Звук будильника*"
    stop sound

    scene sanya room with fade

    play sound "audio/deep-moan.mp3"
    "*Вздох*"
    stop sound

    "Ну что, день первый пошёл..."
    "Как же меня это всё заебало: эти бесконечные лабораторные работы, сдачи курсачей..."
    "A экзамены так вообще смех какой-то: ты забиваешь на учёбу болт весь семестр, а потом в поте лица пыхтишь без сна над какой-нибудь электротехникой, которая тебе нахрен не сдалась!"
    "Всё бы ничего, но я, конечно, далеко не такого ожидал, когда поступал в универ."
    "Эх, как же хочу вернуться в школьные года, когда ты вечно ищешь способы поднять бабок на алкашку." 
    "Затем идёшь в \"проверенный ларёчек\" и покупаешь литр водки на литр колы в обычные дни, или же литр водки на литр апельсинового сока по праздникам."
    "Сейчас это звучит ужасно, но в этом явно есть своя романтика подростковых лет..."
    "А теперь я уже совсем старый стал, – 20 лет ёпте! Сменил вот недавно паспорт, теперь даже над фоткой в нём не поржать."
    "Господи, как ссать-то охота..."

    scene sanya toilet with fade
        
    play sound "audio/toilet-sound.mp3" volume 0.5
    "*Звук смыва унитаза*"
    stop sound

    scene black scen with fade

    play music "audio/street-music.mp3" 
    $ renpy.pause (5.0)
    scene bus station with fade

    "А я вот иду и думаю: \"а не слишком ли я много пить стал в последнее время?\""
    "Уже будто и не помню себя трезвым..."
    "А вот и мой автобус подъезжает."    
    "Из бесконечного потока мыслей меня смог вытащить только гудок подъезжающего ЛИАЗа."
    sanya "Ладно, пора и честь знать."

    stop music 

    play sound "audio/bus.mp3" volume 0.5
    "*Звук подъезжающего автобуса*"
    stop sound

    play sound "audio/sound-in-bus.mp3" volume 0.5

    scene bus with fade
    "Даже матушку свою довёл."
    "Вчера с мужиками пришли пиво попить, последний день лета проводить, скажем так, а она меня поджидает у туалета и говорит:"
    "\"Хоть бы раз домой вернулся с девчонкой какой-нибудь красивенькой, а не как обычно с парнями в зассаных майках\", — \"Мама, ну мы же панки\"..."
    stop sound

    scene black scen with fade
    play sound "audio/bus.mp3" volume 0.5
    $ renpy.pause (7.5)
    
    scene bus station near nstu with fade
    show pasha neutral with fade

    "Только вышел из автобуса, как тут мне на встречу идёт крупный парень, он явно меня узнал, а вот я его не очень..."
    "Ба-а, так это же Пашка Запивон так за лето подкачался!"
    pasha "Дарова, Саня, как сам, как жизнь? Целое лето тебя не видел же!"
    sanya "Паша, а я же тебя и не узнал сперва, Накачался за лето я вижу!"
    pasha "Да так, самую малость."

    show pasha smiles

    pasha "Слышь, Саня, говорили ты фамилию себе изменил, женился что ли?"
    sanya "Да там свои приколы с этим, ну захотелось мне просто фамилию новую, начать жизнь, знаешь, с чистого листа."
    pasha "А чё имя-то не сменил тогда?"
    sanya "А чё с ним не так? Имя Саня – Заебись!"
    
    $ player_name = "Саня "
    $ player_name_buf = renpy.input("Во дела. Ладно, меченый, как звать-то тебя теперь?", length=16)
    $ player_name_buf = player_name_buf.strip()

    if player_name_buf == "" :
        $ player_name = "Саня Юрченко"
    else :
        $ player_name += player_name_buf
        $ player_name_tmp = player_name_buf

    sanya "[player_name]"
    pasha "О-о-о, панковская фамилия, я вижу! Ну такое дело надо отметить!!"
    pasha "[player_name_buf], пошли сегодня в кефас пиво пить, я тебя ещё за двадцатилетие за уши не тягал!"
    sanya_with_surname "Ну смотри, у меня одна пара, а потом никаких планов. Пошли, конечно, без проблем."
    pasha "Ну всё, патлатый, жду тебя возле курилки после пар."

    hide pasha smiles 
    with dissolve

    $ renpy.pause(1.5)

    show pasha sad 
    with dissolve

    pasha "Как там тебя зовут, ещё раз?"
    
    $ player_name = "Саня "
    $ player_name_buf = renpy.input("Ну я же говорю", length=16)
    $ player_name_buf = player_name_buf.strip()

    if player_name_buf == "" :
        $ player_name = "Саня Юрченко"
        $ player_name_buf = "Юрченко"
    else :
        $ player_name += player_name_buf
    
    if player_name_buf != player_name_tmp :
        pasha "А-а-а, а я-то почему-то запомнил [player_name_tmp], ну ладно, [player_name_buf], теперь никогда не забуду!"
    else :
        pasha "А-а-а, ну я так и запомнил! Давай, [player_name_buf], бывай!"
    
    hide pasha sad
    with dissolve

    $ renpy.pause(1.0)

    