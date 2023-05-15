import logging
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### can use logger.debug('message') to log messages to the console
logger = logging.getLogger(__name__)


def group_history(request):
    return render(request, 'group_history.html')

