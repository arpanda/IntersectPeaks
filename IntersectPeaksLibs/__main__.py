import argparse
from pathlib import Path
from .logger import logger_setup
from .intersect import IntersectInfo


def main():
    parser = argparse.ArgumentParser(description="A python library for analyzing peaks by intersecting with relevant "
                                                 "datasets")
    parser.add_argument('-log', '--log_file', type=str, help='log file')
    parser.add_argument('-v', '--verbose', type=str,
                        choices=["none", "debug", "info", "warning", "error", "d", "e", "i", "w"],
                        help="verbose level: debug, info (default), warning, error", default="info")
    parser.add_argument('-peak_type', '--peak_type', type=str, help='Type of peak', default="narrowPeaks")
    parser.add_argument('-path1', '--data_path1', type=str, help='Data path 1')
    parser.add_argument('-path2', '--data_path2', type=str, help='Data path 2')

    args = parser.parse_args()

    logger = logger_setup(args.verbose, args.log_file)
    logger.debug("Start logging...")

    if Path(args.data_path1).exists() and Path(args.data_path2).exists():
        ip_1 = IntersectInfo(args.data_path1, args.data_path2)
        ip_1.file_count()

