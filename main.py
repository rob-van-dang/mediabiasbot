import logging

import praw

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
log = logging.getLogger('mediabiasbot')

# MAIN ########################################################################
if __name__ == "__main__":
    reddit = praw.Reddit()
    if not reddit.read_only:
        log.info("Logged in Successfully")
