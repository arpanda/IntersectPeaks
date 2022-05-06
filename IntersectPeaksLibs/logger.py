import logging


def logger_setup(verbose, log_file):
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    if verbose in {"debug", "d"}:
        level = logging.DEBUG
    elif verbose in {"info", "i"}:
        level = logging.INFO
    elif verbose in {"warning", "w"}:
        level = logging.WARNING
    elif verbose in {"error", "e"}:
        level = logging.ERROR
    else:
        level = logging.CRITICAL

    if log_file:
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format=log_format)
        logger = logging.getLogger('parseCentromere')
        ch = logging.StreamHandler()
        formatter = logging.Formatter(log_format)
        ch.setFormatter(formatter)
        ch.setLevel(level)
        logger.addHandler(ch)
    else:
        logging.basicConfig(level=level, format=log_format)
        logger = logging.getLogger('parseCentromere')

    return logger

