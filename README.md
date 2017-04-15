# Withings CLI

## Step 1: Set your API key and secret

```bash
withings config apikey [KEY]
withings config apisecret [KEY]
```

[Register as a Withings developer](https://oauth.withings.com/partner/add)
and you will get these keys.

Note! Do not disclose your API secret to anyone. As per the Withings'
Terms of Service, you are responsible for maintaining the secrecy
and security of your keys.

Note! Keys will be stored to `~/.withings`, programmatically chmod to 0600.

## Step 2: Add user

```bash
withings add me
```

Note! When calling add, a browser will be opened. For withings-cli to be
able to access user data, he/she should allow it to do so. This is done by
logging in to Withings account, which is wanted to be added (*me* in this case).

## Step 3: Check who am I

In case step 2 was accomplished successfully, the following call
should show me's details.

```bash
withings whois me
```

## Step 4: General query

The following query will fetch me's body measures.

```bash
withings query -s measure -p action getmeas me
```
