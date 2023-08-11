import os
import struct

# 计算MP4的时长的函数
def get_video_duration(video_file):
    with open(video_file,'rb') as fp:
        data = fp.read()
        
    index = data.find(b'mvhd') + 4
    
    #time_scale是文件媒体一秒的刻度值，
    time_scale = struct.unpack('>I', data[index+13:index+13+4])
    #该媒体文件的时间长度
    durations = struct.unpack('>I', data[index+13+4:index+13+4+4])
    #用时间长度 / 每秒的刻度值  = 时长（秒）
    duration = durations[0] / time_scale[0]
    return duration

def get_file_sizes(path):
    """
    获取指定目录下所有文件和子目录的大小，返回一个字典，键为文件名，值为文件大小（单位为字节）
    """
    file_sizes = {}
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if "mp4" in file_path:
                file_sizes[file_path] = get_video_duration(file_path)
    return file_sizes

if __name__ == '__main__':
    #计算当前文件夹下所有mp4的时长，包括子文件夹里的
    count = 0
    path = os.getcwd()
    file_sizes = get_file_sizes(path)
    
    #返回的是mp4文件信息的字典，将字典遍历，统计所有数据
    for i in file_sizes:
        count = count + file_sizes.get(i)
        
    #将秒转换成分钟
    minute = count / 60
    print(minute)