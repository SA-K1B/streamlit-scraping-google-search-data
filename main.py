import streamlit as st
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse


def get_google_links(query, num_pages=1):
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')  # Run in headless mode
    driver = webdriver.Chrome(options=options)
    
    driver.get("https://www.google.com/")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(50)  # Wait for results to load
    # st.text("Hello")
    links = []
    for _ in range(num_pages):
        # <cite class="tjvcx GvPZzd cHaqb" role="text">https://www.startech.com.bd</cite>
        search_results = driver.find_elements(By.CSS_SELECTOR, ".qLRx3b.tjvcx.GvPZzd.cHaqb")
        search_results2 = driver.find_elements(By.CSS_SELECTOR, ".tjvcx.GvPZzd.cHaqb")
        # print(search_results)
        for cite in search_results:
            if cite.text:
                links.append(cite.text)
        for cite in search_results2:
            if cite.text:
                links.append(cite.text)
        print(links)
        # for result in search_results:
        #     all_links.append(result.get_attribute("href"))
        # next_button = driver.find_elements(By.ID, "pnnext")
        # if next_button:
        #     next_button[0].click()
        #     time.sleep(2)
        # else:
        #     break
    st.text("Finished")
    driver.quit()
    return links

st.title("Google Search Link Collector")

query = st.text_input("Enter your search query:")

if st.button("Search") and query:
    with st.spinner("Fetching results..."):
        # get_google_links(query)
        links = get_google_links(query)
        cleaned_links=[]
        for link in links:
          if link:
           # Parse the URL and extract only the base URL (scheme + domain)
             parsed_url = urlparse(link.split(' › ')[0])  # Split at ' › ' and parse the base URL
             base_url = parsed_url.scheme + "://" + parsed_url.netloc  # Form the base URL
             cleaned_links.append(base_url)
        # print(links)
        df = pd.DataFrame({"Links": cleaned_links})
        st.table(df)
