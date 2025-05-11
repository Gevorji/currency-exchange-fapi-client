# UserCreatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**category** | [**UserCategory**](UserCategory.md) |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**id** | **int** |  | 

## Example

```python
from currency_exchange_fapi_client.models.user_created_response import UserCreatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserCreatedResponse from a JSON string
user_created_response_instance = UserCreatedResponse.from_json(json)
# print the JSON string representation of the object
print(UserCreatedResponse.to_json())

# convert the object into a dict
user_created_response_dict = user_created_response_instance.to_dict()
# create an instance of UserCreatedResponse from a dict
user_created_response_from_dict = UserCreatedResponse.from_dict(user_created_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


