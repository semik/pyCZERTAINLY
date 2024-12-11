import pyCZERTAINLY
import pyCZERTAINLY.configuration
from pyCZERTAINLY.models.connector_dto import ConnectorDto
from pyCZERTAINLY.models.connector_status import ConnectorStatus
from pyCZERTAINLY.models.function_group_code import FunctionGroupCode
from pyCZERTAINLY.rest import ApiException
from pprint import pprint
import urllib3
import argparse


# cmdline arguments

parser = argparse.ArgumentParser(
    description="initC.py: an example how to use API to check status of CZERTAINLY")

parser.add_argument('--URL', required=True, default='https://czertainly.local',
                    help='URL where CZERTAINLY is running  (default: %(default)s)')
parser.add_argument('--cert', required=True,
                    help='PEM file with admin certificate for CZERTAINLY instance' )
parser.add_argument('--key', required=True,
                    help='PEM file with key for admin certificate for CZERTAINLY instance' )
parser.add_argument('--insecure', action='store_true', default=False,
                    help='disable certificate validation (default: %(default)s)')
parser.add_argument('--show-uri', action='store_true', default=False,
                    help='show URI for connectors (default: %(default)s)')

args = parser.parse_args()

if args.insecure:
    urllib3.disable_warnings()

# initialize API using cmdline arguments
api_config = pyCZERTAINLY.Configuration(
    host = args.URL
)

api_config.verify_ssl = not args.insecure
if args.insecure:
    urllib3.disable_warnings()

api_config.cert_file = args.cert
api_config.key_file = args.key

# Iterate over all connectors, print their name and status
print("Creating api_client: ", end="", flush=True)
api_client = pyCZERTAINLY.ApiClient(api_config)
print("OK")

print("Creating connectors_api: ", end="", flush=True)
connectors_api = pyCZERTAINLY.ConnectorManagementApi(api_client)
print("OK")

try:
    # List Connectors by Function Group and Kind
    print("Status of all connectors:")
    connectors = connectors_api.list_connectors()
    for connector in connectors:
        try:
            approve_status = connectors_api.approve(connector.uuid)
            print(f"  {connector.name}: {approve_status.message.value}")
            exit(1)
        except Exception as e:
            if e.status == 422:
                print(f"  {connector.name}: already CONNECTED")

except Exception as e:
    print("Exception when calling ConnectorManagementApi->list_connectors: %s\n" % e)

# example usage:
# ~/.venvs/pyCZERTAINLY/bin/python ./health.py --insecure --URL https://czertainly.doma.tomasek.cz/api --cert /home/semik/3K/admin.pem --key /home/semik/3K/admin.key