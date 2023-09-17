# MergePdfsRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**urls** | **List[object]** | URL array. We support normal http/https URLs and data URLs - Normal URLs: URLs start with http/https, e.g: \&quot;https://fileserver.com/a1.pdf\&quot;) - Data URLs: URLs prefixed with the \&quot;data:\&quot; scheme, e.g \&quot;data:application/pdf;base64,JVBERi0xLjIg...[truncated]\&quot;  | 
**export_type** | **str** | - Either &#x60;file&#x60; or &#x60;json&#x60;(Default).   - The option &#x60;json&#x60; returns a JSON object, and the output PDF is stored on a CDN.   - The option &#x60;file&#x60; returns binary data of the generated PDF(Secure and completely private) and the response HTTP header Content-Disposition is set to attachment. It has a file size limit of 6MB.  | [optional] 
**expiration** | **int** | - Expiration of the generated PDF in minutes(default to &#x60;0&#x60;, store permanently)   - Use &#x60;0&#x60; to store on cdn permanently   - Or use the range between &#x60;1&#x60; minute and &#x60;43200&#x60; minutes(30 days) to specify the expiration of the generated PDF  | [optional] 
**cloud_storage** | **int** | - Upload the generated PDFs/images to our storage CDN, default to &#x60;1&#x60;. If you have configured &#x60;Post Action&#x60; to upload the PDFs/Images to your own S3, please set it to &#x60;0&#x60;.  | [optional] 

## Example

```python
from APITemplateio.models.merge_pdfs_request import MergePdfsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MergePdfsRequest from a JSON string
merge_pdfs_request_instance = MergePdfsRequest.from_json(json)
# print the JSON string representation of the object
print MergePdfsRequest.to_json()

# convert the object into a dict
merge_pdfs_request_dict = merge_pdfs_request_instance.to_dict()
# create an instance of MergePdfsRequest from a dict
merge_pdfs_request_form_dict = merge_pdfs_request.from_dict(merge_pdfs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


