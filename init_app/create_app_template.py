import argparse
import os
import logging
from pprint import pformat


def get_logger(name, verbose=False):
    _logger = logging.getLogger(name)
    stream = logging.StreamHandler()
    format = logging.Formatter('[%(process)d] %(asctime)s:%(lineno)d:%(funcName)s:%(levelname)s:%(message)s')
    stream.setFormatter(format)
    _logger.setLevel(logging.DEBUG)
    _logger.addHandler(stream)
    return _logger


parser = argparse.ArgumentParser(description="Create a python project template")

parser.add_argument(
'-n',
'--name',
help='Please provide project name',
required=True,
default=None,
dest='name',
)
parser.add_argument(
'-p',
'--path',
help='Please provide path to create the structure',
required=False,
default=None,
dest='path',
)
parser.add_argument(
'--ui',
help='Please provide path to create the structure',
required=False,
action='store_true',
default=False,
dest='ui',
)
parser.add_argument(
'-v',
help='Show debug information',
required=False,
action='store_true',
default=False,
dest='verbose',
)

args = parser.parse_args()
logger = get_logger('template_logger',verbose=args.verbose)
logger.info(f'Creating template for {args.name}')
_path = os.getcwd() if args.path is None else args.path
path = os.path.abspath(_path)
name = args.name
ui_flag = args.ui

sub_dirs = ['scripts','lib','etc','out','logs']
ui_sub_dirs = ['static','templates']
if ui_flag is True:
    sub_dirs.extend(ui_sub_dirs)

base_dir = os.path.join(path, name)
logger.debug(f'Creating folders in path {base_dir}')
try:
    os.mkdir(base_dir)
    for dir in sub_dirs:
        try:
            _dir = os.path.join(base_dir, dir)
            logger.debug(f'Creating directory {_dir}')
            os.mkdir(_dir)
        except Exception as err:
            print(err)
    with open(os.path.join(base_dir, 'README.md'), 'w+') as f:
        f.write(f'Readme for {name}')
except FileExistsError:
    logger.info(f'{base_dir} already exists!!')
except Exception as err:
    logger.error('Could not create template!')
    logger.error(err)
    logger.info(f'Removing {base_dir}')
    os.removedirs(base_dir)
