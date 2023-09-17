# ResponseSuccessImageFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**download_url** | **str** | Download URL | [optional] 
**download_url_png** | **str** | Download URL PNG | [optional] 
**template_id** | **str** | Template ID | [optional] 
**transaction_ref** | **str** | Transaction reference | [optional] 
**post_actions** | [**List[ResponseSuccessPDFFilePostActionsInner]**](ResponseSuccessPDFFilePostActionsInner.md) |  | [optional] 

## Example

```python
from APITemplateio.models.response_success_image_file import ResponseSuccessImageFile

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessImageFile from a JSON string
response_success_image_file_instance = ResponseSuccessImageFile.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessImageFile.to_json()

# convert the object into a dict
response_success_image_file_dict = response_success_image_file_instance.to_dict()
# create an instance of ResponseSuccessImageFile from a dict
response_success_image_file_form_dict = response_success_image_file.from_dict(response_success_image_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


