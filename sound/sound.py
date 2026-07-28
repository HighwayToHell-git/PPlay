import os
import pygame


# Папка, где лежат музыкальные файлы
folder = os.path.dirname(__file__)


# Список треков
tracks = []


# Инициализация аудиосистемы
pygame.mixer.init()



# Загрузка треков из папки
def load_trak():
    tracks.clear()

    for file in os.listdir(folder):

        # Берём только mp3 файлы
        if file.lower().endswith(".mp3"):
            tracks.append(file)


    return len(tracks)



# Получить название трека
def get_sound(index: int):

    if 0 <= index < len(tracks):
        return tracks[index]

    return None



# Проиграть трек
def play(index: int):

    file = get_sound(index)


    if file:
        path = os.path.join(folder, file)


        # Останавливаем старый трек
        pygame.mixer.music.stop()


        # Загружаем новый
        pygame.mixer.music.load(path)


        # Запускаем
        pygame.mixer.music.play()



# Пауза
def pause():
    pygame.mixer.music.pause()



# Продолжить
def resume():
    pygame.mixer.music.unpause()



# Остановить
def stop():
    pygame.mixer.music.stop()



# Изменить громкость
def set_volume(value):

    pygame.mixer.music.set_volume(
        float(value)
    )