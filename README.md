# APITemplateio
# Introduction


Welcome to the [APITemplate.io](https://apitemplate.io) API v2! This is the official APITemplate.io library for Python. For more details, see our [REST API Reference](https://apitemplate.io/apiv2/).

APITemplate.io provides PDF generation services including [Template-based PDF generation](https://apitemplate.io/pdf-generation-api/), [HTML to PDF](https://apitemplate.io/html-to-pdf-api/), and [URL to PDF conversions](https://apitemplate.io/create-pdf-from-url/), as well as an [image generation API](https://apitemplate.io/image-generation-api/).

This page contains the documentation on how to use APITemplate.io through API calls. With the APITemplate.io API, you can create PDF documents and images, as well as manage your templates.

Our API is built on RESTful HTTP, so you can utilize any HTTP/REST library of your choice in your preferred programming language to interact with APITemplate.io's API.

**Steps to produce PDFs/Images**
1. Design your template(s) using our intuitive drag-and-drop template editor or the HTML editor and save it.
2. Integrate your workflow, either with platforms like Zapier, Make.com/Integromat, Bubble.io, or any programming languages that support REST API, to send us the JSON data along with the template ID/URL/or HTML content.
3. Our REST API will then return a download URL for the images (in PNG and JPEG formats) or PDFs.

# Authentication
Upon signing up for an account, an API key will be generated for you. If needed, you can reset this API key via the web console (under the \"API Integration\" section).

To integrate with our services, you need to authenticate with the APITemplate.io API. Provide your secret key in the request header using the X-API-KEY field.


# Content Type and CORS

**Request Content-Type**
The Content-Type for POST and GET requests is set to application/json.

**Cross-Origin Resource Sharing**
This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with  [W3C spec](https://www.w3.org/TR/cors/).
And that allows cross-domain communication from the browser.
All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.



# Regional API endpoint(s)
A regional API endpoint is intended for customers in the same region. The data for the request and generated PDFs/images are processed and stored within the region.

The regions are:

| Region               | Endpoint                            | Max Timeout (Seconds) | Max Payload Size(MB)** |
|----------------------|-------------------------------------|-----------------------|-------------------------|
| Default (Singapore)  | https://rest.apitemplate.io         | 100                   | 1                       |
| Europe (Frankfurt)   | https://rest-de.apitemplate.io      | 100                   | 1                       |
| US East (N. Virginia)| https://rest-us.apitemplate.io      | 100                   | 1                       |
| Australia (Sydney)   | https://rest-au.apitemplate.io      | 30                    | 6                       |


Alternative Regions:
| Region               | Endpoint                            | Max Timeout (Seconds) | Max Payload Size(MB)** |
|----------------------|-------------------------------------|-----------------------|-------------------------|
| Default (Singapore)  | https://rest-alt.apitemplate.io     | 30                    | 6                       |
| Europe (Frankfurt)   | https://rest-alt-de.apitemplate.io  | 30                    | 6                       |
| US East (N. Virginia)| https://rest-alt-us.apitemplate.io  | 30                    | 6                       |

** Note:
- Payload size applies to request and response
- If \"export_type\" is set to `json` which output file that on AWS S3 doesn't have the limitation
- If the \"export_type\" is set to `file` which returns binary data of the generated PDF, the file size of the generated PDF is limited to either 6MB or 1MB based on the region



Other regions are available on request, contact us at hello@apitemplate.io for more information

# Rate limiting
Our API endpoints use IP-based rate limiting to ensure fair usage and prevent abuse. Users are allowed to make up to **100 requests per 10 seconds**. This rate limit is designed to accommodate a reasonable volume of requests while maintaining optimal performance for all users.

However, if you exceed this limit and make additional requests, you will receive a response with HTTP code 429. This status code indicates that you have reached the rate limit and need to wait before making further requests.


This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: Version 2.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://apitemplate.io](https://apitemplate.io)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import APITemplateio
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install----user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import APITemplateio
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import APITemplateio
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
    except ApiException as e:
        print("Exception when calling APIIntegrationApi->create_image: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://rest.apitemplate.io*

Class | Method | HTTP request | Description
------------|---------------|---------------|---------------
*APIIntegrationApi* | [**create_image**](docs/APIIntegrationApi.md#create_image) | **POST** /v2/create-image | Create an Image
*APIIntegrationApi* | [**create_pdf**](docs/APIIntegrationApi.md#create_pdf) | **POST** /v2/create-pdf | Create a PDF
*APIIntegrationApi* | [**create_pdf_from_html**](docs/APIIntegrationApi.md#create_pdf_from_html) | **POST** /v2/create-pdf-from-html | Create a PDF from HTML
*APIIntegrationApi* | [**create_pdf_from_url**](docs/APIIntegrationApi.md#create_pdf_from_url) | **POST** /v2/create-pdf-from-url | Create a PDF from URL
*APIIntegrationApi* | [**delete_object**](docs/APIIntegrationApi.md#delete_object) | **GET** /v2/delete-object | Delete an Object
*APIIntegrationApi* | [**list_objects**](docs/APIIntegrationApi.md#list_objects) | **GET** /v2/list-objects | List Generated Objects
*PDFManipulationAPIApi* | [**merge_pdfs**](docs/PDFManipulationAPIApi.md#merge_pdfs) | **POST** /v2/merge-pdfs | Join/Merge multiple PDFs
*TemplateManagementApi* | [**get_template**](docs/TemplateManagementApi.md#get_template) | **GET** /v2/get-template | Get PDF template
*TemplateManagementApi* | [**list_templates**](docs/TemplateManagementApi.md#list_templates) | **GET** /v2/list-templates | List Templates
*TemplateManagementApi* | [**update_template**](docs/TemplateManagementApi.md#update_template) | **POST** /v2/update-template | Update PDF Template


## Documentation For Models

 - [CreatePdfFromHtmlRequest](docs/CreatePdfFromHtmlRequest.md)
 - [CreatePdfFromUrlRequest](docs/CreatePdfFromUrlRequest.md)
 - [Error](docs/Error.md)
 - [MergePdfsRequest](docs/MergePdfsRequest.md)
 - [PDFGenerationSettingsObject](docs/PDFGenerationSettingsObject.md)
 - [ResponseSuccess](docs/ResponseSuccess.md)
 - [ResponseSuccessDeleteObject](docs/ResponseSuccessDeleteObject.md)
 - [ResponseSuccessImageFile](docs/ResponseSuccessImageFile.md)
 - [ResponseSuccessListObjects](docs/ResponseSuccessListObjects.md)
 - [ResponseSuccessListTemplates](docs/ResponseSuccessListTemplates.md)
 - [ResponseSuccessListTemplatesTemplatesInner](docs/ResponseSuccessListTemplatesTemplatesInner.md)
 - [ResponseSuccessPDFFile](docs/ResponseSuccessPDFFile.md)
 - [ResponseSuccessPDFFilePostActionsInner](docs/ResponseSuccessPDFFilePostActionsInner.md)
 - [ResponseSuccessQueryImageTemplate](docs/ResponseSuccessQueryImageTemplate.md)
 - [ResponseSuccessSingleFile](docs/ResponseSuccessSingleFile.md)
 - [ResponseSuccessTemplate](docs/ResponseSuccessTemplate.md)
 - [UpdateTemplateRequest](docs/UpdateTemplateRequest.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-KEY
- **Location**: HTTP header


## Author

hello@apitemplate.io


