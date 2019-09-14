# returns true if running as part of a development virtual
# machine, false if not.
#
# relies on the file /opt/tiptap/configs/dev_vm.yml
#
from . import config


def is_dev_vm():
    vm = config.load_config("/opt/tiptap/configs/dev_vm.yml")
    return vm['status']
