"""Содержит все игровые функции игры Flappy Bird."""

import pygame
import sys
import random

from upper_wall import UpperWall
from lower_wall import LowerWall
from carrot import Carrot

pygame.mixer.init()


def check_events(settings, bird, stats):
    """Реагирует на нажатия клавиш."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_high_score(stats)
            sys.exit()
        if event.type == pygame.KEYDOWN:
            check_keydown_events(event, settings, bird, stats)
        if event.type == pygame.KEYUP:
            check_keyup_events(event, bird)


def check_keydown_events(event, settings, bird, stats):
    """Проверяет нажатия клавиш."""
    if event.key == pygame.K_q:
        save_high_score(stats)
        sys.exit()
    if event.key == pygame.K_SPACE:
        if bird.rect.y > 0:
            play_sound('./sounds/wing/wing.wav')
            bird.rect.y -= settings.jump_height
            bird.anim1()


def check_keyup_events(event, bird):
    """Проверяет отжатие клавиш."""
    if event.key == pygame.K_SPACE:
        bird.anim2()


def update_screen(screen, settings, bird, walls, carrots, sb):
    """Обновляет экран и отрисовывает последний кадр."""
    screen.fill(settings.screen_color)
    sb.show_score()
    # Рисует птицу, стены и морковки
    bird.blit_me()
    walls.draw(screen)
    carrots.draw(screen)
    # Отрисовывает последний кадр.Я
    pygame.display.flip()


def spawn_walls(settings, bird, walls, carrots, sb, stats):
    """Спавнит ряд стен с морковкой, а также проверяет их позиции."""
    if len(walls) == 0:
        spawn_upper_walls(settings, walls)
        spawn_carrots(settings, walls, carrots)
        spawn_lower_walls(settings, walls)
    # Спавнит верхние и нижнее стены, если расстояние от одной пары стен до другой верно.
    elif settings.screen_width - list(walls)[-1].rect.x == settings.distance_between_walls[1]:
        spawn_upper_walls(settings, walls)
        spawn_carrots(settings, walls, carrots)
        spawn_lower_walls(settings, walls)
    check_row_of_walls(bird, walls, carrots, sb, stats)


def check_row_of_walls(bird, walls, carrots, sb, stats):
    """Проверяет достигла ли стена края, проверяет столкнулась ли стена или морковка с птицей."""
    for wall in walls.copy():
        # Проверяет столкновения птицы со стенами.
        if pygame.sprite.spritecollide(bird, walls, False):
            if stats.bird_lives > 0:
                play_sound('./sounds/die/die.wav')
                stats.bird_lives -= 1
                # Очищаем экран.
                clearing_screen(bird, walls, carrots, sb)
            else:
                # Очищаем экран и завершаем игру.
                play_sound('./sounds/die/die.wav')
                clearing_screen(bird, walls, carrots, sb)
                save_high_score(stats)
                stats.game_active = False
        # Удаляет стены, вышедшие за край экрана.
        if wall.rect.right < 0:
            walls.remove(wall)
        check_carrots(bird, carrots, sb, stats)


def play_sound(path_to_file):
    """Загружает и проигрывает звук."""
    pygame.mixer.music.load(path_to_file)
    pygame.mixer.music.play()


def check_carrots(bird, carrots, sb, stats):
    """Проверяет достигла ли морковка края и задела ли птицу."""
    for carrot in carrots.copy():
        # Проверяет столкновение морковки с птицей.
        if pygame.sprite.spritecollide(bird, carrots, True):
            play_sound('./sounds/point/point.wav')
            stats.score += 1
            sb.prep_score()
            sb.prep_high_score()
        # Удаляет морковки, вышедшие за край экрана.
        if carrot.rect.right < 0:
            carrots.remove(carrot)


def save_high_score(stats):
    """Сохраняет текущий рекордный счёт."""
    if stats.score > stats.high_score:
        with open('record.txt', 'w') as record:
            record.write(str(stats.score))


def clearing_screen(bird, walls, carrots, sb):
    """Очищаем экран от стен, морковок и ставим птичу в начальное положение."""
    sb.prep_score()
    walls.empty()
    carrots.empty()
    bird.start_pos()


def spawn_carrots(settings, walls, carrots):
    """Спавнит морковки."""
    carrot = Carrot(settings)
    # Задаём местоположение.
    carrot.rect.centery = list(walls)[-1].height + settings.distance_between_walls[0] / 2
    carrot.rect.left = settings.screen_width + 10
    carrots.add(carrot)


def spawn_upper_walls(settings, walls):
    """Спавнит верхние трубы."""
    upper_wall = UpperWall(settings)
    # Инициализируем высоту стен, затем изменяет размер картинки под данную высоту.
    upper_wall.height = random.randint(100, 600)
    upper_wall.update_image()
    # Задаём начальное положение.
    upper_wall.rect.left = settings.screen_width
    upper_wall.rect.top = 0
    # Добавляем в группу.
    walls.add(upper_wall)


def spawn_lower_walls(settings, walls):
    """Спавнит нижние стены."""
    lower_wall = LowerWall(settings)
    # Инициализируем высоту стен, затем изменяет размер картинки под данную высоту.
    lower_wall.height = settings.screen_height - settings.distance_between_walls[0] - list(walls)[-1].height
    lower_wall.update_image()
    # Задаём начальное положение
    lower_wall.rect.left = settings.screen_width
    lower_wall.rect.bottom = settings.screen_height
    # Добавляем в группу.
    walls.add(lower_wall)
