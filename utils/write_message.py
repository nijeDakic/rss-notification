from models import Entry

def write_message(entry: Entry) -> str:
    message = f'''
    📢 {entry.title}\n
    🕒 Објављено: {entry.date.strftime("%d. %m. %Y.")}, {entry.date.strftime("%H:%M")}\n
    ✍️ Аутор: {entry.author}\n
    🔗 Линк: {entry.link}\n
    '''
    return message

# myb add content preview, not probable
# 📄 Садржај:
