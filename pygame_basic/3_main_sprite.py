import pygame

pygame.init() #초기화 (반드시 필요)

#화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("Mingyu Game") # 게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("D:\\alsrb\\Nado\\pygame_basic\\background.png") #슬래쉬 1개 or 백슬래쉬 2개

# 캐릭터(스프라이트) 불러오기
character =  pygame.image.load("D:\\alsrb\\Nado\\pygame_basic\\character.png")
character_size = character.get_rect().size # 이미지의 크기를 구해옴
character_width = character_size[0] # 캐릭터 가로크기
character_height = character_size[1] # 캐릭터 세로크기
character_x_pos = (screen_width - character_width) / 2 # 화면 가로의 절반 크기에 해당하는 곳에 위치 (가로 위치)
character_y_pos = screen_height - character_height # 화면 세로 크기 가장 아래에 위치 (세로 위치)




# 이벤트 루프
running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # pygame 무조건 필요한 것, 어떤 이벤트가 발생하였는가
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가 ?
            running = False

    #screen.fill((0,0,255))    # (r,g,b)로 화면 색 채우기
    screen.blit(background, (0,0)) # 맨 왼쪽 위가 (0, 0), 배경그리기
    screen.blit(character, (character_x_pos, character_y_pos))

    pygame.display.update() # 게임화면을 다시 그리기 !

# pygame 종료
pygame.quit()