import nltk
import csv
import utils

def sentence_generator_from_file(
        comments_file_path,
        sentence_limit=10000,
        min_sentence_length=5,
        max_sentence_length=30
    ):
    sentence_counter = 0
    removed_lines_counter = 0
    processed_lines_counter = 0
    total_reddit_sentences = 0  # To track total Reddit sentences (valid or invalid)

    with open(comments_file_path, 'r', encoding='utf-8') as file:
        # Read the CSV file
        csv_reader = csv.reader(file)
        
        # Skip header if exists (optional, depending on your dataset structure)
        header = next(csv_reader, None)  # Adjust if the CSV has headers

        for line in csv_reader:
            total_reddit_sentences += 1  # Increment total sentence count for every line

            if not line:  # Skip empty lines
                removed_lines_counter += 1
                continue
            
            # Assuming the comment text is in the first column (adjust index as necessary)
            comment_text = line[0].strip()  # Adjust the index to match your dataset structure
            if not comment_text or comment_text in ('[removed]', '[deleted]'):
                removed_lines_counter += 1
                continue

            # Clean and tokenize the text
            cleaned_text = utils.clean_text(comment_text)
            sentences = nltk.sent_tokenize(cleaned_text)

            for sentence in sentences:
                words = nltk.word_tokenize(sentence)

                # Filter sentences by word length
                if len(words) < min_sentence_length or len(words) > max_sentence_length:
                    continue

                # Yield valid sentences
                yield words
                processed_lines_counter += 1
                sentence_counter += 1

                if sentence_limit is not None and sentence_counter >= sentence_limit:
                    # Print summary before returning
                    print(f"Total deleted sentences: {removed_lines_counter}")
                    print(f"Total processed sentences: {processed_lines_counter}")
                    print(f"Total Reddit sentences in file: {total_reddit_sentences}")
                    return

    # Print summary after processing all lines
    print(f"Total deleted sentences: {removed_lines_counter}")
    print(f"Total processed sentences: {processed_lines_counter}")
    print(f"Total Reddit sentences in file: {total_reddit_sentences}")


if __name__ == '__main__':
    # Adjust path to your CSV file
    generator = sentence_generator_from_file(
        r'C:\Users\minha\Desktop\project work\FormalityClassifier-master\data\reddit_comments.csv',
        1000  # Adjust sentence limit if needed
    )

    for sent in generator:
        print(' '.join(sent))
