# ResponseSuccess


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 

## Example

```python
from APITemplateio.models.response_success import ResponseSuccess

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccess from a JSON string
response_success_instance = ResponseSuccess.from_json(json)
# print the JSON string representation of the object
print ResponseSuccess.to_json()

# convert the object into a dict
response_success_dict = response_success_instance.to_dict()
# create an instance of ResponseSuccess from a dict
response_success_form_dict = response_success.from_dict(response_success_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


