# ResponseSuccessQueryImageTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Status | [optional] 
**width** | **int** | Width | [optional] 
**height** | **int** | Height | [optional] 
**layers** | **List[object]** | Array of layers | [optional] 

## Example

```python
from APITemplateio.models.response_success_query_image_template import ResponseSuccessQueryImageTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of ResponseSuccessQueryImageTemplate from a JSON string
response_success_query_image_template_instance = ResponseSuccessQueryImageTemplate.from_json(json)
# print the JSON string representation of the object
print ResponseSuccessQueryImageTemplate.to_json()

# convert the object into a dict
response_success_query_image_template_dict = response_success_query_image_template_instance.to_dict()
# create an instance of ResponseSuccessQueryImageTemplate from a dict
response_success_query_image_template_form_dict = response_success_query_image_template.from_dict(response_success_query_image_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


