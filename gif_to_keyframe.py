from PIL import Image
im = Image.open("YOUR_GIF_FILE.gif")

WIDTH = 32  # Number of "pixels"
HEIGHT = 32  # Number of "pixels"
PIXEL_UNIT = 'vmin'  # The CSS unit to be used for every "PIXEL"
PIXEL_SIZE = 1  # Count of CSS unit
KEYFRAME_NAME = 'magicAnimation'  # Name of the CSS keyframe to be created

frames = []
for frame in range(0, im.n_frames):
    im.seek(frame)
    smaller = im.resize((WIDTH, HEIGHT)).convert('RGBA')
    frames.append(smaller)

print(f'@keyframes {KEYFRAME_NAME} {"{"}')
for i, frame in enumerate(frames):
    print(f'{round(i / (len(frames) - 1) * 100)}% {"{"}box-shadow: ', end='')
    for x in range(WIDTH):
        for y in range(HEIGHT):
            print(f'{PIXEL_SIZE * x}{PIXEL_UNIT} {PIXEL_SIZE * y}{PIXEL_UNIT} 0 2px rgba{frame.getpixel((x, y))}{", " if y < (HEIGHT - 1) or x < (WIDTH - 1) else ""}', end='')
    print(f';background: rgb{frame.getpixel((0, 0))};{"}"}')

print('}')
