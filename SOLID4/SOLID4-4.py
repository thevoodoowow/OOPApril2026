from abc import abstractmethod


class AudioPlay:
    @abstractmethod
    def play_audio(self, file: str):
        pass


class VideoPlay:
    @abstractmethod
    def play_video(self, file: str):
        pass


class SubtitleDisplay:
    @abstractmethod
    def show_subtitles(self, file: str):
        pass


class AudioPlayer(AudioPlay):

    def play_audio(self, file: str):
        print(f"Воспроизведение аудио: {file}")


class VideoPlayer(AudioPlay, VideoPlay, SubtitleDisplay):

    def play_audio(self, file: str):
        print(f"Воспроизведение аудио: {file}")

    def play_video(self, file: str):
        print(f"Воспроизведение видео: {file}")

    def show_subtitles(self, file: str):
        print(f"Субтитры: {file}")


def start_music(player: AudioPlay, track: str):
    player.play_audio(track)


def start_movie(player: VideoPlay, movie: str):
    player.play_video(movie)


audio = AudioPlayer()
video = VideoPlayer()

start_music(audio, "song.mp3")
start_movie(video, "film.mp4")
