# CreatePdfFromUrlRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The URL  | [optional] 
**settings** | [**PDFGenerationSettingsObject**](PDFGenerationSettingsObject.md) |  | [optional] 

## Example

```python
from APITemplateio.models.create_pdf_from_url_request import CreatePdfFromUrlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePdfFromUrlRequest from a JSON string
create_pdf_from_url_request_instance = CreatePdfFromUrlRequest.from_json(json)
# print the JSON string representation of the object
print CreatePdfFromUrlRequest.to_json()

# convert the object into a dict
create_pdf_from_url_request_dict = create_pdf_from_url_request_instance.to_dict()
# create an instance of CreatePdfFromUrlRequest from a dict
create_pdf_from_url_request_form_dict = create_pdf_from_url_request.from_dict(create_pdf_from_url_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


