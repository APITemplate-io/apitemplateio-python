# ResponseSuccessListObjects


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**objects** | **List[object]** |  | [optional] 

## Example

```python
from APITemplateio.models.response_success_list_objects import ResponseSuccessListObjects

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessListObjects from a JSON string
response_success_list_objects_instance = ResponseSuccessListObjects.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessListObjects.to_json()

# convert the object into a dict
response_success_list_objects_dict = response_success_list_objects_instance.to_dict()
# create an instance of ResponseSuccessListObjects from a dict
response_success_list_objects_form_dict = response_success_list_objects.from_dict(response_success_list_objects_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


