# Google Search Link Collector

This is a Streamlit app that allows users to input a search query, fetches the top links from Google search results, and displays them in a table. The app uses Selenium to automate the process of collecting links from Google search pages.

## Features

- **Input Search Query**: Users can input their search query.
- **Fetch Links**: Automatically collects top links from Google search results.
- **Display Results**: Displays the collected links in a neat table.


## Installation

To run this app, you need Python installed along with the necessary libraries. Follow the steps below to set up the project:

**1. Clone the Repository**:
 ```sh
    git clone https://github.com/SA-K1B/streamlit-scraping-google-search-data.git
    cd streamlit-scraping-google-search-data
 ```

**2. Set Up a Virtual Environment**:

#### On Windows:
```sh
    python -m venv venv
    venv\Scripts\activate
```    
#### On macOS/Linux:
```sh
    python3 -m venv venv
    source venv/bin/activate
```
**3. Install Required Libraries**:



```sh
    pip install -r requirements.txt
```
**4. Run the App**

```sh
    streamlit run main.py
```