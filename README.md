# News App

This Python script allows you to fetch and display the latest news headlines from various categories such as business, entertainment, general, health, science, sports, and technology. The script uses the News API to retrieve news articles and presents them in a user-friendly format.

## Features

- **Multiple News Categories**: Choose from categories like business, entertainment, general, health, science, sports, and technology.
- **Real-time News**: Fetch the latest news headlines based on your selected category.
- **Simple and Easy to Use**: The script uses simple prompts to guide you through selecting the news category you want to read.

## Prerequisites

- Python 3.x
- `requests` library
- `newsapi-python` library
- `BeautifulSoup` (optional for further parsing, though not used in the current code)

## Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/Sahuvivek12/simple-news-app-in-python.git
   cd simple-news-app-in-python
   ```

2. Install the required Python packages:

   ```bash
   pip install requests newsapi-python beautifulsoup4
   ```

3. Obtain an API key from [News API](https://newsapi.org/) by signing up and replace `credentials.API_Key` with your API key in the code.

4. Create a `credentials.py` file in the same directory and add your API key:

   ```python
   API_Key = 'your_news_api_key_here'
   ```

## Usage

Run the script and follow the prompts to select the type of news you want to read:

```bash
python news_app.py
```

You'll be prompted to choose a news category:

```plaintext
What news do you want to read, 
0 for business news, 
1 for entertainment news, 
2 for general news, 
3 for health news, 
4 for science news, 
5 for sports news, 
6 for technology news
```

After selecting a category, the latest headlines will be displayed along with links to read more.

## Example Output

```plaintext
What news do you want to read, 
0 for business news, 
1 for entertainment news, 
2 for general news, 
3 for health news, 
4 for science news, 
5 for sports news, 
6 for technology news
:- 2

News: Example Headline 1
Read more: https://example.com/article1
**************************************************
News: Example Headline 2
Read more: https://example.com/article2
**************************************************
```

## Contributing

Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
