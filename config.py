class Config:
    # Universal
    SCALE = 4

    # Screen
    SCREEN_DEFAULT_WIDTH = 1080
    SCREEN_DEFAULT_HEIGHT = 720
    SCREEN_ASPECT_RATIO = SCREEN_DEFAULT_WIDTH / SCREEN_DEFAULT_HEIGHT

    SCREEN_SIZE = (SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT)

    # Camera
    CAMREA_LEFT_SIDE = SCREEN_DEFAULT_WIDTH / -2
    CAMREA_RIGHT_SIDE = SCREEN_DEFAULT_WIDTH / 2
    CAMREA_BOTTOM_SIDE = SCREEN_DEFAULT_HEIGHT / -2
    CAMREA_TOP_SIDE = SCREEN_DEFAULT_HEIGHT / 2

    CAMERA_SIDES = (CAMREA_LEFT_SIDE, CAMREA_RIGHT_SIDE, CAMREA_BOTTOM_SIDE, CAMREA_TOP_SIDE)

    # Pieces
    PIECE_SIZE = 16

    PLAYER_1_PRIMARY_COLOR = (1, 1, 1)
    PLAYER_1_SECONDARY_COLOR = (0.7, 0.7, 0.7)

    PLAYER_2_PRIMARY_COLOR = (0, 0, 0)
    PLAYER_2_SECONDARY_COLOR = (0.3, 0.3, 0.3)

    # Board
    BOARD_SIZE = 8
    BOARD_PADDING = 2

    BOARD_PRIMARY_COLOR = (0.451, 0.318, 0.235)
    BOARD_SECONDARY_COLOR = (0.9, 0.86, 0.83)

    BOARD_RING_SIZE = 1 / SCALE
    BOARD_RING_COLOR = (0.25, 0.23, 0.22)

    # Selection
    SELECTED_COLOR = (0.75, 1, 0.8)
    VALID_COLOR = (0.80, 0.85, 1)

    # Promotion
    PROMOTION_ROWS = 4
    PROMOTION_COLUMNS = 1

    # Testing
    '''SCREEN_DEFAULT_WIDTH = int(((BOARD_RING_SIZE * BOARD_SIZE + 1) + (PIECE_SIZE + BOARD_PADDING * 2) * BOARD_SIZE) * SCALE)
    SCREEN_DEFAULT_HEIGHT = int(((BOARD_RING_SIZE * BOARD_SIZE + 1) + (PIECE_SIZE + BOARD_PADDING * 2) * BOARD_SIZE) * SCALE)
    SCREEN_ASPECT_RATIO = SCREEN_DEFAULT_WIDTH / SCREEN_DEFAULT_HEIGHT

    SCREEN_SIZE = (SCREEN_DEFAULT_WIDTH, SCREEN_DEFAULT_HEIGHT)
    
    CAMREA_LEFT_SIDE = SCREEN_DEFAULT_WIDTH / -2
    CAMREA_RIGHT_SIDE = SCREEN_DEFAULT_WIDTH / 2
    CAMREA_BOTTOM_SIDE = SCREEN_DEFAULT_HEIGHT / -2
    CAMREA_TOP_SIDE = SCREEN_DEFAULT_HEIGHT / 2

    CAMERA_SIDES = (CAMREA_LEFT_SIDE, CAMREA_RIGHT_SIDE, CAMREA_BOTTOM_SIDE, CAMREA_TOP_SIDE)'''