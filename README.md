# rss-notification

How env should look

```
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
SENDER_NUMBER=
MY_NUMBER=
RSS_URL=
```

entry object:

```
entry {
    id: url (converted to int later)
    title: string
    summary: text
    link: string
    author: string
    published: date
}
```

TO-DO

- [x] add better time tracking
- [ ] add object of entry
- [ ] add tracking latest id
- [ ] add unsubscribing?
