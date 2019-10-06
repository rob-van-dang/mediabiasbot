import praw

# MAIN ########################################################################
if __name__ == "__main__":
    reddit = praw.Reddit()
    print(reddit.read_only)
