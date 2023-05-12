import win32evtlogutil


def write_event_viewer_log(status_messages_list, event_type):
    """Write to the system log (Event Viewer)"""
    win32evtlogutil.ReportEvent(
        appName="CheckIPPort - IP/Port Scanner",
        eventID=1337,
        eventCategory=9000,
        eventType=event_type,
        strings=[message for message in status_messages_list],
        data=b"CheckIPPort")


status_messages = ["10.56.17.11:80 Closed", "10.56.17.12:445 Open"]
write_event_viewer_log(status_messages, 0)  # event types: 0=info 1=error 2=warning
