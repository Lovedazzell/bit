from celery import shared_task
import time
from celery_progress.backend import ProgressRecorder


    
@shared_task(bind=True)
def countdown(self, seconds):
    progress_recorder = ProgressRecorder(self)
    result = 0
        
    for i in range(170):
        time.sleep(1)
        result += i
        progress_recorder.set_progress(i + 1, 170)
    return result