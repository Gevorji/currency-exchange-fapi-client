# currency_exchange_fapi_client.AuthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_create_token**](AuthApi.md#auth_create_token) | **POST** /tokens/gain | Create Token
[**auth_create_user**](AuthApi.md#auth_create_user) | **POST** /clients/register | Create User
[**auth_refresh_access_token**](AuthApi.md#auth_refresh_access_token) | **POST** /tokens/refresh | Refresh Access Token
[**auth_revoke_users_token**](AuthApi.md#auth_revoke_users_token) | **PATCH** /tokens/revoke | Revoke Users Token


# **auth_create_token**
> TokenCreatedResponse auth_create_token(username, password, device_id=device_id, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)

Create Token

### Example


```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.token_created_response import TokenCreatedResponse
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password = 'password_example' # str | 
    device_id = 'none' # str |  (optional) (default to 'none')
    grant_type = 'grant_type_example' # str |  (optional)
    scope = '' # str |  (optional) (default to '')
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # Create Token
        api_response = await api_instance.auth_create_token(username, password, device_id=device_id, grant_type=grant_type, scope=scope, client_id=client_id, client_secret=client_secret)
        print("The response of AuthApi->auth_create_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_create_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password** | **str**|  | 
 **device_id** | **str**|  | [optional] [default to &#39;none&#39;]
 **grant_type** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] [default to &#39;&#39;]
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

### Return type

[**TokenCreatedResponse**](TokenCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Invalid credentials |  -  |
**403** | User disabled |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_create_user**
> UserCreatedResponse auth_create_user(username, password1, password2)

Create User

### Example


```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.user_created_response import UserCreatedResponse
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.AuthApi(api_client)
    username = 'username_example' # str | 
    password1 = 'password1_example' # str | 
    password2 = 'password2_example' # str | 

    try:
        # Create User
        api_response = await api_instance.auth_create_user(username, password1, password2)
        print("The response of AuthApi->auth_create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_create_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 
 **password1** | **str**|  | 
 **password2** | **str**|  | 

### Return type

[**UserCreatedResponse**](UserCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful Response |  -  |
**400** | Submitted values invalid |  -  |
**409** | User already exists |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_refresh_access_token**
> TokenCreatedResponse auth_refresh_access_token(grant_type, refresh_token)

Refresh Access Token

### Example

* Basic Authentication (HTTPBasic):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.token_created_response import TokenCreatedResponse
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = currency_exchange_fapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.AuthApi(api_client)
    grant_type = 'grant_type_example' # str | Required to be an exact \\\"refresh_token\\\" value
    refresh_token = 'refresh_token_example' # str | 

    try:
        # Refresh Access Token
        api_response = await api_instance.auth_refresh_access_token(grant_type, refresh_token)
        print("The response of AuthApi->auth_refresh_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_refresh_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Required to be an exact \\\&quot;refresh_token\\\&quot; value | 
 **refresh_token** | **str**|  | 

### Return type

[**TokenCreatedResponse**](TokenCreatedResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**400** | Token is invalid |  -  |
**401** | Invalid credentials |  -  |
**403** | User disabled or token owner is not a user, or token is revoked |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_revoke_users_token**
> TokensRevokedResponse auth_revoke_users_token(tokens=tokens)

Revoke Users Token

### Example

* Basic Authentication (HTTPBasic):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.tokens_revoked_response import TokensRevokedResponse
from currency_exchange_fapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = currency_exchange_fapi_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: HTTPBasic
configuration = currency_exchange_fapi_client.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.AuthApi(api_client)
    tokens = ['tokens_example'] # List[str] |  (optional)

    try:
        # Revoke Users Token
        api_response = await api_instance.auth_revoke_users_token(tokens=tokens)
        print("The response of AuthApi->auth_revoke_users_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_revoke_users_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tokens** | [**List[str]**](str.md)|  | [optional] 

### Return type

[**TokensRevokedResponse**](TokensRevokedResponse.md)

### Authorization

[HTTPBasic](../README.md#HTTPBasic)

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**401** | Invalid credentials |  -  |
**403** | User disabled |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

