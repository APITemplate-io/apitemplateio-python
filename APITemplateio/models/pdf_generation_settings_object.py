# coding: utf-8

"""
    APITemplate.io API Reference

    # Introduction   Welcome to the [APITemplate.io](https://apitemplate.io) API v2!  APITemplate.io provides PDF generation services including [Template-based PDF generation](https://apitemplate.io/pdf-generation-api/), [HTML to PDF](https://apitemplate.io/html-to-pdf-api/), and [URL to PDF conversions](https://apitemplate.io/create-pdf-from-url/), as well as an [image generation API](https://apitemplate.io/image-generation-api/).  This page contains the documentation on how to use APITemplate.io through API calls. With the APITemplate.io API, you can create PDF documents and images, as well as manage your templates.  Our API is built on RESTful HTTP, so you can utilize any HTTP/REST library of your choice in your preferred programming language to interact with APITemplate.io's API.  **Steps to produce PDFs/Images** 1. Design your template(s) using our intuitive drag-and-drop template editor or the HTML editor and save it. 2. Integrate your workflow, either with platforms like Zapier, Make.com/Integromat, Bubble.io, or any programming languages that support REST API, to send us the JSON data along with the template ID/URL/or HTML content. 3. Our REST API will then return a download URL for the images (in PNG and JPEG formats) or PDFs.  # Authentication Upon signing up for an account, an API key will be generated for you. If needed, you can reset this API key via the web console (under the \"API Integration\" section).  To integrate with our services, you need to authenticate with the APITemplate.io API. Provide your secret key in the request header using the X-API-KEY field.   # Content Type and CORS  **Request Content-Type** The Content-Type for POST and GET requests is set to application/json.  **Cross-Origin Resource Sharing** This API features Cross-Origin Resource Sharing (CORS) implemented in compliance with  [W3C spec](https://www.w3.org/TR/cors/). And that allows cross-domain communication from the browser. All responses have a wildcard same-origin which makes them completely public and accessible to everyone, including any code on any site.    # Regional API endpoint(s) A regional API endpoint is intended for customers in the same region. The data for the request and generated PDFs/images are processed and stored within the region.  The regions are:  | Region               | Endpoint                            | Max Timeout (Seconds) | Max Payload Size(MB)** | |----------------------|-------------------------------------|-----------------------|-------------------------| | Default (Singapore)  | https://rest.apitemplate.io         | 100                   | 1                       | | Europe (Frankfurt)   | https://rest-de.apitemplate.io      | 100                   | 1                       | | US East (N. Virginia)| https://rest-us.apitemplate.io      | 100                   | 1                       | | Australia (Sydney)   | https://rest-au.apitemplate.io      | 30                    | 6                       |   Alternative Regions: | Region               | Endpoint                            | Max Timeout (Seconds) | Max Payload Size(MB)** | |----------------------|-------------------------------------|-----------------------|-------------------------| | Default (Singapore)  | https://rest-alt.apitemplate.io     | 30                    | 6                       | | Europe (Frankfurt)   | https://rest-alt-de.apitemplate.io  | 30                    | 6                       | | US East (N. Virginia)| https://rest-alt-us.apitemplate.io  | 30                    | 6                       |  ** Note: - Payload size applies to request and response - If \"export_type\" is set to `json` which output file that on AWS S3 doesn't have the limitation - If the \"export_type\" is set to `file` which returns binary data of the generated PDF, the file size of the generated PDF is limited to either 6MB or 1MB based on the region    Other regions are available on request, contact us at hello@apitemplate.io for more information  # Rate limiting Our API endpoints use IP-based rate limiting to ensure fair usage and prevent abuse. Users are allowed to make up to **100 requests per 10 seconds**. This rate limit is designed to accommodate a reasonable volume of requests while maintaining optimal performance for all users.  However, if you exceed this limit and make additional requests, you will receive a response with HTTP code 429. This status code indicates that you have reached the rate limit and need to wait before making further requests. 

    The version of the OpenAPI document: Version 2.0
    Contact: hello@apitemplate.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictBool, StrictStr

class PDFGenerationSettingsObject(BaseModel):
    """
    The settings object contains various properties to configure the PDF generation. 
    """
    paper_size: Optional[StrictStr] = Field(None, description="Specifies the paper size for the PDF. The available options are Letter, Legal, Tabloid, Ledger, A0, A1, A2, A3, A4, A5,A6 or custom. custom dimensions specified as \"custom_width\" and \"custom_height\". ")
    custom_width: Optional[StrictStr] = Field(None, description="Custom width for the custom paper size. Valid units are mm, px and cm. eg: 30mm ")
    custom_height: Optional[StrictStr] = Field(None, description="Custom height for the custom paper size. Valid units are mm, px and cm. eg: 30mm ")
    orientation: Optional[StrictStr] = Field(None, description="Specifies the orientation of the PDF. The available options are \"1\" for portrait and \"2\" for landscape. ")
    header_font_size: Optional[StrictStr] = Field(None, description="Specifies the font size for the header in the PDF. ")
    margin_top: Optional[StrictStr] = Field(None, description="Specify the top margin for the PDF in millimeters (mm). ")
    margin_right: Optional[StrictStr] = Field(None, description="Specify the right margin for the PDF in millimeters (mm). ")
    margin_bottom: Optional[StrictStr] = Field(None, description="Specify the bottom margin for the PDF in millimeters (mm). ")
    margin_left: Optional[StrictStr] = Field(None, description="Specify the left margin for the PDF in millimeters (mm). ")
    print_background: Optional[StrictStr] = Field(None, description="Specifies whether to print the background graphics and colors in the PDF. Set to \"1\" to include backgrounds or \"0\" to exclude them. ")
    display_header_footer: Optional[StrictBool] = Field(None, alias="displayHeaderFooter", description="Specifies whether to display the header and footer in the PDF. Set to true to include the header and footer or false to exclude them. ")
    custom_header: Optional[StrictStr] = Field(None, description="Specify custom HTML markup for the headerof the PDF. These properties should contain valid HTML markup, including any necessary CSS styles. ")
    custom_footer: Optional[StrictStr] = Field(None, description="Specify custom HTML markup for the footer of the PDF. These properties should contain valid HTML markup, including any necessary CSS styles. ")
    __properties = ["paper_size", "custom_width", "custom_height", "orientation", "header_font_size", "margin_top", "margin_right", "margin_bottom", "margin_left", "print_background", "displayHeaderFooter", "custom_header", "custom_footer"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> PDFGenerationSettingsObject:
        """Create an instance of PDFGenerationSettingsObject from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> PDFGenerationSettingsObject:
        """Create an instance of PDFGenerationSettingsObject from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return PDFGenerationSettingsObject.parse_obj(obj)

        _obj = PDFGenerationSettingsObject.parse_obj({
            "paper_size": obj.get("paper_size"),
            "custom_width": obj.get("custom_width"),
            "custom_height": obj.get("custom_height"),
            "orientation": obj.get("orientation"),
            "header_font_size": obj.get("header_font_size"),
            "margin_top": obj.get("margin_top"),
            "margin_right": obj.get("margin_right"),
            "margin_bottom": obj.get("margin_bottom"),
            "margin_left": obj.get("margin_left"),
            "print_background": obj.get("print_background"),
            "display_header_footer": obj.get("displayHeaderFooter"),
            "custom_header": obj.get("custom_header"),
            "custom_footer": obj.get("custom_footer")
        })
        return _obj


