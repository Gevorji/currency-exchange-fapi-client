# currency_exchange_fapi_client.UsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_downgrade_users_category**](UsersApi.md#users_downgrade_users_category) | **PATCH** /admin/users/{user_id}/category/downgrade | Downgrade Users Category
[**users_get_all_users**](UsersApi.md#users_get_all_users) | **GET** /admin/users/all | Get All Users
[**users_get_user**](UsersApi.md#users_get_user) | **GET** /admin/users/search | Get User
[**users_make_user_active**](UsersApi.md#users_make_user_active) | **PATCH** /admin/users/{user_id}/activate | Make User Active
[**users_make_user_inactive**](UsersApi.md#users_make_user_inactive) | **PATCH** /admin/users/{user_id}/deactivate | Make User Inactive
[**users_promote_users_category**](UsersApi.md#users_promote_users_category) | **PATCH** /admin/users/{user_id}/category/promote | Promote Users Category


# **users_downgrade_users_category**
> UserOut users_downgrade_users_category(user_id, to)

Downgrade Users Category

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.transition_users_categories import TransitionUsersCategories
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)
    user_id = 56 # int | 
    to = currency_exchange_fapi_client.TransitionUsersCategories() # TransitionUsersCategories | 

    try:
        # Downgrade Users Category
        api_response = await api_instance.users_downgrade_users_category(user_id, to)
        print("The response of UsersApi->users_downgrade_users_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_downgrade_users_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **to** | [**TransitionUsersCategories**](.md)|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | Performed update conflicts with current state of user category |  -  |
**404** | User not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_all_users**
> List[UserOut] users_get_all_users()

Get All Users

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)

    try:
        # Get All Users
        api_response = await api_instance.users_get_all_users()
        print("The response of UsersApi->users_get_all_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_all_users: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[UserOut]**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_get_user**
> UserOut users_get_user(username)

Get User

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)
    username = 'username_example' # str | 

    try:
        # Get User
        api_response = await api_instance.users_get_user(username)
        print("The response of UsersApi->users_get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_get_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**404** | User not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_make_user_active**
> UserOut users_make_user_active(user_id)

Make User Active

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Make User Active
        api_response = await api_instance.users_make_user_active(user_id)
        print("The response of UsersApi->users_make_user_active:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_make_user_active: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | User is already active or user is admin |  -  |
**404** | User not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_make_user_inactive**
> UserOut users_make_user_inactive(user_id)

Make User Inactive

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)
    user_id = 56 # int | 

    try:
        # Make User Inactive
        api_response = await api_instance.users_make_user_inactive(user_id)
        print("The response of UsersApi->users_make_user_inactive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_make_user_inactive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | User already deactivated or user is admin |  -  |
**404** | User not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_promote_users_category**
> UserOut users_promote_users_category(user_id, to)

Promote Users Category

### Example

* OAuth Authentication (OAuth2PasswordBearer):

```python
import currency_exchange_fapi_client
from currency_exchange_fapi_client.models.transition_users_categories import TransitionUsersCategories
from currency_exchange_fapi_client.models.user_out import UserOut
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

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Enter a context with an instance of the API client
async with currency_exchange_fapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = currency_exchange_fapi_client.UsersApi(api_client)
    user_id = 56 # int | 
    to = currency_exchange_fapi_client.TransitionUsersCategories() # TransitionUsersCategories | 

    try:
        # Promote Users Category
        api_response = await api_instance.users_promote_users_category(user_id, to)
        print("The response of UsersApi->users_promote_users_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_promote_users_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **int**|  | 
 **to** | [**TransitionUsersCategories**](.md)|  | 

### Return type

[**UserOut**](UserOut.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**409** | Performed update conflicts with current state of user category |  -  |
**404** | User not found |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

