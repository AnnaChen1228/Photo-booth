import subprocess

# 設定輸入圖片的路徑和檔名
image1_path = 'C:\\Users\\chiehyu\\Desktop\\image1.jpg'
image2_path = 'C:\\Users\\chiehyu\\Desktop\\image2.jpg'
image3_path = 'C:\\Users\\chiehyu\\Desktop\\image3.jpg'
image4_path = 'C:\\Users\\chiehyu\\Desktop\\image4.jpg'

def transVideo(img,out):
# 設定輸出影片的路徑和檔名
    #output_path = 'C:\\Users\\chiehyu\\Desktop\\output.mp4'

    # 執行 FFmpeg 命令
    command = [
        'ffmpeg',
        '-loop', '1', '-i', img[0],  
        '-loop', '1', '-i', img[1],  
        '-loop', '1', '-i', img[2],  
        '-loop', '1', '-i', img[3],  
        '-filter_complex',
        '[0:v]setpts=PTS-STARTPTS,trim=0:1[v0];'
        '[1:v]setpts=PTS-STARTPTS,trim=0:2[v1];'
        '[2:v]setpts=PTS-STARTPTS,trim=0:2[v2];'
        '[3:v]setpts=PTS-STARTPTS,trim=0:2[v3];'
        '[v0][v1][v2][v3]concat=n=4:v=1:a=0[outv]'.format(
            1, 1, 1, 1),
        '-map', '[outv]',
        '-c:v', 'libx264',
        '-pix_fmt', 'yuv420p',
        '-r', '1',
        '-y',
        out,
    ]
    subprocess.call(command)

    print("影片輸出完成！")
