from subprocess import Popen, PIPE
import subprocess
import re
import logging
_logger = logging.getLogger("IntersectPeaksLibs.external_program")


class ExternalProgram:
    def __init__(self, cmd, execute_cmd=False, show_cmd=False):
        self.cmd = cmd
        self.execute_cmd = execute_cmd
        self.show_cmd = show_cmd

    def print_cmd(self):
        _logger.info(f"CMD: {self.cmd}\n")

    def run_cmd(self):
        if self.execute_cmd:
            _logger.info("Running cmd...")
            if self.show_cmd:
                _logger.info(f"CMD: {self.cmd}\n")
            ps = subprocess.Popen(self.cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = ps.communicate()[0]
            return output

    def run_new_cmd(self, cmd):
        ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = ps.communicate()[0]
        return output

    def show_output(self, ln=10):
        output = self.run_cmd()
        if output:
            rows_str = output.decode('utf8')
            for idx, line in enumerate(rows_str.split('\n')):
                _logger.info(line)
                if idx > ln:
                    break
        else:
            _logger.info("\n No output\n")

    def line_count(self):
        wc_cmd = f"{self.cmd} | wc"
        output = self.run_new_cmd(wc_cmd)
        if output:
            r_str = output.decode('utf8')

            group = re.split(r'\W+', r_str.strip())
            _logger.info(group)
            return group


def file_line_count(file_path):
    p = Popen(['wc', file_path], stdout=PIPE)
    wc = None
    for line in p.stdout:
        wc, wc1, wc2, file = line.rstrip().split()
    return int(wc)

