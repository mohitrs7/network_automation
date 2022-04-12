import logging
import sys
import xml.etree.ElementTree as ET
import time
from pprint import pprint
import os
log = logging.getLogger(__name__)
pr_dir = os.path.abspath('../Script')
sys.path.insert(1, pr_dir)
try:
    from ncclient import manager
    import xmltodict
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)
from utility import Utility
from bgp_rpc_data import BgpRpcData


class BgpLib(Utility, BgpRpcData):
    ##############################################################
    # This method will configure BGP on  router based on input RPC
    # attributes :
    #              dut :            device under test
    #              config_data :    RPC data in form of tuple (RPC, rpc description)
    #              desc_:            Description of proc
    # Usage :
    #               self.dut1 = self.config_bgp(self.dut1, self.dut1_config_data, desc_="This proc will configure BGP on DUT1")
    ##############################################################

    def config_bgp(self, dut, config_data, desc_=""):
        try:
            rpc_obj = dut.edit_config(config_data[0], target='running', default_operation="merge")
            if "<ok/>" in str(rpc_obj):
                print(f"{config_data[1]}")
            else:
                log.error(f"RCP {config_data[0]} failed")
        except Exception:
            log.exception("Exception in BGP config")

    ##############################################################
    # This method will be used to get bgp operational data
    # attributes :
    #              dut :         device under test
    #              get_data :    BGP get data RPC
    #              desc_:        Description of proc
    # Usage :
    #     self.dut1 = self.get_bgp_data(self.router1, """<bgp:bgp-state xmlns:bgp="http://ciena.com/ns/yang/ciena-bgp"/>""")
    ##############################################################
    def get_bgp_data(self, dut, get_data, desc_=""):
        try:
            print("getting BGP state data ......")
            get_status = dut.get(filter=("subtree", get_data))
            return str(get_status)
        except Exception:
            log.exception("Exception in BGP state data")

    ##############################################################
    # This method converts xml RPC to ordered dict
    # attributes :
    #              object_data :     RPC data
    # Usage :
    #     self.dut1 = self.convert_xml_to_dict(object_data)
    ##############################################################
    def convert_xml_to_dict(self, object_data):
        output = xmltodict.parse(str(object_data))
        if bool(output):
            return output

    ##############################################################
    # This method will validates BGP neighbors , it takes XML RPC , convert it into ordered dict and matches with expected_state
    # attributes :
    #              dut :                dictionary contains all mandatory and non mandatory parameters
    #              rpc_data :           session type to be configured for device operation
    #              expected_state:      No. of tries manager attempts before closing the session
    # Usage :
    #     self.dut1 = self.create_session(self.router1, session_type="yui", desc_="create netconf session to device 1")
    ##############################################################
    def validate_bgp_neighbor(self, dut, rpc_data, expected_state, desc_=""):
        bgp_data_output = self.get_bgp_data(dut, rpc_data)
        output = self.convert_xml_to_dict(bgp_data_output)
        out_state = output['rpc-reply']['data']['bgp-state']['instance']['peer']['address-family']['state']
        if str(out_state) == expected_state:
            print(f"BGP neighbor state verified, current state is {out_state}")
        else:
            logging.error("Failed to validate BGP peer state")

    ##############################################################
    # This method will be used to get bgp configuration data
    # attributes :
    #              dut :         device under test
    #              get_data :    BGP get config data RPC
    #              desc_:        Description of proc
    # Usage :
    #     self.dut1 = self.get_bgp_config_data(self.router1, """<bgp:bgp xmlns:bgp="http://ciena.com/ns/yang/ciena-bgp"/>""")
    ##############################################################
    def get_bgp_config_data(self, dut, getConfig_data, desc_=""):
        try :
            print("getting config data for  BGP......")
            get_status = dut.get_config(source="running", filter=("subtree", getConfig_data))
            return str(get_status)
        except Exception:
            log.exception("Exception in BGP config data")

    ##############################################################
    # This method will configure BGP parameters on  router based on input RPC
    # attributes :
    #              dut :            device under test
    #              config_data :    RPC data
    #              desc_:           Description of proc
    # Usage :
    #               self.dut1 = self.modify_bgp_data(self.dut1, self.dut1_config_data, desc_="This proc will configure BGP on DUT1")
    ##############################################################
    def modify_bgp_data(self, dut, config_data, desc_=""):
        try:
            rpc_obj = dut.edit_config(config_data, target='running', default_operation="merge")
            if "<ok/>" in str(rpc_obj):
                print("BGP data modified")
            else:
                log.error(f"Rpc {config_data} failed")
        except Exception:
            log.exception("Exception in BGP config")

    ##############################################################
    # This method will configure BGP parameters on  router based on input RPC
    # attributes :
    #              dut_ssh :    ssh connection for device under test
    #              command :    command to run on cli prompt
    #              desc_:       Description of proc
    # Usage :
    #               get_data = self.get_cli_output(self.dut1_ssh, "sh bgp peers", desc_="This proc will display BGP peer info on DUT1")
    ##############################################################
    def get_cli_output(self, dut_ssh, command, desc_=""):
        try:
            dut_ssh.send("\n")
            dut_ssh.send(command)
            dut_ssh.send("\n")
            time.sleep(10)
            output = dut_ssh.recv(10000)
            if output is not None:
                pprint(output)
                return output
            else:
                print("No data retrieved from cli")
        except Exception:
            log.exception("Exception in BGP peer show command")

    ##############################################################
    # This method will configure BGP parameters on  router based on input RPC
    # attributes :
    #              dut_ssh :    ssh connection for device under test
    #              command :    command to run on cli prompt
    #              desc_:       Description of proc
    # Usage :
    #               get_data = self.get_cli_output(self.dut1_ssh, "sh bgp peers", "Connect", desc_="This proc will display BGP peer info on DUT1")
    ##############################################################
    def get_bgp_state_cli(self, dut_ssh, command, bgp_state, desc_=""):
        try:
            cli_data = self.get_cli_output(dut_ssh, command)
            if cli_data:
                if bgp_state in str(cli_data):
                    print(f"BGP state is {bgp_state} as expected")
                else:
                    print("BGP state is not as expected")
            else:
                print("CLI data does not display any output")
        except Exception:
            log.exception("Exception in BGP peer show command")

    ##############################################################
    # This method will configure BGP parameters on  router based on input RPC
    # attributes :
    #              dut_ssh :    ssh connection for device under test
    #              command :    command to run on cli prompt
    #              desc_:       Description of proc
    # Usage :
    #               get_data = self.get_cli_output(self.dut1_ssh, "sh bgp peers", "Connect", desc_="This proc will display BGP peer info on DUT1")
    ##############################################################
    def ping_interface(self, dut_ssh, destination, desc_=""):
        try:
            command = "ping ip destination "+ destination+ "\n"
            dut_ssh.send("\n")
            dut_ssh.send(command)
            dut_ssh.send("\n")
            time.sleep(10)
            output = dut_ssh.recv(10000)
            # if output is not None:
            #     pprint(output)
            if output is not None:
                if "Success Rate is 100.00 percent" in str(output):
                    print(f"ping success to destination {destination}")
                else:
                    print(f"ping failed for destination {destination}")
            else:
                print("CLI data does not display any output")
        except Exception:
            log.exception("Exception in BGP peer show command")

    ##############################################################
    # This method creates the router interface based on provided input
    # attributes :
    #              router_data_dict :dictionary contains all mandatory and non mandatory parameters
    #              session_type :    session type to be configured for device operation
    #              MAX_RETRIES:      No. of tries manager attempts before closing the session
    #              desc_:            Description of proc
    # Usage :
    #     self.dut1 = self.create_session(self.router1, session_type="yui", desc_="create netconf session to device 1")
    ##############################################################
    def get_bgp_bulk_rpc_cmd(self, xpath, msgID="7"):
        rpc = ET.Element("rpc")
        rpc.set("xmlns", "urn:ietf:params:xml:ns:netconf:base:1.0")
        rpc.set("message-id", msgID)
        get_bulk = ET.SubElement(rpc, "get-bulk")
        get_bulk.set("xmlns", "http://yumaworks.com/ns/yumaworks-getbulk")
        list_target = ET.SubElement(get_bulk, "list-target")
        list_target.text = xpath
        get_bulk_str = ET.tostring(rpc).decode()
        return get_bulk_str

    ##############################################################
    # This method creates the router interface based on provided input
    # attributes :
    #              router_data_dict :dictionary contains all mandatory and non mandatory parameters
    #              session_type :    session type to be configured for device operation
    #              MAX_RETRIES:      No. of tries manager attempts before closing the session
    #              desc_:            Description of proc
    # Usage :
    #     self.dut1 = self.create_session(self.router1, session_type="yui", desc_="create netconf session to device 1")
    ##############################################################
    def send_get_bulk_rpc(self, nc_obj, xpath="/bgp-state/instance/peer/address-family/peer-adjacency-in"):
        try:
            get_bulk = self.get_ppm_bulk_rpc_cmd(xpath)
            if get_bulk:
                RPC_Reply = nc_obj.send_str(get_bulk, timeout=35000)
                self.ctfLogInfo ("RPC_Reply is: %s" % RPC_Reply)
                if RPC_Reply is not None:
                    return RPC_Reply
                else:
                    self.ctfLogInfo("GET bulk not found")
                    return False
            else:
                self.ctfLogInfo ("Build GET bulk ppm RPC command returned False")
                return False
        except Exception as error:
            self.ctfLogInfo("Exception occurs in send_get_bulk_rpc methd , exception is : {}".format(error))
            return False
