from pathlib import Path
import logging
_logger = logging.getLogger("IntersectPeaksLibs.intersect")


class IntersectInfo:
    def __init__(self, file_a, files_b, exclude_list=[]):
        self.file_a = Path(file_a).glob("*")
        self.files_b = files_b

    def file_count(self):
        _logger.info(f"File Count: {len(self.file_a)}")
