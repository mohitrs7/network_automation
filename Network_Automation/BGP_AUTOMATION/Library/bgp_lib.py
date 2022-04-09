import logging
import sys
log = logging.getLogger(__name__)
sys.path.insert(0, 'C:\\Users\\mrusia\\Desktop\\Network_Automation\\BGP_AUTOMATION\\Script\\')
try:
    from ncclient import manager
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(0)
from utility import Utility
from bgp_rpc_data import Bgp_rpc_data


class Bgp_lib(Utility, Bgp_rpc_data):
    def config_bgp(self, dut, config_data):
        print("configuring BGP......")
        try:
            import pdb
            pdb.set_trace()
            rpc_obj = dut.edit_config(config_data, target='running')
            print(rpc_obj)
        except Exception:
            log.exception("Exception in BGP config")

    def validate_bgp(self):
        pass
