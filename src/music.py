from youtubesearchpython import VideosSearch;

class Music():
    def __init__(self):
        pass;
    
    def search(self, name):
        videos = [];
        for video in VideosSearch(name).result()["result"]:
            videos.append({
                "title" : video["title"],
                "date_published" : video["publishedTime"],
                "duration" : video["duration"],
                "thumbnail" : video["thumbnails"][0]["url"],
                "link" : video["link"],
                "author" : video["channel"]["name"],
                "author_id" : video["channel"]["id"],
            });
        return videos;
