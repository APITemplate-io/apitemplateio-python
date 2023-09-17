# APITemplateio.APIIntegrationApi

All URIs are relative to *https://rest.apitemplate.io*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_image**](APIIntegrationApi.md#create_image) | **POST** /v2/create-image | Create an Image
[**create_pdf**](APIIntegrationApi.md#create_pdf) | **POST** /v2/create-pdf | Create a PDF
[**create_pdf_from_html**](APIIntegrationApi.md#create_pdf_from_html) | **POST** /v2/create-pdf-from-html | Create a PDF from HTML
[**create_pdf_from_url**](APIIntegrationApi.md#create_pdf_from_url) | **POST** /v2/create-pdf-from-url | Create a PDF from URL
[**delete_object**](APIIntegrationApi.md#delete_object) | **GET** /v2/delete-object | Delete an Object
[**list_objects**](APIIntegrationApi.md#list_objects) | **GET** /v2/list-objects | List Generated Objects


# **create_image**
> ResponseSuccessImageFile create_image(template_id, body, output_image_type=output_image_type, expiration=expiration, cloud_storage=cloud_storage, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta)

Create an Image

This endpoint creates a JPEG file(along with PNG) with JSON data and your template 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_image_file import ResponseSuccessImageFile
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    template_id = '00377b2b1e0ee394' # str | Your template id, it can be obtained in the web console
    body = None # object | 
    output_image_type = '1' # str | - Output image type(JPEG or PNG format), default to `all`. Options are `all`, `jpegOnly`,`pngOnly`.  (optional)
    expiration = 5 # int | - Expiration of the generated PDF in minutes(default to `0`, store permanently)   - Use `0` to store on cdn permanently   - Or use the range between `1` minute and `10080` minutes(7 days) to specify the expiration of the generated PDF  (optional)
    cloud_storage = 1 # int | - Upload the generated PDFs/images to our storage CDN, default to `1`. If you have configured `Post Action` to upload the PDFs/Images to your own S3, please set it to `0`.  (optional)
    postaction_s3_filekey = 'postaction_s3_filekey_example' # str | - This is to specify the file name for `Post Action(S3 Storage)`. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  (optional)
    postaction_s3_bucket = 'postaction_s3_bucket_example' # str | - This is to overwrite the AWS Bucket for `Post Action(S3 Storage)`.  (optional)
    meta = 'inv-iwj343jospig' # str | - Specify an external reference ID for your own reference. It appears in the `list-objects` API.  (optional)

    try:
        # Create an Image
        api_response = api_instance.create_image(template_id, body, output_image_type=output_image_type, expiration=expiration, cloud_storage=cloud_storage, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta)
        print("The response of APIIntegrationApi->create_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->create_image: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Your template id, it can be obtained in the web console | 
 **body** | **object**|  | 
 **output_image_type** | **str**| - Output image type(JPEG or PNG format), default to &#x60;all&#x60;. Options are &#x60;all&#x60;, &#x60;jpegOnly&#x60;,&#x60;pngOnly&#x60;.  | [optional] 
 **expiration** | **int**| - Expiration of the generated PDF in minutes(default to &#x60;0&#x60;, store permanently)   - Use &#x60;0&#x60; to store on cdn permanently   - Or use the range between &#x60;1&#x60; minute and &#x60;10080&#x60; minutes(7 days) to specify the expiration of the generated PDF  | [optional] 
 **cloud_storage** | **int**| - Upload the generated PDFs/images to our storage CDN, default to &#x60;1&#x60;. If you have configured &#x60;Post Action&#x60; to upload the PDFs/Images to your own S3, please set it to &#x60;0&#x60;.  | [optional] 
 **postaction_s3_filekey** | **str**| - This is to specify the file name for &#x60;Post Action(S3 Storage)&#x60;. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  | [optional] 
 **postaction_s3_bucket** | **str**| - This is to overwrite the AWS Bucket for &#x60;Post Action(S3 Storage)&#x60;.  | [optional] 
 **meta** | **str**| - Specify an external reference ID for your own reference. It appears in the &#x60;list-objects&#x60; API.  | [optional] 

### Return type

[**ResponseSuccessImageFile**](ResponseSuccessImageFile.md)

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

# **create_pdf**
> ResponseSuccessPDFFile create_pdf(template_id, body, export_type=export_type, expiration=expiration, output_html=output_html, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)

Create a PDF

This endpoint creates a PDF file with JSON data and your template. We support synchoronus and asynchronous PDF generation.

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_pdf_file import ResponseSuccessPDFFile
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    template_id = '00377b2b1e0ee394' # str | Your template id, it can be obtained in the web console
    body = None # object | 
    export_type = 'json' # str | - Either `file` or `json`(Default).   - The option `json` returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter `expiration`   - The option `file` returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  (optional)
    expiration = 5 # int | - Expiration of the generated PDF in minutes(default to `0`, store permanently)   - Use `0` to store on cdn permanently   - Or use the range between `1` minute and `10080` minutes(7 days) to specify the expiration of the generated PDF  (optional)
    output_html = '0' # str | - Either `1` or `0`(Default). - To enable output of html content, set the value to `1` and it will return in the JSON response as html_url field (as a URL)  (optional)
    output_format = 'pdf' # str | - Either `pdf`(Default) or `html`. - It's generating PDF by default. However, you can specify output_format=html to generate only HTML(It will return in the JSON response as download_url field as a URL).  (optional)
    filename = 'invoice_89326.pdf' # str | - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with `.pdf`  (optional)
    image_resample_res = '150' # str | - We embed the original images by default, meaning large PDF file sizes. Specifying the option 'image_resample_res' helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  (optional)
    is_cmyk = '0' # str | - Use CMYK color profile, 1=true, 0=false. Default to '0'  (optional)
    cloud_storage = 1 # int | - Upload the generated PDFs/images to our storage CDN, default to `1`. If you have configured `Post Action` to upload the PDFs/Images to your own S3, please set it to `0`.  (optional)
    pdf_standard = 'pdf_standard_example' # str | Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  (optional)
    postaction_s3_filekey = 'postaction_s3_filekey_example' # str | - This is to specify the file name for `Post Action(S3 Storage)`. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  (optional)
    postaction_s3_bucket = 'postaction_s3_bucket_example' # str | - This is to overwrite the AWS Bucket for `Post Action(S3 Storage)`.  (optional)
    meta = 'inv-iwj343jospig' # str | - Specify an external reference ID for your own reference. It appears in the `list-objects` API.  (optional)
    var_async = '0' # str | - Either `1` or `0`(Default).  `0` is synchronous call(default), `1` is asynchronous call - To generate PDF asynchronously, set the value to `1` and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If `async` is set to `1`, then `webhook_url` is mandatory  (optional)
    webhook_url = 'https://yourwebserver.com' # str | - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If `async` is set to `1`, then you have to specify the `webhook_url`.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://`[yourwebserver.com]`?&primary_url=`[primary_url]`&transaction_ref=`[transaction_ref]`&status=`[status]`&message=`[message]`  - `[yourwebserver.com]`: The web services to handle the callback, which is the `webhook_url` - `[primary_url]`: The URL to the PDF document - `[transaction_ref]`: The transaction reference number - `[status]` : Status of the transaction, either `success` or `error` - `[message]` : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&primary_url=https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&transaction_ref=b692183d-46d7-3213-891a-460a5814ad3f&status=success  (optional)

    try:
        # Create a PDF
        api_response = api_instance.create_pdf(template_id, body, export_type=export_type, expiration=expiration, output_html=output_html, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)
        print("The response of APIIntegrationApi->create_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->create_pdf: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**| Your template id, it can be obtained in the web console | 
 **body** | **object**|  | 
 **export_type** | **str**| - Either &#x60;file&#x60; or &#x60;json&#x60;(Default).   - The option &#x60;json&#x60; returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter &#x60;expiration&#x60;   - The option &#x60;file&#x60; returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  | [optional] 
 **expiration** | **int**| - Expiration of the generated PDF in minutes(default to &#x60;0&#x60;, store permanently)   - Use &#x60;0&#x60; to store on cdn permanently   - Or use the range between &#x60;1&#x60; minute and &#x60;10080&#x60; minutes(7 days) to specify the expiration of the generated PDF  | [optional] 
 **output_html** | **str**| - Either &#x60;1&#x60; or &#x60;0&#x60;(Default). - To enable output of html content, set the value to &#x60;1&#x60; and it will return in the JSON response as html_url field (as a URL)  | [optional] 
 **output_format** | **str**| - Either &#x60;pdf&#x60;(Default) or &#x60;html&#x60;. - It&#39;s generating PDF by default. However, you can specify output_format&#x3D;html to generate only HTML(It will return in the JSON response as download_url field as a URL).  | [optional] 
 **filename** | **str**| - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with &#x60;.pdf&#x60;  | [optional] 
 **image_resample_res** | **str**| - We embed the original images by default, meaning large PDF file sizes. Specifying the option &#39;image_resample_res&#39; helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  | [optional] 
 **is_cmyk** | **str**| - Use CMYK color profile, 1&#x3D;true, 0&#x3D;false. Default to &#39;0&#39;  | [optional] 
 **cloud_storage** | **int**| - Upload the generated PDFs/images to our storage CDN, default to &#x60;1&#x60;. If you have configured &#x60;Post Action&#x60; to upload the PDFs/Images to your own S3, please set it to &#x60;0&#x60;.  | [optional] 
 **pdf_standard** | **str**| Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  | [optional] 
 **postaction_s3_filekey** | **str**| - This is to specify the file name for &#x60;Post Action(S3 Storage)&#x60;. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  | [optional] 
 **postaction_s3_bucket** | **str**| - This is to overwrite the AWS Bucket for &#x60;Post Action(S3 Storage)&#x60;.  | [optional] 
 **meta** | **str**| - Specify an external reference ID for your own reference. It appears in the &#x60;list-objects&#x60; API.  | [optional] 
 **var_async** | **str**| - Either &#x60;1&#x60; or &#x60;0&#x60;(Default).  &#x60;0&#x60; is synchronous call(default), &#x60;1&#x60; is asynchronous call - To generate PDF asynchronously, set the value to &#x60;1&#x60; and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then &#x60;webhook_url&#x60; is mandatory  | [optional] 
 **webhook_url** | **str**| - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then you have to specify the &#x60;webhook_url&#x60;.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://&#x60;[yourwebserver.com]&#x60;?&amp;primary_url&#x3D;&#x60;[primary_url]&#x60;&amp;transaction_ref&#x3D;&#x60;[transaction_ref]&#x60;&amp;status&#x3D;&#x60;[status]&#x60;&amp;message&#x3D;&#x60;[message]&#x60;  - &#x60;[yourwebserver.com]&#x60;: The web services to handle the callback, which is the &#x60;webhook_url&#x60; - &#x60;[primary_url]&#x60;: The URL to the PDF document - &#x60;[transaction_ref]&#x60;: The transaction reference number - &#x60;[status]&#x60; : Status of the transaction, either &#x60;success&#x60; or &#x60;error&#x60; - &#x60;[message]&#x60; : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&amp;primary_url&#x3D;https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&amp;transaction_ref&#x3D;b692183d-46d7-3213-891a-460a5814ad3f&amp;status&#x3D;success  | [optional] 

### Return type

[**ResponseSuccessPDFFile**](ResponseSuccessPDFFile.md)

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

# **create_pdf_from_html**
> ResponseSuccessPDFFile create_pdf_from_html(create_pdf_from_html_request, export_type=export_type, expiration=expiration, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)

Create a PDF from HTML

- This endpoint creates a PDF file from HTML with JSON data 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.create_pdf_from_html_request import CreatePdfFromHtmlRequest
from APITemplateio.models.response_success_pdf_file import ResponseSuccessPDFFile
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    create_pdf_from_html_request = APITemplateio.CreatePdfFromHtmlRequest() # CreatePdfFromHtmlRequest | 
    export_type = 'json' # str | - Either `file` or `json`(Default).   - The option `json` returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter `expiration`   - The option `file` returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  (optional)
    expiration = 5 # int | - Expiration of the generated PDF in minutes(default to `0`, store permanently)   - Use `0` to store on cdn permanently   - Or use the range between `1` minute and `10080` minutes(7 days) to specify the expiration of the generated PDF  (optional)
    output_format = 'pdf' # str | - Either `pdf`(Default) or `html`. - It's generating PDF by default. However, you can specify output_format=html to generate only HTML(It will return in the JSON response as download_url field as a URL).  (optional)
    filename = 'invoice_89326.pdf' # str | - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with `.pdf`  (optional)
    image_resample_res = '150' # str | - We embed the original images by default, meaning large PDF file sizes. Specifying the option 'image_resample_res' helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  (optional)
    is_cmyk = '0' # str | - Use CMYK color profile, 1=true, 0=false. Default to '0'  (optional)
    cloud_storage = 1 # int | - Upload the generated PDFs/images to our storage CDN, default to `1`. If you have configured `Post Action` to upload the PDFs/Images to your own S3, please set it to `0`.  (optional)
    pdf_standard = 'pdf_standard_example' # str | Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  (optional)
    postaction_s3_filekey = 'postaction_s3_filekey_example' # str | - This is to specify the file name for `Post Action(S3 Storage)`. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  (optional)
    postaction_s3_bucket = 'postaction_s3_bucket_example' # str | - This is to overwrite the AWS Bucket for `Post Action(S3 Storage)`.  (optional)
    meta = 'inv-iwj343jospig' # str | - Specify an external reference ID for your own reference. It appears in the `list-objects` API.  (optional)
    var_async = '0' # str | - Either `1` or `0`(Default).  `0` is synchronous call(default), `1` is asynchronous call - To generate PDF asynchronously, set the value to `1` and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If `async` is set to `1`, then `webhook_url` is mandatory  (optional)
    webhook_url = 'https://yourwebserver.com' # str | - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If `async` is set to `1`, then you have to specify the `webhook_url`.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://`[yourwebserver.com]`?&primary_url=`[primary_url]`&transaction_ref=`[transaction_ref]`&status=`[status]`&message=`[message]`  - `[yourwebserver.com]`: The web services to handle the callback, which is the `webhook_url` - `[primary_url]`: The URL to the PDF document - `[transaction_ref]`: The transaction reference number - `[status]` : Status of the transaction, either `success` or `error` - `[message]` : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&primary_url=https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&transaction_ref=b692183d-46d7-3213-891a-460a5814ad3f&status=success  (optional)

    try:
        # Create a PDF from HTML
        api_response = api_instance.create_pdf_from_html(create_pdf_from_html_request, export_type=export_type, expiration=expiration, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)
        print("The response of APIIntegrationApi->create_pdf_from_html:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->create_pdf_from_html: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pdf_from_html_request** | [**CreatePdfFromHtmlRequest**](CreatePdfFromHtmlRequest.md)|  | 
 **export_type** | **str**| - Either &#x60;file&#x60; or &#x60;json&#x60;(Default).   - The option &#x60;json&#x60; returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter &#x60;expiration&#x60;   - The option &#x60;file&#x60; returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  | [optional] 
 **expiration** | **int**| - Expiration of the generated PDF in minutes(default to &#x60;0&#x60;, store permanently)   - Use &#x60;0&#x60; to store on cdn permanently   - Or use the range between &#x60;1&#x60; minute and &#x60;10080&#x60; minutes(7 days) to specify the expiration of the generated PDF  | [optional] 
 **output_format** | **str**| - Either &#x60;pdf&#x60;(Default) or &#x60;html&#x60;. - It&#39;s generating PDF by default. However, you can specify output_format&#x3D;html to generate only HTML(It will return in the JSON response as download_url field as a URL).  | [optional] 
 **filename** | **str**| - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with &#x60;.pdf&#x60;  | [optional] 
 **image_resample_res** | **str**| - We embed the original images by default, meaning large PDF file sizes. Specifying the option &#39;image_resample_res&#39; helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  | [optional] 
 **is_cmyk** | **str**| - Use CMYK color profile, 1&#x3D;true, 0&#x3D;false. Default to &#39;0&#39;  | [optional] 
 **cloud_storage** | **int**| - Upload the generated PDFs/images to our storage CDN, default to &#x60;1&#x60;. If you have configured &#x60;Post Action&#x60; to upload the PDFs/Images to your own S3, please set it to &#x60;0&#x60;.  | [optional] 
 **pdf_standard** | **str**| Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  | [optional] 
 **postaction_s3_filekey** | **str**| - This is to specify the file name for &#x60;Post Action(S3 Storage)&#x60;. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  | [optional] 
 **postaction_s3_bucket** | **str**| - This is to overwrite the AWS Bucket for &#x60;Post Action(S3 Storage)&#x60;.  | [optional] 
 **meta** | **str**| - Specify an external reference ID for your own reference. It appears in the &#x60;list-objects&#x60; API.  | [optional] 
 **var_async** | **str**| - Either &#x60;1&#x60; or &#x60;0&#x60;(Default).  &#x60;0&#x60; is synchronous call(default), &#x60;1&#x60; is asynchronous call - To generate PDF asynchronously, set the value to &#x60;1&#x60; and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then &#x60;webhook_url&#x60; is mandatory  | [optional] 
 **webhook_url** | **str**| - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then you have to specify the &#x60;webhook_url&#x60;.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://&#x60;[yourwebserver.com]&#x60;?&amp;primary_url&#x3D;&#x60;[primary_url]&#x60;&amp;transaction_ref&#x3D;&#x60;[transaction_ref]&#x60;&amp;status&#x3D;&#x60;[status]&#x60;&amp;message&#x3D;&#x60;[message]&#x60;  - &#x60;[yourwebserver.com]&#x60;: The web services to handle the callback, which is the &#x60;webhook_url&#x60; - &#x60;[primary_url]&#x60;: The URL to the PDF document - &#x60;[transaction_ref]&#x60;: The transaction reference number - &#x60;[status]&#x60; : Status of the transaction, either &#x60;success&#x60; or &#x60;error&#x60; - &#x60;[message]&#x60; : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&amp;primary_url&#x3D;https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&amp;transaction_ref&#x3D;b692183d-46d7-3213-891a-460a5814ad3f&amp;status&#x3D;success  | [optional] 

### Return type

[**ResponseSuccessPDFFile**](ResponseSuccessPDFFile.md)

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

# **create_pdf_from_url**
> ResponseSuccessPDFFile create_pdf_from_url(create_pdf_from_url_request, export_type=export_type, expiration=expiration, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)

Create a PDF from URL

- This endpoint creates a PDF file from a URL 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.create_pdf_from_url_request import CreatePdfFromUrlRequest
from APITemplateio.models.response_success_pdf_file import ResponseSuccessPDFFile
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    create_pdf_from_url_request = APITemplateio.CreatePdfFromUrlRequest() # CreatePdfFromUrlRequest | 
    export_type = 'json' # str | - Either `file` or `json`(Default).   - The option `json` returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter `expiration`   - The option `file` returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  (optional)
    expiration = 5 # int | - Expiration of the generated PDF in minutes(default to `0`, store permanently)   - Use `0` to store on cdn permanently   - Or use the range between `1` minute and `10080` minutes(7 days) to specify the expiration of the generated PDF  (optional)
    output_format = 'pdf' # str | - Either `pdf`(Default) or `html`. - It's generating PDF by default. However, you can specify output_format=html to generate only HTML(It will return in the JSON response as download_url field as a URL).  (optional)
    filename = 'invoice_89326.pdf' # str | - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with `.pdf`  (optional)
    image_resample_res = '150' # str | - We embed the original images by default, meaning large PDF file sizes. Specifying the option 'image_resample_res' helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  (optional)
    is_cmyk = '0' # str | - Use CMYK color profile, 1=true, 0=false. Default to '0'  (optional)
    cloud_storage = 1 # int | - Upload the generated PDFs/images to our storage CDN, default to `1`. If you have configured `Post Action` to upload the PDFs/Images to your own S3, please set it to `0`.  (optional)
    pdf_standard = 'pdf_standard_example' # str | Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  (optional)
    postaction_s3_filekey = 'postaction_s3_filekey_example' # str | - This is to specify the file name for `Post Action(S3 Storage)`. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  (optional)
    postaction_s3_bucket = 'postaction_s3_bucket_example' # str | - This is to overwrite the AWS Bucket for `Post Action(S3 Storage)`.  (optional)
    meta = 'inv-iwj343jospig' # str | - Specify an external reference ID for your own reference. It appears in the `list-objects` API.  (optional)
    var_async = '0' # str | - Either `1` or `0`(Default).  `0` is synchronous call(default), `1` is asynchronous call - To generate PDF asynchronously, set the value to `1` and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If `async` is set to `1`, then `webhook_url` is mandatory  (optional)
    webhook_url = 'https://yourwebserver.com' # str | - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If `async` is set to `1`, then you have to specify the `webhook_url`.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://`[yourwebserver.com]`?&primary_url=`[primary_url]`&transaction_ref=`[transaction_ref]`&status=`[status]`&message=`[message]`  - `[yourwebserver.com]`: The web services to handle the callback, which is the `webhook_url` - `[primary_url]`: The URL to the PDF document - `[transaction_ref]`: The transaction reference number - `[status]` : Status of the transaction, either `success` or `error` - `[message]` : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&primary_url=https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&transaction_ref=b692183d-46d7-3213-891a-460a5814ad3f&status=success  (optional)

    try:
        # Create a PDF from URL
        api_response = api_instance.create_pdf_from_url(create_pdf_from_url_request, export_type=export_type, expiration=expiration, output_format=output_format, filename=filename, image_resample_res=image_resample_res, is_cmyk=is_cmyk, cloud_storage=cloud_storage, pdf_standard=pdf_standard, postaction_s3_filekey=postaction_s3_filekey, postaction_s3_bucket=postaction_s3_bucket, meta=meta, var_async=var_async, webhook_url=webhook_url)
        print("The response of APIIntegrationApi->create_pdf_from_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->create_pdf_from_url: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_pdf_from_url_request** | [**CreatePdfFromUrlRequest**](CreatePdfFromUrlRequest.md)|  | 
 **export_type** | **str**| - Either &#x60;file&#x60; or &#x60;json&#x60;(Default).   - The option &#x60;json&#x60; returns a JSON object, and the output PDF is stored on a CDN. Use this with the parameter &#x60;expiration&#x60;   - The option &#x60;file&#x60; returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment.  | [optional] 
 **expiration** | **int**| - Expiration of the generated PDF in minutes(default to &#x60;0&#x60;, store permanently)   - Use &#x60;0&#x60; to store on cdn permanently   - Or use the range between &#x60;1&#x60; minute and &#x60;10080&#x60; minutes(7 days) to specify the expiration of the generated PDF  | [optional] 
 **output_format** | **str**| - Either &#x60;pdf&#x60;(Default) or &#x60;html&#x60;. - It&#39;s generating PDF by default. However, you can specify output_format&#x3D;html to generate only HTML(It will return in the JSON response as download_url field as a URL).  | [optional] 
 **filename** | **str**| - Default to UUID (e.g 0c93bd9e-9ebb-4634-a70f-de9131848416.pdf). Use this to specify custom file name, it should end with &#x60;.pdf&#x60;  | [optional] 
 **image_resample_res** | **str**| - We embed the original images by default, meaning large PDF file sizes. Specifying the option &#39;image_resample_res&#39; helps reduce the PDF file size by downsampling the images of the current PDF to a resolution(in DPI). Common values are 72, 96, 150, 300 and 600.  | [optional] 
 **is_cmyk** | **str**| - Use CMYK color profile, 1&#x3D;true, 0&#x3D;false. Default to &#39;0&#39;  | [optional] 
 **cloud_storage** | **int**| - Upload the generated PDFs/images to our storage CDN, default to &#x60;1&#x60;. If you have configured &#x60;Post Action&#x60; to upload the PDFs/Images to your own S3, please set it to &#x60;0&#x60;.  | [optional] 
 **pdf_standard** | **str**| Default to PDF1.4. Options are PDFA1B, PDFA2 and PDFA3 (This is an experimental feature)  | [optional] 
 **postaction_s3_filekey** | **str**| - This is to specify the file name for &#x60;Post Action(S3 Storage)&#x60;. - Please do not specify the file extension - Please make sure the file name is unique - You might use slash (/) as the folder delimiter  | [optional] 
 **postaction_s3_bucket** | **str**| - This is to overwrite the AWS Bucket for &#x60;Post Action(S3 Storage)&#x60;.  | [optional] 
 **meta** | **str**| - Specify an external reference ID for your own reference. It appears in the &#x60;list-objects&#x60; API.  | [optional] 
 **var_async** | **str**| - Either &#x60;1&#x60; or &#x60;0&#x60;(Default).  &#x60;0&#x60; is synchronous call(default), &#x60;1&#x60; is asynchronous call - To generate PDF asynchronously, set the value to &#x60;1&#x60; and the API call returns immediately. Once the PDF document is generated, we will make a HTTP/HTTPS GET to your URL(webhook_url) and will retry for 3 times before giving up. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then &#x60;webhook_url&#x60; is mandatory  | [optional] 
 **webhook_url** | **str**| - It is the URL of your webhook URL, it starts with http:// or https:// and has to be urlencoded. - If &#x60;async&#x60; is set to &#x60;1&#x60;, then you have to specify the &#x60;webhook_url&#x60;.   #### Format of Webhook callback  Once the PDF is generated, we will initiate a HTTP/HTTPS GET call to the following URL:  https://&#x60;[yourwebserver.com]&#x60;?&amp;primary_url&#x3D;&#x60;[primary_url]&#x60;&amp;transaction_ref&#x3D;&#x60;[transaction_ref]&#x60;&amp;status&#x3D;&#x60;[status]&#x60;&amp;message&#x3D;&#x60;[message]&#x60;  - &#x60;[yourwebserver.com]&#x60;: The web services to handle the callback, which is the &#x60;webhook_url&#x60; - &#x60;[primary_url]&#x60;: The URL to the PDF document - &#x60;[transaction_ref]&#x60;: The transaction reference number - &#x60;[status]&#x60; : Status of the transaction, either &#x60;success&#x60; or &#x60;error&#x60; - &#x60;[message]&#x60; : Status message  ***The following is a sample webhook call back to your server***  https://yourwebserver.com?&amp;primary_url&#x3D;https%3A%2F%2Fpub-cdn.apitemplate.io%2F2021%2F06%2Fb692183d-46d7-3213-891a-460a5814ad3f.pdf&amp;transaction_ref&#x3D;b692183d-46d7-3213-891a-460a5814ad3f&amp;status&#x3D;success  | [optional] 

### Return type

[**ResponseSuccessPDFFile**](ResponseSuccessPDFFile.md)

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

# **delete_object**
> ResponseSuccessDeleteObject delete_object(transaction_ref)

Delete an Object

Delete a PDF or an image from CDN and mark the transaction as deleted 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_delete_object import ResponseSuccessDeleteObject
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    transaction_ref = '1618d386-2343-3d234-b9c7-99c82bb9f104' # str | Object transaction reference

    try:
        # Delete an Object
        api_response = api_instance.delete_object(transaction_ref)
        print("The response of APIIntegrationApi->delete_object:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->delete_object: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transaction_ref** | **str**| Object transaction reference | 

### Return type

[**ResponseSuccessDeleteObject**](ResponseSuccessDeleteObject.md)

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

# **list_objects**
> ResponseSuccessListObjects list_objects(limit=limit, offset=offset, template_id=template_id, transaction_type=transaction_type)

List Generated Objects

Retrieves all the generated PDFs and images 

### Example

* Api Key Authentication (ApiKeyAuth):
```python
import time
import os
import APITemplateio
from APITemplateio.models.response_success_list_objects import ResponseSuccessListObjects
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
    api_instance = APITemplateio.APIIntegrationApi(api_client)
    limit = '300' # str | Retrieve only the number of records specified. Default to 300 (optional)
    offset = '0' # str | Offset is used to skip the number of records from the results. Default to 0 (optional)
    template_id = '00377b2b1e0ee394' # str | Filtered by template id (optional)
    transaction_type = 'MERGE' # str | Filtered by transaction type, options are `PDF`, `JPEG` or `MERGE` (optional)

    try:
        # List Generated Objects
        api_response = api_instance.list_objects(limit=limit, offset=offset, template_id=template_id, transaction_type=transaction_type)
        print("The response of APIIntegrationApi->list_objects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling APIIntegrationApi->list_objects: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| Retrieve only the number of records specified. Default to 300 | [optional] 
 **offset** | **str**| Offset is used to skip the number of records from the results. Default to 0 | [optional] 
 **template_id** | **str**| Filtered by template id | [optional] 
 **transaction_type** | **str**| Filtered by transaction type, options are &#x60;PDF&#x60;, &#x60;JPEG&#x60; or &#x60;MERGE&#x60; | [optional] 

### Return type

[**ResponseSuccessListObjects**](ResponseSuccessListObjects.md)

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

