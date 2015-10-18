import pygame

def resize(width, img):
    size = img.get_size()
    img_ratio = size[1]/size[0]
    return pygame.transform.scale(img, (int(width), int(width*img_ratio)))
