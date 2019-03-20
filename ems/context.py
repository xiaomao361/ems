from ems import models
import random


def not_read_notices(request):
    notices = models.Notice.objects.filter(is_read=0)
    num = random.randint(1, len(models.Joke.objects.all()))
    joke = models.Joke.objects.get(id=num)
    return {'not_read_notices': notices, 'joke': joke}
