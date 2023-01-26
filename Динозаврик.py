import pygame
from random import randint
import random
import sys
import os
from PIL import Image

pygame.init()
launch_sound = pygame.mixer.Sound("launch_sound.mp3")
launch_sound.play()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Динозаврик")
pygame_icon = pygame.image.load('dino_icon.png')
pygame.display.set_icon(pygame_icon)
clock = pygame.time.Clock()
file = open('Сообщение для пользователя.txt')
file_read = file.readlines()
file_phrase = []
for i in file_read:
    file_phrase.append(i)
file.close()
file2 = open('best_score.txt')
best_score = file2.readlines()
for i in best_score:
    best_score = i
file2.close()
title_fon = file_phrase[0]
title_fon2 = file_phrase[1]
title_fon3 = file_phrase[2]
title_fon4 = file_phrase[3]
title_fon5 = file_phrase[4]
title_fon6 = file_phrase[5]
title_fon7 = file_phrase[6]
title_fon8 = file_phrase[7]
f4 = pygame.font.SysFont("Minecraft", 30)
name_font = pygame.font.SysFont('Helvetica', 40)
dino_walk1 = pygame.image.load("dino_run1.png").convert_alpha()
dino_walk2 = pygame.image.load("dino_run2.png").convert_alpha()
dino_walk = [dino_walk1, dino_walk2]
dino_index = 0
dino_jump = pygame.image.load("dino_stand.png").convert_alpha()
dino_surf = dino_walk[dino_index]
dino_rect = dino_surf.get_rect(midbottom = (200, 450))
dino_gravity = 0
cactus_frame1 = pygame.image.load("cactus1.png").convert_alpha()
cactus_frame2 = pygame.image.load("cactus2.png").convert_alpha()
cactus_frames = [cactus_frame2, cactus_frame1]
cactus_frame_index = 0
cactus_surf = cactus_frames[cactus_frame_index]
cactus_rect_list = []
cactus_speed = 4
level_sound = pygame.mixer.Sound("sound2.mp3")
jump_sound = pygame.mixer.Sound("sound1.mp3")
dead_sound = pygame.mixer.Sound("dead.mp3")
pause_sound = pygame.mixer.Sound("pause.mp3")
star_sound = pygame.mixer.Sound("star_sound.mp3")
game_sound = pygame.mixer.Sound("game_sound.mp3")
open_sound = pygame.mixer.Sound("open_settings.mp3")
close_sound = pygame.mixer.Sound("close_settings.mp3")
cloud = pygame.image.load("cloud.png").convert_alpha()
cloud_rect = cloud.get_rect(midbottom = (randint(1200, 1500), randint(100, 200)))
cloud_list = []
cloud_rect_list = []
skeleton = pygame.image.load("skeleton.png").convert()
skeleton.set_colorkey((245, 245, 245, 255))
skeleton_rect = skeleton.get_rect(midbottom = (randint(1200, 1500), randint(500, 700)))
skeleton_list = []
skeleton_rect_list = []
skull = pygame.image.load("череп.png").convert_alpha()
skull_rect = skull.get_rect(midbottom = (randint(1200, 1500), randint(500, 700)))
skull_list = []
skull_rect_list = []
game_active = False
width = screen.get_width()
height = screen.get_height()
color = (255, 255, 255)
color_light = (170, 170, 170)
color_dark = (100, 100, 100)
color_black = (0, 0, 0)
smallfont = pygame.font.SysFont('Corbel', 35)
text_play = smallfont.render('Играть', True, color)
text_settings = smallfont.render('Настройки', True, color)
text_play_en = smallfont.render('Play', True, color)
text_settings_en = smallfont.render('Settings', True, color)
text_return = smallfont.render('<--', True, color)
text_sound = smallfont.render('Звук:', True, color)
text_on = smallfont.render('Вкл.', True, color)
text_off = smallfont.render('Выкл.', True, color)
text_sound_en = smallfont.render('Sound:', True, color)
text_on_en = smallfont.render('On', True, color)
text_off_en = smallfont.render('Off', True, color)
text_language = smallfont.render('Язык:', True, color)
text_language_eng = smallfont.render('Language:', True, color)
text_language_rus = smallfont.render('Рус.', True, color)
text_language_rus_en = smallfont.render('Rus.', True, color)
text_language_en = smallfont.render('Engl.', True, color)
text_title = name_font.render(title_fon[:-1], True, (0, 0, 255))
text_title2 = name_font.render(title_fon2[:-1], True, (0, 0, 255))
text_title3 = name_font.render(title_fon3[:-1], True, (0, 0, 255))
text_title4 = name_font.render(title_fon4[:-1], True, (0, 0, 255))
text_title5 = name_font.render(title_fon5[:-1], True, (0, 0, 255))
text_title6 = name_font.render(title_fon6[:-1], True, (0, 0, 255))
text_title7 = name_font.render(title_fon7[:-1], True, (0, 0, 255))
text_title8 = name_font.render(title_fon8[:-1], True, (255, 0, 0))
game_over_font = pygame.font.SysFont('Bullpen3D', 50)
text_game_over_en = game_over_font.render('Game over', True, (255, 0, 0))
text_game_over_ru = game_over_font.render('Игра окончена', True, (255, 0, 0))
text_again_ru = smallfont.render('Заново', True, color)
text_again_en = smallfont.render('Again', True, color)
text_exit_en = smallfont.render('Exit', True, color)
text_exit_ru = smallfont.render('Выйти', True, color)
text_best_en = smallfont.render('Best result:', True, color)
text_best_ru = smallfont.render('Лучший результат:', True, color)
text_score_en = smallfont.render('Points scored:', True, color)
text_score_ru = smallfont.render('Набрано очков:', True, color)
truth_sound = True
truth_language = True
score = 0
GRAVITY = 0.2
screen_rect = (0, 0, width, height)
all_sprites = pygame.sprite.Group()


