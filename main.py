import logging

import praw

logging.basicConfig()
LOG = logging.getLogger('mediabiasbot')
LOG.setLevel(logging.INFO)
SUBREDDIT_NAME = 'testingground4bots'


def check_comment(comment):
    LOG.info(comment.body)


def check_submission(submission):
    LOG.info("===" + submission.id + "===")
    LOG.info("===" + submission.title + "===")
    LOG.info("===" + submission.url + "===")


# MAIN ########################################################################
if __name__ == "__main__":
    reddit = praw.Reddit()
    if not reddit.read_only:
        LOG.info("======= Logged in Successfully =======")
    sub = reddit.subreddit(SUBREDDIT_NAME)

    submission_stream = sub.stream.submissions(pause_after=-1)
    comment_stream = sub.stream.comments(pause_after=-1)
    while True:
        # Check submission stream
        for submission in submission_stream:
            if submission is None:
                break
            check_submission(submission)

        # Check comment stream
        for comment in comment_stream:
            if comment is None:
                break
            check_comment(comment)
