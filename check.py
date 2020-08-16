from googleapiclient.discovery import build
import json
my_api_key = "AIzaSyAf0XX45t9abNDLtoQvV1Fiq_YNpNY0yPw"
my_cse_id = "010728687077558550988:pau9qvmk86m"


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


result = google_search("Coffee", my_api_key, my_cse_id)
print(json.dumps(result['items'][0], indent=4))
