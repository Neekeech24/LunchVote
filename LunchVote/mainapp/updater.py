from apscheduler.schedulers.background import BackgroundScheduler
from .votes_update import update_votes


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(update_votes, 'cron', hour='13')
    scheduler.start()