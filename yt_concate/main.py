from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.read_caption import ReadCaptions
from yt_concate.pipeline.steps.step import StepException
from yt_concate.utils import Utils
from yt_concate.pipeline.steps.postflight import Postflight
from yt_concate.pipeline.steps.initialize_yt import InitializeYT
from yt_concate.pipeline.steps.search import Search
from yt_concate.pipeline.steps.download_videos import DownloadVideos
from yt_concate.pipeline.steps.edit_video import EditVideo

from yt_concate.pipeline.pipeline import Pipeline
CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA' # car
# CHANNEL_ID = 'UCpJmBQ8iNHXeQ7jQWDyGe3A' # life 407 2022/3/19


def main():
    inputs = {
        'channel_id': CHANNEL_ID,
        'search_word': 'incredible',
        'limit': 156,
    }
    steps = [
        Preflight(),
        GetVideoList(),
        InitializeYT(),
        DownloadCaptions(),
        ReadCaptions(),
        Search(),
        DownloadVideos(),
        EditVideo(),
        Postflight(),
    ]
    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()



# # alternative method
# import os
# path = path
# for root, dirs, files in os.walk(path):
#     print(len(files))
#     for file in files:
#         old = path + "\\" + file
#         new = path + "\\" + file + ".mp4"
#         os.rename(old, new)