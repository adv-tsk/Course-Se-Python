# -*- coding: utf-8 -*-

import os

from . import config


# firefox settings
FIREFOX = {
    'binary': '/usr/bin/firefox',
    'executable_path': os.path.join(os.path.dirname(config.BASE_DIR), 'geckodriver'),
}


# chrome settings
CHROME = {

}

# ei settings
IE = {

}
