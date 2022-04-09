#!/usr/bin/python
import sys
import logging

# getting currentdir
sys.path.insert(0, 'C:\\Users\\mrusia\\Desktop\\Network_Automation\\BGP_AUTOMATION\\Library\\')
from bgp_config_data import router_config_data
from bgp_setup import Router_setup_info
from bgp_lib import Bgp_lib
from utility import Utility
from bgp_rpc_data import Bgp_rpc_data

try:
    from ncclient import manager
    # from j5inja2 import Environment, FileSystemLoade
    import xmltodict
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)

logging.basicConfig(filename="bgp_auth_validation.log", level=logging.DEBUG)


class Bgp_Auth_validation(router_config_data, Router_setup_info, Bgp_lib, Utility, Bgp_rpc_data):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testArgs = kwargs
        self.initLib()
        self.testInit()

    def testInit(self):
        self.dut1 = self.create_session(self.router1, session_type="yui")
        self.dut2 = self.create_session(self.router2, session_type="yui")

    def initLib(self):
        self.topology_info()
        self.router_data()
        self.config_data()

    def configure_bgp(self):
        for data in self.dut1_config_data:
            self.config_bgp(self.dut1, data)
        import pdb
        pdb.set_trace()
        self.config_bgp(self.dut2, self.dut2_bgp_rpc_config_data)

    def validate_bgp_neighbourship(self, bgp_dict):
        pass

    def config_bgp_auth(self):
        pass

    def testCleanup(self):
        self.dut1.close_session()
        self.dut2.close_session()


if __name__ == '__main__':
    ni = Bgp_Auth_validation()
    ni.configure_bgp()
    # ni.validate_bgp_neighborship()
    # ni.config_bgp_auth()
