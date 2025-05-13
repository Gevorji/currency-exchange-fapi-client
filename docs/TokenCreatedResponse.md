# TokenCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | 
**access_expires_in** | [**AccessExpiresIn**](AccessExpiresIn.md) |  | 
**refresh_token** | **str** |  | [optional] 
**refresh_expires_in** | [**RefreshExpiresIn**](RefreshExpiresIn.md) |  | 
**scope** | **List[str]** |  | [optional] 

## Example

```python
from currency_exchange_fapi_client.models.token_created_response import TokenCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokenCreatedResponse from a JSON string
token_created_response_instance = TokenCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(TokenCreatedResponse.to_json())

# convert the object into a dict
token_created_response_dict = token_created_response_instance.to_dict()
# create an instance of TokenCreatedResponse from a dict
token_created_response_from_dict = TokenCreatedResponse.from_dict(token_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


