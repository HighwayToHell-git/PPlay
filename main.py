from tkinter import *
from tkinter import ttk

# Импорт функций аудиоплеера
from KagamiPlayer.sound.sound import (
    load_trak,
    get_sound,
    play,
    pause,
    resume,
    stop,
    set_volume
)


# Загружаем список треков
tracks_count = load_trak()

# Текущий трек
current_track = 0

# Состояние проигрывания
playing = False
paused = False


# Создание окна
app = Tk()

app.title("PPlay")
app.geometry("500x230")
app.resizable(False, False)
app.configure(bg="#202020")


# Обновление названия текущего трека
def update_name():
    name = get_sound(current_track)

    if name:
        trackName.config(text=name)


# Выбор трека через список
def select_track(event=None):
    global current_track
    global playing
    global paused

    # Получаем индекс выбранного трека
    current_track = trackList.current()

    # Запускаем трек
    play(current_track)

    playing = True
    paused = False

    playButton.config(text="⏸")

    update_name()


# Кнопка Play / Pause
def play_pause():
    global playing
    global paused


    if playing:
        # Поставить на паузу
        pause()

        playing = False
        paused = True

        playButton.config(text="▶")


    elif paused:
        # Продолжить воспроизведение
        resume()

        playing = True
        paused = False

        playButton.config(text="⏸")


    else:
        # Начать воспроизведение
        play(current_track)

        playing = True
        paused = False

        playButton.config(text="⏸")


    update_name()



# Следующий трек
def next_track():
    global current_track
    global playing
    global paused


    if tracks_count == 0:
        return


    current_track += 1


    # Если дошли до конца списка
    if current_track >= tracks_count:
        current_track = 0


    # Обновляем список
    trackList.current(current_track)

    # Запускаем новый трек
    play(current_track)


    playing = True
    paused = False

    playButton.config(text="⏸")

    update_name()



# Предыдущий трек
def back_track():
    global current_track
    global playing
    global paused


    if tracks_count == 0:
        return


    current_track -= 1


    # Если первый трек - идём в конец списка
    if current_track < 0:
        current_track = tracks_count - 1


    trackList.current(current_track)

    play(current_track)


    playing = True
    paused = False

    playButton.config(text="⏸")

    update_name()



# Изменение громкости
def change_volume(value):
    set_volume(value)



# Выпадающий список треков
trackList = ttk.Combobox(
    app,
    state="readonly",
    width=45
)


# Добавляем треки в список
trackList["values"] = [
    get_sound(i)
    for i in range(tracks_count)
]


trackList.pack(pady=10)


# Обработка выбора трека
trackList.bind(
    "<<ComboboxSelected>>",
    select_track
)



# Название текущего трека
trackName = Label(
    app,
    text="Нет трека",
    bg="#202020",
    fg="white",
    font=("Arial", 12)
)

trackName.pack(pady=5)



# Панель кнопок
panel = Frame(
    app,
    bg="#202020"
)

panel.pack(pady=10)



# Кнопка назад
backButton = Button(
    panel,
    text="◀◀",
    width=8,
    command=back_track
)


# Play/Pause
playButton = Button(
    panel,
    text="▶",
    width=8,
    command=play_pause
)


# Кнопка вперед
nextButton = Button(
    panel,
    text="▶▶",
    width=8,
    command=next_track
)



# Размещение кнопок
backButton.grid(
    row=0,
    column=0,
    padx=5
)


playButton.grid(
    row=0,
    column=1,
    padx=5
)


nextButton.grid(
    row=0,
    column=2,
    padx=5
)



# Текст громкости
volumeLabel = Label(
    app,
    text="Громкость",
    bg="#202020",
    fg="white"
)

volumeLabel.pack()



# Ползунок громкости
volume = Scale(
    app,
    from_=0,
    to=1,
    resolution=0.01,
    orient=HORIZONTAL,
    length=300,
    command=change_volume
)


# Громкость по умолчанию
volume.set(0.5)

volume.pack()



# Запуск программы
app.mainloop()