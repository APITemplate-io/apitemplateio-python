# ResponseSuccessSingleFile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**primary_url** | **str** | Generated PDF document | [optional] 
**total_pages** | **int** | Page count | [optional] 
**transaction_ref** | **str** | Transaction reference | [optional] 

## Example

```python
from APITemplateio.models.response_success_single_file import ResponseSuccessSingleFile

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessSingleFile from a JSON string
response_success_single_file_instance = ResponseSuccessSingleFile.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessSingleFile.to_json()

# convert the object into a dict
response_success_single_file_dict = response_success_single_file_instance.to_dict()
# create an instance of ResponseSuccessSingleFile from a dict
response_success_single_file_form_dict = response_success_single_file.from_dict(response_success_single_file_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


