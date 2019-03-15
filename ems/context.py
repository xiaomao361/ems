from ems import models


def not_read_notices(request):
    notices = models.Notice.objects.filter(is_read=0)
    return {'not_read_notices': notices}
