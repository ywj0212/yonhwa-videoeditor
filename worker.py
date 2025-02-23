import traceback, sys, os
from moviepy import VideoFileClip, ImageClip, CompositeVideoClip, AudioFileClip
from moviepy.audio.fx import AudioFadeIn, AudioFadeOut, AudioNormalize
from proglog import ProgressBarLogger
from PySide6.QtCore import (QObject, QThread, Signal)
from utils import resource_path


class Worker(QObject):
  progress = Signal(float)
  finished = Signal(str)

  lp_loop_relpath: str = "./lp_loop.mov"

  ty: int = 0
  bgm_path: str = ''
  bg_path: str = ''
  bgm_from: str = ''
  bgm_to: str = ''
  save_path: str = ''

  def set_value(self, ty: int, bgm_path: str, bg_path: str, bgm_from: str, bgm_to: str, save_path: str):
    self.ty = ty
    self.bgm_path = bgm_path
    self.bg_path = bg_path
    self.bgm_from = bgm_from
    self.bgm_to = bgm_to
    self.save_path = save_path

  def run(self):
    lp_loop_path = resource_path(self.lp_loop_relpath)

    # print(ty, bgm_path, bg_path, bgm_from, bgm_to, save_path)
    class BarLogger(ProgressBarLogger):
      def set_signal(self, sig):
        self.progressSignal = sig
      def bars_callback(self, bar, attr, value, old_value=None):
        # Every time the logger progress is updated, this function is called        
        percentage = (value / self.bars[bar]['total']) * 100
        self.progressSignal.emit(percentage)
      
    try:
      if self.ty == 0:
        if not os.path.exists(lp_loop_path):
          self.finished.emit(f"오류! LP 영상 파일을 찾을 수 없음:\n{lp_loop_path}")
          return
        
        bgm_loop_padding = 1.4
        bgm_fadein = 0.15
        bgm_fadeout = 4
        duration = bgm_fadein + self.bgm_to - self.bgm_from + bgm_fadeout + bgm_loop_padding
        
        bg_clip: ImageClip = ImageClip(self.bg_path).with_duration(duration)
        lp_loop_clip: VideoFileClip = VideoFileClip(lp_loop_path, has_mask=True)
        lp_len: int = int(lp_loop_clip.duration)
        lp_loop_clip = lp_loop_clip.resized(1.01).with_position((380, 163))
      
        if duration > lp_len:
          self.finished.emit(f"오류! 플레이리스트 영상 길이는 {lp_len}초를 넘길 수 없음!\r\n현재 요청 영상 길이(Fade In/Out 포함): {duration}")
          return

        bgm_clip: AudioFileClip = AudioFileClip(self.bgm_path)
        bgm_len: int = int(bgm_clip.duration)
        if self.bgm_from >= self.bgm_to:
          self.finished.emit(f"오류! 시작 시간이 종료 시간보다 늦습니다!")
          return
        bgm_from: float = max(self.bgm_from - bgm_fadein, 0)
        bgm_to: float = min(self.bgm_to + bgm_fadeout, bgm_len)
        bgm_clip = bgm_clip.subclipped(bgm_from, bgm_to)
        bgm_clip = bgm_clip.with_effects([
          AudioFadeIn(bgm_fadein),
          AudioFadeOut(bgm_fadeout),
          AudioNormalize()
        ]) # fade in-out & normalization

        album_crop_clip: ImageClip = bg_clip.cropped(x1=172, y1=152, width=551.5, height=550).with_position((172, 152)).with_duration(duration)
        final_clip: CompositeVideoClip = CompositeVideoClip([bg_clip, lp_loop_clip, album_crop_clip]).with_duration(duration)

        logger = BarLogger()
        logger.set_signal(self.progress)
        bgm_clip.with_volume_scaled(0.95)
        final_clip = final_clip.with_audio(bgm_clip)

        output_path: str = os.path.join(self.save_path, f"{os.path.splitext(os.path.basename(self.bg_path))[0]}.mp4")

        if os.path.exists(output_path):
          self.finished.emit("저장 경로에 파일이 이미 존재합니다!\r\n" + output_path)
          return
      
        if not bg_clip.size == (1080, 1080):
          self.finished.emit(f"인코딩 중(플레이리스트)... 잠시만 기다려주세요\r\n{bg_clip.size[0]}x{bg_clip.size[1]} 23.976fps, {duration:.2f}초({bgm_from:.2f} - {bgm_to:.2f})\r\n주의: 권장 해상도(1080x1080)와 일치하지 않습니다!")
        else:
          self.finished.emit(f"인코딩 중(플레이리스트)... 잠시만 기다려주세요\r\n{bg_clip.size[0]}x{bg_clip.size[1]} 23.976fps, {duration:.2f}초({bgm_from:.2f} - {bgm_to:.2f})")

        final_clip.write_videofile(output_path, fps=23.976, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger=logger)
        self.finished.emit(f"파일이 출력되었습니다! (플레이리스트)\r\n저장 경로: {output_path}")
        return

      elif self.ty == 1:
        bgm_loop_padding = 1.8
        bgm_fadein = 0.15
        bgm_fadeout = 2
        duration = bgm_fadein + self.bgm_to - self.bgm_from + bgm_fadeout + bgm_loop_padding

        bgm_clip: AudioFileClip = AudioFileClip(self.bgm_path)
        bgm_len: int = int(bgm_clip.duration)
        if self.bgm_from >= self.bgm_to:
          self.finished.emit(f"오류! 시작 시간이 종료 시간보다 늦습니다!")
          return
        bgm_from: float = max(self.bgm_from - bgm_fadein, 0)
        bgm_to: float = min(self.bgm_to + bgm_fadeout, bgm_len)
        bgm_clip = bgm_clip.subclipped(bgm_from, bgm_to)
        bgm_clip = bgm_clip.with_effects([
          AudioFadeIn(bgm_fadein),
          AudioFadeOut(bgm_fadeout),
          AudioNormalize()
        ]) # fade in-out & normalization

        bg_clip: ImageClip = ImageClip(self.bg_path).with_duration(duration)

        logger = BarLogger()
        logger.set_signal(self.progress)
        bgm_clip.with_volume_scaled(0.95)
        final_clip = bg_clip.with_audio(bgm_clip)

        output_path: str = os.path.join(self.save_path, f"{os.path.splitext(os.path.basename(self.bg_path))[0]}.mp4")

        if os.path.exists(output_path):
          self.finished.emit("저장 경로에 파일이 이미 존재합니다!\r\n" + output_path)
          return
        
        if not bg_clip.size == (1080, 1080):
          self.finished.emit(f"인코딩 중(일본어 어휘)... 잠시만 기다려주세요\r\n{bg_clip.size[0]}x{bg_clip.size[1]} 23.976fps, {duration:.2f}초({bgm_from:.2f} - {bgm_to:.2f})\r\n주의: 권장 해상도(1080x1080)와 일치하지 않습니다!")
        else:
          self.finished.emit(f"인코딩 중(일본어 어휘)... 잠시만 기다려주세요\r\n{bg_clip.size[0]}x{bg_clip.size[1]} 23.976fps, {duration:.2f}초({bgm_from:.2f} - {bgm_to:.2f})")

        final_clip.write_videofile(output_path, fps=23.976, temp_audiofile="temp-audio.m4a", remove_temp=True, codec="libx264", audio_codec="aac", logger=logger)
        self.finished.emit(f"파일이 출력되었습니다! (일본어 어휘)\r\n저장 경로: {output_path}")
        return
    
    except Exception as e:
      self.finished.emit(f"오류가 발생했습니다!\r\n>> {e}\r\n{traceback.format_exc()}")
      return