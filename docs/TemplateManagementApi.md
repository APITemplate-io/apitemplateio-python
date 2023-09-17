# APITemplateio.TemplateManagementApi

All URIs are relative to *https://rest.apitemplate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_template**](TemplateManagementApi.md#get_template) | **GET** /v2/get-template | Get PDF template
[**list_templates**](TemplateManagementApi.md#list_templates) | **GET** /v2/list-templates | List Templates
[**update_template**](TemplateManagementApi.md#update_template) | **POST** /v2/update-template | Update PDF Template


# **get_template**
> ResponseSuccessTemplate get_template(template_id=template_id)

Get PDF template

Retrieves information of the PDF template (**This is an experimental API, contact support to learn more**) 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_template import ResponseSuccessTemplate
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
    api_instance = APITemplateio.TemplateManagementApi(api_client)
    template_id = '00377b2b1e0ee394' # str | Your template id, it can be obtained in the web console(Manage Templates) (optional)

    try:
        # Get PDF template
        api_response = api_instance.get_template(template_id=template_id)
        print("The response of TemplateManagementApi->get_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateManagementApi->get_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Your template id, it can be obtained in the web console(Manage Templates) | [optional] 

### Return type

[**ResponseSuccessTemplate**](ResponseSuccessTemplate.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns status and template information |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_templates**
> ResponseSuccessListTemplates list_templates(limit=limit, offset=offset, format=format, template_id=template_id, group_name=group_name, with_layer_info=with_layer_info)

List Templates

Retrieves the information of templates 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_list_templates import ResponseSuccessListTemplates
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
    api_instance = APITemplateio.TemplateManagementApi(api_client)
    limit = '300' # str | Retrieve only the number of records specified. Default to 300 (optional)
    offset = '0' # str | Offset is used to skip the number of records from the results. Default to 0 (optional)
    format = 'JPEG' # str | To filter the templates by either 'PDF' or 'JPEG' (optional)
    template_id = '00377b2b1e0ee394' # str | To filter the templates by template id (optional)
    group_name = 'custom' # str | To filter the templates by the group name (optional)
    with_layer_info = '0' # str | Return along with layer information for image templates, 0=false , 1=true. Default to '0' (optional)

    try:
        # List Templates
        api_response = api_instance.list_templates(limit=limit, offset=offset, format=format, template_id=template_id, group_name=group_name, with_layer_info=with_layer_info)
        print("The response of TemplateManagementApi->list_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateManagementApi->list_templates: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Retrieve only the number of records specified. Default to 300 | [optional] 
 **offset** | **str**| Offset is used to skip the number of records from the results. Default to 0 | [optional] 
 **format** | **str**| To filter the templates by either &#39;PDF&#39; or &#39;JPEG&#39; | [optional] 
 **template_id** | **str**| To filter the templates by template id | [optional] 
 **group_name** | **str**| To filter the templates by the group name | [optional] 
 **with_layer_info** | **str**| Return along with layer information for image templates, 0&#x3D;false , 1&#x3D;true. Default to &#39;0&#39; | [optional] 

### Return type

[**ResponseSuccessListTemplates**](ResponseSuccessListTemplates.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns status and output file |  -  |
**0** | unexpected error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_template**
> ResponseSuccess update_template(update_template_request)

Update PDF Template

This endpoint updates PDF template (**This is an experimental API, contact support to learn more**)

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success import ResponseSuccess
from APITemplateio.models.update_template_request import UpdateTemplateRequest
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
    api_instance = APITemplateio.TemplateManagementApi(api_client)
    update_template_request = APITemplateio.UpdateTemplateRequest() # UpdateTemplateRequest | 

    try:
        # Update PDF Template
        api_response = api_instance.update_template(update_template_request)
        print("The response of TemplateManagementApi->update_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateManagementApi->update_template: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_template_request** | [**UpdateTemplateRequest**](UpdateTemplateRequest.md)|  | 

### Return type

[**ResponseSuccess**](ResponseSuccess.md)

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

