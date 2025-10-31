# pip install opencv-python
import cv2 # opencv

# pip install mss
import mss # 跨平台截屏

# pip install numpy
import numpy as np

# pip install ffmpeg-python # 系统上需要安装ffmpeg
import ffmpeg

with mss.mss() as sct:
    # 获取主屏幕分辨率
    monitor = sct.monitors[1]

    # 使用 MJPG 编码，只进行帧内压缩（jpg），不进行帧间压缩，视频非常大
    #fourcc = cv2.VideoWriter_fourcc(*'MJPG')
    #output_file = 'mjpg.mp4'

    # 使用 H.264 编码，进行帧间压缩，大小是MJPG的50-200分之一
    fourcc = cv2.VideoWriter_fourcc(*'avc1') # avc1就是mac上的h264
    output_file = 'avc1.mp4'

    # 创建视频写入对象
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (monitor['width'], monitor['height']))

    print("开始录制屏幕... 按 Ctrl+C 停止。")
    try:
        while True:
            screenshot = sct.grab(monitor)
            frame = np.array(screenshot)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGBA2BGR)
            out.write(frame)
    except KeyboardInterrupt:
        print("\n录制结束。")
    finally:
        out.release()
        cv2.destroyAllWindows()

(
    ffmpeg
    .input('avc1.mp4')
    .output('h264.mp4', vcodec='libx264', crf=28) # crf: 0-51，越大压缩效率越高，h264默认23
    .overwrite_output()
    .run()
)
