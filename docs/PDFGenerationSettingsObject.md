# PDFGenerationSettingsObject

The settings object contains various properties to configure the PDF generation. 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**paper_size** | **str** | Specifies the paper size for the PDF. The available options are Letter, Legal, Tabloid, Ledger, A0, A1, A2, A3, A4, A5,A6 or custom. custom dimensions specified as \&quot;custom_width\&quot; and \&quot;custom_height\&quot;.  | [optional] 
**custom_width** | **str** | Custom width for the custom paper size. Valid units are mm, px and cm. eg: 30mm  | [optional] 
**custom_height** | **str** | Custom height for the custom paper size. Valid units are mm, px and cm. eg: 30mm  | [optional] 
**orientation** | **str** | Specifies the orientation of the PDF. The available options are \&quot;1\&quot; for portrait and \&quot;2\&quot; for landscape.  | [optional] 
**header_font_size** | **str** | Specifies the font size for the header in the PDF.  | [optional] 
**margin_top** | **str** | Specify the top margin for the PDF in millimeters (mm).  | [optional] 
**margin_right** | **str** | Specify the right margin for the PDF in millimeters (mm).  | [optional] 
**margin_bottom** | **str** | Specify the bottom margin for the PDF in millimeters (mm).  | [optional] 
**margin_left** | **str** | Specify the left margin for the PDF in millimeters (mm).  | [optional] 
**print_background** | **str** | Specifies whether to print the background graphics and colors in the PDF. Set to \&quot;1\&quot; to include backgrounds or \&quot;0\&quot; to exclude them.  | [optional] 
**display_header_footer** | **bool** | Specifies whether to display the header and footer in the PDF. Set to true to include the header and footer or false to exclude them.  | [optional] 
**custom_header** | **str** | Specify custom HTML markup for the headerof the PDF. These properties should contain valid HTML markup, including any necessary CSS styles.  | [optional] 
**custom_footer** | **str** | Specify custom HTML markup for the footer of the PDF. These properties should contain valid HTML markup, including any necessary CSS styles.  | [optional] 

## Example

```python
from APITemplateio.models.pdf_generation_settings_object import PDFGenerationSettingsObject

# TODO update the JSON string below
json = "{}"
# create an instance of PDFGenerationSettingsObject from a JSON string
pdf_generation_settings_object_instance = PDFGenerationSettingsObject.from_json(json)
# print the JSON string representation of the object
print PDFGenerationSettingsObject.to_json()

# convert the object into a dict
pdf_generation_settings_object_dict = pdf_generation_settings_object_instance.to_dict()
# create an instance of PDFGenerationSettingsObject from a dict
pdf_generation_settings_object_form_dict = pdf_generation_settings_object.from_dict(pdf_generation_settings_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


