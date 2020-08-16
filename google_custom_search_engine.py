from apiclient.discovery import build

API_KEY = "AIzaSyAf0XX45t9abNDLtoQvV1Fiq_YNpNY0yPw"
SEARCH_ENGINE_ID = "010728687077558550988:pau9qvmk86m"


def google_search(query, api_key, search_engin_id):
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    try:
        results = []
        for i in range(1, 30, 10):
            result = resource.list(
                q=query, cx=search_engin_id, start=i).execute()
            results += result['items']
        return results
    except:
        print("Search not available. Search again.")


def show_results(results):
    for item in results:
        print(item['title'], "  ", item['link'])


while True:
    print("\nPress Enter with Empty Search Field, if don't want tosearch\n")
    query = input("Search: ")

    if len(query) < 1:
        break
    print("\nResults.......\n")
    search_items = google_search(query, API_KEY, SEARCH_ENGINE_ID)
    show_results(search_items)
    print("\n")
