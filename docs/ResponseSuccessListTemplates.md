# ResponseSuccessListTemplates


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**templates** | [**List[ResponseSuccessListTemplatesTemplatesInner]**](ResponseSuccessListTemplatesTemplatesInner.md) |  | [optional] 

## Example

```python
from APITemplateio.models.response_success_list_templates import ResponseSuccessListTemplates

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessListTemplates from a JSON string
response_success_list_templates_instance = ResponseSuccessListTemplates.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessListTemplates.to_json()

# convert the object into a dict
response_success_list_templates_dict = response_success_list_templates_instance.to_dict()
# create an instance of ResponseSuccessListTemplates from a dict
response_success_list_templates_form_dict = response_success_list_templates.from_dict(response_success_list_templates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


