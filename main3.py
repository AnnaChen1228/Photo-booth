import tkinter as tk
import cv2
import os
import conbine_ffmpeg_new
import filter
import transVideo_new
import share_new

fold_name = ''
window1=None
count=0#照片數量
grid=0#排版
img=[]#儲存圖片位置
out_img="./" + fold_name + "/out.jpg"#最終

def shot(count):#拍照+排版
    cap = cv2.VideoCapture(0)
    global window1
    global img
    global grid
    border=radioVar8.get()
    border_color=None
    if border==1:
        border_color="black"
    else:
        border_color="white"
    window1.destroy()
    i = 0
    while i < count:
        ret, frame = cap.read()
        k = cv2.waitKey(1)
        if k == 27:
            break
        elif k == ord("\r"):
            filename = "./" + fold_name + "/" + str(i) + ".jpg"
            img.append(filename)
            print(filename)
            cv2.imwrite(filename, frame)
            i += 1
        cv2.imshow("Capture", frame)
    cap.release()
    cv2.destroyAllWindows()
    if grid==2:
        conbine_ffmpeg_new.combine_images_2x2(img,out_img,border_color)
    elif grid==3:
        conbine_ffmpeg_new.combine_images_4x1(img,out_img,border_color)
    elif grid==4:
        conbine_ffmpeg_new.combine_images_1x4(img,out_img,border_color)
    on_ok_pressed()

def Capture(user):
    global fold_name
    global window1
    global count
    global grid
    grid=radioVar4.get()
    if grid==1:
        count=1
    else:
        count=4
    
    print(count)
    print(grid)
    fold_name = user
    os.system("mkdir " + fold_name)
    print(user)
    window.withdraw()  # 隱藏主視窗
    window1 = tk.Toplevel()  # 創建新視窗
    window1.title("Hint")
    window1.geometry("500x120+250+150")
    label1 = tk.Label(window1, text="Please press \"enter\" to take a picture !", font=("Arial", 20))
    label2 = tk.Label(window1, text="& press \"esc\" to leave !", font=("Arial", 20))
    label1.pack()
    label2.pack()
    button = tk.Button(window1, text="OK", command=lambda: shot(count))
    button.pack()
    window1.protocol("WM_DELETE_WINDOW", lambda: on_close(window1))  # 覆寫關閉視窗的行為

def on_ok_pressed():#顯示主視窗
    window1.destroy()  # 關閉新視窗
    window.deiconify()  # 重新顯示原始視窗

def on_close(windows):#僅保留一個視窗
    windows.destroy()
    windows.deiconify()  # 重新顯示主視窗

def color(i):#濾鏡
    if i==1:
        print("color ture")
        global window1
        window.withdraw()  # 隱藏主視窗
        window1 = tk.Toplevel()  # 創建新視窗
        window1.title("Choose color")
        window1.geometry("500x500")
        label2=tk.Label(window1,text='Choose color:')
        label2.pack()
        radioVar7=tk.IntVar()#濾鏡
        radioVar1.set(0)
        radio1=tk.Radiobutton(window1,text='1',variable=radioVar7,value=1)
        radio2=tk.Radiobutton(window1,text='2',variable=radioVar7,value=2)
        radio3=tk.Radiobutton(window1,text='3',variable=radioVar7,value=3)
        radio4=tk.Radiobutton(window1,text='4',variable=radioVar7,value=4)
        radio1.pack()
        radio2.pack()
        radio3.pack()
        radio4.pack()
        window1.protocol("WM_DELETE_WINDOW", lambda: on_close(window1))
        colorbtn=tk.Button(window1,text='OK',command=lambda:filter1(radioVar7.get()))#進行濾鏡
        colorbtn.pack()

def filter1(num):#濾鏡
    filter.Filter(num)
    on_ok_pressed()

