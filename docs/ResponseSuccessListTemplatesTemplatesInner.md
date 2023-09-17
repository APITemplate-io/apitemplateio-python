# ResponseSuccessListTemplatesTemplatesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 
**group_name** | **str** |  | [optional] 

## Example

```python
from APITemplateio.models.response_success_list_templates_templates_inner import ResponseSuccessListTemplatesTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessListTemplatesTemplatesInner from a JSON string
response_success_list_templates_templates_inner_instance = ResponseSuccessListTemplatesTemplatesInner.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessListTemplatesTemplatesInner.to_json()

# convert the object into a dict
response_success_list_templates_templates_inner_dict = response_success_list_templates_templates_inner_instance.to_dict()
# create an instance of ResponseSuccessListTemplatesTemplatesInner from a dict
response_success_list_templates_templates_inner_form_dict = response_success_list_templates_templates_inner.from_dict(response_success_list_templates_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


