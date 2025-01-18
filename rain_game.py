import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 400, 600  # 난이도 조정: 화면 크기
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("비 피하기 게임")

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 30

# 음악 및 효과음
pygame.mixer.music.load("background_music.mp3")  # 배경음악 파일 경로
pygame.mixer.music.play(-1)  # 무한 반복
bonus_sound = pygame.mixer.Sound("bonus.wav")  # 점수 보너스 효과음
shield_sound = pygame.mixer.Sound("shield.wav")  # 보호막 효과음

# 플레이어 설정
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - player_height - 10
player_speed = 7
shield_active = False

# 비 설정
rain_width, rain_height = 30, 30
rain_speed = 5

# 아이템 설정
item_width, item_height = 30, 30
item_types = ["shield", "bonus"]
item_spawn_chance = 0.01  # 아이템 생성 확률

# 점수
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
rain_list = []
item_list = []

while running:
    screen.fill(WHITE)  # 배경 화면

    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 키 입력
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # 비 생성
    if random.random() < 0.02:  # 비 생성 확률
        rain_x = random.randint(0, WIDTH - rain_width)
        rain_y = -rain_height
        rain_list.append([rain_x, rain_y])

    # 비 움직임
    for rain in rain_list[:]:
        rain[1] += rain_speed
        # 비와 충돌 확인
        if (
            rain[1] + rain_height > player_y
            and rain[0] < player_x + player_width
            and rain[0] + rain_width > player_x
        ):
            if shield_active:
                shield_active = False  # 보호막 소멸
                rain_list.remove(rain)
            else:
                running = False  # 게임 종료
        # 화면 밖으로 나가면 제거
        if rain[1] > HEIGHT:
            rain_list.remove(rain)

    # 아이템 생성
    if random.random() < item_spawn_chance:
        item_x = random.randint(0, WIDTH - item_width)
        item_y = -item_height
        item_type = random.choice(item_types)
        item_list.append([item_x, item_y, item_type])

    # 아이템 움직임
    for item in item_list[:]:
        item[1] += rain_speed
        # 아이템과 충돌 확인
        if (
            item[1] + item_height > player_y
            and item[0] < player_x + player_width
            and item[0] + item_width > player_x
        ):
            if item[2] == "shield":
                shield_active = True
                shield_sound.play()
            elif item[2] == "bonus":
                score += 10
                bonus_sound.play()
            item_list.remove(item)
        # 화면 밖으로 나가면 제거
        if item[1] > HEIGHT:
            item_list.remove(item)

    # 비와 아이템 그리기
    for rain in rain_list:
        pygame.draw.rect(screen, RED, (rain[0], rain[1], rain_width, rain_height))
    for item in item_list:
        color = CYAN if item[2] == "shield" else GREEN
        pygame.draw.rect(screen, color, (item[0], item[1], item_width, item_height))

    # 플레이어 그리기
    player_color = BLUE if not shield_active else CYAN  # 보호막 상태 시 색 변경
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # 점수 표시
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    # 화면 업데이트
    pygame.display.flip()
    clock.tick(FPS)

# 게임 종료 메시지
screen.fill(WHITE)
game_over_text = font.render("Game Over!", True, RED)
final_score_text = font.render(f"Final Score: {score}", True, BLACK)
screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2 - 20))
screen.blit(final_score_text, (WIDTH // 2 - 100, HEIGHT // 2 + 20))
pygame.display.flip()
pygame.time.wait(3000)
pygame.quit()