def vedio(i):#轉影片
    if i==1:
        #global img
        out= "./" + fold_name + "/" +"output.mp4"
        transVideo_new.transVideo(img,out)
        print("vedio ture")

def share1(i):#分享
    if i==1:
        global window1
        window.withdraw()  # 隱藏主視窗
        window1 = tk.Toplevel()  # 創建新視窗
        window1.title("Share")
        window1.geometry("500x500")
        label5=tk.Label(window1,text="Your ID:")
        label5.pack()
        id=tk.Entry(window1)
        id.pack()
        label6=tk.Label(window1,text="Your PassWord:")
        label6.pack()
        pd=tk.Entry(window1,show='*')
        pd.pack()
        label7=tk.Label(window1,text="Message")
        msg=tk.Entry(window1)
        label7.pack()
        msg.pack()
        window1.protocol("WM_DELETE_WINDOW", lambda: on_close(window1))
        msgbtn=tk.Button(window1,text='OK',command=lambda:share_ig(id.get(),pd.get(),out_img,msg.get()))#進行分享
        msgbtn.pack()
        print("share ture")

def share_ig(id,psd,out_img,msg):
    global window1
    result=share_new.share(id,psd,out_img,msg)
    on_ok_pressed()
    if result==False:
        labe=tk.Label(window,text="Your ID or password is Wrong!")
    else:
        labe=tk.Label(window,text="")
    labe.pack()


window = tk.Tk()
window.title("Photograph")
window.geometry('300x600')
window.resizable()

label1 = tk.Label(window, text='Take a photo\nEnter your name:')
label1.pack()
test = tk.Entry(window)  # 輸入資料夾名稱
test.pack()
label5=tk.Label(window,text='Choose count:')
label5.pack()

radioVar4 = tk.IntVar()  # 濾鏡
radio9 = tk.Radiobutton(window, text='1*1', variable=radioVar4, value=1)
radio10= tk.Radiobutton(window, text='2*2', variable=radioVar4, value=2)
radio11= tk.Radiobutton(window, text='4*1', variable=radioVar4, value=3)
radio12= tk.Radiobutton(window, text='1*4', variable=radioVar4, value=4)
radio9.pack()
radio10.pack()
radio11.pack()
radio12.pack()

label6=tk.Label(window,text='Border color:')
label6.pack()
radioVar8 = tk.IntVar()  # 邊框顏色
radio9 = tk.Radiobutton(window, text='Black', variable=radioVar8, value=1)
radio10= tk.Radiobutton(window, text='White', variable=radioVar8, value=2)
radio9.pack()
radio10.pack()
camera = tk.Button(window, text="OK", command=lambda: Capture(test.get()))
camera.pack()

label2 = tk.Label(window, text='Step2\n Choose color:')#濾鏡
label2.pack()
radioVar1 = tk.IntVar()  
radio1 = tk.Radiobutton(window, text='Yes', variable=radioVar1, value=1, command=lambda: color(1))
radio2 = tk.Radiobutton(window, text='Flase', variable=radioVar1, value=2, command=lambda: color(2))
radio1.pack()
radio2.pack()

label3 = tk.Label(window, text='Step3\nTransform to vedio(if you choose four picture):')# 影片
label3.pack()
radioVar2 = tk.IntVar()  
radio5 = tk.Radiobutton(window, text='Yes', variable=radioVar2, value=1, command=lambda: vedio(1))
radio6 = tk.Radiobutton(window, text='No', variable=radioVar2,value=2, command=lambda: vedio(2))
radio5.pack()
radio6.pack()

label4 = tk.Label(window, text='Step4\nShare on IG:')# 分享
label4.pack()
radioVar3 = tk.IntVar() 
radio7 = tk.Radiobutton(window, text='Yes', variable=radioVar3, value=1, command=lambda: share1(1))
radio8 = tk.Radiobutton(window, text='No', variable=radioVar3, value=2, command=lambda: share1(1))
radio7.pack()
radio8.pack()
window.mainloop()
