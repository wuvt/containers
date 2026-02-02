import requests
import xml.etree.ElementTree as ET
from http.server import BaseHTTPRequestHandler, HTTPServer
from datetime import datetime, timezone, timedelta

VT_CAP_FEED_URL = "https://content.alerts.vt.edu/alerts-cap-inbound/api/cap"

SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8000

FETCH_WINDOW = timedelta(weeks=365)
SERVE_WINDOW = timedelta(days=1)

def fetch_and_translate_feed(host_header, feed = True):
    window = int((datetime.now() - FETCH_WINDOW).timestamp() * 1000)
    response = requests.get(VT_CAP_FEED_URL + f"?after={window}")
    response.raise_for_status()
    vt_cap_xml = ET.fromstring(response.content)
    atom_root = ET.Element("feed", xmlns="http://www.w3.org/2005/Atom")
    title = ET.SubElement(atom_root, "title", type="text")
    title.text = "VT ALERTS IPAWS EAS FEED"
    
    feed_id = ET.SubElement(atom_root, "id")
    feed_id.text = f"http://{host_header}/IPAWSOPEN_EAS_SERVICE/rest/feed"
    
    latest_entry_time = None
    one_minute_ago = datetime.now(timezone.utc) - SERVE_WINDOW
    
    entries = []
    for alert_node in vt_cap_xml:
        if alert_node.tag == '{urn:oasis:names:tc:emergency:cap:1.2}alert':
            scope_node = alert_node.find("{urn:oasis:names:tc:emergency:cap:1.2}scope")
            if scope_node is None or scope_node.text != "Public":
                continue

            sent_node = alert_node.find("{urn:oasis:names:tc:emergency:cap:1.2}sent")
            
            current_entry_time = None
            if sent_node is not None and sent_node.text:
                current_entry_time = datetime.fromisoformat(sent_node.text)
            else:
                current_entry_time = datetime.now(timezone.utc)

            alert_key = alert_node.get("key")
            if not alert_key:
                continue
            
            entry = ET.Element("entry")
            
            single_alert_url = f"{VT_CAP_FEED_URL}/{alert_key}"
            entry_title = ET.SubElement(entry, "title", type="text")
            entry_title.text = f"VTALERT"
            ET.SubElement(entry, "link", href=single_alert_url)
            entry_id = ET.SubElement(entry, "id")
            entry_id.text = single_alert_url
            entry_updated = ET.SubElement(entry, "updated")

            ET.SubElement(entry, "category", term="LAE", label="event")
            ET.SubElement(entry, "category", term="51", label="statefips")

            entry_updated.text = current_entry_time.replace(tzinfo=timezone.utc).isoformat().replace('+00:00', 'Z')

            if latest_entry_time is None or current_entry_time > latest_entry_time:
                latest_entry_time = current_entry_time
            
            if current_entry_time < one_minute_ago:
                continue
            
            entries.append(entry)

    updated = ET.Element("updated")
    if latest_entry_time:
        updated.text = latest_entry_time.replace(tzinfo=timezone.utc).isoformat().replace('+00:00', 'Z')
    else:
        updated.text = datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')
    
    atom_root.insert(1, updated)
    
    if feed:
        entries.sort(key=lambda e: e.find('updated').text, reverse=True)
        
        for entry in entries:
            atom_root.append(entry)
            
    return ET.tostring(atom_root, encoding='unicode')

class IPAWSHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/IPAWSOPEN_EAS_SERVICE/rest/update' or \
        self.path == '/IPAWSOPEN_EAS_SERVICE/rest/feed':
            self.send_response(200)
            self.send_header("Content-type", "application/xml")
            self.end_headers()
            atom_feed = fetch_and_translate_feed(self.headers['Host'], feed=self.path.endswith("feed"))
            if atom_feed:
                self.wfile.write(atom_feed.encode('utf-8'))

server_address = (SERVER_HOST, SERVER_PORT)
httpd = HTTPServer(server_address, IPAWSHandler)
print(f"serving {SERVER_HOST}:{SERVER_PORT}")
httpd.serve_forever()
