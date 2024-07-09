# Soderblog Reimagined

Soderblog Reimagined is a modern revival of the iconic ["Soderberg's Seen, Read"](https://extension765.com/blogs/soderblog/seen-read-2023) yearly blog, bringing the director's unique choices to people. This project aims to honor the original blog's legacy while introducing fresh, innovative features to enhance the user experience.

## Vision

to be written

## Key Features

- Intuitive navigation that guides readers through a curated selection of content
- A responsive design that ensures a seamless experience across all devices
- Interactive elements that encourage reader's to look for more
- A thoughtfully organized archive that makes it easy to explore past entries
- Integration of movie and book API's to fasten the searching process

Soderblog Reimagined invites both long-time followers and new readers to experience the world through Soderberg's unique lens, fostering a community of curious, observant individuals in the digital realm.

---

## Current Backlog

### Data

- ~~Scrapping all data from 2009 to 2023~~
- Cleaning, fixing entries
- use TMDB API for both series and movies, store _director_, _year_, _country of origin_, _description_, _screenwriter_, _genre(s)_
- use TMDB API for images, store base_url, file_path
- use Google's Books API for books and plays, store _writer_, _description_, _selfLink_
- turn final csv to json file

### Front End

- start with creating a vue.js application
- add json file to public folder
- ~~find js data viz library to use(echarts)~~
- work on requests()
- pagination
- lazy loading
- design dashboard
- add data visuals
- TMDB, Google Books reference
- add google analytics(page by page)
