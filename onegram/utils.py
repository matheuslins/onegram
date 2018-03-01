import json
import logging
import time
import jmespath

from random import uniform
from requests import Response

from . import settings as settings_module

logger = logging.getLogger(__name__)


def load_settings(custom_settings={}):
    settings = {k:getattr(settings_module, k)
                for k in dir(settings_module) if k.isupper()}
    settings.update(custom_settings)
    return settings

def jsearch(jspath, content):
    if isinstance(content, dict):
        dct = content
    else:
        if isinstance(content, Response):
            text = content.text
        elif isinstance(content, str):
            text = content
        else:
            raise TypeError()
        dct = json.loads(text)

    return jmespath.search(jspath, dct)

def sleep(t, var=.5):
    if t:
        sleep_time = uniform((1-var)*t, (1+var)*t) 
        logger.info(f'{sleep_time:.{2}f} seconds')
        time.sleep(sleep_time)
