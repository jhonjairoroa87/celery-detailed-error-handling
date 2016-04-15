from __future__ import absolute_import
from proj.tasks import print_add, print_div, print_log

if __name__ == '__main__':
    print_add.delay(2, 4)
    print_div.delay(2, 1)
    print_div.delay(2, 0)  # this raises an internal error, no error is shown in the launcher console
    print_log.delay(2)
    print_log.delay(-1)  # this raises an internal error, no error is shown in the launcher console



