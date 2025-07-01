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

## TO-DO

- [x] add better time tracking
- [x] add object of entry
- [x] add convert time from string util
- [x] add custom refresh time
- [x] add better message function
- [ ] add converting what rss fetch into entry object, as i need it
- [ ] fix sleep function to just compare time during the day without dates

### OPTIONAL

- [ ] add tracking latest id for extra sekurity
- [ ] add database for users and sent notifications
- [ ] add unsubscribing