def massage():
    if truth_language:
        text_massage_space = smallfont.render("Нажмите пробел для прыжка.", True, color_black)
        text_massage_pause = smallfont.render("Нажмите ESC, чтобы поставить игру на паузу.", True, color_black)
        text_massage_speed = smallfont.render("Со временем игра ускоряется!", True, color_black)
    else:
        text_massage_space = smallfont.render("Press the space bar to jump.", True, color_black)
        text_massage_pause = smallfont.render("Press ESC to pause the game.", True, color_black)
        text_massage_speed = smallfont.render("Over time, the game accelerates!", True, color_black)
    screen.blit(text_massage_space, (50, 120))
    screen.blit(text_massage_pause, (50, 200))
    screen.blit(text_massage_speed, (50, 275))


def load_image(name, color_key=None):
    fullname = os.path.join(name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Не удаётся загрузить:', name)
        raise SystemExit(message)
    image = image.convert_alpha()
    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


class Particle(pygame.sprite.Sprite):
    fire = [load_image("star.png")]
    for scale in (5, 10, 20):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()
        self.velocity = [dx, dy]
        self.rect.x, self.rect.y = pos
        self.gravity = GRAVITY

    def update(self):
        self.velocity[1] += self.gravity
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    particle_count = 20
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


class Game():
    def dino_animation(self):
        global dino_surf
        global dino_index
        if dino_rect.bottom < 300:
            dino_surf = dino_jump
        else:
            dino_index += 0.1
            if dino_index >= len(dino_walk):
                dino_index = 0
            dino_surf = dino_walk[int(dino_index)]

    def collisions(self, dino, cactus):
        if cactus:
            for cactus_rect in cactus:
                if dino.colliderect(cactus_rect):
                    return False
        return True

    def display_score(self, scores):
        if truth_language:
            score_surf = f4.render(f'Счет:    {scores}', False, (64, 64, 64))
        else:
            score_surf = f4.render(f'Score:    {scores}', False, (64, 64, 64))
        score_rect = score_surf.get_rect(center = (600, 95))
        screen.blit(score_surf, score_rect)
        return scores

    def cactus_movement(self, cactus_list):
        if cactus_list:
            for cactus_rect in cactus_list:
                cactus_rect.x -= int(cactus_speed)
                screen.blit(cactus_frame1, cactus_rect)
            cactus_list = [obstacle for obstacle in cactus_list if obstacle.x > -100]
            return cactus_list
        else:
            return []

    def cloud_movement(self, cloud_list):
        if cloud_list:
            for cloud_rect in cloud_list:
                cloud_rect.x -= 1
                screen.blit(cloud, cloud_rect)
            return cloud_list
        else:
            return []

    def skeleton_movement(self, skeleton_list):
        if skeleton_list:
            for skeleton_rect in skeleton_list:
                skeleton_rect.x -= 6
                screen.blit(skeleton, skeleton_rect)
            return skeleton_list
        else:
            return []

    def skull_movement(self, skull_list):
        if skull_list:
            for skull_rect in skull_list:
                skull_rect.x -= 6
                screen.blit(skull, skull_rect)
            return skull_list
        else:
            return []

    
def end_screen(scoress):
    pygame.mouse.set_visible(True)
    text_score = smallfont.render(str(scoress), True, color)
    text_best_score = smallfont.render(best_score, True, color)
    gifFrameList = split_animated_gif(r"gif.gif")
    currentFrame = 0
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 690 <= mouse[0] <= 690 + 180 and 530 <= mouse[1] <= 530 + 70:
                    intro()
                if 470 <= mouse[0] <= 470 + 180 and 530 <= mouse[1] <= 530 + 70:
                    pygame.quit()
                    exit()
        pygame.draw.rect(screen, color_black, [450, 100, 450, 520])
        if 690 <= mouse[0] <= 690 + 180 and 530 <= mouse[1] <= 530 + 70:
            pygame.draw.rect(screen, color_light, [690, 530, 180, 70])
        else:
            pygame.draw.rect(screen, color_dark, [690, 530, 180, 70])
        if 470 <= mouse[0] <= 470 + 180 and 530 <= mouse[1] <= 530 + 70:
            pygame.draw.rect(screen, color_light, [470, 530, 180, 70])
        else:
            pygame.draw.rect(screen, color_dark, [470, 530, 180, 70])
        if truth_language:
            screen.blit(text_score_ru, (460, 415))
            screen.blit(text_best_ru, (460, 465))
            screen.blit(text_exit_ru, (505, 545))
            screen.blit(text_again_ru, (725, 545))
        else:
            screen.blit(text_score_en, (460, 415))
            screen.blit(text_best_en, (460, 465))
            screen.blit(text_exit_en, (525, 545))
            screen.blit(text_again_en, (740, 545))
        screen.blit(text_score, (745, 415))
        screen.blit(text_best_score, (745, 465))
        rect = gifFrameList[currentFrame].get_rect(center = (675, 260))
        screen.blit(gifFrameList[currentFrame], rect)
        currentFrame = (currentFrame + 1) % len(gifFrameList)
        pygame.display.update()
        clock.tick(10)


def intro():
    global truth_sound
    global truth_language
    truth_settings = True
    count_star = 0
    pygame.mouse.set_visible(True)
    while True:
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 550 <= mouse[0] <= 550 + 250 and 250 <= mouse[1] <= 250 + 100 and truth_settings:
                    if truth_sound:
                        game_sound.play()
                    main()
                if 550 <= mouse[0] <= 550 + 250 and 380 <= mouse[1] <= 380 + 100:
                    if truth_sound:
                        open_sound.play()
                    truth_settings = False
                if 545 <= mouse[0] <= 545 + 100 and 270 <= mouse[1] <= 270 + 100 and not truth_settings and truth_sound:
                    truth_sound = False
                if 715 <= mouse[0] <= 715 + 100 and 270 <= mouse[1] <= 270 + 100 and not truth_settings and not truth_sound:
                    truth_sound = True
                if 545 <= mouse[0] <= 545 + 100 and 490 <= mouse[1] <= 490 + 100 and not truth_settings and truth_language:
                    truth_language = False
                if 715 <= mouse[0] <= 715 + 100 and 490 <= mouse[1] <= 490 + 100 and not truth_settings and not truth_language:
                    truth_language = True
                if truth_settings:
                    create_particles(pygame.mouse.get_pos())
                    if truth_sound:
                        star_sound.play()
                    count_star += 1
                if 460 <= mouse[0] <= 460 + 70 and 110 <= mouse[1] <= 110 + 30 and not truth_settings:
                    if truth_sound:
                        close_sound.play()
                    truth_settings = True
        if truth_settings:
            background_surf = pygame.image.load('image.jpg')
            background_rect = background_surf.get_rect(bottomright=(1280, 720))
            screen.blit(background_surf, background_rect)
            if 550 <= mouse[0] <= 550 + 250 and 250 <= mouse[1] <= 250 + 100:
                pygame.draw.rect(screen, color_light, [550, 250, 250, 100])
            else:
                pygame.draw.rect(screen, color_dark, [550, 250, 250, 100])
            if 550 <= mouse[0] <= 550 + 250 and 380 <= mouse[1] <= 380 + 100:
                pygame.draw.rect(screen, color_light, [550, 380, 250, 100])
            else:
                pygame.draw.rect(screen, color_dark, [550, 380, 250, 100])
            if truth_language:
                screen.blit(text_play, (550 + 70, 280))
                screen.blit(text_settings, (550 + 45, 410))
            else:
                screen.blit(text_play_en, (550 + 90, 280))
                screen.blit(text_settings_en, (550 + 65, 410))
            if count_star >= 5 and count_star < 10:
                screen.blit(text_title, (500, 100))
            elif count_star >= 10 and count_star < 15:
                screen.blit(text_title2, (460, 100))
            elif count_star >= 15 and count_star < 20:
                screen.blit(text_title3, (410, 100))
            elif count_star >= 20 and count_star < 25:
                screen.blit(text_title4, (280, 100))
            elif count_star >= 25 and count_star < 30:
                screen.blit(text_title5, (200, 100))
            elif count_star >= 30 and count_star < 35:
                screen.blit(text_title6, (500, 100))
            elif count_star >= 35 and count_star < 40:
                screen.blit(text_title7, (230, 100))
            elif count_star == 40:
                screen.blit(text_title8, (450, 100))
            elif count_star == 41:
                pygame.quit()
                exit()
        else:
            pygame.mouse.set_visible(True)
            count_star = 0
            pygame.draw.rect(screen, color_black, [450, 100, 450, 520])
            if 460 <= mouse[0] <= 460 + 70 and 110 <= mouse[1] <= 110 + 30:
                pygame.draw.rect(screen, color_light, [460, 110, 70, 30])
            else:
                pygame.draw.rect(screen, color_dark, [460, 110, 70, 30])
            screen.blit(text_return, (470, 105))
            if truth_language:
                screen.blit(text_settings, (580, 105))
                screen.blit(text_sound, (500, 180))
                screen.blit(text_language, (500, 385))
            else:
                screen.blit(text_settings_en, (585, 105))
                screen.blit(text_sound_en, (500, 180))
                screen.blit(text_language_eng, (500, 385))
            pygame.draw.rect(screen, color_dark, [535, 260, 290, 120])
            pygame.draw.rect(screen, color_dark, [535, 480, 290, 120])
            if truth_sound:
                pygame.draw.rect(screen, color_light, [545, 270, 100, 100])
            else:
                pygame.draw.rect(screen, color_light, [715, 270, 100, 100])
            if truth_language:
                pygame.draw.rect(screen, color_light, [545, 490, 100, 100])
            else:
                pygame.draw.rect(screen, color_light, [715, 490, 100, 100])
            if truth_language:
                screen.blit(text_on, (555, 225))
                screen.blit(text_off, (720, 225))
                screen.blit(text_language_rus, (555, 430))
                screen.blit(text_language_en, (720, 430))
            else:
                screen.blit(text_on_en, (555, 225))
                screen.blit(text_off_en, (720, 225))
                screen.blit(text_language_rus_en, (555, 430))
                screen.blit(text_language_en, (720, 430))
        all_sprites.update()
        all_sprites.draw(screen)
        clock.tick(100)
        pygame.display.update()


def split_animated_gif(gif_file_path):
    ret = []
    gif = Image.open(gif_file_path)
    for frame_index in range(gif.n_frames):
        gif.seek(frame_index)
        frame_rgba = gif.convert("RGBA")
        pygame_image = pygame.image.fromstring(
            frame_rgba.tobytes(), frame_rgba.size, frame_rgba.mode)
        ret.append(pygame_image)
    return ret


def main():
    global truth_sound
    global cactus_speed
    file2 = open('best_score.txt')
    best_score = file2.readlines()
    for i in best_score:
        best_score = i
    file2.close()
    cactus_frame1 = pygame.image.load("cactus1.png").convert_alpha()
    cactus_frame2 = pygame.image.load("cactus2.png").convert_alpha()
    cactus_frames = [cactus_frame2, cactus_frame1]
    dino_gravity = 0
    cactus_rect_list = []
    cloud_rect_list = []
    skeleton_rect_list = []
    skull_rect_list = []
    cactus_frame_index = 0
    cactus_surf = cactus_frames[cactus_frame_index]
    score = 0
    cactus_spawn_speed = 1500
    cactus_speed = 4
    level_timer = pygame.USEREVENT + 4
    pygame.time.set_timer(level_timer, 10000)
    skeleton_timer = pygame.USEREVENT + 5
    pygame.time.set_timer(skeleton_timer, 15000)
    skull_timer = pygame.USEREVENT + 6
    pygame.time.set_timer(skull_timer, 35000)
    cactus_timer = pygame.USEREVENT + 1
    pygame.time.set_timer(cactus_timer, cactus_spawn_speed)
    cactus_animation_timer = pygame.USEREVENT + 2
    pygame.time.set_timer(cactus_animation_timer, 600)
    cloud_timer = pygame.USEREVENT + 3
    pygame.time.set_timer(cloud_timer, 4000)
    game_active = True
    running = True
    pygame.mouse.set_visible(False)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    massage_timer = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and game_active:
                if truth_sound:
                    pause_sound.play()
                game_active = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE and not game_active:
                if truth_sound:
                    pause_sound.play()
                game_active = True
            if game_active:
                if event.type == pygame.USEREVENT:
                    score += 1
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE and dino_rect.bottom >= 450:
                        dino_gravity = -23
                        if truth_sound:
                            jump_sound.play()
                if event.type == cactus_timer:
                    cactus_rect_list.append(cactus_surf.get_rect(bottomright = (randint(1100, 1400), 450)))
                if event.type == cactus_animation_timer:
                    if cactus_frame_index == 0:
                        cactus_frame_index = 1
                    else:
                        cactus_frame_index = 0
                    cactus_surf = cactus_frames[cactus_frame_index]
                if event.type == cloud_timer:
                    cloud_rect_list.append(cloud.get_rect(midbottom = (randint(1200, 1500), randint(100, 200))))
                if event.type == level_timer:
                    cactus_speed += 2
                    if truth_sound:
                        level_sound.play()
                    massage_timer = False
                if event.type == skeleton_timer:
                    skeleton_rect_list.append(skeleton.get_rect(midbottom = (randint(1200, 1500), randint(530, 710))))
                if event.type == skull_timer:
                    skull_rect_list.append(skull.get_rect(midbottom = (randint(1200, 1500), randint(530, 710))))
        if game_active:
            play = Game()
            pygame.draw.rect(screen, (240, 240, 240), (0, 0, 1280, 720))
            play.display_score(score)
            play.dino_animation()
            dino_gravity += 0.8
            dino_rect.y += dino_gravity
            if dino_rect.bottom >= 450:
                dino_rect.bottom = 450
            screen.blit(dino_surf, dino_rect)
            cactus_rect_list = play.cactus_movement(cactus_rect_list)
            game_active = play.collisions(dino_rect, cactus_rect_list)
            pygame.draw.rect(screen, (230, 230, 230), (0, 720, 1280, 150))
            cloud_rect_list = play.cloud_movement(cloud_rect_list)
            skeleton_rect_list = play.skeleton_movement(skeleton_rect_list)
            skull_rect_list = play.skull_movement(skull_rect_list)
            pygame.draw.line(screen, (100, 100, 100), (0, 450), (1280, 450), 4)
            if massage_timer:
                massage()
        if not play.collisions(dino_rect, cactus_rect_list):
            if truth_sound:
                dead_sound.play()
            if score > int(best_score):
                best_score = str(score)
                f = open('best_score.txt', 'w')
                f.write(str(score))
                f.close()   
            screen.fill(pygame.Color("red"))
            end_screen(score)
        pygame.display.update()
        clock.tick(130)
    pygame.quit()
    exit()
intro()
