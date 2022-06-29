from core.tasks import countdown


def my_scheduled_job():
    from core.models import Test
    Test.objects.create(name  = 'love')
    # countdown.delay(10)
    
    
        
    
    