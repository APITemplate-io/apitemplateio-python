# ResponseSuccessTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**template_id** | **str** | Template ID | [optional] 
**body** | **str** | HTML body of the template | [optional] 
**css** | **str** | CSS of the template | [optional] 
**settings** | **str** | Print settings of the template | [optional] 

## Example

```python
from APITemplateio.models.response_success_template import ResponseSuccessTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessTemplate from a JSON string
response_success_template_instance = ResponseSuccessTemplate.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessTemplate.to_json()

# convert the object into a dict
response_success_template_dict = response_success_template_instance.to_dict()
# create an instance of ResponseSuccessTemplate from a dict
response_success_template_form_dict = response_success_template.from_dict(response_success_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


