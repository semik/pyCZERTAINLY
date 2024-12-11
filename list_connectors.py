import pyCZERTAINLY
from pyCZERTAINLY.models.connector_dto import ConnectorDto
from pyCZERTAINLY.models.connector_status import ConnectorStatus
from pyCZERTAINLY.models.function_group_code import FunctionGroupCode
from pyCZERTAINLY.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:45309
# See configuration.py for a list of all supported configuration parameters.
configuration = pyCZERTAINLY.Configuration(
    host = "https://czertainly.doma.tomasek.cz/api/",

)
configuration.verify_ssl = False
configuration.cert_file = '/home/semik/3K/admin.pem'
configuration.key_file = '/home/semik/3K/admin.key'

# Enter a context with an instance of the API client
with pyCZERTAINLY.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pyCZERTAINLY.ConnectorManagementApi(api_client)
    #function_group = pyCZERTAINLY.FunctionGroupCode() # FunctionGroupCode |  (optional)
    #status = pyCZERTAINLY.ConnectorStatus() # ConnectorStatus |  (optional)

    try:
        # List Connectors by Function Group and Kind
        api_response = api_instance.list_connectors()
        print("The response of ConnectorManagementApi->list_connectors:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectorManagementApi->list_connectors: %s\n" % e)