# Sentiment_Analyzer
Sentiment Analyzer using Roberta model

# Sentiment Analysis with RoBERTa

A simple command-line sentiment analysis tool using the pre-trained RoBERTa model from Cardiff NLP. This tool analyzes text input and provides sentiment scores for positive, negative, and neutral sentiments.

## Features

- **Real-time sentiment analysis** using state-of-the-art RoBERTa model
- **Continuous analysis mode** - analyze multiple texts in one session
- **Confidence scores** for each sentiment category
- **Simple command-line interface**
- **Error handling** for robust operation

## Model Information

This tool uses the `cardiffnlp/twitter-roberta-base-sentiment` model, which is:
- Pre-trained on Twitter data
- Fine-tuned for sentiment classification
- Optimized for social media text but works well on general text

## Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Setup

1. **Clone or download** this repository to your local machine

2. **Install dependencies** using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python sentiment_analysis.py
   ```

## Usage

### Basic Usage

1. Run the script:
   ```bash
   python sentiment_analysis.py
   ```

2. Enter text when prompted:
   ```
   Enter the text you want to analyse: I love this product!
   ```

3. View the results:
   ```
   Sentiment Analysis Results:
   ------------------------------
   Negative:   2.15%
   Neutral :  12.33%
   Positive:  85.52%

   Predicted: Positive (85.5% confidence)
   ```

4. Continue with more analyses or type `quit` to exit

### Exit Commands

To stop the program, you can use any of these commands:
- `quit`
- `exit`
- `q`
- Just press Enter (empty input)

## Example Session

```
Sentiment Analysis with RoBERTa
========================================
Type 'quit', 'exit', or 'q' to stop the program

Enter the text you want to analyse: This movie is amazing!

Sentiment Analysis Results:
------------------------------
Negative:   1.23%
Neutral :   8.45%
Positive:  90.32%

Predicted: Positive (90.3% confidence)

==================================================

Enter the text you want to analyse: I hate waiting in long queues

Sentiment Analysis Results:
------------------------------
Negative:  78.91%
Neutral :  18.45%
Positive:   2.64%

Predicted: Negative (78.9% confidence)

==================================================

Enter the text you want to analyse: quit
Thank you for using the sentiment analyzer! Goodbye!
```

## Technical Details

### Model Architecture
- **Base Model**: RoBERTa (Robustly Optimized BERT Pretraining Approach)
- **Fine-tuning**: Cardiff NLP team's Twitter sentiment dataset
- **Output**: Three-class classification (Negative, Neutral, Positive)

### Input Limitations
- Maximum input length: 512 tokens
- Longer texts are automatically truncated
- Works best with English text

### Performance
- **Accuracy**: High accuracy on social media and general text
- **Speed**: Fast inference on CPU
- **Memory**: Requires ~500MB RAM for model loading

## File Structure

```
sentiment-analysis/
├── sentiment_analysis.py    # Main application script
├── requirements.txt         # Python dependencies
├── README.md               # This documentation file
└── .gitignore             # Git ignore file (optional)
```

## Troubleshooting

### Common Issues

1. **Import Error**: Make sure all dependencies are installed
   ```bash
   pip install -r requirements.txt
   ```

2. **Memory Error**: The model requires significant memory. Close other applications if needed.

3. **Network Issues**: First run requires internet connection to download the model (~500MB)

4. **Long Loading Time**: Model downloads and loads on first run. Subsequent runs are faster.

### Model Download

On first run, the script will automatically download:
- Tokenizer files (~2MB)
- Model weights (~500MB)

Files are cached locally for future use.

## Contributing

Feel free to submit issues, suggestions, or improvements:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project uses the MIT License. The RoBERTa model follows its respective licensing terms from Hugging Face and Cardiff NLP.

## Acknowledgments

- **Cardiff NLP** for the pre-trained sentiment model
- **Hugging Face** for the transformers library
- **Facebook AI** for the original RoBERTa architecture

## Support

For questions or issues:
- Check the troubleshooting section above
- Review the Hugging Face model documentation
- Submit an issue in the repository

---

**Note**: This tool is designed for educational and research purposes. For production use, consider additional validation and testing with your specific use case.

