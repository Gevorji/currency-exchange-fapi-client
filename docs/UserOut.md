# UserOut


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | 
**category** | [**UserCategory**](UserCategory.md) |  | [optional] 
**is_active** | **bool** |  | [optional] [default to True]
**id** | **int** |  | 

## Example

```python
from currency_exchange_fapi_client.models.user_out import UserOut

# TODO update the JSON string below
json = "{}"
# create an instance of UserOut from a JSON string
user_out_instance = UserOut.from_json(json)
# print the JSON string representation of the object
print(UserOut.to_json())

# convert the object into a dict
user_out_dict = user_out_instance.to_dict()
# create an instance of UserOut from a dict
user_out_from_dict = UserOut.from_dict(user_out_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


