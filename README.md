# Withings CLI

A simple way to query Withings API from command line.

### Set your API key and secret

[Register as a Withings developer](https://oauth.withings.com/partner/add)
and configure your Withings API key and secret.

```bash
withings config apikey [KEY]
withings config apisecret [SECRET]
```

Note! Do not disclose your API secret to anyone. As per the Withings'
Terms of Service, you are responsible for maintaining the secrecy
and security of your keys.

Note! Keys will be stored to `~/.withings`, programmatically chmod to 0600.

### Add user

```bash
withings add me
```

Note! When calling add, a browser will be opened. For withings-cli to be
able to access user data, he/she should allow it to do so. This is done by
logging in to Withings account, which is wanted to be added (*me* in this case).

### Check who am I

In case step 2 was accomplished successfully, the following call
should show me's details.

```bash
withings whois me
```

### Try a general query

The following query will fetch me's body measures.

```bash
withings query -v1 -s measure -p action getmeas me
```

Query format maps with [Withings API reference](https://oauth.withings.com/api/doc),
and looks like this

```
withings query -v[VERSION] -s SERVICE -p NAME VALUE -p NAME VALUE ... USER
```

### Read help for more commands

```bash
withings --help
```
