# Theme choosing (Crypto)
0. Modeling high-frequency limit order book dynamics with support vector machines

1. [AVA - Advanced Volatility Arbitrage](http://web.stanford.edu/class/msande448/2019/Final_reports/gr6.pdf), Stanford, 2019

_In a nutshell:_ Built model to predict with high accuracy where the market is expected to move over the next n minutes.

<details>
    <ul>
        <li>Problem:
            <ul>
                <li>Crypto is massively volatile</li>
                <li>No crypto asset w. smooth index effect</li>
            </ul>
        </li>
        <li>Data: BTC price, Z-score return</li>
        <li>NLU + sentiment: Reddit (<b>r/btc</b> and <b>r/Bitcoin</b>)</li>
            <ul><li>NLTK + TextBlob</li>
                <li>SocialSent</li></ul>
    </ul>
</details>

__Con:__ Not much about trading strategy.

2. [Cryptocurrencies Trading Strategy based on Sentiment Analysis](http://web.stanford.edu/class/msande448/2019/Final_reports/gr4.pdf), Stanford, 2019

_In a nutshell:_ relationship between social network/news data and cryptocurrencies price.

<details>
    <ul>
        <li>Data: BTC-USD from <a href="https://www.coinbase.com">Coinbase</a>, Google Trend and Twitter</li>
        <li>Signal: (sell, buy) * (positive, negative) matrix</li>
        <li>Eval plots: scatter, binned, forward biases, proxy backtest</li>
        <li>Strategy: threshold-based strategy</li>
    </ul>
</details>

__Pro:__ good `Acknowledgement` (thank you teacher)

__Con:__ This article is more like how to build a predictor instead of studying trading strategy. We probably need to delve into improving strategy more and backtest as well.

3. [Technical trading and cryptocurrencies](http://rd8hp6du2b.search.serialssolutions.com/log?L=RD8HP6DU2B&D=SNE&J=ANNAOFOPERE&P=Link&PT=EZProxy&A=Technical+trading+and+cryptocurrencies&H=c1a25a53db&U=http%3A%2F%2Fezproxy.cul.columbia.edu%2Flogin%3Furl%3Dhttps%3A%2F%2Flink.springer.com%2Fopenurl.asp%3Fgenre%3Darticle%26id%3Ddoi%3A10.1007%2Fs10479-019-03357-1), Robert Hudson, 2019

_In a nutshell:_ Employ almost 15,000 technical trading rules from the main five classes of technical trading rules and find significant predictability and profitability for each class of technical trading rule in each cryptocurrency.

<details>
    <ul>
        <li>Data: 
            <ul>
                <li>Bitcoin: <a href="https://www.coindesk.com/price/bitcoin">CoinDesk</a>(2010-07-18), <a href="https://www.bitstamp.net">Bitstamp</a>(2012-12-01)</li>
                <li><a href="https://litecoin.com/en/">Litecoin</a>, <a href="https://ethereum.org">Ethereum</a> and <a href="https://ripple.com">Ripple</a>: <a href="https://coinmarketcap.com">CoinMarketCap</a></li>
                <li>Maximum period possible</li>
            </ul></li>
        <li>Technical trading rules:
            <ol>
                <li>Qualitative: identify patterns from charts</li>
                <li>Quantitative: construct trading signals from time-series analysis</li>
            </ol>
            --- use below five classes ---
            <ol>
                <li>Moving average: attempt to ride trends and identify imminent breaks by examining moving averages, and are quite similar to the time-series momentum effect</li>
                <li>Filter rules: attempt to follow trends by buying (selling) whenever the price has increased (decreased) by a given percentage</li>
                <li>Support-resistance trading rules: create support or resistance bounds around the price which if they breach, indicates further movement in the same direction</li>
                <li>Oscillator trading rules: attempt to identify overbought (oversold) assets and therefore anticipate the imminent market correction</li>
                <li>Channel breakout rules: identify time-varying support and resistance levels which, once breached, indicate further movement in the same direction.</li>
            </ol>
        </li>
    </ul>
</details>

__Pro:__ Maybe we can choose trading strategies from here


4. ✅ [High frequency momentum trading with cryptocurrencies](http://rd8hp6du2b.search.serialssolutions.com/log?L=RD8HP6DU2B&D=ADALY&J=RESEININB&P=Link&PT=EZProxy&A=High+frequency+momentum+trading+with+cryptocurrencies&H=accf7f9d6d&U=http%3A%2F%2Fezproxy.cul.columbia.edu%2Flogin%3Furl%3Dhttps%3A%2F%2Fwww.sciencedirect.com%2Fscience%2Flink%3Fref_val_fmt%3Dinfo%3Aofi%2Ffmt%3Akev%3Amtx%3Ajournal%26svc_val_fmt%3Dinfo%3Aofi%2Ffmt%3Akev%3Amtx%3Asch_srv%26rfr_dat%3Dsaltver%3A1%26rfr_dat%3Dorigin%3ASERIALSSOL%26ctx_enc%3Dinfo%3Aofi%2Fenc%3AUTF-8%26ctx_ver%3DZ39.88-2004%26rft_id%3Dinfo%3Adoi%2F10.1016%2Fj.ribaf.2019.101176%26rft.issn%3D02755319%26rft.volume%3D52%26rft.spage%3D101176%26rft.aulast%3DChu%26rft.date%3D2020%26rfr_dat%3Dmd5%3Aed0d4b99c37646f6153a3619e6a3ea2c), Jeffery Chu, 2020

_In a nutshell:_ Implemented two variations of a signal-based momentum trading strategy.

<details>
    <ul>
        <li>Data: hourly prices of crypto versus the US dollar (2017-02-25 to 2017-08-17) from <a href="https://www.cryptocompare.com">CryptoCompare</a> choosing top 7 using the CCAGG exchange data</li>
        <li>Method: </li>
</details>

5. [A High-Frequency Algorithmic Trading Strategy for Cryptocurrency](), Au Vo, 2018

_In a nutshell:_

6. [Constructing cointegrated cryptocurrency portfolios for statistical arbitrage](http://columbia.summon.serialssolutions.com/2.0.0/link/0/eLvHCXMwrV3bSgMxEB2UggripSpequQHYptttruLpaLSIr6J9bnsZhNbKN3ehBZ_3pndxGoFn3zOw7IzycmZzMwZgJs1PFDDQcZJXG_BCRTEtXofojnx7CWDPF3LJd46uNW9In5cqTHCs2uRsW53aJlDeJopej2vEommqRmhvB1POM2ToryrG64R26ELlLtBqrEJJUFimNRTfv9UVN83eIDHzOUwa2H1pd2hZ0O8G0OOMYr8idN1e_l09uHju6rCYvnrz9akHf_1Tw5gz3JWdldsskPY0KMybLmS-TJsu-7m2RF0aQJooUk7emMq-5KjSFmz31LT5XieqVwTSi2b1X6LEf83GTpvxpA_M2pwyrWj8YPxNBnMpwh4x_DaaXcfHrmd3MAV2lZybXTq-0Ym2kcwRZKSNoQOpcAwPqqbNDFSJsbUfIxVYk_HHkVhfqAx1vRrlAnyTmA3pgr_0TzvBExPgQnlaaSrOlFehDGsoFE1kVF1FQSBMUacQcUZtWfP4ay3suj538sXsIPujopC3AqUDC7rS-Qq1ptX-X75BJc83Tg), __Tim Leung__, 2019

_In a nutshell:_

__Con:__ Focusing on construct crypto portfolio. But tests the port through 3 strategies.


# Proposal

### Objective

Figure out the differences between cryptocurrency market and other fiat currency market. Understand the trading strategy used in \ref{1} . Test different trading strategies on cryptocurrencies market and backtest them. 

### Product and Market

### Data

### Literature