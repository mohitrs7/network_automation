import sys
import paramiko

try:
    from ncclient import manager
except ImportError as ie:
    print("It cannot import module and submodule, please install it via pip install ncclient command", ie)
    sys.exit(1)


class Utility():

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

    def create_session(self, router_data_dict, session_type="yui", MAX_RETRIES=3, desc_=""):
        # Establish our NETCONF Session
        mandatory_args = ['host', 'username', 'password']
        non_mandatory_args = ['hostkey_verify']

        for ags in mandatory_args:
            if ags not in list(router_data_dict.keys()):
                print(f"router_data_dict is missing few mandatory args {mandatory_args}")
                return False
            else:
                exec(f"{ags} = router_data_dict[f'{ags}']", locals(), globals())

        for ags in non_mandatory_args:
            if ags in list(router_data_dict.keys()):
                exec(f"{ags} = router_data_dict[f'{ags}']", locals(), globals())
            else:
                exec(f"{ags}=\'-\'", locals(), globals())

        if session_type == "yui":
            for _ in range(MAX_RETRIES):
                try:
                    session =  manager.connect(host=host, port=830, username=username, password=password,
                                         hostkey_verify=hostkey_verify)
                    if session.connected:
                        print(f"DUT {host} connected successfully")
                        return session
                except Exception as error:
                    print(f"Exception occurs during connection, msg is {error}")
                    return False
        elif session_type == "ssh":
            for _ in range(MAX_RETRIES):
                client = paramiko.client.SSHClient()
                client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                try :
                    client.connect(host, username=username, password=password, port=22)
                except Exception as _e:
                    sys.stdout.write(_e)
                    sys.exit(1)
                    #client.close()
