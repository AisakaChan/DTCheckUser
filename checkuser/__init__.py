import argparse
import logging

from .infra.http.flask import app
from .infra.ws.websocket import ws
from .infra.ws.socketio import io

logger = logging.getLogger(__name__)

__version__ = '2.0.1'
__author__ = 'Aisaka Taiga'
__email__ = '@aisaka_chan'

__description__ = (
    'DTCheckerMod - CHECKUSER | '
    'BY ' + __author__ + ' <' + __email__ + '> | '
    'VERSION: ' + __version__
)


args = argparse.ArgumentParser(description=__description__)
args.add_argument(
    '-v',
    '--version',
    action='version',
    version='%(prog)s ' + __version__,
)
