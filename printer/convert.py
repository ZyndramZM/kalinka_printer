from __future__ import print_function
import time
import cloudmersive_convert_api_client
from cloudmersive_convert_api_client.rest import ApiException
from pprint import pprint


def to_PDF(filepath):
    # Configure API key authorization: Apikey
    configuration = cloudmersive_convert_api_client.Configuration()
    configuration.api_key['Apikey'] = '1748048b-c983-49a8-952d-dea639c83e20'
    # Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
    # configuration.api_key_prefix['Apikey'] = 'Bearer'
    # create an instance of the API class
    api_instance = cloudmersive_convert_api_client.ConvertDocumentApi(
        cloudmersive_convert_api_client.ApiClient(configuration))

    try:
        # Convert Document to PDF
        api_response = api_instance.convert_document_autodetect_to_pdf(filepath)
        pprint(api_response)
        return api_response
    except ApiException as e:
        print("Exception when calling ConvertDocumentApi->convert_document_autodetect_to_pdf: %s\n" % e)
