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

Note! When calling add a browser will be opened. For withings-cli to be
able to access user data, the user should allow it to do so (*me* in
this case).

### Check who am I

The following call should show mes details — if the above was accomplished.

```bash
withings whois me
```

### Try query mes body measures

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
