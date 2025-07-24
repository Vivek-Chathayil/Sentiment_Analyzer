from transformers import AutoTokenizer, AutoModelForSequenceClassification
from scipy.special import softmax

MODEL = "cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
model = AutoModelForSequenceClassification.from_pretrained(MODEL)

print("Sentiment Analysis with RoBERTa")
print("=" * 40)

# Initialize global variable
scores_dict = {}

def polarity_scores_roberta(text):
    """
    Analyze sentiment of input text using RoBERTa model
    """
    global scores_dict
    try:
        # Tokenize and encode the text
        encoded_text = tokenizer(text, return_tensors='pt', truncation=True, max_length=512)
        
        # Get model output
        output = model(**encoded_text)
        scores = output[0][0].detach().numpy()
        scores = softmax(scores)
        
        # Store scores in global dictionary
        scores_dict = {
            'roberta_neg': scores[0],
            'roberta_neu': scores[1],
            'roberta_pos': scores[2]
        }
        return scores_dict
    
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return None

def format_sentiment_results():
    """
    Format and display sentiment analysis results
    """
    global scores_dict
    
    if not scores_dict:
        print("No sentiment data available. Please run analysis first.")
        return
    
    sentiment_labels = {
        'roberta_neg': 'Negative',
        'roberta_neu': 'Neutral', 
        'roberta_pos': 'Positive'
    }
    
    print("\nSentiment Analysis Results:")
    print("-" * 30)
    
    for key, score in scores_dict.items():
        label = sentiment_labels[key]
        percentage = score * 100
        print(f"{label:8}: {percentage:6.2f}%")
    
    # Find the dominant sentiment
    max_key = max(scores_dict, key=scores_dict.get)
    dominant_sentiment = sentiment_labels[max_key]
    confidence = scores_dict[max_key] * 100
    
    print(f"\nPredicted: {dominant_sentiment} ({confidence:.1f}% confidence)")

def main():
    """
    Main function to run continuous sentiment analysis
    """
    print("Type 'quit', 'exit', or 'q' to stop the program\n")
    
    while True:
        # Get user input
        text = input("Enter the text you want to analyse: ").strip()
        
        # Check for exit conditions
        if text.lower() in ['quit', 'exit', 'q', '']:
            print("Thank you for using the sentiment analyzer! Goodbye!")
            break
        
        # Run sentiment analysis
        result = polarity_scores_roberta(text)
        
        if result:
            # Display results
            format_sentiment_results()
            print("\n" + "="*50 + "\n")  # Separator for next analysis
            
        else:
            print("Failed to analyze sentiment. Please check your input and try again.\n")

# Main execution
if __name__ == "__main__":
    main()