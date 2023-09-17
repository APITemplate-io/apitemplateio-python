# APITemplateio.PDFManipulationAPIApi

All URIs are relative to *https://rest.apitemplate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**merge_pdfs**](PDFManipulationAPIApi.md#merge_pdfs) | **POST** /v2/merge-pdfs | Join/Merge multiple PDFs


# **merge_pdfs**
> ResponseSuccessSingleFile merge_pdfs(merge_pdfs_request, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta)

Join/Merge multiple PDFs

This endpoint merges/joins multiple PDF URLs into a single PDF file

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.merge_pdfs_request import MergePdfsRequest
from APITemplateio.models.response_success_single_file import ResponseSuccessSingleFile
from APITemplateio.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://rest.apitemplate.io
# See configuration.py for a list of all supported configuration parameters.
configuration = APITemplateio.Configuration(
    host = "https://rest.apitemplate.io"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with APITemplateio.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = APITemplateio.PDFManipulationAPIApi(api_client)
    merge_pdfs_request = APITemplateio.MergePdfsRequest() # MergePdfsRequest | 
    postaction_s3_filekey = 'postaction_s3_filekey_example' # str | - This is to specify the file name for `Post Action(S3 Storage)`. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  (optional)
    postaction_s3_bucket = 'postaction_s3_bucket_example' # str | - This is to overwrite the AWS Bucket for `Post Action(S3 Storage)`.  (optional)
    meta = 'inv-iwj343jospig' # str | - Specify an external reference ID for your own reference. It appears in the `list-objects` API.  (optional)

    try:
        # Join/Merge multiple PDFs
        api_response = api_instance.merge_pdfs(merge_pdfs_request, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta)
        print("The response of PDFManipulationAPIApi->merge_pdfs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PDFManipulationAPIApi->merge_pdfs: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **merge_pdfs_request** | [**MergePdfsRequest**](MergePdfsRequest.md)|  | 
 **postaction_s3_filekey** | **str**| - This is to specify the file name for &#x60;Post Action(S3 Storage)&#x60;. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  | [optional] 
 **postaction_s3_bucket** | **str**| - This is to overwrite the AWS Bucket for &#x60;Post Action(S3 Storage)&#x60;.  | [optional] 
 **meta** | **str**| - Specify an external reference ID for your own reference. It appears in the &#x60;list-objects&#x60; API.  | [optional] 

### Return type

[**ResponseSuccessSingleFile**](ResponseSuccessSingleFile.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns status and output file |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

