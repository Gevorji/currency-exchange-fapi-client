# ExchangeRateOutSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**base_currency** | [**CurrencyOutSchema**](CurrencyOutSchema.md) |  | 
**target_currency** | [**CurrencyOutSchema**](CurrencyOutSchema.md) |  | 
**rate** | **float** |  | 

## Example

```python
from currency_exchange_fapi_client.models.exchange_rate_out_schema import ExchangeRateOutSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeRateOutSchema from a JSON string
exchange_rate_out_schema_instance = ExchangeRateOutSchema.from_json(json)
# print the JSON string representation of the object
print(ExchangeRateOutSchema.to_json())

# convert the object into a dict
exchange_rate_out_schema_dict = exchange_rate_out_schema_instance.to_dict()
# create an instance of ExchangeRateOutSchema from a dict
exchange_rate_out_schema_from_dict = ExchangeRateOutSchema.from_dict(exchange_rate_out_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


