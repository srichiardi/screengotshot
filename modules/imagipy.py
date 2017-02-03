from PIL import Image, ImageFont, ImageDraw
import time

def add_url_time(url, original_image_path):
    
    CHAR_PX_W = 9
    CHAR_PX_H = 15
    LINE_SPACE = 5
    
    raw_shot = Image.open(original_image_path)
    
    width, height = raw_shot.size
    
    char_per_line = width / CHAR_PX_W
    
    lines_nr = (len(url) / char_per_line) + 1
    
    hdr_height = CHAR_PX_H * lines_nr + (lines_nr + 1) * LINE_SPACE
    
    ftr_height = CHAR_PX_H + 10 # assuming footer will always be one line
    
    new_height = height + hdr_height + ftr_height
    
    new_img = Image.new('RGB', (width, new_height), 'white')
    
    new_img.paste(im=raw_shot, box=(0, hdr_height), mask=raw_shot)
    
    raw_shot.close()
    
    font = ImageFont.truetype("arial.ttf", CHAR_PX_H)
    
    draw = ImageDraw.Draw(new_img, mode='RGB')
    
    # slice url in 128 lines
    sliced_list = [url[i:i+char_per_line] for i in range(0,len(url),char_per_line)]
    
    offset = 5
    for line in sliced_list:
        draw.text((5, offset), line, "black", font=font)
        offset += CHAR_PX_H + LINE_SPACE
    
    timestamp = "Image taken on " + time.strftime("%d.%m.%Y at %H:%M:%S", time.gmtime()) + " GMT +0"
    
    draw.text((5, height + hdr_height + 5), timestamp, "black", font=font)
    
    new_img.save(original_image_path)

    
