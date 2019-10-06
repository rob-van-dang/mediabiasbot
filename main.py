import logging

import praw

logging.basicConfig()
LOG = logging.getLogger('mediabiasbot')
LOG.setLevel(logging.INFO)
SUBREDDIT_NAME = 'testingground4bots'


def check_comments(submission):
    submission.comment_sort = 'new'
    for tl_comment in submission.comments:
        if tl_comment.body:
            LOG.info(tl_comment.body)


# MAIN ########################################################################
if __name__ == "__main__":
    reddit = praw.Reddit()
    if not reddit.read_only:
        LOG.info("======= Logged in Successfully =======")

    sub = reddit.subreddit(SUBREDDIT_NAME)
    for submission in sub.stream.submissions():
        LOG.info("===" + submission.id + "===")
        LOG.info("===" + submission.title + "===")
        LOG.info("===" + submission.url + "===")
        check_comments(submission)
