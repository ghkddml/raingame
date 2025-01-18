비를 피하는 간단한 게임은 중학생도 쉽게 이해하고 만들 수 있도록 파이썬과 Pygame 라이브러리를 사용해서 제작할 수 있습니다. 아래는 간단한 코드 예제입니다.

### **게임 설명**
- 플레이어는 캐릭터(네모)를 화살표 키로 움직여 비(떨어지는 직사각형)로부터 피해야 합니다.
- 비는 점점 빠르게 떨어지고, 비와 충돌하면 게임이 종료됩니다.

---

### **코드**

```python
import pygame
import random
import sys

# 초기화
pygame.init()

# 화면 설정
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("비 피하기 게임")

# 색상
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# FPS 설정
clock = pygame.time.Clock()
FPS = 30

# 플레이어 설정
player_width, player_height = 50, 50
player_x, player_y = WIDTH // 2, HEIGHT - player_height - 10
player_speed = 7

# 비 설정
rain_width, rain_height = 30, 30
rain_x = random.randint(0, WIDTH - rain_width)
rain_y = -rain_height
rain_speed = 5

# 점수
score = 0
font = pygame.font.Font(None, 36)

# 게임 루프
running = True
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

    # 비 움직임
    rain_y += rain_speed

    # 비와 충돌 확인
    if (
        rain_y + rain_height > player_y
        and rain_x < player_x + player_width
        and rain_x + rain_width > player_x
    ):
        running = False  # 게임 종료

    # 비가 화면을 벗어나면 다시 생성
    if rain_y > HEIGHT:
        rain_y = -rain_height
        rain_x = random.randint(0, WIDTH - rain_width)
        rain_speed += 0.5  # 비가 점점 빨라짐
        score += 1  # 점수 증가

    # 플레이어와 비 그리기
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (rain_x, rain_y, rain_width, rain_height))

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
```

---

### **설명**
1. **설치 방법**
   - 파이썬을 설치합니다.
   - Pygame 라이브러리를 설치합니다:
     ```bash
     pip install pygame
     ```

2. **게임 실행**
   - 위 코드를 복사하여 파이썬 파일(`rain_game.py`)에 저장합니다.
   - 터미널에서 실행:
     ```bash
     python rain_game.py
     ```

3. **게임 규칙**
   - 키보드 방향키(←, →)를 사용하여 플레이어를 움직입니다.
   - 떨어지는 빨간색 비를 피하고, 점수를 높이세요.
   - 비에 맞으면 게임이 종료됩니다.

---

### **추가 아이디어**
- 난이도 조정: 시작 속도나 화면 크기 변경.
- 아이템 추가: 보호막이나 점수 보너스.
- 배경음악 및 효과음 추가.

이 정도면 중학생도 쉽게 이해하고 재미있게 만들 수 있을 것입니다! 😊