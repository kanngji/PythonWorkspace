import pygame
import random
###########################################33
# 기본 초기화 

pygame.init()

#화면 크기 설정
screen_width = 480
screen_height = 640

screen = pygame.display.set_mode((screen_width, screen_height))

#화면 타이틀 설정
pygame.display.set_caption("마카롱 피하기") #게임이름

#FPS
clock = pygame.time.Clock()

# 1. 사용자 게임 초기화 (배경 화면 , 게임이미지 , 좌표 , 폰트)

#배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\강지훈\\Desktop\\PythonWorkspace\\pygame\\macaronbackground.png")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load("C:\\Users\\강지훈\\Desktop\\PythonWorkspace\\pygame\\dooli.png")
character_size = character.get_rect().size #이미지의 크기를 구해온다
character_width = character_size[0] #캐릭터의 가로크기
character_height = character_size[1] #캐릭터의 세로크기
character_x_pos = screen_width / 2 - (character_width / 2) #캐릭터 시작점
character_y_pos = screen_height - character_height #캐릭터 세로 크기 가장 아래에 시작

#이동할 좌표
to_x = 0

#이동속도
character_speed = 0.6

#적 enemy 캐릭터
enemy = pygame.image.load("C:/Users/강지훈/Desktop/PythonWorkspace/pygame/macaron.png")
enemy_size = enemy.get_rect().size #이미지의 크기를 구해온다
enemy_width = enemy_size[0] #에너미의 가로크기
enemy_height = enemy_size[1] #에너미의 세로크기
enemy_x_pos = random.randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 5


#에너미 하늘에서 떨어지는 코드 구현




#폰트 정의
game_font = pygame.font.Font(None, 40) #폰트 객체 생성 (폰트, 크기)

#시작 시간
start_ticks = pygame.time.get_ticks() #시작 tick을 받아옴

#이벤트 루프
running = True #게임이 진행중인가?

while running:
    dt = clock.tick(30)

    # 2. 이벤트 처리 (키보드 , 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False

        if event.type == pygame.KEYDOWN: #키가 눌러졌는지 확인
            if event.key == pygame.K_LEFT:
                to_x -= character_speed # to_x = to_x -5
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed # to_x = to_x + 5


        if event.type == pygame.KEYUP: #방향키를 떼면 멈춤
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0

    # 3. 게임 캐릭터 위치 정의
    character_x_pos += to_x * dt
    

    # 가로 경계값 처리
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    enemy_y_pos += enemy_speed

    if enemy_y_pos > screen_height:
        enemy_y_pos = 0
        enemy_x_pos = random.randint(0, screen_width - enemy_width)

    #충돌 처리를 위한 rect 정보 업데이트
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos
    
    

    #충돌체크
    if character_rect.colliderect(enemy_rect):
        print("둘리는 마카롱을 먹었습니다")
        running = False

    # screen.fill((0, 0, 255)) 배경색깔 채우기 rgb로 
    screen.blit(background, (0, 0))        #배경 그리기
    screen.blit(character, (character_x_pos, character_y_pos)) #캐릭터 그리기
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
   

    #타이머 집어넣기
    #경과 시간 계산
        
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 
    # 경과 시간(ms)을 1000으로 나누어서 초 단위(s)로 표시

    # 출력할 글자 , True , 글자 색상

    pygame.display.update() #게임화면을 다시 그리기!


#pygame 종료
pygame.quit()