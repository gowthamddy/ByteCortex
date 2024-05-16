# ByteCortex

ByteCortex is an Abstractive Text Summarizer designed to summarize articles, websites, and long books through URL inputs. Additionally, it estimates the reading time for users.

## How It Works

1. **Text Retrieval**: `scraper.py` retrieves text from a specified URL and performs formatting and cleaning.

2. **Tokenization and Analysis**: The cleaned text is passed to `summarizer.py`, which utilizes Spacy for tokenization into sentences and words.

3. **Frequency Analysis**: A dictionary is used to store word frequencies, normalized by dividing by the maximum frequency to ascertain relative frequency.

4. **Sentence Scoring**: Sentence scores are determined by summing the word frequencies within each sentence.

5. **Summary Generation**: Utilizing a heap queue, sentences with the highest scores are selected and concatenated to generate the summary.

6. **Reading Time Estimation**: Subsequently, the estimated reading time is computed.

7. **Presentation**: Finally, the title, summary, and estimated reading time are presented to the user.

## Tech Stack Used

- Python version >= 3.0
- Spacy v3.10
- Flask
- Beautiful Soup v4.0 or above
  
## Project Workflow

![Alt text](https://raw.githubusercontent.com/YourUsername/YourRepository/main/ByteCortex/uml2.png)
  
## Demo

[![Demo Video](http://img.youtube.com/vi/pU-SXB1o6S0/maxresdefault.jpg)](https://youtu.be/pU-SXB1o6S0)

