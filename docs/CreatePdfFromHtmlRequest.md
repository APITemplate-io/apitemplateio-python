# CreatePdfFromHtmlRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **str** | The HTML body content for the PDF. This property supports HTML markup and can include Jinja2 syntax (e.g {{name}}). The value of {{name}} will be replaced with the actual value provided in the data object.  | [optional] 
**css** | **str** | The CSS styles to be applied to the PDF. This property should contain valid CSS markup and should also include the style tag.  | [optional] 
**data** | **object** | The data object containing values for dynamic content in the HTML body. This object should include properties with corresponding values.  | [optional] 
**settings** | [**PDFGenerationSettingsObject**](PDFGenerationSettingsObject.md) |  | [optional] 

## Example

```python
from APITemplateio.models.create_pdf_from_html_request import CreatePdfFromHtmlRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePdfFromHtmlRequest from a JSON string
create_pdf_from_html_request_instance = CreatePdfFromHtmlRequest.from_json(json)
# print the JSON string representation of the object
print CreatePdfFromHtmlRequest.to_json()

# convert the object into a dict
create_pdf_from_html_request_dict = create_pdf_from_html_request_instance.to_dict()
# create an instance of CreatePdfFromHtmlRequest from a dict
create_pdf_from_html_request_form_dict = create_pdf_from_html_request.from_dict(create_pdf_from_html_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


