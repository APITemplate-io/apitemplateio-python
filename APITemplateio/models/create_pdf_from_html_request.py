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


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr
from APITemplateio.models.pdf_generation_settings_object import PDFGenerationSettingsObject

class CreatePdfFromHtmlRequest(BaseModel):
    """
    CreatePdfFromHtmlRequest
    """
    body: Optional[StrictStr] = Field(None, description="The HTML body content for the PDF. This property supports HTML markup and can include Jinja2 syntax (e.g {{name}}). The value of {{name}} will be replaced with the actual value provided in the data object. ")
    css: Optional[StrictStr] = Field(None, description="The CSS styles to be applied to the PDF. This property should contain valid CSS markup and should also include the style tag. ")
    data: Optional[Dict[str, Any]] = Field(None, description="The data object containing values for dynamic content in the HTML body. This object should include properties with corresponding values. ")
    settings: Optional[PDFGenerationSettingsObject] = None
    __properties = ["body", "css", "data", "settings"]

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
    def from_json(cls, json_str: str) -> CreatePdfFromHtmlRequest:
        """Create an instance of CreatePdfFromHtmlRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> CreatePdfFromHtmlRequest:
        """Create an instance of CreatePdfFromHtmlRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return CreatePdfFromHtmlRequest.parse_obj(obj)

        _obj = CreatePdfFromHtmlRequest.parse_obj({
            "body": obj.get("body"),
            "css": obj.get("css"),
            "data": obj.get("data"),
            "settings": PDFGenerationSettingsObject.from_dict(obj.get("settings")) if obj.get("settings") is not None else None
        })
        return _obj

