# Scenario:
# 2) Simulate a YouTube video. The rule is: A user cannot 'Like' a video without 'Watching' it first.
# Class Name: YouTubeVideo
# Attributes:
# title: Name of the video.
# views: Initially 0.
# likes: Initially 0.
# Methods:
# watch():Increase the views count by 1.
# Print "User watched the video."
# like():Check if views is greater than 0.If yes, increase likes count by 1.
# If no (views is 0), print "Error: You must watch the video before liking it."
# details():
# Print the Title, Total Views, and Total Likes.


class YouTubeVideo:
    def __init__(self, title):
        self.title = "FunnyVideos"
        self.views = 0
        self.likes = 0

    def watch(self):
        self.views +=1
        print("User watched the video")

    def like(self):
        if self.views > 0:
            self.likes +=1
            print("User liked the video")
        else:
            print("You must watch the video before liking it")

    def details(self):
        print("\n----- VIDEO DETAILS -----")
        print(f"Title : {self.title}")
        print(f"Total Views : {self.views}")
        print(f"Total Likes : {self.likes}")
        print("--------------------------")

    video = YouTubeVideo("Python Tutorial")

    video.like()
    video.watch()
    video.like()
    video.watch()
    video.like()
    video.details()

