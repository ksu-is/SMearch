from flask import Flask, render_template, request, redirect, url_for
import webbrowser

app = Flask(__name__)

def search_social_media(query, platform):
    # Construct the Google search URL with the site: operator for the specified platform
    search_url = f"https://www.google.com/search?q={query}+site%3A{platform}.com"
    return search_url

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        platform = request.form["platform"]
        query = request.form["query"]
        final_search_url = search_social_media(query, platform)
        
        if final_search_url:
            return redirect(final_search_url)
        else:
            return "Failed to construct search URL."
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
