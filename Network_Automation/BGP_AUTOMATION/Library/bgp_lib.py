import logging
import sys
log = logging.getLogger(__name__)
sys.path.insert(0, 'C:\\Users\\mrusia\\Desktop\\Network_Automation\\BGP_AUTOMATION\\Script\\')
try:
    from ncclient import manager
    import xmltodict
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)
from utility import Utility
from bgp_rpc_data import BgpRpcData


class BgpLib(Utility, BgpRpcData):

    def config_bgp(self, dut, config_data, desc_=""):
        try:
            rpc_obj = dut.edit_config(config_data[0], target='running', default_operation="merge")
            if "<ok/>" in str(rpc_obj):
                print(f"{config_data[1]}")
            else:
                log.error(f"RCP {config_data[0]} failed")
        except Exception:
            log.exception("Exception in BGP config")

    def get_bgp_data(self, dut, get_data):
        try:
            print("getting BGP state data ......")
            get_status = dut.get(filter=("subtree", get_data))
            return str(get_status)
        except Exception:
            log.exception("Exception in BGP state data")

    def convert_xml_to_dict(self, object_data):
        output = xmltodict.parse(str(object_data))
        if bool(output):
            return output

    def validate_bgp_neighbor(self, dut, rpc_data, expected_state, desc_=""):
        bgp_data_output = self.get_bgp_data(dut, rpc_data)
        output = self.convert_xml_to_dict(bgp_data_output)
        out_state = output['rpc-reply']['data']['bgp-state']['instance']['peer']['address-family']['state']
        if str(out_state) == expected_state:
            print(f"BGP neighbor state verified, current state is {out_state}")
        else:
            logging.error("Failed to validate BGP peer state")

    def get_bgp_config_data(self, dut, getConfig_data):
        try :
            print("getting config data for  BGP......")
            get_status = dut.get_config(source="running", filter=("subtree", getConfig_data))
            return str(get_status)
        except Exception:
            log.exception("Exception in BGP config data")

    def modify_bgp_data(self, dut, config_data, desc_=""):
        try:
            rpc_obj = dut.edit_config(config_data, target='running', default_operation="merge")
            if "<ok/>" in str(rpc_obj):
                print("BGP data modified")
            else:
                log.error(f"Rpc {config_data} failed")
        except Exception:
            log.exception("Exception in BGP config")