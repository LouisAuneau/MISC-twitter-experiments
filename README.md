# Clustering Twitter
This personnal project aims to cluster twitter accounts by topic.

## Setup
You will need a Twitter developer account (more information [here](https://developer.twitter.com/en.html))

Install python dependencies with:
```
pip install -r requirements.txt
```

Then setup your environment file following `.env.exemple`'s template inside a `.env` file.
Include the tokens and keys generated through the Twitter Developer UI, as well as a list of public twitter accounts with at least 100 tweets.
```
cp .env.example .env
vim .env
```

## Run

To load tweets inside a *csv* file, use the `data_load.ipynb` notebook.


## Todo

[x] Load tweets
[ ] Topic extraction per account