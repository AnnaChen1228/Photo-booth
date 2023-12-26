import subprocess

def apply_filter(input_image, output_image, filter):
    command = f'ffmpeg -y -i {input_image} -vf "{filter}" {output_image}'
    subprocess.run(command, shell=True)

def Filter(num,input,output):
    if num == 1:
        filter = 'curves=preset=color_negative'#彩色負片
    elif num == 2:
        filter = 'hue=s=0'  # 黑白濾鏡
    elif num == 3:
        filter = 'negate'  # 反色濾鏡
    elif num == 4:
        filter = 'colorbalance=rs=0.3:bs=0.3'  # 色彩平衡濾鏡
    elif num ==5:
        filter ='unsharp=7:7:-1.0:7:7:-1.0' #模糊
    elif num==6:
        filter ='eq=brightness=0.06:contrast=1.2:saturation=1.5'#增亮
    elif num==7:
        filter ='edgedetect=low=0.1:high=0.1:mode=colormix'#描線
    else:
        filter = ''  # 預設情況，不使用濾鏡

    apply_filter(input, output, filter)
