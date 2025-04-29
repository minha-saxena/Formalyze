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
    total_reddit_sentences = 0  

    with open(comments_file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        
        header = next(csv_reader, None)  

        for line in csv_reader:
            total_reddit_sentences += 1  

            if not line: 
                removed_lines_counter += 1
                continue

            comment_text = line[0].strip()
            if not comment_text or comment_text in ('[removed]', '[deleted]'):
                removed_lines_counter += 1
                continue

            cleaned_text = utils.clean_text(comment_text)
            sentences = nltk.sent_tokenize(cleaned_text)

            for sentence in sentences:
                words = nltk.word_tokenize(sentence)

                
                if len(words) < min_sentence_length or len(words) > max_sentence_length:
                    continue

             
                yield words
                processed_lines_counter += 1
                sentence_counter += 1

                if sentence_limit is not None and sentence_counter >= sentence_limit:
                    
                    print(f"Total deleted sentences: {removed_lines_counter}")
                    print(f"Total processed sentences: {processed_lines_counter}")
                    print(f"Total Reddit sentences in file: {total_reddit_sentences}")
                    return


    print(f"Total deleted sentences: {removed_lines_counter}")
    print(f"Total processed sentences: {processed_lines_counter}")
    print(f"Total Reddit sentences in file: {total_reddit_sentences}")


if __name__ == '__main__':

    generator = sentence_generator_from_file(
        r'C:\Users\minha\Desktop\project work\FormalityClassifier-master\data\reddit_comments.csv',
        1000  
    )

    for sent in generator:
        print(' '.join(sent))
