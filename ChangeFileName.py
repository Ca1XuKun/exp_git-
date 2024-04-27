import os

def rename():
    i = 0
    path = r"D:\CODE_WORLD\project_donwload_from_github\yolov8\ultralytics-main\paper.v1i.yolov8\train\labels"

    filelist = os.listdir(path)   #该文件夹下所有的文件（包括文件夹）
    for files in filelist:   #遍历所有文件
        i = i + 1
        Olddir = os.path.join(path, files)    #原来的文件路径
        if os.path.isdir(Olddir):       #如果是文件夹则跳过
                continue
        filename = 'paper'     #文件名
        filetype = '.txt'        #文件扩展名
        Newdir = os.path.join(path, filename + str(i) + filetype)   #新的文件路径
        os.rename(Olddir, Newdir)    #重命名
    return True

if __name__ == '__main__':
    rename()


    #使用方法，把需要修改的文件的路径填入path
    #然后把要改的文件名填入filename
    #把拓展名填入filetypr
    #运行则会顺序重命名为：filename1.filetype、filename2.filetype、filename3.filetype……