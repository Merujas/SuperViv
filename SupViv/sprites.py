import pygame
import os

def load_sprites_from_folder(folder_path):
    """
    Carga todas las hojas de sprites de una carpeta y las divide en frames por dirección.
    """
    sprites = {
        "up": [],
        "down": [],
        "left": [],
        "right": [],
        "up_left": [],
        "up_right": [],
        "down_left": [],
        "down_right": []
    }

    for file_name in os.listdir(folder_path):
        if file_name.endswith(".png"):  # Asegúrate de que el archivo sea una imagen PNG
            # Extraer la dirección del nombre del archivo
            # Ejemplo: "GirlSample_Walk_Down.png" -> "down"
            direction = os.path.splitext(file_name)[0].split("_")[-1].lower()

            if direction not in sprites:
                print(f"Advertencia: Dirección '{direction}' no reconocida en el archivo '{file_name}'")
                continue

            sprite_path = os.path.join(folder_path, file_name)
            sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
            sprites[direction].append(sprite_sheet)

            # Tamaño de cada frame
            SPRITE_WIDTH = sprite_sheet.get_width() // 3  # Suponemos 3 frames por fila
            SPRITE_HEIGHT = sprite_sheet.get_height()

            # Dividir la hoja de sprites en frames
            for col in range(3):  # Suponemos 3 frames por dirección
                x = col * SPRITE_WIDTH
                y = 0
                sprite_rect = pygame.Rect(x, y, SPRITE_WIDTH, SPRITE_HEIGHT)
                sprite = sprite_sheet.subsurface(sprite_rect)
                sprites[direction].append(sprite)

        return sprites