
class Found:
    def __init__(self, yt, caption, time):
        self.yt = yt            # 就是yt.py內class YT instance
        self.caption = caption
        self.time = time        # 時間序列；e.g. 00:11:26,630 --> 00:11:43,430

    #dunder str
    def __str__(self):
        return '<Found(yt=' + str(self.yt) + ')>'

    def __repr__(self):
        content = ' : '.join([
            'yt=' + str(self.yt),
            'caption=' + str(self.caption),
            'time=' + str(self.time)
        ])
        return '<Found(' + content + ')>'