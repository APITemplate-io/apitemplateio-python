# ResponseSuccessPDFFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**download_url** | **str** | Download URL | [optional] 
**template_id** | **str** | Template ID | [optional] 
**total_pages** | **int** | Page count | [optional] 
**transaction_ref** | **str** | Transaction reference | [optional] 
**post_actions** | [**List[ResponseSuccessPDFFilePostActionsInner]**](ResponseSuccessPDFFilePostActionsInner.md) |  | [optional] 

## Example

```python
from APITemplateio.models.response_success_pdf_file import ResponseSuccessPDFFile

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessPDFFile from a JSON string
response_success_pdf_file_instance = ResponseSuccessPDFFile.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessPDFFile.to_json()

# convert the object into a dict
response_success_pdf_file_dict = response_success_pdf_file_instance.to_dict()
# create an instance of ResponseSuccessPDFFile from a dict
response_success_pdf_file_form_dict = response_success_pdf_file.from_dict(response_success_pdf_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


