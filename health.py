import pyCZERTAINLY
from pyCZERTAINLY.models.connector_dto import ConnectorDto
from pyCZERTAINLY.models.connector_status import ConnectorStatus
from pyCZERTAINLY.models.function_group_code import FunctionGroupCode
from pyCZERTAINLY.rest import ApiException
from pprint import pprint
import urllib3
import argparse


# cmdline arguments

parser = argparse.ArgumentParser(
    description="czertainly-health.py: an example how to use API to check status of CZERTAINLY")

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

configuration = pyCZERTAINLY.Configuration(
    host = args.URL
)

configuration.verify_ssl = not args.insecure
if args.insecure:
    urllib3.disable_warnings()

configuration.cert_file = args.cert
configuration.key_file = args.key

# TODO check core
# /api/v1/health/liveness not present in API, cuz is undocumented :(

# Iterate over all connectors, print their name and status
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)

    try:
        # List Connectors by Function Group and Kind
        print("Status of all connectors:")
        api_response = api_instance.list_connectors()
        for connector in api_response:
            try:
                conn_status = api_instance.check_health(connector.uuid)
                print(f"  {connector.name}: {conn_status.status.value}")
            except Exception as e:
                print(f"  {connector.name}: down")

    except Exception as e:
        print("Exception when calling ConnectorManagementApi->list_connectors: %s\n" % e)

# example usage:
# ~/.venvs/pyCZERTAINLY/bin/python ./health.py --insecure --URL https://czertainly.doma.tomasek.cz/api --cert /home/semik/3K/admin.pem --key /home/semik/3K/admin.key