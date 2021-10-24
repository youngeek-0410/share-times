# API

swaggerは作成コストが大きいのでmdで作成します。

## path

### /api/organization

- POST  
    受け付けません。
- GET  
    Organization一覧(is_staffを除く)が返却されます。

### /api/organization/{organization_uuid}

- GET  
    uuidにマッチするOrganizationが返却されます。
- PUT(IsAuthenticated)  
    uuidにマッチするOrganizationを更新します。
    descriptionのみを変更できます。

### /api/waiting_time_history

- GET  
    waiting_time_history一覧が返却されます。  
    ?onluy-latest=true というクエリを追加すると各団体の最新一覧が返却されます。

- POST(IsAuthenticated)  
    waiting_time_historyを追加します。organizationにはログイン中のorganizationが自動的に追加されます。

### /api/waiting_time_history/{waiting_time_history_uuid}

- GET  
    ほぼ使わないと思いますが、uuidにマッチするwaiting_time_historyが返却されます。

- PUT  
    受け付けません。

### /api-auth/login

- POST  
    username, passwordを用いてログインします。(cross-originでは使用しない?)

### /api-auth/logout

- POST  
    ログアウトします。

### /api-token-auth/

- POST  
    username, passwordを用いてログインします。  
    Tokenが返却されるのでそれを使用してAPIを呼び出します。  
    (e.g.) curl <http://localhost/api-token-auth/> -XPOST -d 'username=admin&password=admin'

## parameter

- ?format=json
    json形式で返却します。(使用しなくても場合によってはjsonで返る)

## examples

waiting_time_historyをcreate

```bash
~ $ curl http://localhost/api/waiting_time_history/ -d 'waiting_time=27' -H "Authorization: Token ab164bc3503a0d128a81f67c7ebbef0a816fe5e5" | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   222  100   207  100    15   7666    555 --:--:-- --:--:-- --:--:--  8222
{
  "uuid": "fe6c8764-1276-4617-8c89-d025beb65b24",
  "waiting_time": 27,
  "organization": {
    "uuid": "bd9d5906-7ac2-4884-a0ab-159ed6b9adc0",
    "name": "admin",
    "description": "",
    "type": null
  },
  "created_at": "2021-10-01 22:53:48"
}
```

認証情報(トークン)なしでwaiting_time_historyをcreate

```bash
~ $ curl http://localhost/api/waiting_time_history/ -d 'waiting_time=17' | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    70  100    55  100    15  13750   3750 --:--:-- --:--:-- --:--:-- 23333
{
  "detail": "認証情報が含まれていません。"
}
```

waiting_time_history全取得

```bash
~ $ curl http://localhost/api/waiting_time_history/ | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1641  100  1641    0     0  71347      0 --:--:-- --:--:-- --:--:-- 71347
{
  "4I": [
    {
      "uuid": "2e03114a-051d-4137-b3e1-a20983232046",
      "waiting_time": 5,
      "organization": {
        "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
        "name": "4I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-10-01 21:33:38"
    },
    {
      "uuid": "4d5e3ed0-2862-44ef-8237-a34d2b5ce239",
      "waiting_time": 5,
      "organization": {
        "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
        "name": "4I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-10-01 21:30:46"
    },
    {
      "uuid": "68afb1c3-1ce7-4941-916b-817bb034ae95",
      "waiting_time": 5,
      "organization": {
        "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
        "name": "4I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-10-01 21:29:34"
    },
    {
      "uuid": "8267379d-6dde-472e-a5d5-1dcaabc0d5b4",
      "waiting_time": 5,
      "organization": {
        "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
        "name": "4I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-10-01 21:29:03"
    },
    {
      "uuid": "b6315631-fe6a-4f87-b9c8-d23a8bbf2b3e",
      "waiting_time": 3,
      "organization": {
        "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
        "name": "4I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-09-30 10:39:13"
    }
  ],
  "2I": [
    {
      "uuid": "0a926d5b-324c-452d-943d-6bfa681d6cd6",
      "waiting_time": 10,
      "organization": {
        "uuid": "b9302174-e290-423f-88d4-84bf1c1f5497",
        "name": "2I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-09-29 18:24:44"
    },
    {
      "uuid": "dd86b26e-d63b-4e24-a1ed-8b48fac9b4cc",
      "waiting_time": 0,
      "organization": {
        "uuid": "b9302174-e290-423f-88d4-84bf1c1f5497",
        "name": "2I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-09-29 00:17:26"
    },
    {
      "uuid": "18bbf949-68fd-4547-b287-33f38a530d0d",
      "waiting_time": 10,
      "organization": {
        "uuid": "b9302174-e290-423f-88d4-84bf1c1f5497",
        "name": "2I",
        "description": "",
        "type": "I"
      },
      "created_at": "2021-09-29 00:16:11"
    }
  ]
}
```

waiting_time_history最新のみ取得

```bash
~ $ curl http://localhost/api/waiting_time_history/?only-latest=true | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   418  100   418    0     0  27866      0 --:--:-- --:--:-- --:--:-- 27866
{
  "4I": {
    "uuid": "2e03114a-051d-4137-b3e1-a20983232046",
    "waiting_time": 5,
    "organization": {
      "uuid": "ce2d9fe7-7ec9-4a26-a5ea-403ec9d4f808",
      "name": "4I",
      "description": "",
      "type": "I"
    },
    "created_at": "2021-10-01 21:33:38"
  },
  "2I": {
    "uuid": "0a926d5b-324c-452d-943d-6bfa681d6cd6",
    "waiting_time": 10,
    "organization": {
      "uuid": "b9302174-e290-423f-88d4-84bf1c1f5497",
      "name": "2I",
      "description": "",
      "type": "I"
    },
    "created_at": "2021-09-29 18:24:44"
  }
}
```

tokenの取得

```bash
~ $ curl http://localhost/api-token-auth/ -XPOST -d 'username=admin&password=admin' | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100    81  100    52  100    29    658    367 --:--:-- --:--:-- --:--:--  1012
{
  "token": "ab164bc3503a0d128a81f67c7ebbef0a816fe5e5"
}
```

organization descriptionの更新

```bash
~ $ curl http://localhost/api/organization/bd9d5906-7ac2-4884-a0ab-159ed6b9adc0/  -XPUT -d 'description="test"' -H "Authorization: Token ab164bc3503a0d128a81f67c7ebbef0a816fe5e5" | jq .
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   117  100    99  100    18   3960    720 --:--:-- --:--:-- --:--:--  4680
{
  "uuid": "bd9d5906-7ac2-4884-a0ab-159ed6b9adc0",
  "name": "admin",
  "description": "\"test\"",
  "type": null
}
```
