"""
This module contains ContentsManager hooks used to attach information to notebooks.
"""

import logging

logger = logging.getLogger(__name__)

def pre_save_hook(path, model, contents_manager):
    logger.info(repr(model))
