import ffmpeg

def speed_up_video(input_file, output_file, speed=1.5):
    """目前只处理视频，不处理音频"""
    try:
        input_stream = ffmpeg.input(input_file)
        
        # 处理视频流 - 通过调整pts（presentation timestamp）来改变播放速度
        video = input_stream.video.filter('setpts', f'PTS/{speed}')
        
        output = ffmpeg.output(
            video, 
            output_file, 
            vcodec='libx264', 
            acodec='aac', 
            strict='experimental'
        )
        
        # 执行转换
        ffmpeg.run(output, overwrite_output=True)
        
        print(f"视频已成功转换为{speed}倍速并保存到：{output_file}")
    except ffmpeg.Error as e:
        print(f"FFmpeg错误：{e}")
    except Exception as e:
        print(f"转换过程中发生错误：{str(e)}")

if __name__ == '__main__':
    import os
    import sys

    if len(sys.argv) != 4:
        print(f'{sys.argv[0]} input_file output_file speed')
        os.exit(1)
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    speed = float(sys.argv[3])
    speed_up_video(input_file, output_file, speed=speed)
